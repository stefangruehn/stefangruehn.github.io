---
title: "Kürzel als Eingabehilfe: Wenn der Parser die Fehler verzeiht, die die Hand macht"
date: 2026-09-05T12:00:00+02:00
draft: false
tags: ["claude-code", "workflow", "shortcuts", "accessibility", "Field Notes"]
series: ["Codebuch"]
summary: "Die erste Fassung meiner Kürzelliste stand in runden Klammern — und war damit für den Fall, in dem Tippersparnis am meisten zählt, falsch gebaut. Die Korrektur war als Zweitform für Härtefälle gedacht. Sie ist inzwischen die Hauptform für alle."
---

Teil eins hat gemessen, was der geteilte Kontext [kostet](/de/posts/the-most-expensive-answer-is-yes/).
Teil zwei hat daraus [ein Codebuch gebaut](/de/posts/a-codebook-from-my-own-corpus/).
Hier geht es darum, für wen dieses Codebuch keine Bequemlichkeit ist.

## Kurzfassung

- Meine erste Kürzelliste benutzte runde Klammern.
  Die brauchen Shift — einen gehaltenen Modifier plus zweite Taste.
- Genau das ist die teuerste Bewegung für jeden, dessen Hand nicht genau trifft.
  Die Liste, die Tippen sparen sollte, war für den Fall, in dem das am meisten zählt, falsch gebaut.
- Behoben wurde es durch eine ungeshiftete Form: `[x]` statt `(x)`.
  Drei Anschläge ohne Shift statt vier mit zwei Shift-Griffen.
- Die eigentliche Idee ist nicht die Kürze, sondern das **tolerante Parsen**: Der Parser verzeiht genau die Fehler, die eine ungenaue Hand produziert.
- Der größere Hebel ist ohnehin die seltenere Eingabe, nicht die kürzere.
  Es ist billiger, wenn der Agent rät und ich korrigiere, als wenn er fragt und ich antworte.
- Und die Pointe steht am Ende: Die Zweitform für den Härtefall ist inzwischen die Hauptform für alle.

---

## Der Konstruktionsfehler

Die erste Liste sah so aus: `(?)` für „interviewe mich", `(i)` für „leg das als Idee ab", `($)` für „nimm die sparsame Route".

Runde Klammern sehen ordentlich aus.
Auf meiner US-Tastatur kosten sie Shift, und Shift ist kein Anschlag wie jeder andere.
Es ist ein Modifier, der **gehalten** werden muss, während eine zweite Taste getroffen wird.

Für die meisten ist das nicht der Rede wert.
Für jemanden mit Tremor, Dystonie oder einer anderen Bewegungsstörung ist genau diese Kombination die teuerste Bewegung auf der Tastatur — deshalb gibt es „Einrastfunktion" als Betriebssystem-Einstellung überhaupt.

Damit war die Liste an ihrer eigenen Begründung vorbeigebaut.
Sie sollte Anschläge sparen.
Für den, bei dem jeder Anschlag am meisten zählt, verlangte sie den unangenehmsten.

Die Korrektur ist banal: `[x]` gilt gleichwertig zu `(x)`.
Eckige Klammern liegen auf dem US-Layout ungeshiftet nebeneinander.
Drei Anschläge, keine Modifier.

## Die Fehler sind vorhersagbar

Die Klammerform war das Offensichtliche.
Das Interessantere steckt eine Ebene tiefer.

Eine Hand, die nicht genau trifft, macht nicht irgendwelche Fehler.
Sie macht immer wieder dieselben vier: eine Taste wiederholt sich, weil sie zu lange gehalten wurde; ein Anschlag kommt doppelt; die Nachbartaste erwischt es; die schließende Klammer fehlt.

Also verzeiht der Parser genau diese vier.
Alles hier ist dasselbe Zeichen:

```
[i]    (i)    [[i]    [i]]    [ i ]    [ii]    [i
```

Der Satz, um den es geht, klingt selbstverständlich und ist es historisch nicht:

> Eine Eingabehilfe für eine Bewegungsstörung sollte genau die Fehler verzeihen, die diese Störung produziert.

