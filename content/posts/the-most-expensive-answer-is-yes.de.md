---
title: "Die teuerste Antwort ist ja: Was ein Nutzungslimit wirklich misst"
date: 2026-09-05T11:00:00+02:00
draft: false
tags: ["claude-code", "workflow", "performance", "agents", "context", "Field Notes"]
series: ["Codebuch"]
summary: "Um 10:07 war das Fünf-Stunden-Kontingent erschöpft und drei Agenten tot. Die naheliegende Erklärung waren die drei Agenten. Die Messung sagt: Sie waren 7,8 Prozent. Der Rest war eine Sitzung, die sich an sich selbst erinnerte."
---

Alle Teile, und ein Schema vorweg, das zeigt, worauf man sich einlässt: [Codebuch](/de/series/codebuch/).

## Kurzfassung

- An einem Vormittag im September war mein Fünf-Stunden-Kontingent um 10:07 erschöpft — nach zwei Stunden und 27 Minuten von fünf.
- Sekunden vorher waren drei Rechercheagenten gestorben, jeder beim nächsten eigenen Aufruf, im Abstand von zwölf Sekunden.
- Die naheliegende Erklärung lag auf der Hand: drei Agenten gleichzeitig.
  Die Messung sagt etwas anderes.
  Die drei waren **7,8 Prozent** des Verbrauchs.
- Der Rest war die Sitzung selbst: 394 Anfragen, deren mitgeschleppter Kontext von 68.000 auf 388.000 Tokens wuchs.
- Die Anfragen halbierten sich im Lauf des Vormittags, der Verbrauch je Viertelstunde blieb gleich.
  Je Anfrage ist das der Faktor fünf — bei nachweislich weniger Tätigkeit.
- Über dreißig Runden bestanden aus „ja", „flash" oder „ja, flash".
  Drei Zeichen Eingabe, 388.000 Tokens Abrechnung.
- Am Tag darauf, mit Kontextschnitten an den richtigen Stellen: fast doppelt so viele Runden, ein Drittel weniger Kontext, gleich viel Ergebnis.

---

## Sieben Minuten nach zehn

Ich hatte drei Agenten losgeschickt, jeden mit einem eigenen Rechercheauftrag rund um ein Display, das sein Bild verlor.
Sieben Minuten später waren sie tot.

Sie starben nicht gemeinsam, sondern einzeln, jeder beim nächsten Aufruf, den er von sich aus machte:

```
10:06:45   Agent terminated early due to an API error
10:06:46   Agent terminated early due to an API error
10:06:57   Agent terminated early due to an API error
```

Was dahinterstand, stand im Transkript der Hauptsitzung:

```
rateLimitType: "five_hour"   status: "rejected"   HTTP 429
"You've hit your session limit · resets 12:40pm (Europe/Berlin)"
```

Das Fenster lief von 07:40 bis 12:40.
Erschöpft war es um 10:07, nach zwei Stunden und 27 Minuten.

Die Sitzung konnte den Tod ihrer eigenen Kinder nicht mehr verarbeiten.
Um 10:07:01 kam die Meldung an, und die Antwort darauf war wieder die Limit-Meldung.
Mein Hinweis um 10:07:27, dass das Limit erreicht sei, lief in dieselbe Wand.

## Die Erklärung, die sich anbietet

Drei Agenten parallel, sieben Minuten später ist das Kontingent leer.
Ich glaube, jeder würde denselben Schluss ziehen, und ich habe ihn auch gezogen.

Er ist falsch.

Das ist kein Bauchgefühl gegen ein anderes, denn die Zahlen liegen vor.
Jede Zeile in einer Sitzungsdatei nennt, wie viele Tokens die Anfrage gelesen hat, und die Agenten schreiben ihre eigenen Dateien daneben.
Man muss es nur zusammenzählen.

| | Kontext-Tokens | Ausgabe |
|---|---|---|
| Hauptsitzung, 394 Anfragen | 94,7 M | 734 k |
| drei Agenten zusammen | 8,0 M | 44 k |
| **Anteil der Agenten** | **7,8 %** | **5,7 %** |

Die drei sichtbaren Verdächtigen waren ein Dreizehntel.
Die anderen zwölf Dreizehntel waren die Sitzung, in der ich saß.

## Was die Messung sagt

Interessanter als die Summe ist der Verlauf.
Hier ist derselbe Vormittag, in Viertelstunden zerlegt:

