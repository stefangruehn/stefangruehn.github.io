---
title: "Only the Restore Makes It a Backup: An Agent Backs Up the Environment It Runs In"
date: 2026-09-24T07:00:00+02:00
tags: ["claude-code", "disaster-recovery", "workflow", "linux", "privacy", "Field Notes"]
topics: ["data"]
summary: "I had Claude build a backup of the very working environment it runs in: projects, its memory, its own session logs. The backup was quick to write. What it was worth only showed when I restored it into an empty machine, and the faults that restore found were ones no design had foreseen."
---

## TL;DR

- I had an agent build a backup of the environment it works in: projects, its memory, its own session logs.
- The archive also contains the session that built it.
  Its log kept growing while it was being packed.
- The first probe, unpacking into a side folder, was all green.
  Only the second, into an empty container, found two files that differed: the freshly installed Claude Code had changed the restore before it was verified.
- The passphrase never passed through the agent, and it is not allowed to read the SSH keys.
  It still built and tested how they are backed up.
- One fault was found only by using the thing, another only by thinking it through.
  No design had foreseen either.

## The archive it sits inside

My laptop has a system backup.
What was missing was a backup that lets me carry on right away after a reinstall: the projects, Claude Code's working directory with its memory and all session logs, the Obsidian vaults, the dotfiles and, in the end, the SSH and GPG keys as well.

Claude designed, built and tested it, first in an interview, then as two scripts.
One packs and encrypts, the other restores, and a guide for the emergency comes with them.
Counted on 24 September, the backup holds 9,929 files, 384 MiB encrypted.

What is odd about this task shows up on the first real run.
Among the files being backed up is the log of the session in which Claude wrote the script.
That session was still running when I started the script in a terminal of my own, and it kept writing.
To `tar`, that is a file that changed while being read.
The script treats it as a warning, and the archive's manifest records: "1 claude process(es) were running while packing".

So the backup contains that log up to whichever line `tar` happened to be reading.
For a backup that is fine, the next generation has the rest.
But it shows early what this post is about: that an archive exists says nothing yet about what comes back out of it.

## The passphrase does not pass through the agent

Encryption is symmetric, with gpg, and the passphrase lives in my password manager.
It never passes through Claude.
Every real run happens in my own terminal: Claude writes down the steps, I carry them out, and afterwards Claude checks the results on disk.
For its own tests it uses a throwaway passphrase read from a file.

With the keys this goes one step further.
A rule in Claude Code's settings forbids it to read `~/.ssh`.
So it had to back up the keys without ever seeing them.
It tested this on an artificial home with dummy key files: whether they end up in the archive and whether they come back with the right permissions.
It never read the real ones.

## Two probes, one green

The first probe unpacked the archive into a side folder and checked every file against its checksum.
Everything matched, every repository was on the backed-up commit, the Claude Code version was the same.

That proved that encrypting, unpacking and verifying hold up.
It did not prove the emergency: an empty home in which paths, permissions and the reinstall actually have to work.

A throwaway user will not do for that.
Claude Code files the folders for memory and logs under the project's absolute path, so the user name is part of the folder name.
Under a different name the memories would not find their projects, and the restore script refuses any home that does not match the one backed up.
The second probe therefore ran in a container: a fresh system of the same distribution, the same user name, an empty home.

This time two files differed.
Claude Code's configuration file had changed, and an entry was missing from the folder where it keeps its own backup copies.

The cause was the order of steps.
The script offered to install Claude Code before comparing checksums.
The prompt was confirmed, the installer ran, and it touched exactly those two files.
The tool that was meant to be restored had changed the restore before it was verified.
The first probe supplied the evidence: from the same archive, without the installer, every file had matched.

The fix is a different order, verify first, install second.
The repeat in the container was all green after that.

The same report showed one more thing.
It explained the difference as "expected for files kept by --skip-existing", although that option had not been set at all.
A message that explains a fault away misleads more than no message.
It now appears only when the option really is set.

## What only use found

On the first real run, gpg opened its passphrase dialog.
It is modal: while it is open, no other window can be used, including the password manager that holds the passphrase.
Anyone who has not copied it to the clipboard beforehand cannot get at it while the dialog waits.

That was in no design, and Claude's tests could not show it, because they read the passphrase from a file and never opened a dialog.
It came from use.
Both scripts now stop before the first gpg call and say that the passphrase belongs in the clipboard.

## What only thinking found

The opposite case happened too.
On its first call, gpg creates its own configuration directory in the home.
On a fresh machine that happens while decrypting the archive, before the backed-up directory has come back.
Then the two collide: the restore script finds a file that already exists and aborts.

No probe showed this fault, because the keys only joined the scope after the probes.
It was found by asking what gpg does first on an empty machine.
The fix is a throwaway directory for gpg inside the script's working folder, checked on the artificial home.

One more small thing with consequences belongs to the keys.
The archive contains only files, no directories.
The files come back with their permissions, but the key folders are created anew when unpacking and are then readable by other users.
The restore script now sets their permissions afterwards.

## What I take from it

- A backup is a claim.
  It is proven only by a restore under the conditions it is meant for, and that means into an empty machine.
- The first green probe was not wrong.
  It only checked what was least in doubt anyway.
- If you back up the tool you work with, expect it to have a say in the restore.
  Verify first, install second.
- An agent can back up what it is not allowed to see.
  It needs a dummy to test against, and a human who does the real run.
- The faults came from three directions: from the probe, from use and from thinking it through.
  None of them would have been enough on its own.
