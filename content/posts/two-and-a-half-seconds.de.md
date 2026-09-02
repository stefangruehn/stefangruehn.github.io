---
title: "Zweieinhalb Sekunden und ein Irrtum: Einen Linux-Boot mit Claude Code auseinandergenommen"
date: 2026-09-02T02:30:00+02:00
draft: false
tags: ["claude-code", "linux", "systemd", "boot", "performance"]
summary: "Systemnahe Optimierung gilt als gefährlich, also fasst sie kaum jemand an. Ein Abend mit systemd, eine Änderung, die sauber geladen wurde und trotzdem nichts tat, und eine ehrliche Antwort auf die Frage, ob das Ganze das System sicherer macht."
---

*Dieser Beitrag ist länger und ausführlicher als üblich.*
*Wer dranbleibt, bekommt als Ertrag nicht die eingesparten Sekunden, sondern eine Änderung an der Boot-Konfiguration, die sauber installiert war, fehlerfrei lud — und trotzdem nichts bewirkt hat.*

## Kurzfassung

- Mein Laptop blieb nach einem Kernel-Update beim Booten hängen.
  Das zu reparieren wurde zu einem Abend, an dem ich zum ersten Mal gelesen habe, was mein System beim Start eigentlich tut.
- Der Boot ging von **25,326 s auf 22,842 s**.
  Das ist das uninteressanteste Ergebnis des Abends.
- Der nützlichste Moment war eine Änderung, die korrekt installiert war, fehlerfrei geladen wurde und **überhaupt nichts bewirkt hat**.
  systemd hat sie kommentarlos geschluckt. Nur die Nachkontrolle hat es gefunden.
- Zwei Drittel eines Bootvorgangs — Firmware, Bootloader, initrd — sind durch keine systemd-Konfiguration der Welt erreichbar.
  Wer hier große Zahlen verspricht, misst etwas anderes.
- Ein Kernel-Parameter, den ich selbst und aus gutem Grund gesetzt hatte, war unbemerkt wirkungslos geworden.
  Im Ablauf des Selberschraubens ist keine Stelle vorgesehen, an der jemand fragt, ob ein alter Workaround noch gebraucht wird.
- Macht es das System sicherer? **Teilweise, und nicht aus dem Grund, den man vermuten würde.**
  Eine der Änderungen hat die Sicherheit sogar leicht in die andere Richtung bewegt.
- Der Prompt, den ich empfehlen würde, steht ganz unten.
  Die drei Formulierungen, auf die es ankommt, sind „nur lesen“, „mit welchem einen Befehl nehme ich es zurück“ und „prüfe nach, ob es wirklich gewirkt hat“.

---

## Es fing gar nicht mit Optimierung an

Systemnahe Optimierung hat unter Linux-Gelegenheitsnutzern einen Ruf irgendwo zwischen „unnötig“ und „offene Stromleitung“.
Man liest von jemandem, bei dem nach dem Abschalten einer systemd-Unit das Netzwerk weg war, und beschließt: Läuft doch.
Der Start dauert eben, was er dauert.

Diese Vorsicht ist nicht dumm.
Sie zielt nur auf das Falsche.
Was auf so einem Rechner tatsächlich liegt, ist selten ein bewusster Eingriff.
Es ist Ablagerung.
Ein Kernel-Parameter, vor einem Jahr aus einem Forenbeitrag übernommen.
Ein Dienst, den irgendein Paket beim Installieren aktiviert hat.
Ein Daemon, der rund um die Uhr läuft, obwohl das, wofür er da ist, gar nicht eingeschaltet ist.

Nichts davon ist gefährlich.
Alles davon ist unverstanden.
Und genau deshalb rührt es niemand an: Man weiß nicht, was passiert, wenn man es wegnimmt — also bleibt es liegen und wächst.

Mein Abend begann nicht mit dem Wunsch, schneller zu sein.
Mitten in der Nacht blieb der Laptop nach einem Kernel-Update beim Booten stehen.
Splash-Screen, sonst nichts.
Der nächste Versuch mit demselben Kernel lief durch — ein einmaliges Ereignis in zwanzig Boots, also genau die Sorte Problem, die man normalerweise wegatmet.

