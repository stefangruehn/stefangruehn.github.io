---
title: "Wer die Kette gebaut hat: Stoff, Form und Verfahren"
date: 2026-09-18T10:40:00+02:00
draft: true
tags: ["claude-code", "writing", "self-reference", "reverse-engineering", "authorship", "Essay"]
themen: ["autor"]
series: ["Autorschaft"]
summary: "In „Erfahren und erlaufen“ stand, der Stoff komme ausnahmslos von mir und die Form von Claude. Die Serie über eine undokumentierte Platine ist der erste Fall, in dem diese Zweiteilung nicht aufgeht, denn dort kam auch das Verfahren von Claude. Beim Menschen bleiben dann die Frage und das Urteil, und drei Pflichten."
---

Am 6. September stand hier ein Beitrag mit einer sauberen Arbeitsteilung.
[Erfahren und erlaufen](/de/posts/how-much-of-this-is-mine/) sagt: Der Inhalt kommt von mir, die Struktur meistens von Claude.
In der Kurzfassung steht dazu ein Wort, das ich damals für eine Verstärkung hielt: **bisher ausnahmslos**.

Am selben Tag entstand die Serie [Werkzeugketten](/de/series/werkzeugketten/), drei Beiträge über Forensik an einer Platine ohne brauchbare Dokumentation.
Sie ist der erste Fall, in dem der Satz nicht mehr stimmt.
Das „bisher“ hat seine Arbeit schneller getan, als ich dachte.

## Kurzfassung

- *Erfahren und erlaufen* teilt die Arbeit in zwei Anteile: Der Stoff kommt von mir, die Form von Claude.
  Die Serie *Werkzeugketten* ist der erste Fall, in dem das nicht aufgeht.
- Zu Hardware-Forensik hatte ich kaum Vorwissen.
  Ohne das, was Claude beigesteuert hat, hätte es dort nichts zu formen gegeben.
- Der fehlende dritte Anteil ist das **Verfahren**: zu wissen, welche Kette man baut, um eine Frage zu beantworten.
  Registerwerte stehen im Datenblatt, das Verfahren steht nirgends.
- Der alte Merksatz *Behalte den Stoff, gib die Form ab* hält weiter, aber nur unter einer Bedingung, die bisher unsichtbar war: dass der Stoff schon da ist.
- Fehlt er, liefere ich die Frage und das Urteil.
  Dafür schulde ich drei Dinge: Prüfbarkeit, offengelegte Herkunft und dass Frage und Urteil bei mir bleiben.
- Der alte Prüfsatz besteht seine eigene Ausnahme, ausgerechnet über das Geräusch.
  Er beweist dabei allerdings weniger, als ich ihm zugetraut hatte.

---

## Wo die Zweiteilung nicht aufgeht

Die Serie behandelt dreizehn Ketten an einem Drehknopf mit rundem Bildschirm und zwei Mikrocontrollern.
Jede ist aus vorhandenen Werkzeugen zusammengesteckt und endet in genau einer Tatsache.
Welcher Befehl in der Initialisierungstabelle des Herstellers fehlt.
Auf welchen Pins die beiden Prozessoren miteinander reden.
Welche Leitungen die Speicherkarte wirklich benutzt.

Keine dieser Ketten hätte ich vorher benennen können.
Die Werksfirmware auszulesen, bevor man etwas Eigenes auf den Chip schreibt, kannte ich: Das hatte ich Monate vorher schon einmal gemacht, ohne Claude.
Was man danach mit so einem Abbild anfängt, wusste ich nicht.
Ich wusste nicht, dass die Log-Texte in einem Firmware-Abbild als Anker taugen, von denen aus man die Funktion findet, die sie ausgibt.
Und ich wäre nicht darauf gekommen, 840 Pinbelegungen durchzuprobieren, statt eine zu raten.

