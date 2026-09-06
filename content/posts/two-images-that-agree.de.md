---
title: "Zwei Abbilder, die sich einig sind: Forensik an fremder Firmware"
date: 2026-09-06T14:05:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
themen: ["rechner"]
series: ["Jede Frage ihre eigene Kette"]
summary: "Ein Firmware-Abbild beschreibt nicht, was jemand vorhatte, sondern was ausgeführt wird. Drei Ketten enden in einem Abbild: eine liest die Werksfirmware, eine liest zwei gegeneinander, und eine liest dieselbe zweimal — und findet den Unterschied."
---

Teil eins hat drei Ketten beschrieben, die auf [Papier enden](/de/posts/the-schematic-is-a-hypothesis/), und den Schaltplan dabei dreimal widerlegt.
Papier beschreibt eine Absicht.
Ein Firmware-Abbild beschreibt, was ausgeführt wird — und auf dieser Platine lagen zwei davon, jedes vor dem ersten eigenen Schreibzugriff gesichert.

## Kurzfassung

- Die erste Frage dieses Teils: Warum zeigt die Werksfirmware auf demselben Glas ein stabiles Bild und die eigene nicht?
  Ein Abbild kann diese Frage beantworten, weil es die Antwort enthält.
- **Ankertechnik:** Log-Texte im Abbild sind die Fixpunkte.
  Die Adresse eines Textes steht in einer Konstantentabelle, und von dort führt eine einzelne Ladeanweisung zurück in die Funktion, die ihn ausgibt.
- Ergebnis: Die Werksfirmware benutzt **nicht** die Standard-Initialisierungstabelle des Herstellertreibers, sondern eine eigene mit 184 Einträgen — und die endet mit dem Befehl, der in der Standardtabelle fehlt.
- **Zwei Abbilder gegeneinander** ergaben das Protokoll zwischen den beiden Prozessoren vollständig: Baudrate, Pins, Rahmenformat, Befehlsvorrat.
  Beide Enden unabhängig gelesen, beide einig — und die Pins widersprechen dem Schaltplan.
- **Dieselbe Firmware zweimal gelesen** und verglichen: alles bytegleich außer 1 985 Bytes.
  Der Unterschied *ist* der Befund.
- Am Ende: Mitschreiben ist keine Ordnungsliebe, sondern ein Werkzeug.
  Von drei Recherchen, die am Nutzungslimit starben, blieb genau das erhalten, was zu dem Zeitpunkt in der Datei stand.

---

## Kette 4: Forensik an der Werksfirmware

Das Ausgangsproblem stand am Ende von Teil eins: Das gezeichnete Bild verblasst nach ein bis zwei Sekunden.
Das Datenblatt hatte die Physik dazu geliefert.
Offen blieb, was die Werksfirmware anders macht — denn sie zeigt auf demselben Panel ein Bild, das steht.

Die Kette:

```
espflash read-flash -B 921600 0 0x1000000 backup/factory-flash-esp32s3-....bin
  -> Abbildkopf bei 0x10000 lesen -> Segmente trennen
  -> xtensa-esp32s3-elf-objdump -b binary --adjust-vma=<Ladeadresse>
  -> Log-Texte als Anker
```

Der erste Schritt ist billig und unumkehrbar wichtig: **das Auslesen kommt vor dem ersten Schreiben.**
16 MB über die serielle Schnittstelle bei 921 600 Baud, ein paar Minuten.
Danach existiert der Auslieferungszustand als Datei, und alles Weitere ist Arbeit an einer Kopie.

Zwei Sätze zur Ordnung, weil an dieser Stelle die einzige Datei entsteht, die nicht weitergegeben wird.
Das Abbild ist fremde Firmware: Es bleibt auf der Platte, `backup/*.bin` steht in der `.gitignore`, und was in diesen Beiträgen steht, sind ausschließlich die Befunde daraus — keine Bytes.
Das Gerät gehört mir, Secure Boot und Flash-Verschlüsselung sind ab Werk aus; es wird hier nichts umgangen, was jemand als Schutz gemeint hätte.
Warum das die einzige Stelle der ganzen Serie ist, an der man wirklich etwas falsch machen kann, steht [in einem eigenen Beitrag](/de/posts/the-wrong-statute/).

