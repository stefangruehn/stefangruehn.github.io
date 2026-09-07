---
title: "Die kleinste Änderung ist zwei: was 57 Commits über die Kopplung dieses Blogs sagen"
date: 2026-09-07T02:17:00+02:00
draft: false
tags: ["claude-code", "workflow", "komplexität", "chaos", "messung", "selbstbezug", "Essay"]
themen: ["schreiben"]
series: ["Rueckkopplung"]
summary: "In sieben Tagen sind 39 Beitragsdateien entstanden und 86 bestehende geändert worden. Die meisten Änderungen fassen zwei Dateien an, eine fasste achtzehn an. Diese Verteilung ist der Grund, warum sich ein Blog wie ein gekoppeltes System verhält — und die Stelle, an der ich beiläufig an ihm drehe."
---

Die kleinste mögliche Änderung an diesem Blog ist zwei Dateien.
Es gibt keine Änderung an einer Stelle, weil jeder Beitrag zweisprachig ist.

## Kurzfassung

- Gezählt über 57 Commits vom 31. August bis 6. September: 39 neue Beitragsdateien, 86 Änderungen an bestehenden.
  Am Bestand wurde mehr als doppelt so oft gearbeitet wie am Neuen.
- 29 der 57 Commits fassen keinen bestehenden Beitrag an.
  Wenn einer es tut, sind es im Mittel 3,1 Dateien, im Median 2 — und einmal 18.
- Die 18 stammen aus einer einzigen Entscheidung: Themenseiten als ersten Einstieg einzuführen.
  Ein Satz im Gespräch, achtzehn Beiträge im Commit.
- Was ich dabei verstelle, ist nicht das Tempo, sondern die Kopplung.
  Jede Strukturentscheidung erhöht dauerhaft die Zahl der Stellen, die eine spätere Entscheidung anfassen muss.
- Damit sind drei der vier Zutaten beisammen, die aus einer Schleife eine Schwingung machen: Rückkopplung, Verzögerung, Verstärkung.
  Die vierte wäre eine begrenzte Ressource, und die ist gemessen: 7,8 Prozent am Vormittag, 70 Prozent am Mittag.
- Was hier nicht gemessen ist: Chaos.
  Sieben Tage sind keine Zeitreihe, und die Zahl der geänderten Dateien ist keine Population.
- Was sich messen ließe, steht am Ende: das Verhältnis von Bestandsarbeit zu Neuem, über Wochen statt über Tage.

---

## Die Zählung

Der erste Commit liegt auf dem 31. August 2026, der letzte dieser Zählung auf dem 6. September.
Dazwischen liegen 57 Commits.

In ihnen entstehen 39 neue Beitragsdateien — das sind, weil jeder Beitrag doppelt existiert, knapp zwanzig Beiträge einschließlich der Entwürfe.
Und es werden 86-mal bestehende Beitragsdateien geändert.

Das Verhältnis überrascht beim ersten Hinsehen: Auf jede neu geschriebene Datei kommen gut zwei Änderungen an schon geschriebenen.
Ein Blog in seiner ersten Woche sieht von außen aus wie eine Sammlung, die wächst.
Von innen ist er zu zwei Dritteln Umbau.

Pro Tag sieht das so aus:

| Tag | neu | geändert |
|---|---|---|
| 31.08. | 3 | 3 |
| 01.09. | 0 | 8 |
| 02.09. | 6 | 14 |
| 03.09. | 6 | 24 |
| 04.09. | 0 | 2 |
| 05.09. | 6 | 3 |
| 06.09. | 18 | 32 |

Am 3. September kommen auf sechs neue Dateien 24 Änderungen, am 5. September auf sechs neue Dateien drei.
Das ist derselbe Blog, zwei Tage auseinander, mit einem Verhältnis, das um den Faktor acht springt.

## Wie weit eine Änderung reicht

Interessanter als die Summe ist, wie sich die 86 auf die Commits verteilen.

29 der 57 Commits fassen überhaupt keinen bestehenden Beitrag an: neue Beiträge, Layoutarbeit, Werkzeuge, Konfiguration.
Bei den übrigen liegt der Median bei 2 und der Mittelwert bei 3,1.

Der Median 2 ist der Grundton dieses Blogs.
Zwei heißt: deutsche Fassung, englische Fassung, sonst nichts.
Eine Korrektur an einem Satz ist hier nie eine Änderung, sondern immer zwei.

{{< ausbreitung >}}

Die fünf größten Ausschläge sehen anders aus:

| Dateien | Anlass |
|---|---|
| 18 | Themenseiten als ersten Einstieg einführen |
| 8 | die Serie veröffentlichen und die Reihenfolge richtigstellen |
| 7 | auf den deutschen Seiten „KI" schreiben statt „AI" |
| 6 | die Schluss-Überschriften sagen lassen, was der Abschnitt tut |
| 4 | die beiden Laptop-Beiträge unter einem gemeinsamen Stichwort bündeln |

Keiner dieser fünf Anlässe ist ein Beitrag.
Alle fünf sind Entscheidungen über die Form, und jede einzelne hat mehr Beiträge angefasst, als an dem Tag geschrieben wurden.

## Der Parameter

Der Satz, mit dem die 18 anfingen, war kein technischer Auftrag.
Er lief darauf hinaus, dass Leser nicht mit einer Liste nach Datum empfangen werden sollten, sondern mit Fragen — was hier eigentlich verhandelt wird.

Aus diesem Wunsch folgt eine Regel: Jeder Beitrag gehört zu genau einem Thema, und jedes Thema hat eine Seite.
Achtzehn Beitragsdateien mussten dafür ein Feld bekommen.

