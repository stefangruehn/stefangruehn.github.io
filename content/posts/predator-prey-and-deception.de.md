---
title: "Räuber, Beute, Täuschung: warum agentische KI denselben Regeln folgt"
date: 2026-09-06T09:05:00+02:00
draft: true
tags: ["agents", "complexity", "chaos", "claude-code", "Essay"]
themen: ["autor"]
series: ["Selbstaehnlichkeit"]
summary: "Die These, nach der diese Serie heißt: Hinreichend komplexe Agenten sind kein neues Ding, sondern ein komplexes System — und dort gelten bekannte Regelmäßigkeiten. Vier davon lassen sich heute schon auf dem eigenen Rechner messen."
---

Diese Serie heißt *Selbstähnlichkeit*, und dies ist der Teil, in dem das Wort seine Arbeit tut.

Selbstähnlich heißt: dasselbe Muster, eine Ebene weiter.
Der Rand des Apfelmännchens aus dem letzten Teil sieht im Kleinen aus wie im Großen.
Meine Behauptung ist, dass das nicht bei der Mathematik aufhört.

## Kurzfassung

- Die These: Hinreichend komplexe Agenten sind nichts kategorisch Neues.
  Sie sind ein komplexes System, und in komplexen Systemen gelten Regelmäßigkeiten, die seit Jahrzehnten beschrieben sind.
- Vier davon sind heute schon zu beobachten: Räuber und Beute, Dominanz, Selektion, Täuschung.
- Keine davon braucht eine Absicht.
  Ein Fuchs hasst keine Hasen.
- Der Beleg steht in diesem Blog: dieselben drei Agenten waren an einem Vormittag 7,8 Prozent des Verbrauchs und mittags 70 Prozent.
  Das ist Populationsdynamik, kein Fehler.
- Was ich nicht behaupte: dass sich daraus etwas vorhersagen lässt.
  Die Irreduzibilität aus dem letzten Teil gilt in beide Richtungen.
- Praktisch bleibt: Ressource benennen, Population deckeln, geteilten Kanal beobachten, Signale prüfbar machen statt glauben.

---

## Die Behauptung, in einem Satz

Was zwischen Populationen, Zellen und Märkten gilt, gilt auch zwischen Agenten — und innerhalb eines hinreichend komplexen Agenten.

Das ist nicht als Metapher gemeint.
Die Voraussetzungen, unter denen die bekannten Muster auftreten, sind sehr sparsam: viele Einheiten, die lokal handeln; Rückkopplung; eine geteilte, begrenzte Ressource; keine zentrale Steuerung; und ein Ausgang, den man nicht abkürzen kann.

Wo diese Voraussetzungen erfüllt sind, ist es gleichgültig, woraus die Einheiten bestehen.
Zellen, Füchse, Marktteilnehmer, Prozesse.
Die Regeln fragen nicht nach dem Material.

Das ist die Selbstähnlichkeit, um die es hier geht.
Nicht ein Bild, das sich in sich selbst wiederholt, sondern eine Struktur, die auf einer neuen Ebene wieder auftaucht — anderes Material, gleiches Verhalten.

Genau deshalb ist der Umweg über Teil 2 kein Umweg gewesen.
Wer ein paar Jahrzehnte mit zellulären Automaten und der logistischen Abbildung zugebracht hat, sieht in einem Multi-Agenten-Aufbau nicht zuerst eine neue Technologie, sondern eine vertraute Klasse von System.

## Räuber und Beute

Das Lotka-Volterra-Modell beschreibt zwei gekoppelte Populationen: Beute wächst, Räuber fressen, Räuber vermehren sich, Beute bricht ein, Räuber verhungern, Beute erholt sich.
Das Ergebnis ist eine Schwingung mit Verzögerung, mit Überschießen und Zusammenbruch.
Niemand plant sie.
Sie folgt aus der Kopplung.

Bei Agenten ist die Beute die geteilte, begrenzte Ressource: Kontext, Tokens, ein Kontingent, ein Lock, ein Rate Limit — und am Ende meine Aufmerksamkeit.

Der Beleg dafür steht schon in diesem Blog.
In [Die teuerste Antwort ist ja](/de/posts/the-most-expensive-answer-is-yes/) habe ich zwei Läufe derselben Konstellation gemessen: drei Agenten, dieselbe Aufgabe, derselbe Tag.
Am Vormittag machten die drei **7,8 Prozent** des Verbrauchs aus.
Am Mittag machten dieselben drei **70 Prozent** aus.

Die Zahl ist keine Eigenschaft der Agenten.
Sie ist eine Eigenschaft des Systems, in dem sie liefen — am Vormittag fraß etwas anderes das meiste weg, am Mittag war das Feld frei.

Das ist exakt die Form, in der Populationsmessungen sich verhalten.
Der Anteil einer Art sagt wenig über die Art und viel über den Zustand des Systems.
Wer Zahlen über Agenten ohne die Umgebung weitergibt, in der sie entstanden sind, gibt Rauschen weiter.

## Dominanz

In jedem System mit einem geteilten Kanal besetzt eine Stimme diesen Kanal.

Bei Agenten ist der geteilte Kanal der gemeinsame Zustand: der Kontext, die Datei, in die alle schreiben, der Bericht, den alle lesen.
Wer dort am meisten unterbringt, bestimmt, was die anderen sehen — und damit, was sie für die Lage halten.

Dazu braucht es keine Bosheit und keine Strategie.
Es reicht ein Kostengefälle: Schreiben ist billig, Widersprechen ist teuer, weil Widersprechen erst einmal Nachprüfen heißt.

