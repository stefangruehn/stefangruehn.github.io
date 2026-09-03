---
title: "Stille ohne Fehlermeldung: Die Null, die sich mein Audio-Server gemerkt hat"
date: 2026-09-02T16:40:00+02:00
draft: false
tags: ["claude-code", "linux", "audio", "pipewire", "debugging", "chuwi", "nerdfutter", "technical deep dive"]
series: ["Nachhall"]
summary: "Der Lautsprechertest in den Systemeinstellungen blieb stumm, während Musik und Video einwandfrei liefen. Die Ursache war kein defekter Treiber, sondern eine einzelne Zahl, die sich mein Audio-Server treu gemerkt hatte — übrig geblieben aus genau der Fehlersuche, über die ich beim letzten Mal geschrieben habe."
---

Beim letzten Mal ging es hier ums [Messen statt Raten](/de/posts/measure-dont-guess/),
um die Lautsprecher in diesem Laptop und darum, sich öffentlich zu irren und es zu korrigieren.
Dies ist ein kurzes Nachwort dazu.
Drei Tage nach dem Ende jener Arbeit zeigte derselbe Laptop ein neues Symptom — und es stellte sich als Rückstand der Fehlersuche selbst heraus,
nicht der Hardware und nicht der Lösung.

*Nachtrag vom 3.9.2026:* Inzwischen ist daraus eine Serie geworden.
Alle Teile, und ein Schema vorweg, das zeigt, worauf man sich einlässt: [Nachhall](/de/series/nachhall/).

## Kurzfassung

- In Einstellungen → Ton spielte der Dialog **Lautsprecher testen** nichts ab.
  Chrome, Musik und Video liefen völlig normal.
- Jede Schicht meldete Erfolg.
  Die Klangdatei wurde gefunden, der Stream angelegt, die Wiedergabe fehlerfrei beendet. Sie war nur unhörbar.
- Die Ursache war eine Zeile in einer Zustandsdatei: Mein Audio-Server hatte sich für genau die Art Stream, die dieser Dialog erzeugt, **eine Lautstärke von null gemerkt**.
- Meine erste Theorie, wie sie dorthin kam, war falsch, und eine Messung sagte das innerhalb einer Minute.
  Die endgültige Antwort ist ehrlich, aber unvollständig: Ich kann den Mechanismus reproduzieren, nicht den konkreten ursprünglichen Schreibvorgang.
- Die Reparatur war ein Befehl.
  Herauszufinden, *was* zu reparieren war, war der ganze Rest.

## Eine Erfolgsmeldung und kein Ton

Fedora 44, GNOME 50, PipeWire.
Zwei kleine Lautsprechersymbole in den Toneinstellungen, eines je Seite; ein Klick darauf soll einen kurzen Testton in genau diesen Lautsprecher schicken.
Aus keinem der beiden kam etwas.
Alles andere auf dem Rechner gab normal Ton aus, was die halbe Fehlersuche sofort ausschließt.

Unangenehm daran war, dass nirgends ein Fehler gemeldet wurde.
Der Desktop spielt diese Klänge über eine kleine Bibliothek ab, die einen benannten Klang in einem Thema nachschlägt und ihn an den Audio-Server übergibt.
Diese Bibliothek fand die Datei, legte den Stream an, spielte ihn zu Ende und meldete Erfolg.
Es gab keine Fehlermeldung, nach der man hätte suchen können.

Das ist die unangenehme Sorte Fehler: nicht „es ist kaputt", sondern „es hat genau das getan, was es gesagt hat, und passiert ist nichts".

## Messen statt dem Rückgabewert glauben

Der nützliche Schritt war, aufzuhören, Rückgabewerte zu lesen, und stattdessen aufzuzeichnen, was den Rechner tatsächlich verlässt.
Man kann den Audio-Server bitten, eine Kopie von allem herauszugeben, was ein bestimmter Ausgang gerade abspielt.
Also: Aufnahme starten, Testklang abspielen, danach den Spitzenpegel der Aufnahme ansehen.

Dieselbe Klangdatei, zwei verschiedene Abspielwege:

