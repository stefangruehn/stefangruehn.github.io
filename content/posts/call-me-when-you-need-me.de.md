---
title: "Ruf mich, wenn du mich brauchst: zwei Töne, die aus Warten Weggehen machen"
date: 2026-09-06T02:17:32+02:00
tags: ["claude-code", "workflow", "hooks", "linux", "Field Notes"]
themen: ["kosten"]
summary: "Ein Agent, der zwanzig Minuten rechnet, macht mich nur dann frei, wenn er mich zurückholen kann. Sonst sehe ich alle zwei Minuten nach und bin doch gebunden. Zwei Zeilen Konfiguration machen aus dem Nachsehen einen Rückruf, und den Ausgangswert dafür habe ich noch schnell gemessen, bevor ich es eingeschaltet habe."
---

## Kurzfassung

- Zwei Ereignisse, zwei Klänge: `Stop` heißt „fertig, sieh es dir an", `Notification` heißt „ich hänge und brauche eine Entscheidung".
- Der zweite ist der teure. Bis er beantwortet ist, steht die Arbeit.
- Ohne Rückruf pollt der Mensch: alle zwei Minuten hinsehen, meistens umsonst. Mit Rückruf darf er weggehen.
- Der Ausgangswert aus meinen eigenen Transkripten: 471 Wartezeiten in zwei Wochen, zusammen 20,2 Stunden. 14 Prozent davon länger als fünf Minuten, die längste 48.
- Ob der Ton das verkürzt, weiß ich noch nicht. Seit der Einrichtung sind elf Wartezeiten aufgelaufen, daraus folgt nichts.
- Stumm wird die einzelne Sitzung, nicht der Rechner. Das Skript liest dazu die Sitzungs-ID aus den Hook-Daten.
- Die eingebaute Falle: Hooks werden beim Sitzungsstart gelesen. Der Automatismus, den du gerade einträgst, gilt für dich noch nicht.

---

## Wer wartet hier eigentlich auf wen

Wenn ich einen größeren Auftrag gebe, arbeitet der Agent minutenlang.
Theoretisch bin ich in dieser Zeit frei.
Praktisch war ich es nicht, denn ich wusste ja nicht, in welchem der drei möglichen Zustände er gerade steckt: fertig, noch am Rechnen, oder seit acht Minuten mit einer Frage stehengeblieben, die ich mit drei Zeichen beantworten könnte.

Also habe ich nachgesehen.
Alle paar Minuten, und meistens umsonst.

Für dieses Muster gibt es einen Namen, und er kommt aus der Hardware: Das ist Polling.
Du fragst regelmäßig nach, ob es etwas Neues gibt, und bezahlst jede Frage, auch die vielen leeren.
Die Alternative heißt Interrupt: Das Gerät zieht eine Leitung, wenn es etwas hat, und bis dahin ist die CPU mit anderem beschäftigt.
An einer Türklingel akzeptieren wir das als selbstverständlich — niemand geht alle zwei Minuten zur Tür und schaut nach, ob jemand davorsteht.

An meinem Terminal habe ich es zwei Wochen lang anders gemacht.

## Zwei Ereignisse, zwei Bedeutungen

Claude Code kann bei bestimmten Ereignissen ein Kommando ausführen.
Zwei davon interessieren mich:

- **`Stop`** feuert, wenn eine Antwort fertig ist.
- **`Notification`** feuert, wenn das Programm Aufmerksamkeit braucht. Bei mir ist das fast immer eine Erlaubnisfrage.

Beide bekommen einen Klang, und zwar ausdrücklich **nicht denselben**:

```json
"hooks": {
  "Notification": [{ "hooks": [{ "type": "command",
    "command": "~/.claude/hooks/ton.sh /usr/share/sounds/freedesktop/stereo/message-new-instant.oga" }] }],
  "Stop":         [{ "hooks": [{ "type": "command",
    "command": "~/.claude/hooks/ton.sh /usr/share/sounds/freedesktop/stereo/complete.oga" }] }]
}
```

