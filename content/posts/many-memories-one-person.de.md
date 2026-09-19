---
title: "Viele Gedächtnisse, ein Mensch: Wer sich was merkt, wenn ein Agent mitarbeitet"
date: 2026-09-19T04:00:00+02:00
tags: ["claude-code", "context", "memory", "obsidian", "workflow", "Essay"]
themen: ["denken"]
summary: "Ich lagere mein Gedächtnis aus, seit es Papier gibt, inzwischen in einen Obsidian-Vault. Seit ein Agent mitarbeitet, lagert auch er aus, in eigene Dateien. Dieselbe Entscheidung stand danach an drei Orten für drei Leser, und nichts hielt sie zusammen. Neun Tage später war die Kopie beim Agenten die veraltete."
---

## Kurzfassung

- Mein Gedächtnis liegt nur zum Teil in meinem Kopf.
  Der Rest liegt auf Zetteln, im Kalender und seit einiger Zeit in einem Obsidian-Vault.
- Claude Code lagert ebenfalls aus: in eine `CLAUDE.md` je Projekt und in eine Sammlung kleiner Gedächtnisnotizen.
- Beide Seiten bauen sich Speicher, die die andere nicht sieht.
  Mein Vault ist für Claude kein Kontext, seine Notizen lese ich im Alltag nicht.
- An einem Nachmittag im September musste dieselbe Entscheidung an drei Orte geschrieben werden, weil jeder Ort einen anderen Leser hat.
- Nichts hielt die drei zusammen außer Disziplin.
  Neun Tage später wurden 22 Gedächtnisnotizen gestrichen, und eine davon behauptete einen Stand, den der Vault seit drei Tagen widerlegte.
- Was ich daraus mitnehme: Eine Tatsache bekommt einen Ort, und der Ort richtet sich nach dem Leser, der sie braucht.

---

## Der Stapel auf dem Schreibtisch

Ich habe nie alles im Kopf behalten.
Niemand tut das.
Es gibt den Zettel am Monitor, den Kalender an der Wand, das Notizbuch und den Stapel auf dem Schreibtisch, dessen Reihenfolge selbst die Information ist.
Digital kommen die offenen Browser-Tabs dazu, die Shell-History, ein `TODO` im Code.

Für dieses Blog ist es ein Obsidian-Vault.
Er hält fest, worüber ich noch schreiben will, was an schon Veröffentlichtem zu ändern ist und wie weit jede Idee ist.
Ich lese ihn meist auf dem Telefon.
Wie er dorthin kommt, steht in [Auch privat wird kopiert](/de/posts/private-still-means-copied/).
Was dort steht, muss mein Kopf nicht halten, und er hält es auch nicht.
Der Vault ist deshalb kein Zubehör zu meinem Gedächtnis.
Er ist ein Teil davon.

## Der Agent weiß nichts davon

Claude Code, mit dem ich an diesem Blog arbeite, sieht von diesem Teil nichts, solange niemand ihn hineinholt.
Ein Vault ist kein Kontext.
Er kommt erst in die Sitzung, wenn eine Datei daraus gelesen wird, und das passiert, weil ich es anstoße.
Meine [Kürzel](/de/posts/shortcuts-as-an-input-aid/) für „leg das als Idee ab“ oder „bewerte die passenden Beiträge“ sind genau diese Leitung, jedes Mal von Hand ausgelöst.

Umgekehrt gilt dasselbe.
Claude führt ein eigenes Gedächtnis: eine globale `CLAUDE.md` für alle Projekte, eine je Projekt und ein Verzeichnis mit kleinen Notizen, eine Datei je Sache, dazu ein Index namens `MEMORY.md`.
Das ist sein Zettel am Monitor.
Ich lese ihn im Alltag nicht.

Zwei Seiten bauen sich also Speicher, die die andere nicht sieht.
Das allein ist kein Problem.
Es wird eines, sobald eine Seite ihr Ausgelagertes für geteilt hält.

## Drei Ablagen, drei Leser