| Uhrzeit | Anfragen | Kontext je Anfrage | Verbrauch |
|---|---|---|---|
| 07:45 | 59 | 68 k | 4,0 M |
| 08:00 | 63 | 141 k | 8,9 M |
| 08:15 | 51 | 205 k | 10,4 M |
| 08:30 | 44 | 252 k | 11,1 M |
| 08:45 | 33 | 289 k | 9,6 M |
| 09:00 | 36 | 320 k | 11,5 M |
| 09:15 | 25 | 343 k | 8,6 M |
| 09:30 | 32 | 363 k | 11,6 M |
| 09:45 | 30 | 388 k | 11,6 M |
| 10:00 | 21 | 353 k | 7,4 M (angebrochen) |

Lies die erste und die letzte volle Zeile nebeneinander.
Um 07:45 kosteten **59** Anfragen vier Millionen Tokens.
Um 09:45 kosteten **30** Anfragen elf Komma sechs Millionen.

Die Tätigkeit halbiert sich, die Rechnung verdreifacht sich.
Je Anfrage ist das der Faktor fünf, und zwar durchgehend in eine Richtung: Die mittlere Spalte steigt in jeder einzelnen Zeile.

Am Anfang habe ich viel getan und wenig bezahlt.
Am Ende habe ich wenig getan und viel bezahlt.
Dazwischen ist nichts passiert außer dem, was immer passiert: Die Sitzung wurde länger.

## Die Regel darunter

Ein Sprachmodell hat kein Gedächtnis zwischen zwei Anfragen.
Was wie Erinnerung aussieht, ist die vollständige bisherige Unterhaltung, die bei jeder neuen Anfrage noch einmal mitgeschickt und noch einmal gelesen wird.

Daraus folgt eine Rechenregel, die den ganzen Rest erklärt:

> Verbrauch ≈ Anzahl der Anfragen × mittlerer Kontext je Anfrage.

Ein Limit misst also nicht, wie viel ein Agent arbeitet.
Es misst, wie viel er sich merken muss.

Und weil der zweite Faktor mit jeder Runde wächst, wird dieselbe Frage am Ende einer Sitzung um ein Vielfaches teurer als am Anfang — ohne dass die Antwort besser wird.

## Dieselbe Messung, vier Stunden später

Wenn die Lehre lautete „Agenten sind billig", wäre der Beitrag hier zu Ende und die Lehre falsch.

Dreieinhalb Stunden nach dem Abbruch lief dieselbe Konstellation ein zweites Mal: frische Sitzung, wieder drei Agenten, wieder ein Limit.
Diesmal fällt die Messung genau umgekehrt aus.

| Zweites Fenster | Anfragen | Kontext gelesen |
|---|---|---|
| Hauptsitzung 12:48–13:19 | 128 | 11,6 M |
| Agent 1 | 102 | 10,2 M |
| Agent 2 | 113 | 8,9 M |
| Agent 3 | 97 | 8,1 M |
| **Anteil der Agenten** | **71 %** | **70 %** |

7,8 Prozent am Vormittag, 70 Prozent am Mittag.
Gleiche Werkzeuge, gleicher Tag, gleicher Rechner.

Damit ist die erste Zahl keine Eigenschaft von Agenten, sondern eine Eigenschaft dieses einen Vormittags.
Was sich nicht ändert, ist die Regel darunter.
Am Vormittag drehte die Sitzung die vielen Runden mit dem großen Kontext, am Mittag taten es die Agenten — 312 Anfragen zu dritt gegen eine frisch geleerte Sitzung.

Ein Agent ist nicht billig.
**Er fängt nur klein an**, und dann wächst er wie alles andere auch.

Eine ehrliche Anmerkung dazu, weil sie sich beim Nachrechnen aufdrängt: Das erste Fenster hielt 102,7 Millionen Tokens aus, das zweite brach schon bei 38,8 Millionen ab — und in diesem zweiten Fenster gab es keinen Verbrauch außerhalb dieser Sitzung.
Ein Limit ist also nicht in gelesenen Tokens ausgedrückt, jedenfalls nicht linear.
Den eigenen Verbrauch kann man messen.
Die Grenze, an der er abbricht, nicht.

## Dreißig Runden „ja"

Woran arbeitet man um zehn nach zehn, wenn eine Anfrage 388.000 Tokens kostet?