Zwei verschiedene Klänge sind der ganze Trick.
Ein einziger Ton würde bedeuten: „irgendetwas ist passiert, komm gucken", und damit wäre ich wieder am Hinsehen.
Zwei Töne tragen die Information, auf die es ankommt, nämlich ob es eilt.
„Fertig" darf fünf Minuten liegenbleiben, der Kaffee ist wichtiger.
„Ich brauche eine Entscheidung" heißt, dass gerade nichts passiert, solange ich in der Küche stehe.

Die Klangdateien liegen auf jedem Fedora-System schon herum, das ist der Vorrat aus dem freedesktop-Sound-Theme.
Abgespielt werden sie mit `paplay`, das über PipeWire ohnehin da ist.
Nichts installiert, nichts heruntergeladen, kein eigener Sound gebastelt.

## Zwanzig Stunden Warten

Bevor ich das eingeschaltet habe, wollte ich wissen, worüber wir überhaupt reden.
Claude Code legt für jede Sitzung ein Transkript als JSON-Lines ab, mit Zeitstempel an jeder Zeile.
Damit lässt sich genau die Größe ausrechnen, um die es hier geht: die Spanne zwischen der letzten Zeile einer Antwort und meiner nächsten Nachricht.
Werkzeugausgaben und automatische Einschübe zählen dabei nicht mit, nur echte Nachrichten von mir.

Über alle Projekte hinweg, vom 23. August bis zum 5. September:

| | |
|---|---|
| Wartezeiten insgesamt | 471 |
| Summe | 20,2 Stunden |
| Median | 67 Sekunden |
| länger als 2 Minuten | 32 Prozent |
| länger als 5 Minuten | 14 Prozent |
| länger als 10 Minuten | 5 Prozent |
| die längste | 48 Minuten |

Die Zahl, die weh tut, ist nicht der Median.
Eine gute Minute nachdenken, bevor ich antworte, ist keine verlorene Zeit, das ist die Arbeit.
Die 5 Prozent über zehn Minuten sind die interessanten: 23 Fälle, in denen ich schlicht weg war und nicht wusste, dass ich gebraucht werde.

Ehrlich dazugesagt: Diese 20,2 Stunden sind nicht durchweg Leerlauf.
In vielen Spannen habe ich gelesen, geprüft oder überlegt.
Der Zeitstempel weiß nicht, ob ich in der Küche stand oder eine Ausgabe studiert habe, er misst die Wartezeit des Agenten, nicht die Untätigkeit des Menschen.

Und die zweite ehrliche Auskunft: Ob der Ton daran etwas ändert, kann ich noch nicht sagen.
Er läuft seit gestern Abend um kurz nach sechs.
Seitdem sind elf Wartezeiten aufgelaufen, alle unter zwei Minuten, und aus elf Werten folgt genau nichts.
Der Wert dieser Messung liegt darin, dass sie **vorher** entstanden ist.
In zwei Wochen läuft dasselbe Skript noch einmal, und dann gibt es einen Vergleich statt eines Gefühls.

## Stumm wird die Sitzung, nicht der Rechner

Der erste Entwurf war ein Einzeiler in der Konfiguration, ohne Skript dazwischen.
Der hielt genau bis zu dem Abend, an dem zwei Sitzungen gleichzeitig liefen: eine, die lange rechnete und mich rufen sollte, und eine zweite nebenher, deren Töne mich störten.
Ein globaler Schalter hätte beide stummgeschaltet, also genau die mit, auf die ich gewartet habe.

Deshalb liegt zwischen Hook und Lautsprecher ein kleines Skript.
Die Hook-Daten kommen als JSON auf `stdin`, und darin steht die Sitzungs-ID:

```sh
sid=$(printf '%s' "$eingabe" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

[ -n "$sid" ] && [ -e "$HOME/.claude/mute-$sid" ] && exit 0
[ -e "$HOME/.claude/mute-all" ] && exit 0

paplay "$klang" >/dev/null 2>&1 &
```

Eine Sitzung schweigt, solange eine Datei mit ihrer ID existiert.
Zwei Kürzel legen sie an und löschen sie wieder, `[x]` aus, `[o]` an, und das ist die ganze Bedienung.
Andere offene Sitzungen bleiben hörbar, ohne dass ich irgendwo eine ID abtippen müsste.

