---
title: "Der eingefrorene Regler: 23 Dezibel, die niemand mehr korrigiert"
date: 2026-09-03T12:20:00+02:00
draft: false
tags: ["claude-code", "linux", "audio", "alsa", "pipewire", "wireplumber", "systemd", "debugging", "chuwi", "nerdfutter", "technical deep dive"]
series: ["Nachhall"]
summary: "Nach einem Reboot war jede Audioquelle 23 dB zu leise. Die Ursache war ein ALSA-Regler, den seit einem früheren Fix niemand mehr anfasst — und die Reparatur scheiterte erst einmal daran, dass die Kartennamen dieses Laptops zwischen Boots die Plätze tauschen."
---

Teil eins dieser Serie fand ein [Hardware-Problem](/de/posts/measure-dont-guess/) und löste es.
Teil zwei fand, was die [Fehlersuche hinterlassen](/de/posts/a-remembered-zero/) hatte — eine gespeicherte Null.
Dies ist, was die *Lösung* hinterlassen hat.

## Kurzfassung

- Nach einem Reboot war alles zu leise: YouTube, Musikplayer, Systemklänge.
  Kein Programm ausgenommen, also kein Stream-Problem wie in Teil zwei.
- Der ALSA-Regler `Master` stand auf **-23 dB**, und seit dem Soft-Mixer-Fix aus Teil eins fasst ihn niemand mehr an.
  WirePlumber führt ihn nicht mehr nach, weil es ihn nicht mehr nachführen *soll*.
- Der Zielwert wurde gemessen, nicht gerechnet.
  Nominell und akustisch klaffen 3 dB auseinander, und die Rechnung hätte auf einen anderen Regler gezeigt.
- Die erste Reparatur überlebte den Testreboot **nicht**.
  Beide HDA-Controller dieses Laptops heißen `HD-Audio Generic`, und die ALSA-Namen tauschen zwischen Boots die Plätze.
  `asound.state` ist nach Namen gegliedert, meine systemd-Unit war es auch — beide griffen daneben.
- Die zweite Fassung löst die Karte über die PCI-Adresse auf und wartet auf ihre Enumeration.
  Dass die Warteschleife wirklich gebraucht wird, steht nirgends als Fehler.
  Es steht in einer Sekunde zwischen zwei Logzeilen.

## Alles zu leise, kein Programm ausgenommen

Fedora 44, GNOME 50, PipeWire 1.6.8, ein Chuwi CoreBook X mit einem Conexant SN6180.

Das Symptom war diesmal langweilig und dadurch aufschlussreich: Nach einem Reboot war schlicht alles zu leise.
Browser, Musikplayer, Systemklänge, in jeder Anwendung derselbe Verlust.
Genau diese Gleichmäßigkeit schließt aus, was in Teil zwei die Ursache war.
Eine gespeicherte Stream-Lautstärke trifft eine Rolle und lässt den Rest in Ruhe.
Was alle Quellen gleich stark dämpft, sitzt hinter dem Mixer, nicht davor.

Der Regler in den GNOME-Toneinstellungen stand auf Anschlag, und der Sink meldete brav, dass alles in Ordnung sei:

```
Volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
Base Volume: 65536 / 100% / 0.00 dB
Mute: no
```

Null Dezibel Dämpfung, nicht stummgeschaltet, voller Pegel.
Auf der Hardware darunter sah es anders aus:

```
$ amixer -c1 sget Master
  Limits: Playback 0 - 74
  Mono: Playback 51 [69%] [-23.00dB] [on]
```

Dreiundzwanzig Dezibel.
Der Regler, den PipeWire anzeigt, und der Regler, der tatsächlich dämpft, hatten nichts mehr miteinander zu tun.

## Wer den Mixer abschaltet, friert ihn ein

Das ist kein Zufall, sondern die Nachwirkung der Lösung aus Teil eins.
Jene Lösung verlegte Lautstärke und Balance aus dem Tonchip heraus in die Software, damit die Verstärkung jedes Kanals bei seinem eigenen Lautsprecher ankommt:

```
# ~/.config/wireplumber/wireplumber.conf.d/51-chuwi-corebook-x-soft-mixer.conf
api.alsa.soft-mixer = true
```