An Hardware.
Firmware aufspielen, hinsehen, berichten, bestätigen — und wieder von vorn.
Der Zyklus erzeugt genau die Sorte kurzer Runden, bei der das Verhältnis zwischen Eingabe und Rechnung vollständig kippt.

Über dreißig meiner Nachrichten an diesem Vormittag bestanden aus „ja", „flash" oder „ja, flash".

Drei Zeichen.
Und jedes davon zieht den vollständigen bisherigen Verlauf noch einmal durch die Abrechnung.
Zum Schluss waren das 388.000 Tokens für ein Wort, das keine Information trägt, sondern nur eine Erlaubnis.

Das ist die Stelle, an der der Beitrag praktisch wird: Eine Bestätigungsrunde ist nicht billig, weil sie kurz ist.
Sie ist genauso teuer wie jede andere Runde.

Und eine Bestätigung, die man dauerhaft erteilen kann, kostet einmal statt dreißigmal.
Was ein Projekt immer erlauben soll, gehört in seine Konfiguration und nicht in eine Rückfrage je Vorgang.
Für alles, was gefährlich oder nach außen wirksam ist, bleibt die Rückfrage richtig — nur eben nicht für das Flashen desselben Chips zum einunddreißigsten Mal.

## Das Gegenmittel, gemessen

Bis hierhin ist das eine Diagnose.
Das Gegenmittel ist unspektakulär: den Kontext wegwerfen, sobald der Stand woanders steht.

Am nächsten Morgen habe ich es gemessen.
Zwei Vormittage, dasselbe Projekt, fast gleich lang — einmal ohne Schnitt, einmal mit:

```
04.09.  07:48–10:07   394 Anfragen   94,7 M Kontext   734 k Ausgabe   240 k/Anfrage
05.09.  05:03–07:34   713 Anfragen   61,7 M Kontext   682 k Ausgabe    87 k/Anfrage

Anfragen ×1,81     Kontext ×0,65     Ausgabe ×0,93     Kontext je Anfrage ×0,36
```

Fast doppelt so viele Runden.
Ein Drittel weniger Kontext.
Und die Ausgabe — das, was tatsächlich an Arbeit entstanden ist — lag bei 93 Prozent.

Bezahlt habe ich dafür 65 Prozent.
Je Anfrage war der zweite Tag **2,8-mal billiger**, und die teuerste Einzelanfrage hat sich halbiert.

Man sieht die Schnitte im Dateisystem.
Jeder Schnitt legt eine neue Sitzungsdatei an, und am zweiten Tag liegen zwischen ihnen Sekunden statt Stunden:

```
04:06:13 → 04:06:33 → 04:06:50        04:55:33 → 04:55:45
```

Zwei Einschränkungen, damit die Zahlen nicht mehr behaupten, als sie hergeben.
Es sind zwei verschiedene Tage mit verschiedenen Aufgaben, also n = 2; belastbar ist davon allein der Kontext je Anfrage, weil er nicht davon abhängt, wie viel an einem Tag zu tun war.
Und der erste Tag ist noch zu günstig gerechnet — seine Kurve stieg noch, als das Limit sie abschnitt.

Die naheliegende Gegenrechnung wäre, dass sieben Sitzungen statt drei auch sechsmal Wiederaufsetzen bedeuten und die Ersparnis genau dort wieder verloren geht.
Gemerkt habe ich davon nichts.
Die neuen Sitzungen waren sofort arbeitsfähig, und der Grund dafür ist derselbe wie die Ersparnis: Schneiden darf man erst, wenn der Stand geschrieben ist.
Wenn er geschrieben ist, kostet das Wiederaufsetzen nichts.

## Wer den Schnitt vorschlagen muss

Der Schnitt lässt sich nicht automatisieren, und der Grund dafür ist unangenehm sauber.

**Der Agent sieht die Kontextgröße, aber nicht, ob der Gedanke fertig ist.
Ich sehe, ob der Gedanke fertig ist, aber nicht die Kontextgröße.**

Keine der beiden Seiten weiß allein genug, um zu entscheiden.
Also muss der Schnitt von der Seite vorgeschlagen werden, die die Zahl hat, und von der Seite entschieden werden, der die Arbeit gehört.

