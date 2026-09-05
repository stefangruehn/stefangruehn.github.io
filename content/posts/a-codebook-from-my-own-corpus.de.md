---
title: "Ein Codebuch aus dem eigenen Korpus: Die Abkürzungen, die man nicht raten kann"
date: 2026-09-05T11:30:00+02:00
draft: false
tags: ["claude-code", "workflow", "shortcuts", "language", "Field Notes"]
series: ["Codebuch"]
summary: "Wer lange genug mit einem Agenten arbeitet, wiederholt sich. Was man wiederholt, lässt sich abkürzen — aber die guten Abkürzungen kann man nicht raten. Sie stehen in den eigenen Transkripten, und das häufigste Wort fehlte in meiner geratenen Liste."
---

Teil eins hat gemessen, was der geteilte Kontext [wirklich kostet](/de/posts/the-most-expensive-answer-is-yes/) — und dass eine vermiedene Rückfrage einen vollen Durchlauf spart.
Das hier ist der Versuch, sie planmäßig zu vermeiden.

## Kurzfassung

- Aus einem einzigen Kürzel für „bitte interviewe mich dazu" wurde an einem Nachmittag eine Liste, aus der Liste eine kleine Grammatik.
- Die erste Liste habe ich geraten.
  Danach habe ich nachgezählt: 764 verschiedene Nachrichten von mir aus 13 Projekten.
- Das mit Abstand häufigste Wort war `commit` mit 28 Treffern — und es stand in der geratenen Liste **nicht drin**.
- Die Prüfung fand drei Defekte, die beim Schreiben keinem auffallen: einen echten Widerspruch, ein Escape-Zeichen, das mit sich selbst kollidiert, und ein Zeichen, das längst vergeben war.
- Ein Kürzel, das eine bestehende Dauerregel nur wiederholt, ist tote Syntax.
  Es taugt nur als Verstärker.
- Der Unterschied zu jedem Textbaustein: Das Ziel der Expansion ist keine Zeichenkette, sondern eine Anweisung.
  Drei Anschläge können eine halbe Stunde Arbeit auslösen.

---

## Aus einem Zeichen wurde eine Liste

Am Anfang stand eine Bequemlichkeit.
Ich schreibe oft „bitte interviewe mich jetzt dazu, bevor du schreibst" — jedes Mal derselbe Satz, jedes Mal in derselben Situation.

Also wurde daraus ein Zeichen: `[?]`.

Das war als Tippersparnis gedacht und blieb es keine Stunde.
Wenn ein Zeichen funktioniert, fallen einem sofort acht weitere ein, und dann steht man vor der Frage, welche davon es wert sind.
Genau an dieser Stelle fängt die interessante Arbeit an, denn hier hört das Raten auf zu funktionieren.

## Was ich tatsächlich wiederhole

Die Häufigkeiten stehen in den eigenen Transkripten.
Claude Code legt jede Sitzung als Datei ab, und darin steht jede Nachricht, die ich je getippt habe.

```sh
cd ~/.claude/projects
jq -r 'select(.type=="user") | .message.content | strings' ./*/*.jsonl \
  | grep -viE 'toolu_|/tmp/|exit_code' | awk 'length($0)<300' \
  | sort | uniq -c | sort -rn
```

Der führende `./` ist nicht schmückend.
Ohne ihn hält `jq` die Verzeichnisnamen, die mit einem Bindestrich beginnen, für Optionen und bricht ab.

Herausgekommen sind 764 verschiedene Nachrichten aus 13 Projekten, und obenauf lag das hier:

```
commit    28×      hugo      14×      serie     13×
test      13×      merke dir  7×
```

`hugo` und `serie` hatte meine geratene Liste getroffen.
`commit`, das häufigste von allen, stand nicht darauf.

Das ist der ganze Punkt des Messens.
Die Intuition erwischt zuverlässig das, was auffällt — die besonderen Anweisungen, die neuen Werkzeuge, das zuletzt Gelernte.
Sie erwischt nicht das, was so selbstverständlich ist, dass man es beim Nachdenken über die eigene Arbeit überliest.

Ein Codebuch, das man rät, ist ein Codebuch über die eigene Selbstwahrnehmung.
Eins, das man misst, ist eins über die eigene Arbeit.

## Was beim Raten nicht auffällt

Die geratene Liste hatte drei Defekte, und keiner davon war beim Schreiben zu sehen.