Damit rechnet PipeWire Lautstärke und Balance in die Samples und lässt die ALSA-Controls in Ruhe.
Das war richtig, es funktioniert weiterhin, und es hat genau eine Folge, an die ich nicht gedacht hatte:
Wenn WirePlumber den Regler nicht mehr anfasst, fasst ihn *niemand* mehr an.

Vorher war `Master` Teil eines Regelkreises.
Der Desktop-Regler bewegte ihn, `alsactl` sicherte ihn beim Herunterfahren, der nächste Start stellte ihn wieder her.
Jeder Wert, der da hineinlief, wurde beim nächsten Mal wieder korrigiert.
Nach der Änderung läuft nichts mehr hinein.
Was zu diesem Zeitpunkt dort stand, steht dort für immer, und beim nächsten Boot kommt es zurück.

Ob die -23 dB die Reglerstellung aus der Zeit davor sind oder schlicht der Wert, auf den der Codec kommt, kann ich nicht auseinanderhalten.
`alsactl init` setzt den Regler auf einem laufenden System auf 54 statt auf 51, was gegen einen reinen Treiber-Default spricht, aber nichts beweist.
Auseinanderhalten ließe sich das nur mit dem Zustand von vor der Lösung, und den gibt es auf dieser Maschine nicht mehr.
Für das Symptom ist es auch gleich: Der Wert kommt bei jedem Start wieder, und nichts hebt ihn an.

Bemerkenswert ist der Zeitverzug.
Solange die Sitzung von damals lief, war der Pegel in Ordnung — der Regler stand ja noch dort, wo ihn WirePlumber zuletzt hingeschoben hatte.
Der Fix hat nichts kaputtgemacht, was am selben Tag zu merken gewesen wäre.
Er hat einen Wert eingefroren, und die Rechnung kam beim nächsten Reboot.

## Der Zielwert wird gemessen, nicht gerechnet

Die Vorgabe war präzise: Was bisher erst am Anschlag herauskam, soll künftig bei 50 % Reglerstellung anliegen.

Rechnen kann man das.
PulseAudio und PipeWire bilden den Regler kubisch ab, `dB = 60 · log₁₀(v)`, also sind 100 % → 50 % genau -18,06 dB.
`Master` hat 1 dB je Schritt, folglich 51 + 18 = **69**.

Nur ist ein Lautsprecher keine Rechnung.
Das Messinstrument aus Teil eins steht noch: 1-kHz-Ton über `paplay`, gleichzeitig mit dem Innenmikrofon aufnehmen, danach das Band um 1 kHz aus der FFT lesen.
Zwei Minuten Arbeit, und es beantwortet die Frage, die die Rechnung nur behauptet.

| `Master` | Regler | 1 kHz, Mittel | n | sd |
|---|---|---|---|---|
| 51 (-23 dB) | 100 % | -29,95 dB | 6 | 0,09 |
| **69 (-5 dB)** | **50 %** | **-29,96 dB** | 6 | 0,10 |
| 51 (-23 dB) | 50 % | -45,06 dB | 4 | 0,18 |
| 69 (-5 dB) | 100 % | -24,31 dB | 4 | 0,15 |

Die erste und die zweite Zeile trennen **0,01 dB**.
Das ist die ganze Antwort: Die 69 stimmt.

Die Spalten `n` und `sd` stehen da, weil ich sie mir selbst schuldig geblieben war.
Zwei Einzelablesungen derselben Einstellung landeten kurz zuvor zwei Dezibel zu tief, fünf hintereinander streuten um 1,3 dB.
Eine einzelne Messung dieses Aufbaus beantwortet die Frage „sind diese beiden gleich laut" schlicht nicht.
Erst verschränkt gemessen — A, B, A, B, jeweils sechsmal, damit langsame Drift beide Seiten gleich trifft — sinkt die Streuung auf 0,1 dB, und dann trägt der Vergleich.
Der erste Anlauf hatte zufällig zweimal dieselbe Zahl geliefert und mich das für Präzision halten lassen.

Die Zwischenwerte stimmen nicht.
Der Regler von 100 % auf 50 % kostet akustisch **15,11 dB**, der Mixer von 51 auf 69 bringt **15,10 dB** — nominell wären beides 18,06.
Die Kennlinie ist auf beiden Wegen gleich gestaucht, und *deshalb* hebt es sich auf.
Wäre die Stauchung nur auf einer Seite aufgetreten, hätte die Rechnung auf einen anderen Regler gezeigt.
Oben wird es deutlicher: Von 50 % auf 100 % bleiben bei `Master` 69 nur **5,6 dB** Spielraum, nicht die nominellen 18.
Endstufe oder Lautsprecher begrenzen dort, und kein Datenblattwert sagt das voraus.