Klassische Eingabehilfen können das nicht.
Ein Text-Expander, ein Makro, eine Tastenkombination — sie alle brauchen exakte Eingabe, weil ihr Parser exakt sein muss.
Ein falsches Zeichen, und nichts passiert.
Man merkt es, korrigiert es und tippt es noch einmal, was den Fehler oft genug reproduziert.

Vor einem Sprachmodell steht diese Anforderung nicht mehr.
Es hat einen Prior: Aus dem Satz drumherum ist ableitbar, was gemeint war.
Es degradiert graziös, statt abzubrechen — dieselbe Eigenschaft, die dafür sorgt, dass [Tippfehler ohnehin nichts kosten](/de/posts/typos-are-cheap/).

Das verschiebt das Entwurfsziel.
Es geht nicht mehr um eine eindeutige Grammatik, sondern um **rekonstruierbare Absicht**.
Und die Toleranz muss aufgeschrieben werden, sonst passiert sie nur zufällig: Was auffangen wird, steht in der Liste — samt der Regel, dass ein aufgefangener Fehler nie angemerkt wird.

## Der größere Hebel: seltener, nicht kürzer

Die Eingabe zu verkürzen ist der offensichtliche Gewinn und der kleinere.

Der größere ist, die Zahl der nötigen Eingaben zu senken.
Wer für jeden Anschlag bezahlt, für den kostet eine Rückfragerunde mehr als ein falscher erster Versuch — es ist billiger, wenn der Agent rät und ich korrigiere, als wenn er fragt und ich antworte.

Deshalb ist ausgerechnet `[$]` — „nimm die kürzeste Route, auch auf Kosten von Gründlichkeit" — eine Eingabehilfe.
Es sagt nicht „sei schneller".
Es sagt: „frag mich nicht noch dreimal."

Und hier trifft sich dieser Beitrag mit Teil eins, auf eine Weise, die ich nicht geplant hatte.
Dort war das Ergebnis: Eine Rückfrage kostet einen vollständigen Durchlauf des bisherigen Gesprächs, egal wie kurz die Antwort ist.
Hier ist das Ergebnis: Eine Rückfrage kostet Anschläge, die jemand vielleicht nicht hat.

Zwei völlig verschiedene Begründungen — die eine ökonomisch, die andere körperlich — und beide führen auf dieselbe Optimierung.
Wenn zwei unabhängige Argumente auf denselben Entwurf zeigen, ist das der belastbarste Hinweis, den man bekommt.

## Auch eine Pause braucht ein Zeichen

Eine Kürzelliste beschreibt normalerweise Arbeitsanweisungen.
Das Naheliegendste hat mir am längsten gefehlt: die Regie drumherum.

```
[m]   Moment — bitte warte damit, ich brauche eine kurze Pause und bin gleich wieder da.
[b]   Bin wieder da, es kann weiter gehen.
```

`[m]` heißt: nichts Neues anfangen, keinen langen Lauf starten, kurz bestätigen und still warten.
`[b]` nimmt den Faden wieder auf, ohne dass ich den Stand neu erklären muss.

Zwei Anschläge für etwas, das sonst zwei Sätze braucht.

Wer eine Pause frei wählen kann, macht sie einfach.
Wer sie nicht frei wählen kann, muss sie ankündigen — und zahlt für die Ankündigung mit genau der Ressource, die gerade knapp ist.
Ein Zeichen dafür zu haben ist kein Komfort.

Nebenbei ist es wieder Token-Ökonomie: Die Wartezeit soll keine Runde kosten.
Dieselbe Optimierung, zum dritten Mal, aus einer dritten Richtung.

## Ein altes Feld mit einem neuen Ziel

Nichts davon ist meine Erfindung.
Das Feld heißt AAC — *Augmentative and Alternative Communication* — und die Unterfamilie heißt *abbreviation expansion*.
Wortvorhersage, Buchstabenkarten, Systeme wie EZ Keys oder Dasher: Das wird seit Jahrzehnten erforscht und gebaut.

Neu ist genau eine Sache.
Bisher war das Ziel einer Abkürzung immer eine **Zeichenkette** — ein Wort, ein Satz, ein Absatz.
Deshalb war der Kompressionsfaktor durch die Länge des Textes begrenzt, den man am Ende produzieren wollte.