Der zweite Schritt trennt das Abbild in seine Teile.
An Adresse `0x10000` beginnt ein Kopfbereich, der auflistet, welcher Abschnitt der Datei später an welche Adresse im Speicher geladen wird — sechs Segmente, jedes mit Dateioffset, Zieladresse und Länge.
Ohne diese Zuordnung ist ein Disassembler wertlos: Er kann Maschinenbefehle entziffern, aber jeder Sprung und jeder Verweis auf Daten zeigt an eine Adresse, die er nicht kennt.
Mit ihr — `--adjust-vma=<Ladeadresse>` sagt dem Disassembler, wo das Stück im Speicher liegt — stimmen alle Adressen wieder.

Der dritte Schritt ist der eigentliche Trick.
Kompilierter Code hat keine Funktionsnamen mehr, aber er hat **Log-Texte**, und die haben Adressen.
Auf dieser Prozessorarchitektur kann ein Befehl keine vollständige Adresse als Zahl enthalten; Konstanten liegen in einem kleinen Vorrat neben dem Code und werden mit einer eigenen Ladeanweisung geholt.
Sucht man also die Adresse des Textes `ESP_PanelBus_QSPI` in diesem Vorrat und dann die Ladeanweisungen, die diese Stelle lesen, landet man bei genau den Funktionen, die diesen Text ausgeben.
Aus einer Zeichenkette wird ein Einstiegspunkt.

Was so gefunden wurde:

**Die Werksfirmware benutzt eine eigene Initialisierungstabelle.**
Die Bibliothek, gegen die sie gebaut ist, bringt eine 216 Einträge lange Standardtabelle mit — und die wird nur in einem Zweig referenziert, der nicht läuft.
Stattdessen installiert die Anwendung eine eigene mit **184 Einträgen**, die an einer ganz anderen Stelle im Datenbereich liegt.
Deshalb hatte ein früherer Durchgang, der in der Nähe der Bibliotheksdaten gesucht hatte, immer nur die Standardtabelle gefunden.
Die beiden unterscheiden sich in fast jedem Analogregister — und die eigene endet mit `INVON`, `SLPOUT`, **`DISPON`**.
Genau der Befehl, der in der Standardtabelle fehlt und den das Datenblatt als einzigen Ausweg aus dem Aus-Zustand nennt.

**Die Buskonfiguration steht in den Konstruktorkonstanten.**
Aus dem disassemblierten Konstruktor ließ sich die gesamte Einrichtung des Datenbusses zurücklesen: maximale Übertragungsgröße `0x8000` = 32 768 Bytes, Taktmodus 0, 32 Bit Befehlsbreite, Vierleiterbetrieb, keine Fülltakte.
Und ein Detail, das ohne Disassembler nie aufgefallen wäre: Der Konstruktor setzt 40 MHz Takt, und drei Anweisungen später überschreibt die Anwendung ihn mit **80 MHz**, bevor der Bus überhaupt startet.

**Und ein Negativ, das eine ganze Hoffnung beendet.**
Die Frage, wie man dem Anzeigetreiber korrekt ein Register ausliest, sollte an der Werksfirmware abgeschaut werden.
Die Suche nach der Lesefunktion ergab: Sie hat genau zwei Aufrufer im gesamten Abbild, und beide gehören zum Berührungssensor.
**Die Werksfirmware liest den Bildschirm nie.**
Es gibt nichts abzuschauen.
Diese Antwort ist unbefriedigend und trotzdem viel wert — sie verhindert, dass weiter danach gesucht wird.