Nach der Rechnung aus *Erfahren und erlaufen* hätte ich hier den Stoff liefern müssen.
Es gab aber keinen Stoff, bevor die Ketten liefen.
Was die drei Beiträge erzählen, sind die Ergebnisse dieser Ketten.
Ohne sie hätte die Serie keinen Gegenstand gehabt.

## Der dritte Anteil heißt Verfahren

Naheliegend wäre, den fehlenden Anteil Wissen zu nennen.
Das trifft es nicht.

Was ein Register des Bildschirmtreibers tut, steht im Datenblatt.
Was ein Literal-Pool ist, steht in jeder Einführung in Maschinensprache.
Mit welchem Befehl eine Speicherkarte angesprochen werden will, steht in ihrer Spezifikation.
Das alles ist nachschlagbar, langsam, aber grundsätzlich für jeden.

Nachschlagen lässt sich dagegen nicht, **welche Kette man baut**, um an eine bestimmte Antwort zu kommen.
Ein Datenblatt beantwortet die Frage, die man ihm stellt.
Welche Frage man an welche Quelle richtet, in welcher Reihenfolge, und woran man merkt, dass eine Antwort nicht stimmt, steht in keinem.
Die Serie sortiert ihre Ketten danach, wer am Ende antwortet: Papier, ein Abbild oder das Gerät.
Schon diese Sortierung ist ein Verfahren.

So wird aus zwei Anteilen ein dritter: **Stoff, Form und Verfahren.**

## Was aus dem Merksatz wird

*Behalte den Stoff, gib die Form ab.*
Der Satz hält, aber nicht überall.

Er gilt, solange der Stoff schon da ist.
Beim Laptop mit den stummen Lautsprechern aus der Serie [Nachhall](/de/series/nachhall/) war das Symptom meins, der Rechner meiner und das Geräusch auch.
Die Form konnte ich abgeben, weil es etwas gab, das Form annehmen konnte.

Auf einem Feld, das ich nicht beherrsche, verschiebt sich die Grenze.
Dort liefere ich den Stoff nicht.
Ich liefere die **Frage** und das **Urteil**: was gemessen wird, was als Beleg zählt und was in den Text kommt.

Das ist kein Widerruf.
Es ist eine Bedingung, die vorher unsichtbar war, weil sie immer erfüllt war.

## Wo die Grenze unscharf wird

Ganz so sauber, wie die letzten Absätze klingen, ist es nicht.
Auch in *Nachhall* kam nicht alles aus meinem Vorwissen.
Die Symptome waren meine, aber die Steuerelemente, die `amixer` anzeigt, und die Konfigurationsdateien unter `wireplumber.conf.d` kannte ich vorher nicht.

Der Unterschied zwischen beiden Serien ist deshalb wohl gradueller, als die Formel behauptet.
Bei *Nachhall* wusste ich wenigstens, wo ich anfange: beim Geräusch, das fehlte.
Bei *Werkzeugketten* wusste ich das nicht.
Die Knob-Serie ist vermutlich nicht der einzige Fall, in dem das Verfahren von Claude kam.
Sie ist der erste, in dem es sich nicht mehr übersehen lässt.

## Was ich schulde, wenn der Stoff nicht von mir kommt

Das ist die unbequeme Hälfte.
Wer über ein Feld schreibt, das er nicht beherrscht, kann für die Richtigkeit nicht mit eigener Sachkunde einstehen.
Er kann aber drei Dinge tun.

**Erstens: Prüfbarkeit erzwingen.**
Jede Behauptung trägt einen Beleg, den auch jemand ohne Sachkunde nachvollziehen kann: eine Logzeile, einen Befehl, eine Zahl.
Was sich nicht belegen lässt, kommt nicht in den Text.
Die Befundnotizen hinter der Serie tun das schon Zeile für Zeile.
Jeder Eintrag ist als `EVIDENCE` oder `INFERENCE` ausgezeichnet, also als gemessen oder als gefolgert.
Diesen Unterschied kann auch lesen, wer die Kette selbst nie gebaut hätte.
Ich zum Beispiel.

