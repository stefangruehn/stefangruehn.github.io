---
title: "Tippfehler sind billig: Worauf es beim Reden mit Claude Code wirklich ankommt"
date: 2026-09-03T19:40:00+02:00
draft: true
tags: ["claude-code", "rookie", "workflow"]
summary: "In einem zusammenhängenden Messzeitraum habe ich gut vierhundert Nachrichten an Claude Code getippt; in jeder zehnten steht ein Umlaut. Korrigiert wurde nie etwas, verstanden wurde trotzdem alles. Teuer wird nicht die Schreibweise — teuer wird der Satz, der zwei Ergebnisse zulässt."
---

## Kurzfassung

- Ich tippe schnell und schlampig: keine Umlaute, vertauschte Buchstaben, fehlende Wörter.
- Ausgezählt über einen zusammenhängenden Messzeitraum, am dichtesten Tag über hundert Nachrichten: In gut jeder zehnten steht ein Umlaut. Das sind 10,3 Prozent.
- Angemerkt wurde davon nichts. Verstanden wurde trotzdem alles.
- Was Arbeit macht, ist nicht die falsche Schreibweise, sondern der Satz, der zwei verschiedene Ergebnisse zulässt.
- Ein einzelnes Wort kann eine ganze Behauptung tragen. Dann ist eine saubere Ersetzung formal richtig und inhaltlich falsch.
- Die Regel, die beides auflöst: sag, was hinterher **wahr sein soll**, nicht welchen Text du getauscht haben willst.

---

## Zehn Prozent

Ich schreibe auf einer US-Tastatur.
Viele Entwickler hier tun das, und der Grund ist unspektakulär: `[ ] { } \ | @ ~` liegen dort direkt oder hinter Shift, auf einer deutschen Belegung hinter AltGr.
Backtick und Akzent sind auf der deutschen Tastatur außerdem tote Tasten — du tippst sie zweimal oder mit einem Leerzeichen hinterher.
Wer den ganzen Tag Pfade, Codeblöcke und Optionen schreibt, zahlt diese Steuer auf jede Zeile.

Der Preis dafür sind die Umlaute.
Ich habe einen Compose-Key eingerichtet, er liegt auf der rechten Strg-Taste: Compose, dann `"`, dann `a` ergibt ä.
Drei Anschläge statt einem.
Meistens bin ich zu faul dafür.

„Meistens" war lange nur ein Gefühl, also habe ich es zählen lassen.
Ausgewertet wurde ein zusammenhängender Messzeitraum über alle Projekte hinweg, am dichtesten Tag über hundert Nachrichten.
Gut vierhundert Nachrichten von mir, davon 43 mit mindestens einem Umlaut.
Zehn Komma drei Prozent.
Das häufigste Wort, das ich stattdessen schreibe, ist `fuer` — achtundvierzig Mal.

In keiner einzigen davon kam ein Hinweis zurück, dass ich es anders schreiben solle.

## Warum ein Buchstabendreher nichts kostet

Ich habe in diesen Sitzungen „haeufugen" geschrieben, „beginen", „teiner", „vu verwenden".
Nichts davon führte zu einer Rückfrage, und keins davon wurde falsch verstanden.

Der Grund ist unromantisch: Es gibt jeweils nur ein Wort, das gemeint sein kann.
„haeufugen" steht in einem Satz über meine Tippfehler — daraus wird „häufigen", und zwar ohne Rateanteil.
Sprache hat genug Redundanz, dass ein verrutschter Buchstabe die Bedeutung nicht mitnimmt.
Der Satz drumherum trägt sie.

Eine Korrektur hätte mich also Aufmerksamkeit gekostet und nichts eingebracht.
Sie hätte den Blick von der Sache auf die Schreibweise gezogen, mitten in einer Arbeit, in der die Sache das Teure ist.

Das ist keine Nachsicht und kein Charakterzug, sondern eine Voreinstellung.
Wer „korrigier mein Deutsch bitte mit" sagt, bekommt es ab da korrigiert.
Umgekehrt gilt: Es gibt nichts, wofür du dich beim Tippen zusammenreißen müsstest.

## Zwei Lesarten kosten sofort

An einem Abend im September schrieb ich diesen Satz:

> der technical deep dive tag sollte immer mit grossbuchstaben beginen

„beginen" blieb unerwähnt.
Zurück kam trotzdem eine Frage — und zwar nach etwas ganz anderem: Soll es *Technical Deep Dive* heißen oder *Technical deep dive*?

Das ist berechtigt.
„Mit Großbuchstaben beginnen" lässt beides zu, und der Tag steht auf sechs Beiträgen in zwei Sprachen.
Zwei Lesarten, zwei verschiedene Ergebnisse, ein Arbeitsgang Unterschied.

Der Tippfehler im selben Satz war belanglos.
Die Mehrdeutigkeit war es nicht.
Genau dort verläuft die Grenze — nicht zwischen sauber und schlampig geschrieben, sondern zwischen einer Lesart und zweien.

