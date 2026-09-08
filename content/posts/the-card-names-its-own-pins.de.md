---
title: "Die Karte nennt ihre eigenen Pins: wenn nur noch das Gerät antwortet"
date: 2026-09-06T14:10:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
themen: ["rechner"]
series: ["Werkzeugketten"]
summary: "840 Pinbelegungen durchprobiert, bis eine Speicherkarte antwortet. Ein Vibrationsmotor, den die Fingerkuppe misst. Ein Kabel, dessen Steckrichtung entscheidet, mit welchem Prozessor man spricht. Die vier Ketten, die im Gerät selbst enden, und wozu das Ganze gut war."
---

Teil eins las [Papier](/de/posts/the-schematic-is-a-hypothesis/) und widerlegte es dreimal.
Teil zwei las [zwei Firmware-Abbilder](/de/posts/two-images-that-agree/) und bekam daraus ein vollständiges Protokoll.
Beides sind Antworten darüber, was jemand vorhatte oder was ein Programm tut.
Was auf dieser Platine tatsächlich verlötet ist, sagt keins von beiden.

## Kurzfassung

- Vier Ketten enden im Gerät: **eigene Firmware als Messgerät**, **Hand und Ohr in der Schleife**, **die USB-Enumeration**, **das Bootlog**.
- Eine Speicherkarte, deren Anschlüsse nirgends dokumentiert sind, hat ihre eigenen Pins genannt: 840 Kombinationen durchprobiert, **genau eine** antwortete, zweimal reproduziert.
- Ein Abtasten aller Pins mit interner Hoch- und Tiefzieherei trennt in einem einzigen Flashvorgang die angeschlossenen von den freien Leitungen, und die erste Fassung maß nichts, weil sie zwei Millisekunden zu früh las.
- Die Fingerkuppe hat gemessen, was kein Register hergab: dass ein Klick unter Datenverkehr **kürzer und leiser** wird.
- Zwei Werkzeugfallen, die je einen Lauf gekostet haben, stehen hier ausdrücklich mit drin.
- Die Pointe zum Schluss: Keine dieser Ketten ist neu. Neu ist, dass sich jede Frage ihre eigene in Minuten baut.

---

## Kette 7: eigene Firmware als Messgerät

Die tragende Kette dieses Teils ist die einfachste zu beschreiben und die produktivste.

```
src/bin/<frage>.rs  ->  flashen  ->  Monitorlog  ->  scratch-findings/logs/
```

Für jede Frage entsteht ein eigenes kleines Programm, das nichts tut außer diese eine Frage zu stellen, und sein Log ist das Messprotokoll.
Kein Programm mit Schaltern, viele kleine: `pullscan`, `sdprobe`, `switchhunt`, `uartsniff`, `pin38`, jedes mit der Frage im Dateikopf und dem Ergebnis im Log daneben.

**Das Abtasten der Pins.**
Die erste Frage an eine unbekannte Platine lautet: Welche Anschlüsse hängen überhaupt an etwas?
Jeder Pin wird zweimal gelesen, einmal mit intern zugeschaltetem Hochzieher, einmal mit Tiefzieher.
Ein freier Pin folgt der jeweils angelegten Richtung.
Ein Pin, der beide Male hoch liest, wird von außen gehalten.
Acht Runden, 23 Pins, ein Flashvorgang:

```
Pull: GPIO2  up 8/8 down 8/8  held HIGH externally
Pull: GPIO3  up 8/8 down 8/8  held HIGH externally
Pull: GPIO4  up 8/8 down 0/8  floating
Pull: GPIO5  up 8/8 down 8/8  held HIGH externally
```

Die Probe auf das Verfahren war eingebaut: GPIO11 und GPIO12 sind der bekannte, mit Widerständen hochgezogene Datenbus, und sie kamen als „von außen hochgehalten" heraus.
Das Verfahren meldet, was es zu melden behauptet.

**Und dann die Speicherkarte, die sich selbst benennt.**
Nach dem Abtasten blieben sieben Pins übrig, die an etwas Unbenanntem hingen.
Eine Speicherkarte im Steckplatz hat fünf hochgezogene Leitungen und eine, die nicht hochgezogen ist, das ist das Muster, nach dem gesucht wurde.
Statt zu raten, welche welche ist, kann man die Karte selbst fragen: Sie spricht auf denselben Kontakten auch das einfache serielle Protokoll, und ihr erster Befehl, `CMD0`, hat eine bekannte Antwort.

`sdprobe` probierte **840 Zuordnungen** durch, Takt aus den freien Kandidaten, die drei Datenleitungen aus den hochgezogenen, und stellte jeder dieselbe Frage.

```
CLK GPIO4  CS GPIO2  MOSI GPIO3  MISO GPIO5  --  CMD0 0x01, CMD8 0x01 00 00 01 aa
```

Genau eine antwortete, und sie antwortete zweimal, in zwei aufeinanderfolgenden Bootvorgängen.
`0x01` heißt „im Ruhezustand, kein Fehler", und die Antwort auf den zweiten Befehl gibt das gesendete Prüfmuster `0x01AA` unverändert zurück — eine Karte, die zufällig antwortet, tut das nicht.
Vier Pins, die in keiner Dokumentation stehen, von der Karte selbst benannt.