## Zwei Karten, ein Name

Der Rest sollte Fleißarbeit sein: den Wert bei jeder Anmeldung setzen, fertig.

```ini
# ~/.config/systemd/user/chuwi-master-volume.service
[Service]
Type=oneshot
ExecStart=/usr/bin/amixer -c Generic -q sset Master 69
```

Karte per Namen statt per Index, mit einem Kommentar darüber, dass Indizes zwischen Boots wandern können.
Dazu `alsactl store`, damit der Wert auch systemweit hinterlegt ist.

Der Testreboot hat das vollständig widerlegt.
Danach stand `Master` wieder auf 51, und hier genügte eine einzelne Messung: -45,1 dB bei 50 %, fünfzehn Dezibel unter dem Sollwert.
Die Maschine war exakt dort, wo sie vorher war.

Beide HDA-Controller dieses Geräts melden sich als `HD-Audio Generic`, und ALSA vergibt die IDs in Probe-Reihenfolge:

| Boot | analog, `0000:03:00.6` | HDMI, `0000:03:00.1` |
|---|---|---|
| 11:27 | card1, id `Generic` | card0, id `Generic_1` |
| 11:53 | card1, id `Generic_1` | card0, id `Generic` |

Der Index blieb, der Name wanderte.
Ich hatte den Namen gewählt, weil ich den Index für das Wacklige hielt.

Damit fällt auch die zweite Absicherung, und zwar aus demselben Grund:
`asound.state` ist nach Karten-**Namen** gegliedert, in Abschnitten `state.Generic` und `state.Generic_1`.
Die gespeicherte 69 lag unter `state.Generic` und wurde nach dem Tausch auf die HDMI-Karte angewandt, die gar keinen `Master` besitzt.
Erneutes `alsactl store` repariert das nicht, es verschiebt das Problem nur:
Der Abschnitt des jeweils anderen Namens wird dabei mit dem überschrieben, was gerade darunter läuft.
Nach dem nächsten sauberen Shutdown steht die 69 unter `Generic_1` — und beim übernächsten Namenstausch greift die Wiederherstellung wieder daneben.

Auf einer Maschine mit zwei gleichnamigen Karten ist `asound.state` als Ablage für einen bestimmten Regler nicht brauchbar.

## Die PCI-Adresse ist das einzig Stabile

Was sich nicht bewegt, ist die Adresse auf dem Bus.
Also nicht mehr fragen, wie die Karte heißt, sondern welche Karte an `0000:03:00.6` hängt:

```bash
for d in /sys/class/sound/card*; do
    [ -e "$d/device" ] || continue
    [ "$(basename "$(readlink -f "$d/device")")" = "$PCI" ] || continue
    idx=${d##*/card}
    amixer -c "$idx" sget Master >/dev/null 2>&1 || continue
    amixer -c "$idx" -q sset Master "$LEVEL"
    exit 0
done
```

Das Ganze in einer Schleife, die es bis zu dreißig Sekunden lang jede Sekunde erneut versucht, und die Unit ruft nur noch dieses Skript.

## Eine Sekunde im Journal

Die Warteschleife war eine Nebensache beim Schreiben.
Zwei Zeilen, eingebaut aus der Erinnerung an eine Fehlermeldung, ohne Beleg, dass sie nötig ist.

Der zweite Testreboot hat gehalten: Unit sauber durchgelaufen, zwei Messungen bei 50 % mit -30,2 und -30,3 dB im Referenzbereich.
Interessant ist nicht das Ergebnis, sondern wie es zustande kam:

```
12:01:50.304347  Starting chuwi-master-volume.service...
12:01:51.335420  Finished chuwi-master-volume.service.
```

Eintausendeinunddreißig Millisekunden für ein `amixer sset`.
Der Kartenscan selbst dauert Millisekunden — die Sekunde ist der `sleep 1` zwischen einem gescheiterten und einem geglückten Durchlauf.
Beim Login ist die Analogkarte noch nicht enumeriert.
Ohne Schleife wäre auch diese Fassung gescheitert.

