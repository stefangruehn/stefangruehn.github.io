---
title: "Der dritte Kanal: Was ständig gilt, gehört nicht in den Dialog"
date: 2026-10-03T01:50:00+02:00
tags: ["claude-code", "workflow", "context", "measurement", "Field Notes"]
themen: ["kosten"]
summary: "Wie voll der Kontext ist, welches Modell läuft, wie nah das Fünf-Stunden-Limit ist: Im Terminal steht nichts davon, und jede Frage danach kostet eine Runde. Eine Statuszeile zeigt es, ohne etwas zu verbrauchen. Beim Bauen stellte sich heraus, dass der Host alle Zahlen längst kannte und nur keine anzeigte."
---

## Kurzfassung

- Der Zustand einer Agenten-Sitzung ist im Terminal unsichtbar: Füllstand des Kontexts, Modell, Effort, Limits, Stummschaltung.
- Jeder Weg, ihn zu erfahren, ist eine Runde, und eine Runde kostet den vollen mitgeschleppten Kontext. Wer nach dem Kontextstand fragt, bezahlt in genau der Währung, nach der er fragt.
- Die Statuszeile ist ein dritter Kanal neben Eingabe und Ausgabe. Sie zeigt Zustand, ohne Tokens oder Runden zu verbrauchen.
- Die erste Fassung rechnete den Füllstand selbst aus und zeigte 45 Prozent. Der Host lieferte die Zahl fertig mit: 11 Prozent, bei einem Fenster von einer Million Tokens statt der angenommenen 200.000.
- Die wichtigste Zahl war eine, nach der niemand gesucht hatte: das Fünf-Stunden-Limit, live in Prozent.
- Die Zeile halbiert die Asymmetrie zwischen Mensch und Agent. Wie voll es ist, sehe jetzt ich. Ob der Stand gesichert ist, weiß weiterhin nur der Agent.
- Wirksam wird sie erst durch eine Schwelle: Ab gelb schlägt der Agent den Kontextschnitt selbst vor.

---

## 45 Prozent, die 11 waren

Am 7. September wollte ich eine Statuszeile für Claude Code, eine Zeile unter dem Eingabefeld, die ständig anzeigt, was gerade gilt.
Claude baute sie in einem Nachmittag, und die erste Fassung war ordentlich gemacht.
Ein Python-Skript las das Transkript der Sitzung, summierte die Tokens, teilte durch die Größe des Kontextfensters und zeigte das Ergebnis in Prozent.
Es cachte, damit es schnell blieb, es war getestet, und es zeigte 45 Prozent.

Dann lag zum ersten Mal echte Eingabe des Hosts auf der Platte.
Claude Code ruft das Skript bei jeder Aktualisierung auf und gibt ihm dabei ein JSON-Dokument mit, 1,7 Kilobyte groß.
Darin stand `context_window.used_percentage`, fertig gerechnet.
Der Wert war 11, nicht 45.

Der Fehler steckte im Nenner.
Claude hatte gegen ein Fenster von 200.000 Tokens gerechnet, weil das die Größe war, die es aus dem Gedächtnis kannte.
Das Fenster dieser Sitzung war eine Million.
Die Eigenrechnung war sorgfältige Arbeit an einer Zahl, die zwei Zentimeter daneben schon dastand.

Die Regel, die hier verletzt wurde, stammt aus dem Hardware-Projekt, an dem wir zur selben Zeit arbeiteten: Aussagen kommen vom Gerät, nicht aus dem Datenblatt.
Diesmal war das Datenblatt das eigene Gedächtnis des Agenten, und das Gerät war eine kleine JSON-Datei.

## Die Zahl war da, sie stand nur nirgends

Der Irrtum hat die Idee hinter der Zeile verschoben.
Ich hatte angenommen, es fehle eine Messung.
Es fehlte keine.
Der Host kennt seinen Zustand vollständig, und er gibt ihn an das Skript weiter: Füllstand, Modell, Effort-Level, Kosten in Dollar, Trefferquote des Caches.
Er zeigt davon nur nichts an.
Die Statuszeile fügt keine Information hinzu, sie macht vorhandene sichtbar.

