---
title: "Aus einem Beitrag wird eine Regel: Wie dieser Blog an seiner eigenen Entstehung mitschreibt"
date: 2026-09-07T02:15:00+02:00
draft: false
tags: ["claude-code", "workflow", "schreiben", "rekursion", "selbstbezug", "Essay"]
themen: ["schreiben"]
series: ["Rueckkopplung"]
summary: "Ein Beitrag über meine Tastaturkürzel hat nicht nur beschrieben, wie ich arbeite, er hat es geändert. Die Korrektur steht seitdem in der Datei, die mein Agent zu Beginn jeder Sitzung liest. Damit gehört dieser Blog zu den Dingen, über die er berichtet."
---

Gestern erklärte mir Claude, dass sich in diesem Blog mehrere Textstellen gleichzeitig ändern, wenn es nach einem Gespräch mit mir an Struktur und Inhalt arbeitet.
Ich hatte technisch gefragt und eine technische Antwort bekommen.
Der Satz beschreibt aber mehr, als er beantwortet.

## Kurzfassung

- Der Satz klingt nach Werkzeugkunde.
  Er ist eine Aussage über den Bau dieses Blogs: Eine Absicht von mir landet nie an einer Stelle allein, immer an mehreren gleichzeitig.
- Der erste Fall ist harmlos.
  Am 6. September bekam eine Serie einen neuen Namen, vier Dateien in zwei Sprachen mussten nachziehen, zwei davon waren Verzeichnisse.
  Das ist Kopplung, wie in jedem Softwareprojekt.
- Der zweite Fall ist es nicht.
  Ein Beitrag über meine Tastaturkürzel hat die Datei geändert, die Claude Code zu Beginn jeder Sitzung liest.
- Damit ist dieser Blog nicht mehr nur ein Bericht über meine Arbeitsweise.
  Er ist ein Teil davon.
  Der Chuwi-Laptop wird nicht leiser, weil ich über seine Lautsprecher schreibe — die Kürzel dagegen ändern die Maschine, die den nächsten Beitrag herstellt.
- Die Schleife hat fünf Schritte.
  Am 5. September lagen zwischen den beiden Beiträgen dreißig Minuten, und die Regel galt noch am selben Tag.
- Was hier nicht behauptet wird: dass sich der Blog selbst schreibt.
  Jede Runde geht durch eine Entscheidung von mir.
- Neu ist nicht die Rückkopplung.
  Handbücher, Wikis und Werkzeug-Repositories haben sie seit Jahrzehnten.
  Neu sind ihre Umlaufzeit und die Tatsache, dass die Regel ein deutscher Satz ist und kein Code.

---

## Der erste Fall: ein Name

Am 6. September 2026, um 9:30 Uhr, hieß eine Serie dieses Blogs noch *Dieselben Regeln*.
Nach diesem Zeitpunkt heißt sie [Selbstähnlichkeit](/de/series/selbstaehnlichkeit/).

Der alte Name stand zu dem Zeitpunkt an vier Stellen: in beiden Sprachfassungen des ersten Teils und auf den beiden Serienseiten.
Zwei davon waren Verzeichnisse und keine Textstellen, denn bei Hugo ist der Verzeichnisname die Adresse.
Und weil der Blog zweisprachig ist, existiert jeder Name doppelt, als deutscher und als englischer, mit unterschiedlicher Schreibung und unterschiedlicher Adresse.

Beim Veröffentlichen kam mehr dazu.
Vier Texte lassen sich nur dann als ein Text lesen, wenn sie eine Reihenfolge haben, also entstanden zwei neue Layout-Dateien und Einträge in beiden Sprachdateien.
Die Serie war vorher ein Feld im Vorspann von vier Beiträgen.
Danach war sie eine eigene Seite mit eigener Navigation.

Bemerkenswert ist daran noch nichts.
Jedes Softwareprojekt kennt das, es heißt Kopplung, und es ist der Grund, warum Umbenennen als gefährlich gilt.
Ein Name an einer Stelle, Wirkung an vielen, deshalb schleppen Programme jahrelang Namen mit, die niemand mehr für richtig hält.

## Der zweite Fall: eine Klammer

Am 5. September stehen zwei Beiträge dieses Blogs eine halbe Stunde auseinander.

Um 11:30 Uhr erschien [Ein Codebuch aus dem eigenen Korpus](/de/posts/a-codebook-from-my-own-corpus/).
Darin steht, wie meine Kürzelliste entstanden ist: nicht geraten, gezählt, aus 764 verschiedenen Nachrichten in 13 Projekten.
Das häufigste Wort war `commit` mit 28 Treffern, und in der geratenen Liste fehlte es.

Um 12:00 Uhr erschien [Kürzel als Eingabehilfe](/de/posts/shortcuts-as-an-input-aid/).
Der Anlass war ein Konstruktionsfehler, der beim Schreiben des ersten Beitrags auffiel: Die Liste benutzte runde Klammern.
Runde Klammern brauchen Shift, einen gehaltenen Modifier plus zweite Taste, genau die teuerste Eingabe für jede Hand, die nicht sicher trifft.
Eine Liste, die Tippen sparen sollte, war für den Fall falsch gebaut, in dem das am meisten zählt.

Die Korrektur ist eckig: `[x]` statt `(x)`.

Und hier endet die Ähnlichkeit mit dem ersten Fall.
Die Korrektur blieb nicht im Beitrag stehen.
Sie steht seit demselben Tag in `CLAUDE.md`, der Datei, die Claude Code zu Beginn jeder Sitzung einliest.
Dort steht die neue Form, und dazu der Satz, dass der Agent selbst eckig schreiben soll, in Antworten wie in Dokumentation.