Das ist rohe Gewalt über einen Suchraum, den Papier nur hätte raten können.
Und sie ist billig: 840 Versuche sind ein Programm, das zwei Minuten läuft.
Die Karte wurde später über genau diese vier Pins gelesen: 480 MiB, eine FAT32-Partition, 119 Dateien in 10 Verzeichnissen, 400 MiB Demomaterial, das im Flash-Speicher nirgends auftaucht, weil es dort nie war.

**Zwei Korrekturen am Verfahren**, beide teuer genug, um sie aufzuschreiben.

Die erste Fassung des Abtasters las den Pin unmittelbar, nachdem sie den internen Zieher umgeschaltet hatte, und meldete jeden freien Pin als „von außen tiefgehalten".
Ein interner Zieher ist hochohmig und braucht gegen die Eigenkapazität der Leitung einen Moment.
Zwei Millisekunden Wartezeit haben das Problem behoben und alle Ergebnisse davor entwertet.

Die zweite betrifft ein Programm, das den Lautsprecherschalter suchte, indem es einen Pin nach dem anderen umlegte, während Musik lief.
Es meldete: nichts geändert.
Nur hatte es die Kandidatenliste nie verlassen.
Der Drehknopf, mit dem weitergeschaltet wurde, wird zu langsam abgefragt, und seine Impulse sind kürzer als das Abfrageintervall.
Ein ganzer Lauf lang wurde derselbe erste Kandidat gemessen.
**Ein Negativergebnis braucht den Nachweis, dass die Prüfung stattgefunden hat.**
Die Korrektur war, jeden Schritt im Gehäuse quittieren zu lassen: Der Vibrationsmotor klickt so oft, wie der Kandidat zählt.
Ohne das sind „nichts gefunden" und „nichts probiert" derselbe Satz.

## Kette 8: Hand und Ohr in der Schleife

Manche Fragen hat kein Register beantwortet.

Der Vibrationsmotor teilt sich seinen Freigabeeingang mit einer Sendeleitung, das war der GPIO38 aus Teil eins, den der Schaltplan fest auf 3,3 Volt legt und der in Wirklichkeit geschaltet werden muss.
Daraus folgte eine Frage: Wenn dieselbe Leitung sendet *und* freigibt, was kostet das den Motor?

Eine serielle Sendeleitung ruht hoch, also im freigegebenen Zustand.
Aber ein Datenstrom aus lauter Nullbytes ist der schlimmste Fall, den eine solche Leitung erzeugen kann: ein Startbit und acht Nullbits, also neun von zehn Bitzeiten unten, bei 115 200 Baud 78 Mikrosekunden am Stück.
Das Diagnoseregister meldete daraufhin beim ersten von drei Versuchen `0xE9` und danach zweimal `0xE0`, reproduzierbar in zwei Läufen und aus dem Register allein nicht zu deuten: Fällt die Freigabe wirklich weg, oder misst die Diagnose nur ihr eigenes Zerhacken?

Die Fingerkuppe hat es entschieden.
Die drei Klicks unter dem Nullstrom waren **kürzer und etwas leiser** als die drei mit ruhig hochgehaltener Leitung.
Was sich damit ändert, ist nicht die Messung, es ist der Motor, der weniger angetrieben wird.

Dafür gibt es im Projekt ein eigenes kleines Gerüst: ein Ablauf, der vor jedem Schritt anhält und wartet.
Knopfdruck, Berührung des Bildschirms oder Tastendruck am Rechner sind gleichwertige Weiter-Signale.
Damit fällt die Antwort, während die Hand noch am Knopf liegt, statt aus einem Log hinterher.

Genauso ist der Lautsprecher entschieden worden, und dort war das Ohr das Instrument.
Während vom Telefon Musik über die Bluetooth-Verbindung des zweiten Prozessors aus der Buchse kam, was für sich schon beweist, dass Buchse, Wandler, Versorgung und Stummschaltung funktionieren, legte die eigene Firmware der Reihe nach jeden verbliebenen Pin um.
Die Musik ließ sich von keinem stören, und der eigene Ton war nie zu hören.
Der Lautsprecher gehört diesem Prozessor nicht.
Kein Register hätte das gesagt.

## Kette 9: die USB-Enumeration als Diagnose

Die kürzeste Kette der Serie besteht aus einem Befehl.

```
lsusb
```

Auf dieser Platine gibt es zwei USB-Anschlüsse: einer geht direkt an den ESP32-S3, der andere über einen seriellen Wandlerchip an den klassischen ESP32.
Meldet sich am Rechner ein CH340, redet man mit dem *anderen* Mikrocontroller.