Am meisten überrascht hat ein Feld, nach dem wir gar nicht gesucht hatten: `rate_limits.five_hour`, das Fünf-Stunden-Limit, live in Prozent, dazu das Wochenlimit.
An genau dieser Grenze waren am 4. September zwei Sitzungen gestorben.
Bis dahin kam ich an die Zahl nur über `/usage`, also über eine eigene Runde.
Sie stand die ganze Zeit im JSON.
Gefunden hat sie die Zeile beim Bauen, weil die Feldliste aus einer echten Eingabe kam und nicht aus der Dokumentation.

Ein einziges Feld liefert der Host nicht: welchen Vertrag ich habe.
Das Abo steht in der Datei `~/.claude.json`, im Zustand des Clients, nicht im Statuskanal.
Was die laufende Sitzung betrifft, wird durchgereicht, was das Konto betrifft, nicht.

## Jede Frage ist eine Runde

Warum eine Zeile und keine Frage?
Weil eine Frage nicht umsonst ist.
Wie teuer, habe ich in [Die teuerste Antwort ist ja](/de/posts/the-most-expensive-answer-is-yes/) nachgerechnet: Ein „ja, flash“ von drei Zeichen wurde am Ende einer langen Sitzung mit 388.000 Tokens abgerechnet, weil jede Anfrage den ganzen bisherigen Kontext mitschickt.
Eine Runde, die nur einen Zustand abholt, kostet so viel wie eine, die arbeitet.

Daraus folgt eine unangenehme Rechnung.
Wer den Agenten fragt, wie voll sein Kontext ist, macht ihn mit der Frage voller.
Er bezahlt die Auskunft in genau der Währung, nach der er fragt.

Die Statuszeile ist nicht Eingabe und nicht Ausgabe.
Sie ist ein dritter Kanal, der neben dem Dialog läuft, und sie verbraucht keine Runde, kein Token und keine Rückfrage.
Der Preis wird in einer anderen Währung bezahlt.
Das Skript startet bei jeder Aktualisierung als eigener Prozess, liest das JSON und gibt eine Zeile aus.
Gemessen sind es 26 Millisekunden, und das Transkript wird seit der Korrektur gar nicht mehr gelesen.

## Zwei Behelfe für dasselbe Loch

Vor der Zeile gab es zwei Vorkehrungen, die einander widersprachen.
In meinen Anweisungen an Claude stand, dass der Agent ansagen muss, wann ein Kontextschnitt mit `/clear` fällig ist.
Und es gab ein Kürzel, mit dem ich dem Agenten den Kontextstand meldete.
Einmal wusste es also der Agent und sagte es mir, einmal wusste ich es und sagte es ihm.
Im Rückblick ist das der Beleg dafür, dass die Zahl an keiner Stelle einfach dastand: Beide Seiten kannten sie nur ungefähr, und jede hatte einen Behelf in die andere Richtung gebaut.

In der teuersten Antwort hatte ich das noch als Arbeitsteilung beschrieben:
„Der Agent sieht die Kontextgröße, aber nicht, ob der Gedanke fertig ist.
Ich sehe, ob der Gedanke fertig ist, aber nicht die Kontextgröße.“
Die zweite Hälfte stimmt seit dem 7. September nicht mehr.

Das Kürzel ist gestrichen.
Die Ansage bleibt, und der Grund dafür ist die eigentliche Pointe.
Die Zahl sagt, wie voll der Kontext ist.
Sie sagt nicht, ob der Stand auf der Platte liegt, ob also ein Schnitt jetzt etwas wegwirft.
Das eine sehe jetzt ich, das andere weiß weiterhin nur der Agent.
Die Statuszeile beseitigt die Asymmetrie nicht, sie halbiert sie.

## Ton für Ereignisse, Zeile für Zustände