Der Schuldige war nicht der Kernel.
Es war `plymouth-read-write.service`, der Dienst, der dem Splash-Screen mitteilt, dass das Wurzeldateisystem jetzt beschreibbar ist.
Er ist `Type=oneshot` und läuft `Before=sysinit.target`.
Beides zusammen ergibt eine Eigenschaft, die man erst sieht, wenn man danach sucht:

> Ein `Type=oneshot`-Dienst hat per Default `TimeoutStartUSec=infinity`.
> Bleibt er hängen, hängt der Boot. Nicht lange — unbegrenzt.

Die Reparatur ist ein Drop-in mit vier Zeilen und setzt `TimeoutStartSec=15s`.
Das behebt die Ursache nicht, aber es sorgt dafür, dass ein hängender Splash-Screen aus einem unbenutzbaren Rechner höchstens noch einen um fünfzehn Sekunden verspäteten macht.

## Der Parameter, der seinen Grund überlebt hat

Bei der Gelegenheit fiel ein zweiter Fund an.
In meiner Kernel-Kommandozeile stand seit Monaten `modprobe.blacklist=simpledrm`.

Den hatte ich selbst gesetzt, und zwar aus gutem Grund.
Ab einer bestimmten Kernel-Version bootete dieser Laptop zwar, aber der Bildschirm blieb dunkel — ein AMD-GPU-Problem —, und dieser Parameter war die Empfehlung, die ich damals im Netz gefunden hatte.
Ich habe ihn eingetragen, das Bild war wieder da, und ich habe weitergemacht.
Genau so soll es laufen.

Heute kann der Parameter nichts mehr bewirken.
`simpledrm` ist in Fedora-Kerneln fest eingebaut — es steht in `modules.builtin` und hat gar keine `.ko`-Datei —, während `modprobe.blacklist=` von kmod ausgewertet wird und nur bei Modulen greift, die per modprobe geladen werden.
Ob er je gewirkt hat, lässt sich nicht mehr rekonstruieren: Hier sind noch drei Kernel installiert, und in allen dreien ist es fest eingebaut.
Entweder war es damals ein echtes Modul und die Blacklist hat sauber gegriffen, oder der Boot wurde zur selben Zeit aus einem anderen Grund besser.
Der zugrunde liegende Fehler ist inzwischen mit ziemlicher Sicherheit im Kernel behoben.

Das Ergebnis ist in beiden Fällen dasselbe, und das ist der interessante Teil: Der Parameter hing an nichts mehr, und niemand hat es gemerkt.

> Ein manueller Fix kommt mit einem Grund im Gepäck.
> Der Grund verfällt still. Der Fix bleibt.

Das ist der ehrliche Schwachpunkt daran, sein System von Hand zu pflegen, und er hat nichts mit Leichtsinn zu tun.
Man löst nachts unter Druck ein echtes Problem, an einer Maschine, die nichts mehr anzeigt.
Der Fix wirkt.
Ein halbes Jahr später ist die Distribution weitergezogen, der Fehler ist oben behoben, und der Workaround steht immer noch in der Kernel-Kommandozeile — ohne Wirkung, und inzwischen aktiv irreführend, weil er wie eine bewusst getroffene Entscheidung aussieht.
In diesem Ablauf ist keine Stelle vorgesehen, an der jemand zurückkommt und fragt, ob das noch gebraucht wird.
Niemand setzt sich eine Wiedervorlage für seine eigenen Boot-Parameter.

Das ist das stärkste Argument, das ich dafür habe, diese Art Arbeit durch eine agentische AI laufen zu lassen statt von Hand — und es geht dabei nicht um Geschwindigkeit.
Es geht darum, dass als Nebenprodukt ein Protokoll entsteht: was geändert wurde, warum, wogegen gemessen wurde und mit welchem Befehl man es zurücknimmt.
Bevor Claude Code den Parameter angefasst hat, hat es geprüft, ob er überhaupt noch etwas bewirkt — also genau die Frage gestellt, die ich in all den Monaten nicht gestellt hatte.
Von Hand bekommt man die Änderung.
So bekommt man die Änderung samt ihrem Grund, in einer Form, die man nächstes Jahr noch lesen kann.