| Abspielweg | Spitze links | Spitze rechts |
|---|---|---|
| ein schlichter Audio-Player | 4301 | 4301 |
| die Klangbibliothek des Desktops, so aufgerufen wie vom Einstellungsdialog | 0 | 0 |

Exakt null, nicht „leise".
Die Datei war in Ordnung, das Gerät war in Ordnung, und der Unterschied musste daran liegen, *wie* der Desktop danach fragte.

Ein Blick auf den laufenden Stream während der Wiedergabe lieferte die Antwort in einer Zeile:

```
media.role = "test"
Mute: no
Volume: mono: 0 / 0% / -inf dB
```

Nicht stummgeschaltet. Ganz heruntergedreht.

## Was sich der Audio-Server notiert hatte

Audio-Server merken sich Lautstärken pro Anwendung, damit der Videoplayer, den man letzte Woche leiser gestellt hat, heute noch leiser ist.
Dieses Gedächtnis liegt in einer schlichten Textdatei, und darin stand:

```
Output/Audio:media.role:Test={"channelMap":["FL"], "volume":1.0, "mute":false, "channelVolumes":[0.000000]}
```

Der Lautsprechertest kennzeichnet seinen Ton mit der Rolle `test`.
Für diese Kennzeichnung war eine Lautstärke von null gespeichert, und sie wurde jedes einzelne Mal getreulich angewendet.
Die Nachbareinträge — `Music`, `Movie`, die Browser, der Videoplayer — standen alle auf 1.0,
und genau deshalb klang alles andere normal und nur dieser eine Dialog blieb stumm.

Es war nichts kaputt.
Eine Einstellung war einmal aufgezeichnet und seither befolgt worden.

## Hat meine eigene Lösung das verursacht?

Das war meine erste Frage, denn die Arbeit aus dem vorigen Beitrag endete mit einer Änderung an genau diesem Teil des Systems:
Lautstärke und Balance aus dem Tonchip heraus in die Software zu verlegen, damit die Verstärkung jedes Kanals bei seinem eigenen Lautsprecher ankommt.

Die ehrliche Antwort hat drei Teile.

**Die Lösung selbst kann das nicht.** Sie ist eine einzeilige Regel, die eine Eigenschaft der *Soundkarte* ändert.
Die Null sitzt auf einem *Stream*, in einem völlig anderen Mechanismus.
Ich habe die naheliegende Brücke dazwischen geprüft — die Balance an den Anschlag fahren, dann den Lautsprechertest laufen lassen — und nachgesehen, ob das etwas in den gespeicherten Eintrag schreibt.
Tut es nicht. Hypothese erledigt, eine Minute, keine Diskussion.

**Die Fehlersuche rund um die Lösung ist der plausible Ursprung.** Jene Sitzung bestand genau daraus, die Balance an beide Anschläge zu fahren
und dann mit *eben diesem Dialog* herauszufinden, welcher Lautsprecher noch spielt.
Den Mechanismus konnte ich direkt reproduzieren: Gibt man einem `test`-Stream einmal eine Kanallautstärke von null, speichert der Server sie und gibt sie jedem späteren Test-Stream mit.
Der nächste startet von allein mit `0 / 0% / -inf dB`.

**Was ich nicht behaupten kann**, ist der konkrete ursprüngliche Schreibvorgang.
Ihn zu reproduzieren hieße, den Zustand des Rechners vor der Lösung wiederherzustellen, und den gibt es hier nicht mehr.
Also: Mechanismus reproduziert, konkretes Ereignis erschlossen.
Diesen Satz schreibe ich lieber als einen glatteren, der mehr behauptet, als ich gemessen habe.

Es gibt einen vierten Teil, und den finde ich am interessantesten.
Die Lösung hat funktioniert — *deshalb* blieb das hier drei Tage verborgen.
Alles, wofür die Lösung zuständig war, kam richtig heraus, also deutete nichts auf jene Sitzung zurück,
und die eine veraltete Zahl, die sie nie hätte aufräumen können, saß dort und wurde befolgt.

## Die Reparatur

Dafür gibt es keinen Einstellungsdialog, aber einen vorgesehenen Weg:
Der Wert wird gespeichert, wenn sich die Lautstärke eines Streams ändert — also erzeugt man einen Stream mit dieser Kennzeichnung, stellt ihn auf 100 % und lässt den Server es notieren.

