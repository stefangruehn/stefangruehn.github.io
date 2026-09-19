---
title: "Die Sprache zieht nach: Was ein Leser, der alles wörtlich nimmt, mit meinen Sätzen macht"
date: 2026-09-19T11:00:00+02:00
tags: ["claude-code", "language", "writing", "shortcuts", "Essay"]
themen: ["denken"]
summary: "Seit ich täglich mit einem Agenten arbeite, ändert sich nicht nur mein Denken, auch meine Sprache, und schneller als je zuvor. Sie wird genauer, widerspruchsärmer und nimmt Wörter aus der Arbeit mit in den Alltag. Die Richtung ist die einer Programmiersprache: Syntax, Semantik und Pragmatik fallen auseinander, auch dort, wo kein Agent mitliest."
---

## Kurzfassung

- Mein Denken hat sich durch die Arbeit mit einem Agenten verändert.
  Meine Sprache auch, und zwar schneller als je zuvor und in eine bestimmte Richtung.
- Die Richtung ist die einer Programmiersprache.
  Ein Gegenüber, das jedes Wort beim Wort nimmt, macht Fehler sichtbar, die ein Mensch überliest: ein Verb ohne Richtung, ein Wort mit zwei Bedeutungen, ein „liegt“, das nicht sagt, woran es hängt.
- Mein Verfahren trennt inzwischen, was die Linguistik trennt.
  `->` heißt wörtlich und wird von einem Programm geprüft, `~>` heißt sinngemäß und wird es nicht.
  Das ist die Grenze zwischen Syntax und Semantik, und sie ist aus der Praxis entstanden.
- Einige Wörter sind aus der Arbeit in den Alltag gewandert: „steht auf Platte“, „Kontext“, „Diff“, „sinngemäß oder wörtlich“.
- Präziser heißt nicht verständlicher.
  Ein Vokabular, das sich an einem einzigen Gegenüber schärft, kann sich von dem aller anderen entfernen.
- Widerspruchsfrei wird dabei nichts.
  Widerspruchsarm ist das, was sich erreichen lässt.

---

## Freiheit oder Armut

Als ich mir diese Idee notierte, schrieb ich „Widerspruchsfreiheit“ und dahinter in Klammern „-armut?“.
Die Notiz korrigierte sich, während sie entstand.

Freiheit von Widersprüchen verspricht etwas, das kein Text und kein Werkzeug halten kann.
Armut an Widersprüchen ist erreichbar: weniger davon, und die übrigen dort, wo man sie findet.
Das Fragezeichen in der Klammer ist die Beobachtung, um die es hier geht, im Kleinen.
Ich habe früher nicht so geschrieben.

Über das Denken habe ich [an anderer Stelle](/de/posts/many-memories-one-person/) geschrieben: welches Gedächtnis wo liegt, seit ein Agent mitarbeitet.
Dieser Beitrag setzt ihn fort, aber auf einer anderen Ebene.
Es geht um die Sprache, in der ich denke und die ich spreche.

## Ein Leser, der beim Wort nimmt

Claude Code liest meine Sätze anders als ein Mensch.
Ein Mensch ergänzt, was fehlt, und überliest, was schief steht.
Ein Sprachmodell ergänzt auch, aber was es ergänzt, zeigt es mir in seiner Antwort, und dort sehe ich, was ich tatsächlich gesagt habe.

Am selben Tag wie die Notiz ging es um einen Satz im oben verlinkten Beitrag.
Er lautete „Mein Vault erbt nicht in meinen Kopf“.
Gemeint war: Was im Vault steht, kommt nicht von selbst in meinen Kopf, so wie Claudes Anweisungen beim Sitzungsstart automatisch geladen werden.
Der Satz sagt es nicht, denn „erben“ hat eine Richtung.
Man erbt von etwas, nicht in etwas hinein.
Das ist ein Rektionsfehler, und es ist genau die Sorte Fehler, die ein Typprüfer findet: Das Verb erwartet ein Argument einer bestimmten Art und bekommt ein anderes.
Heute steht dort „Mein Vault lädt sich nicht von selbst in meinen Kopf“.
Seitdem steht in den Stilregeln dieses Blogs ein Hinweis: Ein Fachverb, das als Bild dient, behält seine Richtung.