## Kette 5: zwei Abbilder gegeneinander

Die zweite Kette ist die interessanteste, weil sie ohne jedes Messgerät auskommt und trotzdem stärker ist als der Schaltplan.

Auf der Platine sitzen zwei Mikrocontroller, die über eine serielle Leitung miteinander reden.
Beide tragen ihre Werksfirmware, beide wurden ausgelesen, und beide Enden desselben Gesprächs wurden **unabhängig voneinander** disassembliert — dieselbe Ankertechnik, andere Prozessorarchitektur, andere Toolchain.

Was dabei herauskam, deckt sich in jedem Punkt:

| | ESP32-S3 | klassischer ESP32 |
|---|---|---|
| Quelldatei laut Log | `src/driver/uart1.cpp` | `../main/uart1.c` |
| Baudrate | **921 600** | **921 600** |
| Rahmen | 8 Datenbits, keine Parität, 1 Stoppbit | dasselbe |
| Flusskontrolle | keine | keine |
| Pins | **TX GPIO40, RX GPIO39** | **TX IO23, RX IO18** |
| Puffer für Titelbilder | 48 KiB | 48 KiB |

Zwei unabhängig gelesene Abbilder, die sich auf dieselbe Baudrate, dasselbe Rahmenformat und zueinander passende Pins einigen, sind ein stärkerer Beleg als ein Schaltplan — und sie widersprechen ihm.
Der Plan nennt GPIO38 und GPIO48 als serielle Leitung.
Die Firmware benutzt GPIO40 und GPIO39, also ausgerechnet die beiden Pins, die der Plan für den Audio-Takt vorgesehen hat.

Und dann fällt eine ältere Messung an ihren Platz.
Ein Abtasten aller freien Pins hatte GPIO39 als „von außen hochgehalten" gemeldet und niemand wusste, wovon.
Eine serielle Empfangsleitung, deren Gegenüber gerade schweigt, sieht genau so aus: Der andere Chip hält seine Sendeleitung im Ruhezustand hoch, dauerhaft, seit dem Einschalten.
Der Befund lag längst vor, er war nur falsch herum gelesen worden.

Auch das Protokoll selbst ließ sich vollständig zurücklesen, aus den Verteilertabellen beider Seiten:

```
 0   Kennung 0xA3  S3 -> ESP32          0xBD  ESP32 -> S3
 1   Befehl  u8
 2   Länge   u16, little endian
 4   Daten   Länge Bytes
```

Titelbilder werden in nummerierten Paketen übertragen, **und der Empfänger fordert jedes einzelne an** — der Sender läuft nie voraus.
Beide Seiten berechnen dieselbe Schrittweite von 1 016 Bytes je Paket, an zwei Stellen in zwei verschiedenen Abbildern, und beide begrenzen die Nutzlast auf denselben Wert.

Das alles war zu diesem Zeitpunkt noch nicht gemessen, sondern gelesen, und die Notiz sagte das auch so.
Einen Tag später hörte ein Empfänger auf GPIO39 mit: **921 600 Baud, 8N1, null Rahmenfehler, null verlorene Bytes**, Kennung `0xBD` wie gelesen.
Und der Befehl `0x06` entpuppte sich als Metadatenrahmen mit vier Textlängen im Kopf:

```
len 50:  11 0E 0F 00  "Artificial Being\0" "Alien Project\0" "Aztechno Dream\0"
len 39:  06 0E 0F 00  "Skunk\0"            "Alien Project\0" "Aztechno Dream\0"
```

`0x11` ist 17, also die Länge von „Artificial Being" plus die abschließende Null.
Die Summe der vier Längen plus vier Kopfbytes ergibt in allen beobachteten Rahmen exakt die angegebene Gesamtlänge.
Zwei Abbilder hatten das Protokoll vorhergesagt, ein Empfänger hat es bestätigt.

## Kette 6: dieselbe Firmware zweimal lesen