## Ein Wort, das eine Behauptung trägt

Die teure Sorte sieht harmlos aus, weil sie sauber formuliert ist.

Stell dir ein Handbuch vor, in dem der Satz steht:

> Der Dienst schreibt keine **personenbezogenen** Daten ins Log.

Du hältst „personenbezogen" für zu behördlich und möchtest überall „sensibel" lesen.
Also sagst du: *Ersetze überall „personenbezogen" durch „sensibel".*

Der Auftrag ist eindeutig ausführbar.
Vier Fundstellen, vier Ersetzungen, kein Fehler dabei.
Drei davon sind harmlos: eine Überschrift, ein Aufzählungspunkt, ein erklärender Satz.

Die vierte stand in einer Verneinung, und dort kippt sie:

> Der Dienst schreibt keine **sensiblen** Daten ins Log.

Das ist eine andere Aussage.
Sie kann falsch sein, während die alte richtig war — der Dienst schreibt vielleicht sehr wohl Namen und Kennungen ins Log, nur eben nichts, was jemand „sensibel" nennen würde.
Niemand hat hier etwas falsch gemacht: Die Ersetzung war korrekt, der Satz war es danach nicht mehr.

Der Fehler steckte im Auftrag.
Er nannte eine **Zeichenkette** und meinte ein **Ergebnis**.

Ein Tippfehler in diesem Auftrag hätte übrigens nichts geändert.
„Erstze überall personenbezogen durch sensibel" wäre genauso ausgeführt worden, mit demselben falschen Satz am Ende.

## Woran du es vorher merkst

Drei Stellen, an denen ein einzelnes Wort mehr trägt als sich selbst:

- **Verneinungen.** „kein", „nicht", „nie", „ohne". Das verneinte Wort ist die Aussage.
- **Vergleiche.** „schneller als", „mehr als", „der einzige". Wird der Vergleichsgegenstand ausgetauscht, wird der Vergleich zu einer anderen Behauptung.
- **Einschränkungen.** „nur", „erst", „außer", „ab". Sie grenzen etwas ein, und das Eingegrenzte hängt am Wort.

Steht dein Suchbegriff an einer dieser Stellen, lohnt der zweite Satz.
Er ist nicht länger als der erste, er beschreibt nur etwas anderes — nämlich den Zustand statt der Handlung:

> Ich will, dass im Handbuch durchgehend „sensibel" steht, außer wo eine Aussage davon abhängt, dass es um personenbezogene Daten geht.

Das ist keine Anweisung mehr, die man blind ausführen kann.
Sie zwingt zum Lesen jeder einzelnen Fundstelle, und genau das war ja gewollt.

## Was ich gelernt habe

- **Schreibfehler sind gratis.** Sie kosten nichts, weil der Kontext die Bedeutung trägt. Wer sich beim Tippen zusammenreißt, spart an der falschen Stelle.
- **Eindeutigkeit ist nicht dasselbe wie Korrektheit.** Ein grammatikalisch sauberer Satz kann zwei Ergebnisse zulassen, ein hingerotzter nur eins.
- **Zähl die Lesarten, nicht die Fehler.** Wenn dir dein eigener Satz zwei verschiedene Ergebnisse liefern könnte, wird nachgefragt — oder es wird geraten.
- **Sag den Zustand, nicht die Operation.** „Ersetze X durch Y" ist ausführbar. „Hinterher soll gelten, dass …" ist überprüfbar.
- **Verneinungen sind die gefährlichste Stelle im Text.** Dort trägt ein Wort die ganze Behauptung, und eine korrekte Ersetzung macht daraus eine andere.

## Wenn du vor derselben Frage stehst

Du fängst gerade an und fragst dich, wie sorgfältig du formulieren musst.
Die Antwort ist zweigeteilt, und die angenehme Hälfte kommt zuerst.

1. **Tipp, wie du tippst.** Umlaute weglassen, Buchstaben verdrehen, mitten im Satz die Richtung wechseln — nichts davon muss dich bremsen. Es kostet nichts.
2. **Lies deinen Auftrag noch einmal, aber nur mit einer Frage im Kopf:** Kann das auf zwei Arten ausgehen? Nicht: ist das schön geschrieben.
3. **Wenn ja, nenn das Ergebnis.** Ein Satz, der beschreibt, was hinterher stimmen soll, ist mehr wert als drei sauber formulierte Befehle.
4. **Achte besonders auf Verneinungen, Vergleiche und Einschränkungen.** Dort steckt die Bedeutung in einem einzelnen Wort.
5. **Frag zurück, wenn eine Rückfrage kommt.** Sie ist kein Vorwurf, sondern die billigste Stelle im ganzen Ablauf.

Der Aufwand liegt also nicht dort, wo Anfänger ihn vermuten.
Er liegt nicht in der Rechtschreibung und nicht in der Grammatik, sondern in einer einzigen Frage, die du dir bei jedem größeren Auftrag stellen kannst.
Und die kannst du dir auch mit vertauschten Buchstaben stellen.