## Wo die Sekunden tatsächlich liegen

Wenn man schon einmal dabei ist, kann man auch nachsehen, wofür der Boot seine Zeit ausgibt.
`systemd-analyze` zerlegt ihn in fünf Phasen, und die erste Erkenntnis ist ernüchternd.

| Phase | Vorher | Nachher | Differenz |
|---|---:|---:|---:|
| Firmware | 3,456 s | 3,439 s | −0,017 s |
| Bootloader | 3,342 s | 3,443 s | +0,101 s |
| Kernel | 0,941 s | 0,939 s | −0,002 s |
| initrd | 7,827 s | 7,880 s | +0,053 s |
| **Userspace** | **9,758 s** | **7,139 s** | **−2,619 s** |
| **Gesamt** | **25,326 s** | **22,842 s** | **−2,484 s** |

Firmware, Bootloader, Kernel und initrd machen zusammen rund 15,7 s aus und rühren sich zwischen den beiden Messungen nicht — die Streuung dort ist Rauschen, keine Wirkung.
Zwei Drittel meines Bootvorgangs liegen außerhalb dessen, was eine systemd-Konfiguration erreichen kann.
Der einzige Hebel ist der Userspace, und der war 9,758 s lang.

Diese Sekunden sind aber auch nicht gleichmäßig verteilt.
Sie hängen an einer Kette:

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

`NetworkManager-wait-online.service`, 4,038 s, und alles dahinter wartet.
Vier von zehn Userspace-Sekunden gingen dafür drauf, dass das WLAN assoziiert ist.

Drei Dienste verlangten dieses fertige Netz: `docker.service`, `rsyslog.service` und `clamav-freshclam.service`, alle drei mit `Wants=` und `After=network-online.target`.

## Der Umweg, der nicht funktioniert hat

Der naheliegende Schritt: Docker die Abhängigkeit abgewöhnen.
In systemd überschreibt man so etwas mit einem Drop-in, und für viele Einstellungen setzt eine leere Zuweisung die geerbte Liste zurück.
Also:

```ini
# /etc/systemd/system/docker.service.d/no-network-online.conf
[Unit]
Wants=
Wants=containerd.service
After=
After=nss-lookup.target docker.socket firewalld.service containerd.service
```

Die Datei lag am richtigen Ort.
`systemctl show` listete sie unter `DropInPaths`.
`NeedDaemonReload` stand auf `no`.
Und `network-online.target` stand unverändert in `After=` und `Wants=`.

Keine Fehlermeldung.
Nichts im Journal.
Der Eingriff war schlicht wirkungslos.

Die Gegenprobe lief in einer weggeworfenen User-Unit, die niemandem wehtun kann: eine Unit mit zwei Abhängigkeiten anlegen, per Drop-in zurücksetzen, nachsehen, was systemd daraus macht.

```text
$ systemctl --user show cc-test.service -p Wants -p After
# Unit:    Wants/After = network-online.target foo.target
# Drop-in: Wants= / Wants=foo.target / After= / After=foo.target

Wants=network-online.target foo.target
After=basic.target app.slice network-online.target foo.target …
```

Damit war es keine Vermutung mehr, sondern eine Eigenschaft.
**Abhängigkeitslisten sind in systemd rein kumulativ.**
`After=`, `Before=`, `Wants=` und `Requires=` lassen sich per Drop-in nur erweitern, nie zurücknehmen — im Unterschied zu `ExecStart=`, `Environment=` oder `SystemCallFilter=`, wo die leere Zuweisung genau so funktioniert, wie man es erwartet.
Wer eine geerbte Abhängigkeit wirklich loswerden will, muss die ganze Unit nach `/etc/systemd/system/` kopieren und hängt sie damit von Hersteller-Updates ab.

Das ist der Teil, den ich für den eigentlichen Ertrag des Abends halte.
Ein Drop-in, das nichts tut, ist schlimmer als gar keins.
Es steht da, sieht nach einer getroffenen Entscheidung aus und schickt den Nächsten, der ein Problem sucht, in die falsche Richtung — exakt wie der `simpledrm`-Parameter.

> Der Unterschied zwischen „ich habe etwas geändert“ und „es hat gewirkt“ ist der ganze Wert der Übung.