**Ein echter Widerspruch.**
`[-]` sollte „das sehe ich anders" heißen und gleichzeitig „korrigiere mich".
Das sind zwei entgegengesetzte Richtungen in einem Zeichen: Wer irrt sich denn, du oder ich?
Ein Zeichen, das beides bedeuten kann, bedeutet nichts.
Es heißt jetzt nur noch das eine — „das sehe ich anders, begründe deine Position neu oder revidiere sie" —, und damit ist auch klar, wer am Zug ist.

**Ein Escape-Zeichen, das mit sich selbst kollidiert.**
Man braucht eine Möglichkeit zu sagen: *diesmal meine ich wirklich nur das Zeichen.*
Vorgeschlagen war ein Schrägstrich davor.
Nur ist der Schrägstrich selbst ein Kürzel der Liste, `[/]` für „nenn mir eine Alternative" — und am Zeilenanfang ist er in Claude Code der Präfix für Slash-Befehle.
Zwei Kollisionen in einem Zeichen.
Es wurde der Backslash.

**Ein Zeichen, das schon vergeben war.**
`[?]`, der Anlass des Ganzen, stand in den Transkripten bereits achtmal — in einer anderen Bedeutung.

> „verbunden wird per Code-Scan -> verbunden wird per QRCode-Scan (?)"
>
> „auf posts stehen karten, auf series nur badgets. (?)"

Das heißt nicht „interviewe mich".
Das heißt „stimmt das?".

Aufgelöst wurde es ohne Verlust: Genau diese Fälle heißen jetzt `[&]` — „ich vermute, dass …, prüf es, statt es zu übernehmen".
Die alte Bedeutung ist umgezogen, die neue hat das Zeichen bekommen.
Eine Umbuchung, keine Kollision.

Alle drei Defekte haben eines gemeinsam: Sie sind erst sichtbar, wenn man die Liste gegen den eigenen Bestand hält statt gegen die eigene Vorstellung.

## Ein Kürzel, das nichts tut

`[$]` sollte „nimm die tokensparsamste Lösung" heißen.

Das klingt nützlich und war wirkungslos.
Sparsamkeit steht bei mir längst als Dauerregel in der globalen Konfiguration, die vor jeder Sitzung gelesen wird.
Ein Zeichen, das eine Regel wiederholt, die ohnehin gilt, schaltet nichts ein.
Es ist tote Syntax: Man tippt es, es fühlt sich wirksam an, und es ändert nichts.

Gerettet wurde es dadurch, dass es nicht mehr dasselbe sagt, sondern mehr:

> Nimm die tokensparsamste Route — **auch auf Kosten von Gründlichkeit.**

Damit trifft das Zeichen eine Abwägung, die die Dauerregel offenlässt, und ist wieder ein Schalter.
Die Prüffrage für jeden Eintrag einer solchen Liste lautet also nicht „ist das nützlich?", sondern: *Was wäre anders, wenn ich es nicht tippe?*

## Warum das mehr abkürzt als ein Textbaustein

Textersetzung gibt es seit Jahrzehnten, und der Kompressionsfaktor ist immer durch die Länge der Phrase begrenzt.
Vier Zeichen werden zu vierzig, mehr ist nicht drin.

Hier ist das Ziel der Expansion keine Zeichenkette, sondern eine Anweisung.

`[s]` heißt: *Sieh dir die Beiträge im Blog an, die zu dieser Idee passen, Entwürfe eingeschlossen, bewerte sie, und wenn es mehr als zwei sind, schlag eine Serie vor.*
Das sind drei Anschläge und eine halbe Stunde Arbeit.

Genau das macht die Liste zu etwas anderem als eine Bequemlichkeit — und es verbindet sie mit der Rechnung aus Teil eins.
Eine Rückfrage kostet nicht das, was sie an Zeichen wiegt, sondern einen vollständigen Durchlauf des bisherigen Gesprächs.
Ein Zeichen, das eine Rückfrage überflüssig macht, spart nicht drei Anschläge.
Es spart eine ganze Runde.

## Zwei Hälften desselben Dokuments

Ein Codebuch nützt nur, wenn beide Seiten dasselbe darin lesen.
Bei mir liegt es in zwei Dateien.

`SHORTCUTS.md` ist die Hälfte, die ich lese: mit Begründungen, Beispielen und der Erklärung, warum ein Zeichen so heißt und nicht anders.
Die Konfiguration und das Gedächtnis des Agenten sind die Hälfte, die er liest: knapp, ohne Begründung, dafür mit den Regeln fürs Parsen.