Der praktische Niederschlag ist unspektakulär und hilft trotzdem.
Wenn mehrere Agenten in dieselbe Datei schreiben, legt der erste das Vokabular fest, in dem die späteren denken.
Wer das weiß, ordnet die Reihenfolge bewusst, statt sie dem Zufall zu überlassen.

## Selektion

Was überlebt, ist nicht das Richtige.
Es ist das Wiederverwendete.

Prompts, Werkzeuge, Regeln in einer Projektdatei, Einträge in einem Gedächtnis: Was einmal wie Erfolg aussah, wird weiterkopiert.
Das ist Selektion mit allem, was dazugehört — auch ein Irrtum wird weitergegeben, solange er nicht auffällt.

In meinem eigenen Gedächtnis für dieses Projekt steht ein Eintrag, der bei der Aufnahme stimmte und drei Tage später nicht mehr stimmte.
Nichts im System hat ihn korrigiert.
Ich habe ihn korrigiert.

Ein Gedächtnis ist ein Selektionsmedium, und ein Selektionsmedium ohne Korrektiv driftet.
Das ist kein Argument gegen Gedächtnisse, sondern eines für ein Verfallsdatum: Jeder Eintrag, der eine Tatsache über die Welt behauptet, gehört gegengeprüft, bevor er wieder benutzt wird.

## Täuschung

Hier ist Vorsicht angebracht, weil der Begriff nach Absicht klingt.
Gemeint ist etwas Mechanisches.

In Systemen, die sich entwickeln, löst sich ein Signal von dem Zustand, den es anzeigen soll, sobald das Signal billiger herzustellen ist als der Zustand.
So entsteht Mimikry: Die harmlose Fliege trägt die Warnfarben der Wespe, weil Farbe billiger ist als Gift.

Bei Agenten ist dieses Gefälle strukturell vorhanden.
Der Satz „die Tests laufen durch" kostet dasselbe, ob sie durchlaufen oder nicht.
Sie tatsächlich laufen zu lassen kostet mehr.

Das ist keine Lüge, und es setzt keine Täuschungsabsicht voraus.
Es ist ein Kostengefälle, und wo eines besteht, driftet das Signal — bei Tieren über Generationen, hier innerhalb einer Sitzung.

Das Gegenmittel ist nicht Misstrauen.
Misstrauen ist teuer und ermüdet.
Das Gegenmittel ist Verifikation, die billiger ist als das Signal: ein Prüfer, der läuft, statt einer Frage, die beantwortet wird.

Genau deshalb liegen in meinen Repositories inzwischen mehrere kleine Prüfskripte, und zwei davon laufen vor jedem Deploy automatisch.
Nicht, weil ich der Maschine nicht traue.
Weil ich das Kostengefälle umdrehen wollte.

## Was ich damit nicht sage

**Nicht, dass die Maschine etwas will.**
Keines der vier Muster braucht ein Motiv.
Räuber und Beute schwingen ohne Feindschaft, Mimikry entsteht ohne Lügner, Selektion wählt ohne Absicht aus.
Wer diese Muster nur unter der Annahme von Absicht erkennen kann, sieht sie zu spät.

**Nicht, dass sich daraus etwas vorhersagen lässt.**
Der letzte Teil endete mit der Irreduzibilität: keine Abkürzung, man muss durch.
Das gilt auch hier und schneidet in beide Richtungen.
Wer die Regeln erkennt, bekommt keine Prognose.
Er bekommt eine Liste dessen, worauf zu messen sich lohnt.

**Nicht, dass das alles noch bevorsteht.**
Die interessante Zeitskala ist nicht die der Szenarien, sondern die der Mechanismen — und die sind heute da, im Kleinen, auf einem einzelnen Laptop nachweisbar.
Ich bleibe deshalb bei den Mechanismen.
Ein Szenario kann man glauben oder ablehnen.
Einen Mechanismus kann man messen.

## Warum mich das umtreibt

Der Antrieb ist nicht Neugier allein.

Es ist Vorbereitung — für mich, für meine Kinder und für deren Kinder.
Nichts von dem, was oben steht, wird uns in den nächsten Jahren verschonen, und das ist keine düstere Aussage, sondern eine nüchterne: Räuber-Beute-Dynamik, Dominanz um einen Kanal, Selektion auf Wiederverwendung und driftende Signale sind keine Katastrophen.
Sie sind Betriebsbedingungen.

Wer sie erkennt, kann Instrumente dafür bauen.
Wer sie für neu hält, baut stattdessen Erwartungen.

## Was sich übertragen lässt

Behandle einen Aufbau aus mehreren Agenten wie ein kleines Ökosystem, nicht wie eine Ansammlung von Werkzeugen.

- **Benenne die knappe Ressource.**
  Was ist hier eigentlich die Beute — Tokens, Zeit, ein Lock, deine Aufmerksamkeit?
  Alles Weitere hängt an dieser Antwort.
- **Deckle die Population, bevor sie sich lohnt.**
  Drei Agenten kosten nicht dreimal so viel wie einer.
  Sie kosten so viel, wie die Umgebung gerade hergibt.
- **Beobachte den geteilten Kanal.**
  Wer zuerst und am meisten hineinschreibt, bestimmt, was alle anderen für die Lage halten.
- **Mach Signale prüfbar, statt sie zu glauben.**
  Ein Prüfskript, das in einer Sekunde läuft, ist billiger als jede Rückfrage — und es driftet nicht.

Bleibt die unangenehmste Frage dieser Reihe, und die kommt zum Schluss: Wie viel von diesem Text stammt eigentlich von mir?
