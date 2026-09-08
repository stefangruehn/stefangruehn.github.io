---
title: "Das seidige Geräusch mechanischen Rechnens: woher der Stoff kommt"
date: 2026-09-06T09:00:00+02:00
tags: ["chaos", "complexity", "hardware", "books", "Essay"]
themen: ["autor"]
series: ["Selbstaehnlichkeit"]
summary: "Ein Zauberwürfel, vier Regeln über Nachbarzellen, eine Formel mit drei Zeichen und eine Rechenmaschine, die man drehen kann. Vier Gegenstände, die dieselbe Sache zeigen, und ein Satz aus meinen eigenen Notizen, den ich dafür ausschreiben musste."
---

Eine Rechenmaschine hat mir einmal eine Gänsehaut gemacht.
Das ist ein seltsamer Satz, und er ist der kürzeste Weg zu der Frage, worum es hier eigentlich geht.

## Kurzfassung

- Vier Gegenstände haben die Richtung gesetzt: ein Zauberwürfel, Conways *Life*, das Apfelmännchen und eine Curta.
- Allen vieren ist dasselbe gemeinsam.
  Eine Handvoll Regeln, aus denen mehr folgt, als man ihnen ansieht, und kein Weg, das Ergebnis abzukürzen.
- Zwei Bücher haben daraus einen Begriff gemacht: *Gödel, Escher, Bach* und *A New Kind of Science*.
- Der Satz, der alles zusammenhält, passt in eine Zeile: x → r · x · (1 − x).
- Einen Satz aus meinen eigenen Notizen musste ich dafür ausschreiben.
  So knapp notiert, wie er dastand, war er wörtlich genommen falsch, und die ausgeschriebene Fassung ist die interessantere.
- Nichts davon ist Nostalgie.
  Es ist das Werkzeug, mit dem ich im nächsten Teil auf agentische KI sehe.

---

## Vier Gegenstände

**Der Würfel.**
Sechs Seiten, eine Handvoll erlaubter Drehungen, gut 43 Trillionen mögliche Stellungen.
Aus fast nichts folgt ein Raum, den niemand durchsuchen kann.
Man löst so einen Würfel deshalb auch nicht durch Suchen, sondern durch Verfahren: kleine Folgen von Zügen, die genau eine Sache ändern und alles andere zurücklassen, wie es war.
Das war, lange bevor ich das Wort dafür kannte, meine erste Begegnung mit einem Algorithmus.

**Conways *Life*.**
Ende der Achtziger, erster eigener PC, Turbo Pascal, 5¼-Zoll-Disketten.
Vier Regeln darüber, wann eine Zelle lebt und wann sie stirbt, und sie hängen nur von der Zahl der lebenden Nachbarn ab.
Aus diesen vier Regeln fallen Gleiter, die über das Gitter wandern, Blinker, die im Takt schlagen, und Gebilde, die andere Gebilde bauen.
Von all dem steht kein Wort in den Regeln.
Man sieht es erst, wenn man es laufen lässt.

**Das Apfelmännchen.**
z → z² + c, ein einziger Ausdruck, ein paar Zeilen Code drumherum.
Der Rand der Menge ist unendlich fein. Man kann beliebig weit hineinfahren und findet immer wieder Struktur, immer wieder das Ganze im Kleinen.
Ein Bild in brauchbarer Auflösung brauchte auf der Maschine von damals lange genug, dass man den Rechner damit allein lassen konnte.
Es war das zweite Programm, das ich geschrieben habe, und das erste, bei dem ich das Ergebnis nicht vorhergesehen hatte.

**Die Curta.**
Die bekommt einen eigenen Abschnitt.

## Ein Algorithmus, den man drehen kann

Die Curta ist eine mechanische Rechenmaschine, klein genug für eine Hand, gebaut um eine gestufte Walze herum.
Konstruiert hat sie Curt Herzstark. Die entscheidenden Zeichnungen entstanden, während er im Konzentrationslager Buchenwald gefangen war.
Gebaut wurde sie ab 1948 von der Contina AG in Liechtenstein.

Man stellt eine Zahl ein, dreht die Kurbel, und im Inneren läuft die Rechnung durch die Zahnräder.
Man hört sie dabei.
Es ist ein seidiges Geräusch, sehr gleichmäßig, und man spürt es in der Hand als feine Vibration, bis es am Ende der Umdrehung einrastet.

Die Gänsehaut kam nicht von der Nostalgie.
Sie kam von der Einsicht, dass ein Verfahren ein Gegenstand sein kann.
Ein Algorithmus, den man in die Hand nimmt, dreht und dabei arbeiten hört — ohne Strom, ohne Bildschirm, ohne eine einzige Stelle, an der man ihm glauben müsste.