Am 7. September habe ich den Vault umgebaut.
Die Ideen bekamen Statusordner, `1 Notiert` bis `5 Abgelegt`, damit Obsidians Dateiliste auf dem Telefon zeigt, wie weit jede Idee ist.
Frontmatter sieht man dort nicht, Ordner schon.
Dazu kam ein Feld `wartet_auf`, das Datum verschwand aus den Dateinamen, und ein Prüfskript achtet seitdem darauf, dass Status und Ordner zusammenpassen.

Jede dieser Entscheidungen musste an drei Orte geschrieben werden:

| Ablage | Wer liest sie | Wann |
|---|---|---|
| der Vault selbst: README, Vorlage, Frontmatter | ich, meist auf dem Telefon | beim Notieren |
| die `CLAUDE.md` des Projekts | Claude | bei jedem Sitzungsstart in diesem Projekt |
| Claudes Gedächtnisnotizen | Claude | bei Bedarf, auch in anderen Projekten |

Die Aufteilung folgte der Reichweite.
In den Vault kam die Instanz: dieser Vault, diese Ordner.
In Claudes Gedächtnis kam die Bauregel für den nächsten Vault.
Innerhalb einer Minute entstanden so fünf Gedächtnisnotizen: Statusordner, `wartet_auf`, kein Datum im Dateinamen, Prüfer mit Selbsttest und wie man einen Nachbarvault anlegt.

Das klingt ordentlich.
Es hatte eine Lücke, die man erst beim zweiten Hinsehen bemerkt.

## Nichts hält die drei zusammen

Das Prüfskript prüft den Vault.
Es prüft nicht die `CLAUDE.md`, und Claudes Gedächtnis prüft es schon gar nicht.
Dass alle drei Ablagen nach dem Umbau dasselbe sagten, war Disziplin und kein Mechanismus.
Am Ende stand dieselbe Regel in zwei Vault-READMEs, in der `CLAUDE.md` und in einer Gedächtnisnotiz.
Vier Fassungen eines Sachverhalts, und kein Abgleich.

Wie schnell das auseinanderläuft, zeigte sich zwei Tage später.
Am 9. September legte ich die beiden Vaults zu einem zusammen, weil Obsidian Verweise nur innerhalb eines Vaults auflöst und Ideen und Änderungsvorschläge ständig aufeinander zeigten.
Die Notiz „Nachbarvault anlegen“ beschrieb damit einen Weg, den wir gerade verlassen hatten.
Sie wurde am selben Tag ersetzt.
Das ging gut, weil sie in dem Moment im Blick war, in dem sich die Welt änderte.

Bei einer anderen Notiz ging es nicht gut.
Am 16. September ließ ich Claude sein Gedächtnis durchsehen, mit der Frage, was davon inzwischen dauerhaft woanders steht.
22 Notizen mit zusammen 47,6 Kilobyte wurden gestrichen, darunter alle aus dem Vault-Umbau.
Ihr Inhalt stand längst im Vault und in der `CLAUDE.md` des Projekts.
Bei dreien war gar kein Umzug nötig, und Claude begründete es mit einem Satz, der mir seitdem nicht aus dem Kopf geht:
*„der Vault ist aktueller als mein Gedächtnis“.*
Eine der drei behauptete noch, ein Repository habe keinen öffentlichen Remote.
Im Vault stand seit drei Tagen das Gegenteil.

Niemand hatte die Notiz falsch geschrieben.
Am Tag, an dem sie entstand, war sie richtig.
Sie wurde nur nicht mehr gelesen, als sich die Lage änderte, und ein Gedächtnis, das niemand liest, merkt nicht, dass es veraltet.

## Was ein Kopf zuerst verliert

Die Zeit wirkt auf mein Gedächtnis anders als auf das von Claude.
Claudes Notiz bleibt wörtlich stehen und wird still falsch.
Bei mir ist es umgekehrt: Der Stand bleibt, der Grund geht.
Ich weiß nach zwei Wochen noch, dass eine Idee liegt.
Warum sie liegt, weiß ich nicht mehr.