Dasselbe Dokument in zwei Richtungen, und beide müssen von Hand synchron gehalten werden, weil es keinen gemeinsamen Speicher gibt.
Das ist der wunde Punkt der ganzen Konstruktion, und ich habe keine hübsche Lösung dafür.
Was hilft, ist ein Satz am Ende beider Dateien: *Ändert sich etwas, gehört es in diese Datei und in die andere.*

## Wo man das schon kennt

Die Sache ist nicht neu, sie hat nur bisher andere Namen getragen.

- **Quellenkodierung.**
  Kurze Codes für häufige Symbole, lange für seltene — das ist die Idee hinter jedem Kompressionsverfahren.
  Das Codebuch ist hier der geteilte Kontext, und die Verteilung ist meine eigene Anweisungshäufigkeit.
- **Restringierter Code.**
  Basil Bernstein hat beschrieben, dass Gruppen mit viel geteiltem Hintergrund kürzer sprechen können, weil der Rest vorausgesetzt ist.
  Nur wächst dieser geteilte Hintergrund hier nicht über Generationen, sondern über Sitzungen.
- **Grammatikalisierung im Zeitraffer.**
  Häufig gebrauchte Inhaltswörter fallen mit der Zeit zu Funktionsmarkern zusammen — in natürlichen Sprachen dauert das Jahrhunderte.
  Hier dauert es einen Nachmittag, weil beide Seiten das Wörterbuch aufschreiben können, statt es aushandeln zu müssen.
- **Eine gemeinsame Fachsprache.**
  Im Softwareentwurf ist das ein alter Ratschlag: erst die Begriffe klären, dann bauen.
  Neu ist nur, dass der Gesprächspartner beim Klären mithelfen kann.

## Was ich gelernt habe

- **Messen schlägt raten, und zwar reproduzierbar.**
  Das häufigste Wort meiner eigenen Arbeit fehlte auf der Liste, die ich über meine eigene Arbeit geschrieben hatte.
- **Ein Kürzel ist ein Entwurf und hat Defekte.**
  Widersprüchliche Bedeutung, kollidierendes Escape, doppelt vergebenes Zeichen — das sind gewöhnliche Entwurfsfehler und keine Kleinigkeiten.
- **Prüf jeden Eintrag daran, was ohne ihn anders wäre.**
  Was eine bestehende Regel nur wiederholt, wirkt nicht. Was eine Abwägung verschiebt, wirkt.
- **Eine belegte Bedeutung wird umgebucht, nicht überschrieben.**
  Das, was du schon sagst, ist Bestand. Es bekommt ein neues Zeichen, und das freie behält die neue Bedeutung.
- **Der Gewinn steckt nicht in den Anschlägen.**
  Er steckt in der Runde, die dadurch entfällt.

## Wenn du dir selbst eines bauen willst

Das lohnt sich, sobald du merkst, dass du dich wiederholst — und du merkst es später, als es anfängt.

1. **Zähl zuerst, schreib danach.**
   Nimm deine eigenen Transkripte, sortier nach Häufigkeit und sieh dir die ersten zwanzig Zeilen an. Sie werden dich überraschen.
2. **Nimm nur, was oft genug vorkommt.**
   Ein Zeichen für etwas, das du dreimal im Jahr schreibst, musst du dir merken, ohne dass es dir je etwas spart.
3. **Sieh nach, ob das Zeichen schon belegt ist.**
   In deinem eigenen Bestand, nicht in der Theorie. Wenn ja, zieht die alte Bedeutung um.
4. **Schreib zu jedem Eintrag, was ohne ihn anders wäre.**
   Bleibt die Zeile leer, gehört der Eintrag nicht auf die Liste.
5. **Leg es an einer Stelle ab, die beide Seiten lesen.**
   Ein Codebuch, das nur eine Seite kennt, ist keins.

Der Aufwand dafür ist ein Nachmittag, und der größte Teil davon geht für Schritt drei drauf.
Was danach steht, ist keine Sammlung von Abkürzungen mehr, sondern eine kleine gemeinsame Sprache — und die hat eine Eigenschaft, mit der ich nicht gerechnet hatte.
Sie ist für jemanden, der sie dringender braucht als ich, etwas ganz anderes als eine Bequemlichkeit.