Und damit lässt sich die Fehlermeldung des ersten Anlaufs endlich richtig lesen.
Sie lautete:

```
amixer[3682]: Invalid card number 'Generic'.
```

Ich hatte sie als Beleg für den Namenstausch genommen — der Name stand ja darin.
Sie ist keiner.
Zu diesem Zeitpunkt hieß card0 tatsächlich `Generic`; die Karte existierte, sie war nur die falsche.
So klingt der Namensfehler nämlich, nachgeprüft an derselben Maschine:

```
$ amixer -c Generic sget Master
amixer: Unable to find simple control 'Master',0
```

`Invalid card number` heißt etwas anderes: Es gab zu diesem Zeitpunkt gar keine Karte dieses Namens.
Die Meldung nannte das Timing.
Den Namenstausch habe ich unabhängig davon gefunden, in `/sys/class/sound` und in den Abschnittsüberschriften von `asound.state`.

Zwei Defekte in einer einzigen `ExecStart`-Zeile, und sie verdeckten einander.
Nur den Namen zu reparieren hätte nicht gereicht, weil die Karte beim Login noch fehlt.
Nur das Timing zu reparieren auch nicht, weil der Pegel dann auf der HDMI-Karte gelandet wäre.

## Was ich gelernt habe

- **Wer eine Komponente abschaltet, friert ihren Zustand ein.**
  „Ab jetzt fasst das keiner mehr an" heißt auch „ab jetzt korrigiert das keiner mehr".
  Der Soft-Mixer war richtig und ist es geblieben — den Wert, den er einfror, konnte er gar nicht aufräumen.
  Beim Abschalten eines Regelkreises gehört die Frage dazu, wer den letzten Wert künftig verantwortet.
- **Eine Fehlermeldung nennt einen Fehler, nicht *den* Fehler.**
  In `Invalid card number 'Generic'` stand genau das Wort, auf das meine Vermutung zeigte, und sie meldete trotzdem etwas anderes.
  Wer im Text einer Meldung die eigene These wiederfindet, hat sie nicht bestätigt, sondern nur wiedererkannt.
  Die Gegenprobe kostete einen Befehl: nachsehen, wie der vermutete Fehler tatsächlich klingt.
- **Beiläufige Vorsicht kann tragend sein, und man sieht es nur am Zeitstempel.**
  Die Warteschleife war beim Schreiben eine Nebensache und ist der Grund, dass es läuft.
  Am Ergebnis ist das nicht abzulesen: Die Unit meldet mit und ohne Schleife `Finished`.
  Ein grüner Lauf sagt, dass es geklappt hat, nicht, wie knapp.

## Womit ich anfangen würde

Wenn auf deiner Maschine alles gleichmäßig zu leise ist und der Desktop-Regler am Anschlag steht, in dieser Reihenfolge:

1. **Den Hardware-Mixer direkt ansehen**, nicht den Sink.
   `amixer -c<n> scontents` zeigt, was tatsächlich dämpft; `pactl list sinks` zeigt nur, was PipeWire meint.
   Weichen beide voneinander ab, ist die Frage nicht mehr „wie laut", sondern „wer schreibt da hinein".
2. **Prüfen, ob überhaupt noch jemand hineinschreibt.**
   Bei `api.alsa.soft-mixer = true` ist die Antwort: niemand.
   Dasselbe gilt für jedes UCM-Profil und jede Regel, die einen Control aus der Verwaltung nimmt.
3. **Zählen, wie viele Karten gleich heißen.**
   `cat /proc/asound/cards` und `readlink -f /sys/class/sound/card*/device` nebeneinander.
   Sind zwei Namen austauschbar, ist jede namensbasierte Konfiguration — deine eigene und `asound.state` — eine Wette auf die Probe-Reihenfolge.
4. **Den Zielwert messen, nicht ausrechnen.**
   Ein Ton, das eingebaute Mikrofon und eine FFT reichen.
   Die Kennlinie zwischen Regler und Schalldruck ist an den Rändern nicht die, die im Datenblatt steht.
5. **Neu starten, bevor du es für erledigt hältst.**
   Der simulierte Test — Wert zurückdrehen, Unit neu starten — war beide Male grün, auch bei der Fassung, die den Reboot nicht überlebte.

Der Fix ist am Ende ein Dreizeiler in einem Shell-Skript.
Die beiden Reboots davor waren teurer als er und haben mehr gezeigt.