Genau dafür ist `wartet_auf` da.
Das Feld hält fest, woran etwas hängt, etwa „das Repository ist nicht öffentlich“ oder „rechtlich ungeprüft“.
Es ist ausgelagertes Gedächtnis in Reinform, und es ist die Sorte Wissen, die im Kopf zuerst verschwindet.

Auch das Schreiben kostet beide Seiten verschieden viel, und das hat den Vault mitgeformt.
Das Datum flog aus den Dateinamen, weil ich es auf dem Telefon tippen musste, während dasselbe Datum im Frontmatter ohnehin entstand.
Claude kostet eine Gedächtnisnotiz beim Schreiben nichts Vergleichbares.
Mich kostet jede Zeile auf dem Telefon Anschläge.
Deshalb hat mein ausgelagertes Gedächtnis andere Regeln als seines: wenige Felder, viel Struktur in Ordnern, und was sich ableiten lässt, wird abgeleitet.

## Keine Vererbung in den Kopf

Claudes Ablagen haben eine Eigenschaft, die meine nicht haben.
Beim Start einer Sitzung werden die globale `CLAUDE.md`, die des Projekts und der Index der Gedächtnisnotizen automatisch geladen.
Was dort steht, ist da, ohne dass jemand danach fragt.

Mein Vault erbt nicht in meinen Kopf.
Er will gelesen werden, und gelesen wird er nur, wenn ich ihn öffne.
Deshalb muss er auf dem Telefon lesbar sein, und deshalb steht sein Stand in Ordnernamen statt in Feldern, die man erst aufklappen muss.

Die automatische Vererbung hat umgekehrt einen Preis, über den ich schon [an anderer Stelle](/de/posts/the-most-expensive-answer-is-yes/) geschrieben habe: Was bei jedem Start geladen wird, wird bei jeder Anfrage mitbezahlt.
Jede Gedächtnisnotiz steht mit einer Zeile im Index, und der Index ist immer dabei.
Ein Gedächtnis, das immer da ist, ist auch immer teuer.

## Ein Ort je Tatsache

Was ich daraus mitnehme, ist keine Regel für mehr Abgleich.
Abgleich ist Disziplin, und an Disziplin hatte es ja gefehlt.
Es ist eine Regel für weniger Kopien:

- **Eine Tatsache bekommt einen Ort.**
  Steht sie an zweien, ist eine davon früher oder später die veraltete.
- **Der Ort richtet sich nach dem Leser.**
  Was nur Claude braucht, gehört in seine Dateien, was nur ich brauche, in den Vault.
  Was wir beide brauchen, gehört dorthin, wo wir beide ohnehin hinsehen.
  Bei mir ist das der Vault, weil Claude ihn lesen kann und ich Claudes Dateien nicht lese.
- **Wo es geht, prüft ein Programm.**
  Der Vault hat einen Prüfer, Claudes Gedächtnis hat keinen.
  Auch deshalb stehen die Regeln heute in der README und nicht mehr in fünf Notizen.
- **Das Gedächtnis des Agenten wird regelmäßig ausgemistet.**
  Mit der Frage, was davon inzwischen dauerhaft woanders steht.
  Gestrichen wird nur, was einen Fundort hat.

## Womit ich anfangen würde

Wenn du mit einem Agenten arbeitest, der ein eigenes Gedächtnis führt:

1. **Lies es einmal ganz.**
   Den Index und die Notizen dahinter.
   Du wirst Dinge finden, die du für geteilt gehalten hast, und andere, die längst nicht mehr stimmen.
2. **Such die Tatsachen, die an zwei Orten stehen.**
   Eine davon ist die veraltete, oder sie wird es.
3. **Frag bei jeder, wer sie liest.**
   Die Antwort sagt, wo sie hingehört.

Der Agent vergisst nicht.
Er erinnert sich an einen Stand, den es nicht mehr gibt.
Das ist das Gegenteil von meinem Vergessen, und es ist schwerer zu bemerken.
