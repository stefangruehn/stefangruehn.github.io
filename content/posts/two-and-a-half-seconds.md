---
title: "Two and a Half Seconds and One Mistake: Taking a Linux Boot Apart With Claude Code"
date: 2026-09-02T02:30:00+02:00
draft: true
tags: ["claude-code", "linux", "systemd", "boot", "performance"]
summary: "System-level tuning has a reputation for being dangerous, so most of us never touch it. An evening with systemd, a fix that loaded cleanly and did absolutely nothing, and an honest look at whether any of this made the machine safer."
---

*This one is longer and goes deeper than usual.*
*If you stay with it, the payoff isn't the seconds saved — it's the fix that installed cleanly, loaded without a single error, and did nothing at all.*

## TL;DR

- My laptop hung on boot after a kernel update.
  Fixing that turned into an evening of actually reading what my system does at startup.
- Boot went from **25.326 s to 22.842 s**.
  That is the least interesting result of the night.
- The most useful moment was a fix that was installed correctly, loaded without error, and **did nothing at all**.
  systemd accepted it silently. Only checking afterwards caught it.
- Two thirds of a boot — firmware, bootloader, initrd — is untouchable by any amount of systemd configuration.
  Anyone promising you big numbers here is measuring something else.
- A kernel parameter I added myself, for a real reason, had quietly stopped doing anything.
  Nothing in the process of hand-tuning a machine ever asks whether an old workaround is still needed.
- Does it make the system safer? **Partly, and not for the reason you'd assume.**
  One change arguably moved security slightly the wrong way.
- The prompt I'd recommend is at the bottom.
  The three phrases that matter are *"read only"*, *"how do I undo it in one command"*, and *"check that it actually worked"*.

---

## It didn't start as an optimization

System-level tuning has a reputation among casual Linux users somewhere between "unnecessary" and "live wire".
You read about someone who disabled a systemd unit and lost networking, and you conclude: it boots, doesn't it.
Startup takes what it takes.

That caution isn't stupid.
It's just pointed at the wrong thing.
What is actually sitting on a machine like mine is rarely a bold intervention.
It's sediment.
A kernel parameter copied out of a forum post a year ago.
A service some package enabled at install time.
A daemon running around the clock for something that isn't even switched on.

None of it is dangerous.
All of it is unexamined.
And that is exactly why nobody touches it: you don't know what happens if you take it away, so it stays, and it accumulates.

My evening didn't begin with a wish to be faster.
At 01:27 the laptop stopped during boot after a kernel update.
Splash screen, nothing else.
The next attempt with the same kernel came up fine — a single event in twenty boots, which is precisely the kind of problem you normally breathe away.

The culprit wasn't the kernel.
It was `plymouth-read-write.service`, the unit that tells the splash screen the root filesystem is now writable.
It is `Type=oneshot` and runs `Before=sysinit.target`.
Those two together produce a property you only see once you go looking for it:

> A `Type=oneshot` service defaults to `TimeoutStartUSec=infinity`.
> If it hangs, the boot hangs. Not for a while — indefinitely.

The repair is a four-line drop-in setting `TimeoutStartSec=15s`.
That doesn't fix the cause, but it means a stuck splash screen turns an unusable machine into one that is fifteen seconds late.

## The parameter that outlived its reason

While we were in there, a second find turned up.
My kernel command line had carried `modprobe.blacklist=simpledrm` for months.

I put it there myself, and for a good reason.
At some point a kernel update stopped this laptop from booting — an AMD GPU problem — and that parameter was the recommendation I found on the web.
I added it, the machine came up again, and I got on with my life.
That is exactly how it is supposed to go.

Today the parameter cannot do anything.
`simpledrm` is built into Fedora kernels — it's listed in `modules.builtin` and has no `.ko` file at all — while `modprobe.blacklist=` is evaluated by kmod and only ever affects modules loaded through modprobe.
Whether it ever worked I can't reconstruct any more: three kernels are still installed here, and all three have it built in.
Either it was a real module back then and the blacklist bit properly, or the boot got better for a different reason at the same time.
The underlying bug has almost certainly been fixed upstream since.

Either way the outcome is the same, and that is the interesting part: the parameter stopped being attached to anything, and nobody noticed.

> A manual fix arrives with a reason attached.
> The reason expires quietly. The fix stays.

This is the honest failure mode of tuning your own system by hand, and it has nothing to do with recklessness.
You solve a real problem under pressure, at night, on a machine that won't boot.
The fix works.
Six months later the distribution has moved on, the bug is fixed upstream, and your workaround is still sitting in the kernel command line — no longer doing anything, and by now actively misleading, because it looks like a decision somebody made on purpose.
There is no point in that process where anyone comes back and asks whether it is still needed.
Nobody schedules a review of their own boot parameters.