```bash
# einen Stream mit der Rolle des Lautsprechertests offen halten
paplay --property=media.role=test stille.wav &
# ihn suchen und wieder auf voll stellen
pactl set-sink-input-volume "$ID" 100%
```

Geprüft auf demselben Weg wie diagnostiziert — Ausgang aufzeichnen, Test abspielen, Spitzen ablesen:

| Test | Spitze links | Spitze rechts |
|---|---|---|
| linker Lautsprecher | 4301 | 0 |
| rechter Lautsprecher | 0 | 4301 |

Jede Seite spielt auf ihrer eigenen Seite, auf demselben Pegel wie die Referenz.
Kein Neustart, keine Neuanmeldung.

## Eine zweite Stille, mit anderer Ursache

Unterwegs lief ich in eine zweite Stummheit und hätte sie beinahe unter dieselbe Überschrift einsortiert.
Ein Kommandozeilenwerkzeug verweigerte dieselben Klänge mit `Sound disabled`.
Völlig anderer Grund: Die System-Ereignisklänge waren in den Desktop-Einstellungen schlicht abgeschaltet — ein bewusster Schalter, an dem der Lautsprechertest gar nicht vorbeikommt.

Zwei Stillen, ein Einstellungsdialog, nichts miteinander zu tun.
Die Ereignisklänge wieder einzuschalten war eine Einstellung — und brachte eine dritte Kleinigkeit ans Licht:
Benachrichtigungsklänge waren mit 90,48 % statt 100 % gespeichert.
Auf voll gestellt und nachgemessen ergab sich ein Pegelverhältnis von 1,1052 gegenüber den vorhergesagten 1 / 0,904817 = 1,1052.
Vier Stellen Übereinstimmung sind mehr, als die Frage verdient hatte, aber es ist eine schöne Art, sicher zu sein, dass man das geändert hat, was man ändern wollte.

## Was ich gelernt habe

- **„Erfolg" ist eine Aussage über den Codepfad, nicht über die Welt.**
  Jede Schicht hier meldete Erfolg und erzeugte Stille. Nur die Aufzeichnung konnte den Unterschied sehen.
- **Bevorzuge eine Messung, die dich blamieren kann.** Meine Ursachentheorie war ordentlich und falsch.
  Das herauszufinden kostete eine Minute; sonst hätte ich eine selbstbewusst falsche Erklärung aufgeschrieben.
- **Eine funktionierende Lösung und ein sauberes System sind nicht dasselbe.**
  Fehlersuche hinterlässt Ablagerungen. Die Werkzeuge, mit denen man ein Problem untersucht, haben ein eigenes Gedächtnis,
  und das wird nicht zurückgesetzt, wenn die eigentliche Reparatur ankommt.
- **Zustand, der sich still hält, verdient Misstrauen.** „Es merkt sich deine Einstellungen" ist ein Vorteil — bis zu dem Moment,
  in dem es sich etwas merkt, das man nie behalten wollte, und dann steht nirgends eine Fehlermeldung, weil nichts fehlgeschlagen ist.
- **Unvollständige Antworten sind erlaubt.** „Ich habe den Mechanismus reproduziert, aber nicht das konkrete Ereignis" ist ein echtes Ergebnis.
  Es zu einer glatten Ursachengeschichte aufzurunden wäre das einzig Unehrliche an dieser ganzen Übung gewesen.

## Was sich übertragen lässt

Nichts davon setzte tiefes Audiowissen voraus.
Es setzte voraus, eine Erfolgsmeldung nicht zu akzeptieren, und zu wissen, dass man aufzeichnen kann, was eine Maschine tatsächlich abspielt, und einfach die Zahlen ansieht.
Das ist ein allgemeiner Zug, und er funktioniert weit über Ton hinaus: Wenn etwas behauptet, es habe geklappt, und die Wirklichkeit widerspricht,
dann suche die Stelle, an der du das Ergebnis direkt beobachten kannst, statt den Bericht darüber zu lesen.

Die Lösung war ein Befehl.
Die drei Tage Stille waren der Preis dafür, nicht einmal gefragt zu haben, was der Rechner eigentlich ausgibt.