Das Skript hat noch einen zweiten Zweig, den ich hier stehenlasse, weil er ein allgemeines Muster ist: Ältere Fassungen liefern statt der ID nur den Pfad zum Transkript.
Die ID steht dann im Dateinamen, und `basename` holt sie da heraus.
Vier Zeilen für den Fall, dass sich unter mir etwas ändert.

## Der Hook, der beim Eintragen noch nicht gilt

Eine Sache hat mich zwanzig Minuten gekostet, und sie ist typisch für Automatismen, die sich selbst betreffen.

Hooks werden **beim Sitzungsstart** eingelesen.
Trage ich mitten in einer Sitzung einen ein, tut sich in genau dieser Sitzung nichts, bis `/hooks` oder ein Neustart.
Ausgerechnet die Sitzung, in der du die Benachrichtigung einrichtest, hat keine Benachrichtigung.
Und weil du gerade an ihr arbeitest, ist sie auch die, in der du sie prüfen willst.

Die Zwischenlösung ist unelegant und funktioniert: Solange der Hook noch nicht greift, spielt der Agent den Ton selbst, als letzten Befehl seiner Antwort.
Das ist derselbe `paplay`-Aufruf, nur eine Ebene höher.
Wer sich einen Automatismus baut, sollte ihn so bauen, dass er auch von Hand auslösbar ist.
Dann ist der Zustand „noch nicht aktiv" kein Sonderfall, sondern nur ein zusätzlicher Handgriff.

## Was der Ton nicht kann

Er macht Rückfragen nicht billiger.
Eine Frage an mich kostet den Agenten eine volle Runde mit dem gesamten mitgeschleppten Kontext, und das ist der [teuerste Posten](/de/posts/the-most-expensive-answer-is-yes/) im ganzen Betrieb, daran ändert ein Klang nichts.
Was er ändert, ist die Wartezeit davor.

Genau deshalb sind es nur zwei Ereignisse geblieben.
Es gäbe mehr: vor jedem Werkzeugaufruf, nach jedem Werkzeugaufruf, bei jedem Sitzungsende.
Ein Ton, der ständig kommt, wird nach zwei Stunden nicht mehr gehört — und dann höre ich auch den einen nicht mehr, der zählt.

## Was ich gelernt habe

- **Ein Agent macht dich nur frei, wenn er dich zurückholen kann.**
  Sonst tauschst du das Warten am Bildschirm gegen das Nachsehen im Vorbeigehen, und gewonnen hast du wenig.
- **Zwei Zustände brauchen zwei Töne.**
  „Fertig" und „ich hänge" kosten dich verschieden viel. Ein gemeinsamer Ton wirft die Information weg, wegen der du überhaupt hinhörst.
- **Der Schalter gehört an die Sitzung, nicht an die Maschine.**
  Global stummschalten heißt: Du machst genau das aus, worauf du wartest.
- **Automatismen, die sich selbst betreffen, gelten für sich selbst noch nicht.**
  Der Hook greift ab dem nächsten Start. Halte den manuellen Auslöser bereit.
- **Miss vorher.**
  Der Ausgangswert kostet zehn Minuten, solange die Daten noch unberührt sind. Hinterher ist er nicht mehr zu bekommen.

## Das Gleiche an deinem Rechner

Wenn du mit einem Agenten arbeitest, der länger rechnet, als du zusehen magst:

1. **Nimm zwei Ereignisse, nicht acht.** Fertig, und braucht-dich. Alles Weitere verwässert beide.
2. **Nimm zwei verschiedene Klänge.** Die liegen auf deinem System schon herum, du musst nichts installieren und nichts aussuchen, was gut klingt, nur zwei, die du auseinanderhältst.
3. **Bau die Stummschaltung gleich mit, und zwar pro Sitzung.** Der Tag, an dem du zwei Sitzungen parallel fährst, kommt früher als gedacht.
4. **Prüf es in einer neuen Sitzung.** Die, in der du es einträgst, ist die einzige, in der es nicht funktioniert.
5. **Miss deine Wartezeiten, bevor du es einschaltest.** Deine Transkripte liegen schon da, mit Zeitstempel an jeder Zeile.

Seit gestern klingelt mein Rechner, wenn er mich braucht.
Vorher habe ich ihn gerufen, alle zwei Minuten, und meistens hatte er nichts zu sagen.