## Der Unterschied

Drei Beiträge dieses Blogs handeln von einem Chuwi-Laptop und seinen Lautsprechern.
Der Laptop hat davon nichts.
Er wird nicht leiser und nicht lauter, weil jemand über ihn schreibt, der Text liegt neben der Sache, über die er berichtet.

Bei den Kürzeln liegt er nicht daneben.
Die Regel, die in dem Beitrag steht, steht auch in der Datei, die die nächste Sitzung steuert.
Der Beitrag beschreibt nicht, wie ich arbeite — er legt fest, wie ich arbeite.

Die Schleife hat fünf Schritte:

1. Ich arbeite mit einem Agenten. Dabei entstehen Transkripte, als Abfallprodukt.
2. Aus den Transkripten wird gezählt, welche Anweisungen ich wiederhole. Daraus wird eine Kürzelliste.
3. Über die Liste entsteht ein Beitrag. Beim Schreiben fällt ein Fehler an ihr auf.
4. Die Korrektur wandert in `CLAUDE.md` und gilt ab der nächsten Sitzung.
5. Der nächste Beitrag entsteht unter der neuen Regel, und liefert wieder Transkripte.

{{< schleife >}}

Am 5. September lagen zwischen den beiden Beiträgen dreißig Minuten, und die Regel in Schritt 4 galt noch am selben Tag.

## Die Regel ist ein Satz, kein Code

Programme, die sich selbst ändern, sind alt.
Ein Makefile, das ein Makefile erzeugt, ein Formatierer, der seinen eigenen Quelltext formatiert, ein Compiler, der sich selbst übersetzt: Alles davon gibt es seit Jahrzehnten, und niemand nennt es lebendig.

Der Unterschied liegt im Material.
`CLAUDE.md` ist kein Konfigurationsformat.
Es sind deutsche Sätze mit Begründungen, Beispielen und einer Tabelle, und die Begründung wirkt mit: sie erklärt dem Agenten nicht nur, was gilt, sie erklärt auch warum, und deshalb greift die Regel auch in Fällen, die beim Schreiben niemand vorgesehen hat.

Damit ist derselbe Satz zweierlei: lesbarer Text und wirksame Anweisung.
Wer den Kürzel-Beitrag liest, liest ungefähr das, was der Agent liest.
Zwischen dem, was hier erklärt wird, und dem, was hier steuert, gibt es keinen Übersetzungsschritt mehr, und das ist der eigentliche Unterschied zu jedem Handbuch, das ich je geschrieben habe.

## Was hier nicht behauptet wird

Der Blog schreibt sich nicht selbst.

Jeder der fünf Schritte oben geht durch eine Entscheidung von mir.
Ich habe entschieden, aus den Transkripten zu zählen.
Ich habe den Konstruktionsfehler bemerkt.
Genauer: Er fiel auf, während ich über die Liste sprach, und ich habe entschieden, dass er wichtiger ist als der Beitrag, den ich gerade schrieb.
Ich habe entschieden, dass die Korrektur in die Regeldatei gehört und nicht nur in den Text.

Ohne diese Entscheidungen läuft die Schleife nicht.
Sie ist nicht automatisch geworden, sondern billig.
Das ist ein Unterschied, der leicht untergeht, und er ist der ganze Unterschied.

Auch die Umlaufzeit ist nicht überall so kurz.
Sie war es bei den Kürzeln, weil Beobachtung, Beitrag und Regeldatei am selben Nachmittag auf demselben Bildschirm lagen.
Bei einer Regel, die erst nach zwei Wochen als falsch auffällt, ist sie zwei Wochen lang.

## Was ich gelernt habe

- **Es gibt zwei Sorten Beitrag, und man sieht ihnen den Unterschied nicht an.** Der eine berichtet über etwas außerhalb.
  Der andere ändert das Werkzeug, mit dem der nächste entsteht. Der Chuwi-Laptop gehört zur ersten Sorte, die Kürzel zur zweiten.
- **Eine Regel wird erst wirksam, wenn sie an der Stelle steht, die gelesen wird.** Dieselbe Einsicht in einem Beitrag ist eine Anekdote, in `CLAUDE.md` ist sie Verhalten.
- **Begründungen gehören mit in die Regel.** Eine Regel ohne Begründung greift genau in den Fällen, die jemand aufgeschrieben hat. Eine mit Begründung greift auch daneben.
- **Kurze Umlaufzeit ändert die Sorte des Systems, nicht nur sein Tempo.** Eine Schleife, die einmal pro Release durchläuft, merkt man nicht. Eine, die zweimal am Nachmittag durchläuft, merkt man an allem.
- **Der Verstärker ist die Zweisprachigkeit.** Jede Entscheidung, die den Text betrifft, trifft ihn doppelt. Das ist der Grund, warum aus einer Absicht sofort mehrere gleichzeitige Änderungen werden.

## Was sich übertragen lässt

Wer selbst mit einem Agenten arbeitet, hat diese Schleife bereits, ob sie genutzt wird oder nicht.
Es gibt eine Datei, die zu Beginn jeder Sitzung gelesen wird, und alles, was dort nicht steht, muss jedes Mal neu gesagt werden.

Der Handgriff, der sich lohnt, ist klein: Beim nächsten Mal, wenn dir während der Arbeit etwas über deine Arbeit auffällt, eine Formulierung, die dreimal nötig war, eine Rückfrage, die immer dieselbe ist, schreib es nicht in deine Notizen, sondern in die Regeldatei.
Mit Begründung, in ganzen Sätzen.

Der Unterschied zeigt sich nicht sofort.
Er zeigt sich in vierzehn Tagen daran, welche Sätze du nicht mehr tippst.