That is the strongest argument I have for running this kind of work through an agentic AI instead of doing it by hand, and it isn't about speed.
It's that the session produces a record as a by-product: what was changed, why, what it was measured against, and the command that undoes it.
Before touching the parameter, Claude Code checked whether it still had any effect at all — which is exactly the question I had not asked in the months it sat there.
Doing it by hand gets you the change.
Doing it this way gets you the change plus its reason, in a form you can still read next year.

## Where the seconds actually are

Since we were already inside, we looked at what the boot spends its time on.
`systemd-analyze` splits it into five phases, and the first finding is sobering.

| Phase | Before | After | Difference |
|---|---:|---:|---:|
| Firmware | 3.456 s | 3.439 s | −0.017 s |
| Bootloader | 3.342 s | 3.443 s | +0.101 s |
| Kernel | 0.941 s | 0.939 s | −0.002 s |
| initrd | 7.827 s | 7.880 s | +0.053 s |
| **Userspace** | **9.758 s** | **7.139 s** | **−2.619 s** |
| **Total** | **25.326 s** | **22.842 s** | **−2.484 s** |

Firmware, bootloader, kernel and initrd add up to roughly 15.7 s and don't move between the two measurements — the wobble there is noise, not effect.
Two thirds of my boot is outside anything a systemd configuration can reach.
The only lever is userspace, and userspace was 9.758 s.

Those seconds aren't spread evenly either.
They hang off a chain:

```text
$ systemd-analyze critical-chain
graphical.target @9.758s
└─multi-user.target @9.758s
  └─docker.service @6.942s +2.815s
    └─network-online.target @6.938s
      └─NetworkManager-wait-online.service @2.898s +4.038s
        └─NetworkManager.service @2.528s +365ms
          └─network-pre.target @2.525s
            └─firewalld.service @2.524s
```

There it is.
`NetworkManager-wait-online.service`, 4.038 s, and everything behind it waiting.
Four of my ten userspace seconds went into waiting for the Wi-Fi to associate.

Three services demanded that finished network: `docker.service`, `rsyslog.service` and `clamav-freshclam.service`, all three with `Wants=` and `After=network-online.target`.

## The detour that didn't work

The obvious move is to break Docker's dependency.
In systemd you override that with a drop-in, and for many settings an empty assignment resets the inherited list.
So:

```ini
# /etc/systemd/system/docker.service.d/no-network-online.conf
[Unit]
Wants=
Wants=containerd.service
After=
After=nss-lookup.target docker.socket firewalld.service containerd.service
```

The file was in the right place.
`systemctl show` listed it under `DropInPaths`.
`NeedDaemonReload` said `no`.
And `network-online.target` was still sitting in both `After=` and `Wants=`.

No error message.
Nothing in the journal.
The change was simply inert.

The cross-check ran in a throwaway user unit that can't hurt anybody: define a unit with two dependencies, reset them with a drop-in, look at what systemd made of it.

```text
$ systemctl --user show cc-test.service -p Wants -p After
# Unit:    Wants/After = network-online.target foo.target
# Drop-in: Wants= / Wants=foo.target / After= / After=foo.target

Wants=network-online.target foo.target
After=basic.target app.slice network-online.target foo.target …
```

That turned a suspicion into a property.
**Dependency lists in systemd are purely cumulative.**
`After=`, `Before=`, `Wants=` and `Requires=` can only be extended by a drop-in, never withdrawn — unlike `ExecStart=`, `Environment=` or `SystemCallFilter=`, where the empty assignment behaves exactly as you'd expect.
To genuinely remove an inherited dependency you have to copy the whole unit into `/etc/systemd/system/`, which then detaches it from vendor updates.

This is the part I consider the point of the whole evening.
A drop-in that does nothing is worse than no drop-in.
It sits there, looks like a decision somebody made, and sends the next person hunting a problem in the wrong direction — exactly like that `simpledrm` parameter.

> The difference between "I changed something" and "it worked" is the entire value of the exercise.

It costs ten seconds to check. It is the step people skip.

## The lever

If you can't decouple the waiters, remove the waiting.

`NetworkManager-wait-online.service` is the only unit on the system with `Before=network-online.target`, hooked in there by `WantedBy=network-online.target`.
It *is* the waiting.
Without it the target is reached immediately; the three services still order after it, it just costs nothing.
One command, reversible with the same command:

```bash
sudo systemctl disable NetworkManager-wait-online.service
# back with: sudo systemctl enable NetworkManager-wait-online.service
```