Der erste Kanal neben dem Dialog war ein Ton.
In [Ruf mich, wenn du mich brauchst](/de/posts/call-me-when-you-need-me/) ging es darum, dass der Agent mich zurückholt, wenn er fertig ist oder eine Entscheidung braucht, statt dass ich alle zwei Minuten nachsehe.
Dort wurde aus dem Nachsehen ein Rückruf.
Hier wird aus dem Nachfragen eine Anzeige, die ständig anliegt.
Ein Ton meldet, dass etwas passiert ist.
Eine Zeile zeigt, was gerade gilt.

So sieht sie aus:

```
Pro │ Opus 5 · high │ ctx 12% · cache 97% │ 5h 38% · 7d 68% │ snd
```

Von links: das Abo, Modell und Effort, Füllstand und Cache, die beiden Limits, und ob die Töne an sind.
Füllstand und Limits wechseln die Farbe, wenn es eng wird.

Die Auswahl war vor allem Verzicht.
Projekt und Branch stehen auch im JSON, ebenso die Kosten in Dollar.
Sie blieben draußen, aus demselben Grund, aus dem es nur zwei Töne gibt: Ein Ton, der immer kommt, wird nicht mehr gehört, und eine Zeile, die alles zeigt, wird nicht mehr gelesen.

Das unscheinbarste Feld ist das letzte.
Ein stummgeschaltetes Terminal sah bis dahin genauso aus wie ein ruhiges.
Wer die Töne für eine Sitzung abgeschaltet und es vergessen hatte, wartete auf einen Rückruf, der nicht kommen konnte.
Jetzt steht dort `snd` oder `mute`.

## Erst die Schwelle macht die Zeile wirksam

Drei Tage nach dem Bau kam die Regel dazu, die aus der Anzeige ein Werkzeug gemacht hat.
Steht der Füllstand auf gelb, ab 25 Prozent, schlägt Claude den Kontextschnitt in derselben Runde vor, auch wenn der Stand gerade nicht rund ist.
Und vorher sichert es, was noch nicht auf der Platte liegt, ohne zu fragen.

Damit sehen Mensch und Agent zum ersten Mal denselben Zustand zur selben Zeit.
Ich sehe die Farbe umschlagen, und der Agent hat eine Regel an genau dieser Farbe.
Weil die Schwelle in der Zeile steht und in den Anweisungen, kann ich nachprüfen, ob er sich an seine eigene Regel hält.

Die zweite Hälfte der Regel ist die wichtigere.
Eine Schwelle allein hätte den teuersten Fall erzeugt, den es gibt: einen pünktlichen Schnitt durch ungesicherte Arbeit.
Die Zahl sagt eben nur, wie voll es ist.

Ein Kanal, der richtig misst und richtig anzeigt, bleibt folgenlos, solange niemand eine Schwelle daran hängt.

## Was ich gelernt habe

- **Zustand gehört nicht in den Dialog.** Was ständig gilt, abzufragen, kostet jedes Mal eine Runde. Eine Anzeige kostet einen Prozessstart.
- **Erst nachsehen, dann rechnen.** Die erste Fassung hat sorgfältig eine Zahl erfunden, die der Host fertig mitlieferte. Die Feldliste kam am Ende aus einer echten Eingabe und nicht aus dem Gedächtnis.
- **Weniger Felder sind die Entscheidung.** Was im JSON steht, gehört nicht deshalb schon in die Zeile.
- **Die Zahl ersetzt kein Urteil.** Sie sagt, wie voll es ist, nicht, ob ein Schnitt jetzt etwas kostet. Deshalb bleibt die Ansage beim Agenten.
- **Eine Anzeige wirkt erst mit einer Schwelle.** Ohne Regel daran ist sie nur ein Instrument, mit Regel ist sie ein Auslöser für beide Seiten.

## Das Gleiche an deinem Rechner

Claude Code ruft für die Statuszeile ein beliebiges Kommando auf und gibt ihm den Zustand der Sitzung als JSON mit.
Bevor du etwas anzeigst, lass das Kommando diese Eingabe einmal in eine Datei schreiben und sieh sie dir an.
Die Felder ändern sich zwischen Versionen, und was dort steht, ist verlässlicher als jede Liste aus dem Gedächtnis, auch aus dem eines Agenten.
Eine Änderung an der Zeile gilt übrigens sofort, ohne Neustart der Sitzung.