Andere Fälle aus demselben Verfahren haben dieselbe Gestalt.
„Laufzeit“ heißt im Deutschen die Dauer eines Programmlaufs und auch die Umgebung, die mitlaufen muss.
Ein Wort, zwei Bedeutungen, wie ein überladener Bezeichner, bei dem erst der Aufrufer entscheidet, welche Fassung gemeint ist.
In einem Beitrag über Hugo, das als einzelnes Binary ohne solche Umgebung auskommt, steht deshalb heute „Runtime“.
Und aus „Ich weiß nach zwei Wochen noch, dass eine Idee liegt“ wurde „dass eine Idee wartet“.
„Liegt“ sagt, dass etwas nicht weitergeht.
„Wartet“ sagt, dass es an etwas hängt, und genau dieses Etwas war der Punkt des Absatzes.

Keiner dieser Fehler hätte einen menschlichen Leser aufgehalten.
Sie fallen auf, weil ich inzwischen jeden Satz einmal so lese, wie ein Programm ihn lesen würde.

## Syntax, Semantik und das, was dazwischen fehlt

Die Änderungsvorschläge zu diesem Blog haben eine eigene kleine Notation.
Links steht die heutige Stelle, rechts die gewünschte, dazwischen ein Pfeil.
Es gibt zwei Pfeile.
`->` heißt wörtlich: Links steht der exakte Text, und ein Prüfskript sucht ihn im Beitrag.
`~>` heißt sinngemäß: Links steht, was gemeint ist, und niemand prüft es.

Die Unterscheidung ist nicht aus einem Lehrbuch gekommen.
Sie ist entstanden, weil sich die wörtliche Form nachrechnen lässt und die sinngemäße nicht, und weil ich wissen wollte, welche Zeilen das Skript übernehmen kann.
Im Nachhinein ist es die Grenze zwischen Syntax und Semantik.
Die Form eines Satzes kann ein Programm vergleichen.
Was er bedeutet, kann es nicht.

Dieselbe Grenze zieht sich durch die Stilregeln dieses Blogs.
Die meisten Einträge sind Wortlisten und Zielwerte, die ein Skript zählt: Gedankenstriche je tausend Wörter, ein Anglizismus, für den ein deutsches Wort bereitsteht.
Seit Kurzem gibt es daneben Hinweise, die kein Skript prüft, weil jedes Muster zu eng oder zu breit wäre.
Die Regel über die Richtung der Verben ist so ein Hinweis.
Messbar ist die Syntax, der Rest wird gelesen.

Der Semiotiker Charles W. Morris hat 1938 drei Dimensionen der Zeichen unterschieden: Syntax, die Beziehung der Zeichen untereinander, Semantik, ihre Beziehung zu dem, was sie bezeichnen, und Pragmatik, ihre Beziehung zu dem, der sie benutzt.
In meinem Verfahren fehlt die dritte, und gerade auf ihr arbeitet ein Prompt.
[Der erste Auftrag für dieses Blog](/de/posts/the-task-named-the-tool/) bestand aus sechs Wörtern, und eines davon war schon die Antwort auf eine Frage, die niemand gestellt hatte.
Syntaktisch war der Satz in Ordnung, semantisch auch.
Was er tat, stand weder in der Form noch in der Bedeutung, sondern in der Wirkung auf den, der ihn las.

## Eine kleine Sprache mit Grammatik

Ich gebe wiederkehrende Anweisungen als [Kürzel](/de/posts/shortcuts-as-an-input-aid/): ein Zeichen in eckigen Klammern, `[+]` für „committen“, `[?]` für „interview mich dazu“.
Aus einer Liste von Abkürzungen ist mit der Zeit eine kleine Sprache geworden.
Sie hat eine Bindungsregel (ein Kürzel gilt für den Satz, in dem es steht, am Ende der Nachricht für die ganze Nachricht), eine Escape-Regel (ein Backslash davor meint das Zeichen und nicht die Anweisung) und eine Vorrangregel: Ist die doppelte Form selbst ein Kürzel, gilt sie als dieses Kürzel und nicht als Tippfehler des einfachen.
Das sind die Bausteine, aus denen man einen Parser schreibt.
Geschrieben hat ihn niemand, die Regeln stehen in einer Textdatei, und das Sprachmodell hält sich daran.

Zwei dieser Kürzel trennen etwas, das vorher keine eigene Taste hatte.
`[,]` heißt „diese Stelle holpert sprachlich“.
`[-]` heißt „das sehe ich anders“.
Das eine betrifft die Form, das andere die Sache.
Im Gespräch unter Menschen fallen beide oft in einen Satz zusammen, und das Gegenüber muss erraten, ob es umformulieren oder umdenken soll.