The price belongs in the same paragraph.
Services now start before the Wi-Fi has associated.
For Docker that's inconsequential — it builds its own bridge and firewall rules.
For the logger likewise.
The only real worry was the virus signature update running into a dead network.
It didn't: on the first boot afterwards, `freshclam` reported all three databases `up-to-date` at 02:10:16.
A guess, tested and dropped.

## What it came to

After the reboot: 22.842 s instead of 25.326 s.
At its own position the four seconds were entirely gone — `network-online.target` is now reached at 2.898 s instead of 6.938 s.
Only 2.5 s arrived at the total, because Docker now starts earlier and takes about 0.75 s longer doing so.
The bottleneck didn't disappear. It moved.

### Two services that needn't start at all

The same chain had two other residents, and for both the interesting question wasn't "faster?" but "what for?".

**ClamAV** ran as a permanent daemon to refresh virus signatures twelve times a day.
On this machine `clamd@` and `clamav-clamonacc` are both disabled — nothing is scanning continuously, the signatures only serve occasional manual runs.
Fedora ships `clamav-freshclam-once.timer` for exactly this case, `OnCalendar=daily`, `Persistent=true`, disabled by default.
Nothing to build. Just switched on.

**rsyslog** read from the systemd journal via `imjournal` and wrote its contents back out as text into `/var/log/messages`.
The journal here is persistent — 3.9 GB, 92 boots.
So it was a second copy of the same logs, and nothing read it: no fail2ban, no analysis script, only logrotate.

## Does this make the system safer?

That was my own assumption going in, and it holds — but only halfway, and not the half you'd guess.

- **Attack surface: a small plus.**
  One fewer daemon running as root and parsing foreign input.
  Real, but modest — rsyslog wasn't listening on the network here, it was reading a local journal.
- **A possible minus, in the other direction.**
  Virus signatures now update once a day instead of twelve times.
  On a system that actually lets ClamAV scan, that is a loss.
  "Fewer services = safer" is wrong as a rule of thumb; it depends which one.
- **Availability: a large plus.**
  The Plymouth timeout stops a stuck splash screen from turning the laptop into a paperweight.
  That is the most concrete gain of the night and the only one that removes a real failure scenario.
- **Understood configuration: the actual return.**
  Before this, the machine carried an inert kernel parameter, an unbounded timeout, and three services I could not have told you the purpose of.
  Now every deviation from stock is written down — with a reason, and with the command that undoes it.

The last point is the one that matters.
Unexamined configuration isn't dangerous because an attacker exploits it.
It's dangerous because it points the next debugging session in the wrong direction — and because in its presence you don't dare touch anything.
That's the state most private Linux installs are in, and it gets worse over time, not better.

## What I'd tell someone on the fence

You don't need to be a systemd expert for this.
I needed to describe a symptom, read what was proposed, and say yes or no.

Six things I'd take from the evening:

1. **Start with a diagnosis, not a change.**
   The first half hour should produce no edits at all.
2. **Prefer a reversible switch to editing a unit file.**
   `systemctl disable` has an obvious way back. A hand-edited copy of a vendor unit doesn't.
3. **Check whether the thing a service exists for is even enabled.**
   ClamAV was updating signatures for a scanner that was switched off.
4. **Look for what your distribution already ships.**
   The timer I needed was sitting in `/usr/lib/systemd/system/`, disabled, the whole time.
5. **Verify after each step instead of assuming.**
   This is what caught the drop-in that loaded cleanly and did nothing.
6. **Write down what you changed and why.**
   Otherwise you've just produced next year's sediment.

And the realistic expectation: it's two and a half seconds.
The return on the evening wasn't the boot time.
It was the list of what is on this machine, and why.

## The prompt

Don't open with "make my boot faster".
That invites activity.
Better is a prompt that may only read at first, takes one change at a time, and carries the way back for each:

```text
Analyze this system's boot time. Read only, change nothing yet:
systemd-analyze, systemd-analyze critical-chain, systemd-analyze blame,
systemctl --failed, journalctl -b -p err.

Then explain which services actually lengthen the boot, and which of them I
need on this machine at all — check whether the thing that would use a given
service is even active here.

For each proposal I want to know: what it gains, what happens in the worst
case, and the single command that undoes it. Prefer reversible switches over
editing unit files, and check whether the distribution already ships
something for the purpose.

One change at a time, not as a batch. After each step, verify that the change
actually took effect instead of assuming it did. After the reboot we measure
together, and you write down what was changed and why.
```

The three phrases doing the work are *"read only"*, *"the single command that undoes it"*, and *"verify that the change actually took effect"*.

The first makes the session start with a diagnosis instead of tinkering.
The second turns every step into one you can close again — that is the entire reason this evening was harmless.
The third found the inert drop-in that would otherwise still be sitting there today.