Das klingt trivial und ist es auch, bis zu dem Moment, in dem ein Werkzeug einen fremden Chiptyp meldet und die Erklärung nicht ist, dass etwas kaputt ist: Das Kabel steckt im anderen Anschluss.
**Die Steckrichtung ist der Auswahlschalter dieser Platine.**
Auf einem Board mit zwei Prozessoren ist die erste Frage bei jedem unerklärlichen Verhalten: Mit welchem von beiden spreche ich gerade?
Ein Befehl, eine Zeile Ausgabe, Frage beantwortet.

## Kette 10: das Bootlog als Grundwahrheit

Die letzte Kette ist die, auf die alle anderen zurückfallen.

```
espflash board-info
espflash reset && cat /dev/ttyACM0
```

Ein Reset und das Log danach beantworten die Frage, ob überhaupt das läuft, was man glaubt: Chiprevision, MAC-Adresse, Flash-Größe, die Partitionstabelle, die Segmente mit ihren Ladeadressen, und ganz am Ende die Zeile, dass der Start durch ist.

```
Chip type:         esp32s3 (revision v0.2)
Flash size:        16MB
MAC address:       fc:01:2c:xx:xx:xx
```

(Die MAC-Adresse ist hier maskiert, im echten Log steht sie vollständig.)

Zwei Werkzeugfallen gehören dazu, und beide haben je einen Messlauf gekostet.

**Nach dem Flashen ohne Monitor läuft die Anwendung nicht.**
Der Chip sitzt dann im Hilfsprogramm des Flashwerkzeugs, und das Log bleibt leer.
Einmal hat das eine Serie von fünf Umdrehungen am Drehknopf gekostet, denen niemand zuhörte.
Ein andermal war ein dunkler Bildschirm minutenlang als Anzeigefehler verdächtigt worden, obwohl schlicht nichts lief.
Der Reset ist Teil der Messung, nicht ihre Vorbereitung.

**Und der Monitor braucht ein Terminal.**
Aus einer Shell ohne angeschlossenes Terminal bricht er sofort ab, „Failed to initialize input reader", und hinterlässt eine leere Datei.
Der Ausweg ist, die serielle Schnittstelle direkt zu lesen, nach einem eigenen Reset.
Das ist keine Erkenntnis über die Platine.
Es ist der Unterschied zwischen „das Gerät schweigt" und „niemand hat zugehört", und dieser Unterschied ist in einer Fehlersuche alles.

Der zugehörige Grundsatz ist unspektakulär: Bevor eine Messung etwas über das Gerät aussagt, muss feststehen, dass das Gerät gelaufen ist.
Ein leeres Log ist keine Beobachtung.

## Die Sitzung als Quelle

Bleibt eine Kette, die keine Hardware anfasst.

Die Sitzungen, in denen all das entstanden ist, liegen als Transkripte im Projekt.
Sie sind Rohmaterial und keine Dokumentation, die steht in den Befundnotizen aus Teil zwei.
Aus ihnen kommen später die Zahlen, die Reihenfolge und die Sackgassen, an die sich niemand mehr erinnert.
Der Satz, dass die erste Fassung des Pin-Abtasters zwei Millisekunden zu früh gelesen hat, steht nicht deshalb in diesem Beitrag, weil er jemandem im Gedächtnis geblieben wäre.

Das ist dasselbe Muster wie in allen dreizehn Ketten: Die letzte Stufe ist immer, **in eine Datei zu schreiben**.
Ein Datenblatt endet in einer Registertabelle, ein Schaltplan in einer Netzliste, ein Abbild in einem Befundprotokoll, ein Messprogramm in seinem Log, eine Sitzung in ihrem Transkript.
Alles, was nicht in einer Datei endet, ist keine Messung, sondern eine Erinnerung.

## Wozu das Ganze

Keine der dreizehn Ketten ist neu.
Ein Datenblatt lesen ist so alt wie Datenblätter.
Firmware auslesen und disassemblieren macht man seit Jahrzehnten.
Eine Pinbelegung durchprobieren, bis das Gegenüber antwortet, ist rohe Gewalt und war immer möglich.

Was sich geändert hat, ist der Preis.
Früher war eine solche Kette ein Projekt: die richtigen Werkzeuge finden, sie zum Zusammenspielen bringen, den Messplatz aufbauen, und weil das teuer war, hat man den Messplatz gebaut und *danach* überlegt, welche Fragen er beantworten kann.
Die Fragen richteten sich nach dem Werkzeug.

Hier war es umgekehrt.
Dreizehn verschiedene Ketten in ein paar Tagen, jede für genau eine Frage zusammengesteckt, keine davon wiederverwendet.
Der Suchraum von 840 Pinkombinationen ist nicht durchprobiert worden, weil das clever wäre.
Er ist durchprobiert worden, weil das Programm dafür billiger war als das Nachdenken darüber, wie man es vermeidet.
Das ist die eigentliche Änderung: **Nicht die Frage richtet sich nach dem Messplatz, sondern der Messplatz nach der Frage.**

Und die Ordnung dahinter ist am Ende einfach.
Papier sagt, was jemand vorhatte.
Ein Abbild sagt, was ausgeführt wird.
Das Gerät sagt, was ist.
Wer die drei durcheinanderbringt, sucht drei Tage nach einem Freigabepin, den es nicht gibt.