## Zwei Bücher

*Gödel, Escher, Bach* von Douglas R. Hofstadter, 1979.
Ein Buch über Rekursion, Selbstbezug und seltsame Schleifen, und darüber, wie aus Regeln, die selbst nichts bedeuten, Bedeutung entstehen kann.

*A New Kind of Science* von Stephen Wolfram, 2002.
Die systematische Fassung derselben Sache: elementare zelluläre Automaten, durchnummeriert, einer nach dem anderen abgefahren, und mittendrin Regel 110, die aus einer Zeile Vorschrift Muster erzeugt, die man ihr nicht ansieht.
Von dort kommt auch der Begriff, auf den es in dieser Serie ankommt: *computational irreducibility*.
Für manche Prozesse gibt es keine Abkürzung.
Wer wissen will, wie sie ausgehen, muss sie Schritt für Schritt durchlaufen lassen.

Beide Bücher haben mich vor allem staunen lassen über die Geistesgröße ihrer Autoren.
Dass ich heute Wolfram-Code für Datenanalysen schreibe, ist kein Zufall. Von diesem Buch bis zu meiner Arbeit führt eine sehr lange Leitung.

Von zellulären Automaten habe ich nächtelang geträumt.
Das ist keine Redewendung.

## Der eine Satz

Wenn ich das alles auf eine Zeile bringen müsste, wäre es diese:

    x → r · x · (1 − x)

Die logistische Abbildung.
Sie beschreibt, wie viel von etwas nächstes Jahr da ist, wenn dieses Jahr x davon da ist: Wachstum, multipliziert mit der eigenen Begrenzung.
Zwei Zutaten, eine Zeile.

Bei kleinem *r* läuft sie auf einen festen Wert zu.
Dreht man *r* hoch, springt sie irgendwann zwischen zwei Werten hin und her, dann zwischen vieren, dann zwischen achten.
Die Abstände zwischen diesen Verdopplungen schrumpfen in einem festen Verhältnis, der Feigenbaum-Konstante, ungefähr 4,669.
Und dann, kurz danach, ist es Chaos: keine Periode mehr, keine Wiederkehr, und zwei Startwerte, die sich in der achten Nachkommastelle unterscheiden, laufen nach ein paar Dutzend Schritten völlig auseinander.

Robert M. May hat das 1976 in *Nature* aufgeschrieben, unter einem Titel, der bis heute alles sagt: *Simple mathematical models with very complicated dynamics*.

### Wo ich mich präzisieren muss

In meinen Notizen zu diesem Beitrag stand der Satz, die logistische Gleichung lasse sich „trotz aller Rechenpower bis heute nicht simulieren oder auch nur adäquat abbilden, außer durch die Formel selbst".

So notiert ist das zu knapp.
Wörtlich genommen wäre es falsch: Iterieren kann die Gleichung jeder Taschenrechner, und zwar beliebig oft.

Gemeint waren zwei Aussagen, die einzeln haltbar sind.
Erstens gibt es für allgemeines *r* keine geschlossene Lösung, die x nach n Schritten direkt ausrechnet. Ausnahmen wie *r* = 4 sind bekannt und bleiben Ausnahmen.
Zweitens ist die konkrete Bahn bei endlicher Rechengenauigkeit langfristig nicht vorhersagbar, weil jeder Rundungsfehler mitwächst.

Die zweite ist die, die ich meinte: „außer durch die Formel selbst" heißt, dass es keinen Weg an den Schritten vorbei gibt.
Der Begriff, der beides zusammenfasst, ist wieder Wolframs: keine Abkürzung.
Man muss durch.

Ausgeschrieben ist das die stärkere Aussage, nicht die schwächere — und deshalb steht dieser Abschnitt hier, statt dass ich den verkürzten Satz einfach übernommen hätte.

## Was sich übertragen lässt

Wer etwas Komplexes verstehen will, sucht zuerst nach der Formel, die das Ergebnis vorhersagt.
Bei den Systemen, um die es hier geht, gibt es die nicht.
Was es gibt, ist die Regel, die das Ergebnis erzeugt.

Der Unterschied ist ganz praktisch.
Eine Vorhersage kann man glauben oder bezweifeln.
Eine Regel muss man laufen lassen und dabei messen.

Das ist der Grund, warum in diesem Blog so viele Beiträge mit einer Messung enden und nicht mit einer Erklärung.
Und es ist die Brücke zum nächsten Teil: Dieselben Regeln, die für einen Zellautomaten gelten, tauchen wieder auf, sobald hinreichend komplexe Agenten miteinander zu tun bekommen.