Jetzt ist das Ziel eine **Anweisung an einen Agenten**, und diese Grenze fällt weg.
`[s]` sind drei Anschläge und eine halbe Stunde Arbeit.
Für jemanden, der pro Tag nur eine bestimmte Zahl von Tastenanschlägen körperlich verkraftet, ist das eine nicht nur graduelle Verbesserung.

## Was hier nicht belegt ist

Das hier sind Entwurfsargumente und keine Nutzerstudie.

Ich habe keine Messung zu Fehlerverteilungen bei fremder Tastatureingabe erhoben, keine Testpersonen befragt und keine Studie gelesen, die die vier oben genannten Fehlerklassen quantifiziert.
Was ich habe, ist eine Liste, die entlang dieser Annahmen gebaut ist, und die Beobachtung, dass sie sich für den gewöhnlichen Fall auch dann lohnt.

Wer daraus mehr macht, macht zu viel daraus.

## Die Zweitform ist die Hauptform geworden

`[x]` war als Zweitform gedacht.
Die eigentliche Schreibweise sollte `(x)` bleiben, und die eckige Klammer wäre die Variante für den gewesen, dem der Shift-Griff teuer ist.
Sonderfall, Nebeneingang, gut gemeint.

Sie hat noch am selben Tag die runde Form abgelöst.

Nicht aus Rücksicht, sondern weil sie schlicht besser war: eine Taste statt zwei, dieselbe Bedeutung, nichts eingebüßt.
Die runde Form gilt weiter — sie ist nur nicht mehr die, in der jemand schreibt.

Das ist der *curb cut effect*, im Zeitraffer.
Bordsteinabsenkungen wurden für Rollstühle gebaut, und heute benutzt sie jeder mit Rollkoffer, Kinderwagen oder Fahrrad, ohne einen Gedanken daran zu verschwenden.
Nur hat der Weg vom Sonderfall zur Regel dort Jahrzehnte gedauert und Beton gekostet.

Hier hat er einen Nachmittag gedauert, weil ein Codebuch verhandelbar ist und nicht gegossen wird.

Damit dreht sich auch der Anfang um.
Der Konstruktionsfehler war nicht, dass die Liste einen Sonderfall vergessen hatte.
Er war, dass sie an ihrer eigenen Sache vorbeigebaut war — und die Korrektur, die dem Sonderfall galt, war eine Verbesserung für alle, die ihn nicht brauchen.

## Was ich gelernt habe

- **Frag bei jeder Abkürzung, was sie von der Hand verlangt.**
  Nicht nur, wie viele Zeichen sie spart. Ein gehaltener Modifier ist teurer als ein zusätzlicher Anschlag.
- **Toleranz muss aufgeschrieben werden.**
  Ein Modell verzeiht ohnehin viel. Welche Fehler es verzeihen *soll* — und dass es sie nicht anmerkt —, steht sonst nirgends.
- **Zähl die Runden, nicht die Zeichen.**
  Die teuerste Eingabe ist die, die überhaupt erst nötig wird, weil eine Antwort fehlt.
- **Zwei unabhängige Begründungen für denselben Entwurf sind besser als eine gute.**
  Hier zeigen Tokenrechnung und Bewegungsökonomie auf dieselbe Regel.
- **Die Ausnahme kann der bessere Normalfall sein.**
  Wenn die Variante für den Härtefall in jedem Fall besser ist, war sie nie eine Variante.

## Was sich übertragen lässt

Das Ganze handelt von einer Kürzelliste, aber die Bewegung dahinter ist allgemeiner, und sie lässt sich an jeder Schnittstelle machen, die jemand mit den Händen bedient.

**Bau die Toleranz ein, nicht die Präzision.**
Frag nicht, wie du deine Eingabe eindeutig machst, sondern welche vier Fehler deine Nutzer tatsächlich produzieren — und fang genau die auf, still.

**Zähl die Interaktionen, nicht die Klicks.**
Ein Formular mit weniger Feldern ist gut. Ein Formular, das gar nicht erst erscheint, weil die Antwort ableitbar war, ist besser.

**Und wenn du eine barrierefreie Variante baust, sieh sie dir noch einmal an.**
Ist sie für alle anderen auch besser, ist sie keine Variante.
Dann ist sie das, womit du hättest anfangen sollen.