Die Nachkontrolle kostet zehn Sekunden. Sie ist der Schritt, den man gern überspringt.

## Der Hebel

Wenn man die Wartenden nicht entkoppeln kann, nimmt man das Warten weg.

`NetworkManager-wait-online.service` ist die einzige Unit im System mit `Before=network-online.target` und hängt per `WantedBy=network-online.target` dort ein.
Sie *ist* das Warten.
Ohne sie wird das Target sofort erreicht; die drei Dienste dürfen weiterhin danach ordnen, es kostet nur keine Zeit mehr.
Ein Befehl, umkehrbar mit demselben Befehl:

```bash
sudo systemctl disable NetworkManager-wait-online.service
# zurück mit: sudo systemctl enable NetworkManager-wait-online.service
```

Dienste starten jetzt, bevor das WLAN assoziiert ist.
Für Docker ist das folgenlos — es legt Bridge und Firewall-Regeln selbst an.
Für den Logger ohnehin.
Die einzige echte Sorge galt dem Virensignatur-Update, das in ein totes Netz laufen könnte.
Tat es nicht: Im ersten Boot danach meldete `freshclam` alle drei Datenbanken `up-to-date`.
Eine Vermutung, geprüft und verworfen.

## Was dabei herauskam

Nach dem Reboot: 22,842 s statt 25,326 s.
An ihrer Stelle waren die vier Sekunden vollständig weg — `network-online.target` wird jetzt nach 2,898 s erreicht statt nach 6,938 s.
Angekommen sind trotzdem nur 2,5, weil Docker dadurch früher startet und dabei selbst rund 0,75 s länger braucht.
Der Engpass ist nicht verschwunden. Er ist umgezogen.

### Zwei Dienste, die gar nicht erst starten müssen

Dieselbe Kette hatte zwei weitere Bewohner, und bei beiden war die interessante Frage nicht „schneller?“, sondern „wofür eigentlich?“.

**ClamAV** lief als Dauer-Daemon, um zwölfmal am Tag Virensignaturen zu aktualisieren.
Auf diesem Rechner sind `clamd@` und `clamav-clamonacc` beide abgeschaltet — es scannt also gar nichts laufend mit, die Signaturen bedienen nur gelegentliche manuelle Läufe.
Fedora liefert für genau diesen Fall `clamav-freshclam-once.timer` mit, `OnCalendar=daily`, `Persistent=true`, standardmäßig deaktiviert.
Nichts zu bauen. Nur eingeschaltet.

**rsyslog** las über `imjournal` aus dem systemd-Journal und schrieb dessen Inhalt als Text nach `/var/log/messages` zurück.
Das Journal ist hier persistent — 3,9 GB, 92 Boots.
Es war also eine zweite Kopie derselben Logs, und nichts las sie: kein fail2ban, kein Auswertungsskript, nur logrotate.

## Macht das das System sicherer?

Das war meine eigene Annahme, als ich anfing, und sie stimmt — aber nur zur Hälfte, und nicht in der Hälfte, die man vermuten würde.

- **Angriffsfläche: ein kleines Plus.**
  Ein Daemon weniger, der als root läuft und fremde Eingaben parst.
  Real, aber bescheiden — rsyslog lauschte hier nicht am Netz, es las aus einem lokalen Journal.
- **Ein mögliches Minus, in die Gegenrichtung.**
  Die Virensignaturen werden jetzt einmal statt zwölfmal täglich aktualisiert.
  Auf einem System, das ClamAV tatsächlich scannen lässt, wäre das ein Verlust.
  „Weniger Dienste = sicherer“ ist als Faustregel falsch; es kommt darauf an, welcher.
- **Verfügbarkeit: ein großes Plus.**
  Der Plymouth-Timeout verhindert, dass ein hängender Splash-Screen aus dem Laptop einen Briefbeschwerer macht.
  Das ist der handfesteste Gewinn des Abends und der einzige, der ein echtes Ausfallszenario beseitigt.