**Zweitens: die Herkunft offenlegen.**
Auf der Startseite steht, dass jeder Beitrag hier mit Claude Code entsteht und die Zahlen aus echten Sitzungen stammen.
Das legt offen, woher die Form kommt.
Für die Substanz sagt es nichts.
Gezählt am 18. September: In den drei Beiträgen der *Werkzeugketten* kommt Claude nur als Schlagwort `claude-code` vor, im Text kein einziges Mal.
Wer die Serie liest, muss annehmen, dass ich die Ketten kannte.
Dieser Beitrag holt die Angabe nach.

**Drittens: die Frage und das Urteil behalten.**
Welche Frage gestellt wird und welche Antwort zählt, bleibt beim Menschen, auch wenn er die Antwort selbst nicht hätte finden können.
Die Fragen der Serie kamen von meinem Schreibtisch, von einer Platine, auf der die eigene Firmware kein stabiles Bild zustande brachte.
Und die Regel, mit der sie endet, ist ein Urteil: Ein Schaltplan wird geglaubt, wo eine Messung ihm zustimmt.
Ob die Messung reicht, entscheide ich.

Eine vierte Pflicht habe ich erwogen und vorerst nicht aufgenommen, die **Widerspruchsprobe**.
Sie verlangt zwei unabhängige Wege zum selben Ergebnis, weil man dem einzelnen Weg nicht ansieht, ob er stimmt.
Die Serie macht es an einer Stelle vor: Das Protokoll zwischen den beiden Prozessoren wurde aus beiden Firmware-Abbildern getrennt gelesen, und beide waren sich einig.
Sie ist der nächste Kandidat, falls drei Pflichten nicht reichen.

## Der Prüfsatz und seine Ausnahme

*Erfahren und erlaufen* endet auf einem Prüfsatz: Steht in deinem Text mindestens eine Zahl, ein Datum oder ein Geräusch, das niemand außer dir hätte beisteuern können?

Für die *Werkzeugketten* müsste die Antwort nach allem Bisherigen nein lauten.
Sie lautet ja, und zwar über das Geräusch.

Im dritten Teil gab es eine Frage, die kein Register beantworten konnte: ob der Vibrationsmotor schwächer wird, wenn seine Freigabeleitung zugleich Daten sendet.
Das Diagnoseregister meldete Werte, die sich allein nicht deuten ließen.
Entschieden hat die Fingerkuppe.
Die Klicks unter Datenverkehr waren **kürzer und etwas leiser**.
Beim Lautsprecher war es das Ohr.
Während vom Telefon Musik lief, legte die eigene Firmware jeden freien Pin um, und ihr eigener Ton war nie zu hören.

Der alte Prüfsatz besteht also seine eigene Ausnahme.
Er beweist dabei allerdings weniger, als ich ihm zugetraut hatte.
Er zeigt, dass jemand am Gerät saß.
Wer den Weg dorthin kannte, zeigt er nicht.
Für den Stoff reicht der Prüfsatz, für das Verfahren braucht es die drei Pflichten.

## Was sich übertragen lässt

Behalte den Stoff, gib die Form ab.
Wo du keinen Stoff hast, behalte die Frage und das Urteil, und gib das Verfahren nur so ab, dass jeder Schritt eine Spur hinterlässt, die du prüfen kannst.

*Erfahren und erlaufen* warnt vor dem umgekehrten Fall: Liefert die Maschine die Substanz und poliert der Mensch die Formulierungen, entsteht Text, der aussieht wie ein Beitrag und niemanden hat, der ihn braucht.
Nach dieser Warnung hätte es die *Werkzeugketten* nicht geben dürfen.
Dass es sie trotzdem gibt, liegt an der Frage.
Sie war da, bevor es einen Text gab.

Dies ist der erste Teil der Serie [Autorschaft](/de/series/autorschaft/).
Der nächste fragt, wie diese Arbeitsteilung heißt, wenn der Stoff sehr wohl von mir kommt.