Die Kehrseite steht in [einem anderen Beitrag](/de/posts/typos-are-cheap/): Meine Nachrichten an Claude sind voller Tippfehler, und verstanden wird trotzdem.
Die Form ist unscharf, die Bedeutung kommt an.
Das ist ein toleranter Parser, und er arbeitet in beide Richtungen.
Genauer werde ich dort, wo die Bedeutung hängt, nicht bei den Buchstaben.

## Was nach draußen wandert

Das alles könnte eine Werkstattsprache bleiben, die am Rechner gilt und am Küchentisch nicht.
Sie bleibt es nicht.
Ich merke es am eigenen Schreiben, in Nachrichten und Notizen, und beim Sprechen.

Einige Wörter sind mitgewandert.
„Steht auf Platte“ heißt bei mir inzwischen: festgehalten, geht nicht mehr verloren, im Gegensatz zu dem, was nur gesagt wurde.
„Kontext“ ist das, was ein Gegenüber gerade vor Augen hat, und ein „Schnitt“ ist der Moment, in dem man ihn bewusst leert und neu anfängt.
„Diff“ ist die Frage, was sich eigentlich geändert hat, und „committen“ heißt, etwas verbindlich festzumachen.
Und bei allem, was ich weitererzähle, steht jetzt die Frage im Raum, ob es sinngemäß oder wörtlich war.

Das ist ein größeres Alltagsvokabular, aber es ist kein beliebiges.
Die Wörter, die gewandert sind, bezeichnen Unterscheidungen, für die ich vorher kein kurzes Wort hatte: gesichert oder nicht, vor Augen oder nicht, geändert oder nur neu gesagt, zitiert oder umschrieben.
Kenneth E. Iverson hat seinen Turing-Vortrag 1979 *Notation as a Tool of Thought* genannt.
Seine These war, dass eine gute Notation das Denken nicht nur abbildet, sondern formt.
Er meinte Programmiersprachen, und er hatte recht, nur hätte ich nicht erwartet, dass es auch für die Sprache gilt, in der ich mit Menschen rede.

## Präziser, aber für wen

Hier liegt die Spannung, die ich nicht auflösen kann.
In [einem Beitrag über meine Abkürzungen](/de/posts/a-codebook-from-my-own-corpus/) ging es um Basil Bernsteins restringierten Code: Wer viel Hintergrund teilt, kann kürzer sprechen, weil der Rest vorausgesetzt ist.
Wird meine Sprache präziser, oder wird sie nur kürzer und nur für Eingeweihte lesbar?
Vermutlich beides, je nach Gegenüber.
„Steht auf Platte“ ist für Claude und mich ein exakter Begriff.
Für jemanden, der nie mit einem Agenten gearbeitet hat, ist es Jargon.

Es gibt einen öffentlichen Gegenentwurf.
Ralf D. Müller sammelt unter dem Namen [Semantic Anchors](https://llm-coding.github.io/Semantic-Anchors/) etablierte Fachbegriffe, die in einem Sprachmodell ein ganzes Wissensgebiet auf einmal aufrufen und die Menschen genauso verstehen.
Als ich am 19. September nachsehen ließ, welche Anweisungen in Claudes Gedächtnis sich durch einen solchen Begriff ersetzen ließen, fand sich in den Notizen aus dreizehn Projekten, rund 35.000 Wörtern, keine einzige Stelle.
Mein Vokabular ist gewachsen, aber es ist mein eigenes geworden und nicht das des Lehrbuchs.

Präziser heißt also nicht verständlicher.
Eine Sprache, die sich an einem einzigen Leser schärft, der jedes Wort beim Wort nimmt, wird genauer für diesen Leser.
Ob sie es auch für alle anderen wird, ist eine andere Frage, und die Antwort hängt davon ab, ob ich meine Wörter mit nach draußen nehme oder auch erkläre, was sie heißen.

## Armut, nicht Freiheit

Am Anfang stand die Klammer „-armut?“.
Sie ist die kürzeste Fassung dessen, was sich an meiner Sprache geändert hat.
Nicht, dass sie frei von Widersprüchen wäre.
Sondern dass ich beim Schreiben merke, wo einer steht, und ihn im selben Atemzug benenne, statt ihn stehen zu lassen.

Ein Programm, das sich widerspricht, läuft nicht.
Ein Satz, der sich widerspricht, läuft weiter, und das war lange sein Vorteil.
Seit ich täglich mit einem Leser arbeite, der beides beim Wort nimmt, fällt mir der Unterschied öfter auf.
Ob das ein Gewinn ist, weiß ich noch nicht.
Dass es geschieht, merke ich jeden Tag.