Die dritte Kette ist die kürzeste und die, auf die man am wenigsten kommt.

```
espflash read-flash ... lauf1.bin
espflash read-flash ... lauf2.bin
sha256sum lauf1.bin lauf2.bin
cmp -l lauf1.bin lauf2.bin | wc -l
```

Zweimal dasselbe lesen und vergleichen beantwortet zunächst eine Frage über das Werkzeug: Ist die Sicherung überhaupt vertrauenswürdig?
Ein serieller Auslesevorgang über mehrere Minuten bei hoher Baudrate ist kein selbstverständlich fehlerfreier Vorgang, und alles Weitere baut darauf auf.

Die Antwort war: bytegleich — **außer an 1 985 Stellen**, alle innerhalb eines einzigen Bereichs, dem Bereich für nichtflüchtige Einstellungen.

Und hier kippt der Test von einer Werkzeugprüfung in einen Befund.
Der Unterschied ist keine Übertragungsstörung, sondern eine Aussage über das Gerät: **Der Chip schreibt beim Booten sein eigenes Gedächtnis.**
Er tut das jedes Mal, wenn das Auslesewerkzeug ihn zurücksetzt, und in 16 Läufen sind es immer dieselben knapp zwei Kilobyte.
Der Firmwarebereich dagegen ist bitstabil.

Damit weiß man dreierlei aus einem Befehl: dass das Auslesen zuverlässig ist, welcher Teil des Speichers als konstant behandelt werden darf, und dass ein Vergleich zweier Sicherungen künftig genau diesen einen Bereich ignorieren muss.
Ein Unterschied, der reproduzierbar an derselben Stelle auftritt, ist kein Rauschen.
Er ist die Antwort auf eine Frage, die man nicht gestellt hatte.

## Mitschreiben ist ein Werkzeug

Am Ende dieses Teils eine Kette, die über allen anderen liegt.

Jede der Recherchen oben hat ihre Befunde **während der Arbeit** in eine Datei geschrieben, nicht danach.
Die Dateien in `scratch-findings/` fangen als Gerüst an — die offenen Fragen als nummerierte Überschriften, darunter jeweils `(to fill)` — und daneben steht ein Quellenlog: `S1`, `S2`, `S3`, jede Quelle mit Adresse, Zitat und dem Vermerk, ob sie etwas belegt oder widerlegt.
Ganz unten ein Abschnitt mit der Überschrift „Dead ends (do not search again)".

Der Grund dafür ist nicht Ordnungsliebe, sondern eine Erfahrung mit einem Datum.
Am 4. September starben drei parallel laufende Recherchen am Nutzungslimit, mitten im Satz.
Erhalten blieb exakt das, was zu diesem Zeitpunkt in ihren Dateien stand — und das war genug, um weiterzuarbeiten.
Verloren war nicht Information, sondern **Verdichtung**: die Zusammenfassung, die es nie gegeben hat.

Daraus folgt eine Regel, die für Recherche allgemein gilt und nicht nur für Hardware: Wer Befunde für den Abschlussbericht aufspart, riskiert alles auf das Ende.
Wer sie fortlaufend hinschreibt, riskiert nur die Zusammenfassung — und die ist der billigste Teil.

Die Sammlung der toten Spuren ist dabei das unterschätzte Stück.
„Der Schaltplan hat keinen Freigabepin für das Panel", „der gemeldete Fehler betrifft 33 000 Bytes und nicht 3 600", „die Werksfirmware liest den Bildschirm nie" — drei Sätze, die keine Frage beantworten und trotzdem jeder eine Stunde sparen, sobald jemand die Spur zum zweiten Mal aufnimmt.

Der letzte Teil verlässt die Abbilder.
Papier sagt, was gedacht war; ein Abbild sagt, was ausgeführt wird.
Was auf der Platine wirklich verlötet ist, sagt keins von beiden — dazu muss man das Gerät fragen.