Daraus folgt etwas, das ich nicht erwartet hatte.
Ein Agent, der vorschlägt, den Kontext zu leeren, schlägt die Löschung seines eigenen Gedächtnisses vor.
Es gibt keinen Anreiz dafür, der aus der Situation selbst käme.
Es passiert nur, wenn es als Regel aufgeschrieben ist — an dem Vormittag war es das nicht, und das Ergebnis waren drei Agenten in einem fast leeren Kontingent.

## Was der Abbruch zerstört hat

Fast nichts, und die Ausnahme ist der interessantere Teil.

Die Commits von 09:54 und 09:57 waren unversehrt, die 71 uncommitteten Zeilen im Arbeitsverzeichnis ebenfalls.
Die Transkripte der drei Agenten liegen vollständig vor, 296, 361 und 446 Kilobyte.

Verloren war keine Information, sondern Verdichtung.
Alle drei steckten noch im Lesen, keiner war bei der Auswertung.
Das Material war da, der Schluss daraus wurde nie gezogen.

Ein einziger Befund hat sich gerettet, und zwar nur, weil der Agent ihn zufällig als Satz aufgeschrieben hatte, bevor er starb: dass die Initialisierung der Werksfirmware ohne den Befehl endet, der das Display einschaltet.
Genau der Hinweis, hinter dem wir her waren.

Daraus ist eine Arbeitsregel geworden.
Agenten sollen ihre Befunde fortlaufend in eine Datei schreiben, nicht am Ende berichten.
Was nur im Verlauf eines Agenten steht, stirbt mit ihm.
Was in einer Datei steht, nicht.

## Was ich gelernt habe

- **Nicht die Arbeit kostet, sondern die Erinnerung.**
  Eine Sitzung, die nichts tut, als sich zu erinnern, wird mit jeder Runde teurer.
- **Der Ausweg ist nicht Zurückhaltung, sondern Vergessen zur richtigen Zeit.**
  Ein Commit ist auch ein Kontextschnitt: Was dokumentiert ist, muss nicht erinnert werden.
- **Bestätigungsrunden sind der eigentliche Posten.**
  Jedes vermiedene „ja" spart einen vollen Durchlauf. Eine dauerhafte Erlaubnis macht aus dreißig Runden eine.
- **Das sparsame Werkzeug gehört an den Anfang.**
  Als ich die drei Agenten startete, waren 87 der 102 Millionen schon weg. Ich habe das billige Werkzeug zum teuersten Zeitpunkt geholt.
- **Die Intuition zeigt auf die falsche Stelle.**
  Drei Agenten parallel sind sichtbar und fühlen sich nach Aufwand an. Der Kontext, der bei jeder Anfrage stillschweigend mitläuft, ist unsichtbar — und war es zu 92 Prozent.
- **Eine Messung ist noch kein Gesetz.**
  Dieselbe Zahl kam am selben Tag einmal auf 7,8 und einmal auf 70 Prozent. Wer nur einmal misst, schreibt die Hälfte auf.

## Womit ich anfangen würde

Wenn dir dasselbe passiert ist und du wissen willst, woran es lag, ist das die Reihenfolge, in der ich fragen würde.

1. **Wie lang war die Sitzung, als es teuer wurde?**
   Nicht wie viel du getan hast. Wie lange du schon dieselbe Unterhaltung führst.
2. **Wie viele deiner letzten dreißig Nachrichten waren Bestätigungen?**
   Zähl sie. Es sind fast immer mehr, als man denkt, und sie kosten dasselbe wie jede andere Nachricht.
3. **Was davon kannst du einmalig erlauben, statt es jedes Mal zu bestätigen?**
   Alles, was wiederkehrt und weder gefährlich noch nach außen wirksam ist.
4. **Wann stand dein Stand zuletzt vollständig auf Platte?**
   Genau dort war der richtige Moment zu schneiden. Bei mir war es ein Commit um 09:57 — zehn Minuten vor dem Abbruch, und da kostete jede weitere Anfrage schon 388.000 Tokens.
5. **Und erst dann: Wären Agenten hier richtig gewesen?**
   Sie wären es gewesen — aber zu Beginn der Recherche, nicht am Ende eines langen Vormittags.

Die unangenehme Hälfte davon ist die vierte Frage, und sie hat mit Tokens am Ende wenig zu tun.
Wer den Kontext wegwerfen will, muss vorher aufgeschrieben haben, was er weiß.
Die Ersparnis ist nur die Quittung dafür.