- **Verstandene Konfiguration: der eigentliche Ertrag.**
  Vorher trug die Maschine einen wirkungslosen Kernel-Parameter, einen unbegrenzten Timeout und drei Dienste, von denen ich nicht hätte sagen können, wozu sie da sind.
  Jetzt ist jede Abweichung vom Auslieferungszustand aufgeschrieben — mit Grund und mit dem Befehl, der sie zurücknimmt.

Der letzte Punkt ist der, auf den es ankommt.
Unverstandene Konfiguration ist nicht gefährlich, weil ein Angreifer sie ausnutzt.
Sie ist gefährlich, weil sie die nächste Fehlersuche in die falsche Richtung schickt — und weil man sich in ihrer Gegenwart nicht traut, irgendetwas anzufassen.
Das ist der Zustand, in dem die meisten privaten Linux-Installationen sind, und er wird mit der Zeit schlechter, nicht besser.

## Was ich jemandem sagen würde, der noch zögert

Du musst dafür kein systemd-Experte sein.
Ich musste ein Symptom beschreiben, lesen, was vorgeschlagen wurde, und ja oder nein sagen.

Sechs Dinge, die ich aus dem Abend mitnehme:

1. **Mit einer Diagnose anfangen, nicht mit einer Änderung.**
   In der ersten halben Stunde sollte gar nichts geschrieben werden.
2. **Einen umkehrbaren Schalter dem Editieren einer Unit-Datei vorziehen.**
   `systemctl disable` hat einen offensichtlichen Rückweg. Eine handgeänderte Kopie einer Hersteller-Unit nicht.
3. **Nachsehen, ob das, wofür ein Dienst da ist, überhaupt eingeschaltet ist.**
   ClamAV aktualisierte Signaturen für einen Scanner, der aus war.
4. **Schauen, was die Distribution schon mitliefert.**
   Der Timer, den ich brauchte, lag die ganze Zeit deaktiviert in `/usr/lib/systemd/system/`.
5. **Nach jedem Schritt nachprüfen statt annehmen.**
   Genau das hat das Drop-in gefunden, das sauber lud und nichts tat.
6. **Aufschreiben, was geändert wurde und warum.**
   Sonst hat man nur die Ablagerung des nächsten Jahres produziert.

Und die realistische Erwartung: Es sind zweieinhalb Sekunden.
Der Ertrag des Abends war nicht die Bootzeit.
Er war die Liste dessen, was auf diesem Rechner steht und warum.

## Der Prompt

Fang nicht mit „mach meinen Boot schneller“ an.
Das lädt zu Aktionismus ein.
Besser ist ein Prompt, der zuerst nur lesen darf, jede Änderung einzeln nimmt und für jede den Rückweg mitliefert:

```text
Analysiere die Bootzeit dieses Systems. Nur lesen, noch nichts ändern:
systemd-analyze, systemd-analyze critical-chain, systemd-analyze blame,
systemctl --failed, journalctl -b -p err.

Erkläre mir dann, welche Dienste den Boot tatsächlich verlängern und welche
davon ich auf diesem Rechner überhaupt brauche — sieh dabei nach, ob das,
was einen Dienst nutzen würde, hier überhaupt aktiv ist.

Für jeden Vorschlag will ich wissen: was er bringt, was schlimmstenfalls
passiert, und mit welchem einen Befehl ich ihn zurücknehme. Bevorzuge
reversible Schalter gegenüber dem Editieren von Unit-Dateien, und sieh nach,
ob die Distribution für den Zweck schon etwas mitliefert.

Änderungen einzeln, nicht im Paket. Prüfe nach jedem Schritt nach, ob die
Änderung wirklich gewirkt hat, statt es anzunehmen. Nach dem Reboot messen
wir gemeinsam nach, und du schreibst auf, was geändert wurde und warum.
```

Die drei Formulierungen, die die Arbeit machen, sind „nur lesen“, „mit welchem einen Befehl nehme ich es zurück“ und „prüfe nach, ob es wirklich gewirkt hat“.

Die erste sorgt dafür, dass am Anfang eine Diagnose steht und keine Bastelei.
Die zweite macht aus jedem Schritt einen, den man auch wieder zumachen kann — das ist der ganze Grund, warum dieser Abend ungefährlich war.
Die dritte hat das wirkungslose Drop-in gefunden, das sonst noch heute da läge.