Das ist der einmalige Preis, und er ist nicht der Punkt.
Der Punkt ist der dauerhafte: Seit diesem Tag ist jeder neue Beitrag an die Themenordnung gekoppelt.
Wer eine Themenseite umbenennt, fasst alles an, was daran hängt.
Wer ein Thema teilt, muss für jeden Beitrag neu entscheiden.

Dasselbe gilt für Serien.
Eine Serie ist nicht nur ein Feld im Vorspann, sie hat eine Seite, auf der steht, was die einzelnen Teile tun.
Ändert sich ein Teil, stimmt diese Beschreibung nicht mehr.

Ich habe diese Kopplungen nicht als Kopplungen beschlossen.
Ich habe gesagt, was ich mir für den Leser wünsche, und die Kopplung war die Folge.
Genau das meint Parametrisieren im Vorbeigehen: Der Satz handelt vom Einstieg für Leser, seine Wirkung liegt auf der Verbindungsdichte des Systems.

## Drei von vier Zutaten

Damit eine Schleife nicht ruhig einläuft, sondern schwingt, braucht es vier Dinge.

**Rückkopplung.** Sie ist belegt: Die Klammerregel steht in der Datei, die die nächste Sitzung liest.

**Verzögerung.** Sie ist belegt: Eine Regel gilt ab der nächsten Sitzung, ein Hook ab dem nächsten Start.
Zwischen Einsicht und Wirkung liegt immer mindestens ein Schnitt.

**Verstärkung.** Sie ist gemessen: Der Median liegt bei 2, das Maximum bei 18.
Ein Verstärkungsfaktor, der zwischen zwei und achtzehn schwankt, ist nicht linear.

**Eine begrenzte Ressource.** Auch die ist gemessen, an anderer Stelle: [Dieselben drei Agenten](/de/posts/the-most-expensive-answer-is-yes/) machten am Vormittag 7,8 Prozent des Verbrauchs aus und am Mittag 70 Prozent.
Dazwischen lag kein neues Werkzeug, nur ein größerer Kontext.

Vier von vier.
Das ist keine Kleinigkeit und es ist auch kein Beweis.

## Was diese Zahlen nicht zeigen

Sie zeigen kein Chaos.

Die logistische Abbildung, an der sich das zeigen ließe, verlangt eine wiederholte Messung derselben Größe über viele Schritte: x heute, x morgen, x übermorgen, und dann sieht man, ob es einläuft, pendelt oder auseinanderfliegt.
57 Commits über sieben Tage sind dafür zu wenig, und „geänderte Beitragsdateien je Commit" ist keine Population, die sich selbst begrenzt.
Sie ist ein Nebenprodukt meiner Arbeitsweise, kein Zustand des Systems.

Auch die Spitze bei 18 ist kein Ausschlag im Sinn einer Schwingung.
Sie ist ein einmaliger Einbau, wie er in jedem Projekt vorkommt, wenn ein Ordnungsprinzip nachgerüstet wird.

Was die Zahlen zeigen, ist bescheidener und immer noch bemerkenswert: dass die Bedingungen erfüllt sind.
Ob das System sie nutzt, sagt nur eine längere Messung.

## Was sich messen ließe

Die Größe, die ich für aussagekräftig halte, ist das Verhältnis von Änderungen am Bestand zu neuen Dateien, gemessen pro Woche statt pro Tag.

Bleibt es bei etwa zwei zu eins, ist der Umbau gesunder Unterhalt.
Steigt es über mehrere Wochen, frisst die Struktur das Schreiben: Dann geht die Arbeit in die Ordnung der vorhandenen Texte statt in neue.
Fällt es gegen null, ist die Ordnung eingefroren — auch kein gutes Zeichen, nur ein anderes.

Die Zahl steht in jedem Repository, sie muss nur einmal ausgerechnet werden.
In sieben Tagen weiß ich mehr; die Zählung von heute ist der Anfangswert, gegen den ich später vergleiche.

## Was ich gelernt habe

- **Die kleinste Änderung ist selten eins.** Zweisprachigkeit macht aus jedem Fund zwei Handgriffe. Das ist kein Ärgernis, sondern die Grundverstärkung des Systems, und man sollte sie kennen, bevor man Aufwand schätzt.
- **Strukturentscheidungen kosten zweimal.** Einmal beim Einbau, sichtbar im Commit. Und dann dauerhaft, unsichtbar, an jedem Beitrag, der danach entsteht.
- **Wer über den Leser spricht, entscheidet über die Kopplung.** Der Satz klang nach Gestaltung und war eine Aussage über die Verbindungsdichte.
- **Die Bedingungen für eine Schwingung sind leichter erfüllt, als es aussieht.** Rückkopplung, Verzögerung, Verstärkung und eine knappe Ressource — vier Dinge, die in einem Blog von vierzehn Beiträgen bereits alle vorliegen.
- **Bedingungen erfüllt heißt nicht Wirkung nachgewiesen.** Die Trennung zwischen beidem ist der ganze Unterschied zwischen einer Messung und einer schönen Erzählung.

## Was sich übertragen lässt

Wenn dich interessiert, wie stark dein eigenes Projekt gekoppelt ist, brauchst du keine Theorie, sondern eine Zeile Auswertung: Zähle für jeden Commit, wie viele bestehende Inhaltsdateien er anfasst, und sieh dir den Median und das Maximum an.

Der Median sagt dir, was eine gewöhnliche Änderung kostet.
Das Maximum sagt dir, was eine Entscheidung kosten kann.
Klaffen beide weit auseinander, hast du ein System, in dem seltene Entscheidungen teuer sind — und in dem es sich lohnt, vor der nächsten kurz innezuhalten.

Die Zahl selbst ist harmlos.
Interessant wird sie, wenn du sie in vier Wochen noch einmal ausrechnest.
