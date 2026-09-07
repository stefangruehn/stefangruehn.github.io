---
title: "Der Schaltplan ist eine Hypothese: was Papier über eine Platine wirklich sagt"
date: 2026-09-06T14:00:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
themen: ["rechner"]
series: ["Werkzeugketten"]
summary: "Eine Platine ohne brauchbare Doku beantwortet keine Frage von selbst. Man steckt sich für jede Frage eine kurze Kette aus Standardwerkzeugen zusammen — und die erste Gruppe dieser Ketten endet auf Papier. Dreimal hat das Papier hier gelogen."
---

Der Schaltplan zu dieser Platine ist dreimal widerlegt worden.
Einmal beim Lautsprecher, einmal beim Vibrationsmotor, einmal bei der seriellen Verbindung zwischen den beiden Prozessoren.
Nicht in Nebensächlichkeiten, sondern jedes Mal genau in der Aussage, wegen der man ihn aufgeschlagen hatte.

## Kurzfassung

- Das Gerät ist ein Waveshare ESP32-S3 Knob Display: ein Drehknopf mit rundem Bildschirm, **zwei Mikrocontrollern** und einer Dokumentation, die aus einer Wiki-Seite und einem ZIP-Archiv besteht.
- Für jede Frage entsteht eine eigene **kurze Kette** aus vorhandenen Standardteilen, und jede endet in genau einer Tatsache.
  Das Neue daran ist nicht die Technik — jedes Glied ist alt.
  Neu ist, dass so eine Kette in Minuten entsteht statt in einem Nachmittag.
- Dieser Teil behandelt die drei Ketten, die auf **Papier** enden: Datenblatt, Schaltplan, fremder Quelltext.
- Das Datenblatt löste einen Befund, an dem vorher zwei Tage lang geraten worden war — in einem einzigen `grep`.
- Der Schaltplan lieferte die vollständige Pinbelegung und ein **Negativergebnis**, das eine ganze Verdachtsspur beendete.
- Der fremde Quelltext lieferte ebenfalls ein Negativ: die vermutete Fehlerquelle gibt es dort nicht.
  Ein Negativ ist ein Ergebnis, kein Fehlschlag.
- Die Regel am Ende: **Herstellerpapier ist eine Hypothese.** Es wird geglaubt, wo eine Messung ihm zustimmt, und sonst nicht.

---

## Dreimal widerlegt

Zuerst die drei Stellen, an denen das Papier falsch lag, weil sie den Ton für alles Weitere setzen.

**GPIO0 und der Lautsprecher.**
Auf der Platine sitzt ein Analogschalter, der den Digital-Analog-Wandler wahlweise dem einen oder dem anderen Mikrocontroller zuteilt.
Der Schaltplan nennt seinen Steuereingang `I2S_SWITCH_IN` und führt ihn auf GPIO0, und Waveshares eigener Beispielcode schreibt gleich in der ersten Zeile `gpio_set_level(GPIO_NUM_0, 1)` — angeblich, um den Wandler dem ESP32-S3 zu geben.
Gemessen wurde: kein Pegel auf GPIO0 ändert irgendetwas.
Auch keiner der übrigen freien Pins.
Der Lautsprecher gehört dem anderen Chip, und zwar über eine Stummschaltung, die auf einem Blatt steht, auf dem der S3 gar nicht vorkommt.

**`HAPTIC_EN` und der Vibrationsmotor.**
Der Schaltplan legt den Freigabeeingang des Motortreibers fest auf 3,3 Volt — er ist demnach immer eingeschaltet und braucht keinen Pin.
Gemessen wurde: solange GPIO38 nicht aktiv hochgezogen wird, meldet der Treiber `0xE9` in seinem Diagnoseregister, also Endstufe aus.
Sobald der Pin hoch ist, meldet er `0xE0`, und im Gehäuse ist ein Klicken zu spüren.
Runter, `0xE9`. Hoch, `0xE0`. Dreimal in einem einzigen Bootvorgang, in zwei aufeinanderfolgenden Läufen identisch.

**Die serielle Verbindung.**
Der Schaltplan beschriftet GPIO38 als `ESP32S3_TX` und GPIO48 als `ESP32S3_RX` — das wäre die Leitung, über die die beiden Prozessoren miteinander reden.
Beide Pins hängen in Wirklichkeit an nichts, was spricht.
Die Werksfirmware benutzt GPIO40 und GPIO39.

Drei Aussagen, drei Widerlegungen.
Was folgt daraus für den Rest des Papiers?
Nicht, dass es wertlos ist — von 23 vermessenen Pins stimmen 20 mit dem Plan überein.
Sondern dass jede einzelne Aussage darin so lange eine **Hypothese** bleibt, bis das Gerät ihr zustimmt.

## Kette 1: das Datenblatt

Der Bildschirm zeigte ein Bild, das nach ein bis zwei Sekunden verblasste.
Die Hintergrundbeleuchtung blieb an, die Pixeldaten waren nachweislich korrekt, und der Versuch, dem Anzeigetreiber ein Register auszulesen, lieferte nur Nullen.

Die Kette:

```
web search -> dl.espressif.com -> PDF (264 Seiten) -> Text -> grep/sed -> Registertabelle
```

Das Datenblatt zum Anzeigetreiber ST77916 ist öffentlich, es liegt nur nicht dort, wo man es sucht — nicht beim Hersteller des Chips, sondern bei Espressif, unter `dl.espressif.com/AE/esp-iot-solution/ST77916_SPEC_V1.0.pdf`.
Einmal heruntergeladen, ist der Rest gewöhnliche Textarbeit: PDF nach Text, dann suchen.

Vier Antworten fielen daraus, und drei davon hatten vorher tagelang als Vermutung im Raum gestanden.

**Der Chip ist nach jedem Reset ausgeschaltet.**
Auf Seite 171 steht, im Klartext, dass der Befehl `29h` — „Display On" — der einzige Weg aus dem Zustand *display off* ist, und dass Einschalten, Software-Reset und Hardware-Reset alle drei dort landen.
Die Initialisierungstabelle des Herstellertreibers sendet diesen Befehl nicht.
Sie endet beim Aufwecken aus dem Schlafmodus.

**Das Verblassen hat eine benannte Physik.**
Der Schlafmodus, Seite 161: „In diesem Modus wird der DC/DC-Wandler angehalten, der interne Oszillator angehalten und die Abtastung des Panels angehalten."
Ein Panel, dessen Abtastung steht, während die Beleuchtung weiterbrennt, hält seine Ladung noch etwa eine Sekunde und entspannt dann.
Es *verblasst*. Ein abgeschaltetes Display dagegen *springt* innerhalb eines Bildes auf Schwarz.
Der Unterschied zwischen Verblassen und Springen ist damit keine Beobachtungsnuance mehr, sondern ein Unterscheidungsmerkmal mit einer Seitenzahl.

**Das Lesen von Registern ist verriegelt.**
Seite 145, Befehl `F4h`: die Leseoperationen der Herstellerregister sind hinter einen Umschalter gelegt, den man vorher schreiben muss.
Ohne ihn kommt zurück, was zurückkam: nichts.
Zwei Seiten weiter steht außerdem, dass der Lesebefehl `0x0B` heißt und nicht `0x03` — `0x03` ist der Lesebefehl von Flash-Speicherbausteinen und auf diesem Chip überhaupt kein Befehl.
Alle Leseversuche vorher hatten die falsche Zahl gesendet.

**Und es gibt eine stille Fehlerquelle.**
Die interessanten Register — Ladepumpen, Gate-Spannungen, VCOM — liegen in einer zweiten Befehlsebene, die erst geöffnet werden muss.
Schreibt man sie mit geschlossener Ebene, werden die Schreibvorgänge **verworfen, ohne dass irgendetwas einen Fehler meldet**.
Die Initialisierung „gelingt", und der Chip läuft auf seinen Werkseinstellungen weiter.

Ein Nebenbefund, der Zeit kostete und deshalb hierher gehört: Waveshares Wiki-Seite antwortet einem Programm, das sie abholen will, mit **HTTP 403**.
Mit `curl -A "Mozilla/5.0"` kommt sie.
Das ist kein Erkenntnisgewinn über die Platine, aber es ist der Unterschied zwischen „die Quelle existiert nicht" und „die Quelle wollte einen Browser sehen".

## Kette 2: der Schaltplan als Bild

Die zweite Kette ist die einzige hier, in der nicht gesucht, sondern **hingesehen** wird.

```
curl -A "Mozilla/5.0" -> ZIP -> fünf PNG-Blätter -> hinsehen -> Netzliste
```

Ein Schaltplan als Rasterbild hat keinen Text, den man durchsuchen könnte.
Was ihn lesbar macht, ist etwas anderes: Ein Netz — eine elektrische Verbindung — trägt auf jedem Blatt denselben Namen, und die Arbeit besteht darin, diesen Namen von Blatt zu Blatt zu verfolgen und aufzuschreiben, wo er auftaucht.
Fünf Blätter, ein Name nach dem anderen, am Ende eine Tabelle.
Das ist stumpfe Arbeit und deshalb gut delegierbar, aber es ist keine Suche, sondern eine Abschrift.

Zwei Ergebnisse rechtfertigten sie.

Das erste ist die vollständige Pinbelegung: welcher Anschluss des Mikrocontrollers an welcher Leitung des Bildschirms hängt, wo die Berührungssensorik sitzt, wo der Drehgeber, wo die Speicherkarte.
Zwanzig Zeilen, die vorher aus Forenbeiträgen zusammengeraten waren.

Das zweite ist ein **Negativergebnis**, und es war das wertvollere.
Die Verdachtsspur lautete: Vielleicht hat das Panel eine eigene Versorgungsspannung, die über einen Schalttransistor freigegeben werden muss, und dieser Transistor bleibt aus.
Ein sehr ähnliches Board eines anderen Herstellers hat genau so einen Pin, aktiv-low, und ein Rail, das über Leckströme wegsackt, wäre eine ausgezeichnete Erklärung für ein Bild, das langsam verschwindet.

Auf Blatt 1 liegen die beiden Versorgungspins des Anzeigemoduls direkt auf 3,3 Volt.
Kein Schalter, kein Transistor, kein Freigabe-Netz.
Die Spur ist tot, und zwar in dreißig Sekunden statt in einem halben Tag Messen.

Auf demselben Weg fiel die Erklärung für den stummen Lautsprecher an, die weiter oben schon vorweggenommen wurde: Die Stummschaltung des Digital-Analog-Wandlers hängt an einem Anschluss des *anderen* Mikrocontrollers und an sonst nichts.
Sie steht auf einem Blatt, auf dem der ESP32-S3 nicht vorkommt — weshalb sie beim Suchen nach „S3" auch nie aufgetaucht wäre.

## Kette 3: fremder Quelltext statt Dokumentation

Die dritte Papier-Kette liest Quelltext, den jemand anders geschrieben hat, als wäre er die Dokumentation, die fehlt.

Die Frage war: Warum kommen Datenübertragungen an den Bildschirm oberhalb einer bestimmten Größe scheinbar nicht an, obwohl die Bibliothek `Ok` zurückmeldet?
Der Verdacht richtete sich auf die Hardware-Abstraktionsschicht `esp-hal` — und die liegt ohnehin schon auf der Platte, ausgepackt im Paketcache:

```
/home/stefan/.cargo/registry/src/index.crates.io-.../esp-hal-1.1.2/src/spi/master/
```

Kein Klonen, kein Suchen: der Quelltext der Version, die tatsächlich gebaut wurde, Zeile für Zeile.

Das Ergebnis war ein Negativ, und ein gründliches.
Die einzige Größenobergrenze im ganzen Pfad liegt bei 32 736 Bytes, also weit über allem, was hier gesendet wurde.
Die Aufteilung in Speicherbeschreibungen ändert sich bei 4 092 Bytes — auch das lag über der fraglichen Grenze und wurde später ohnehin experimentell überfahren.
Und die Prüfung, welche Werte sich überhaupt mit der Übertragungsgröße ändern, ergab: genau zwei, beide unkritisch.

Dazu kam die Gegenprobe im Änderungsprotokoll und in den Fehlerberichten des Projekts.
Ein gemeldeter Fehler passte auf den ersten Blick genau — bis man ihn zu Ende las: Er tritt bei 33 000 Bytes auf, nicht bei 3 600, und beschreibt exakt die 32-KB-Grenze, die schon aus dem Quelltext bekannt war.
Ein Bericht, der zur eigenen Beobachtung *fast* passt, ist der teuerste Fund einer solchen Suche, und die einzige Rettung ist, ihn bis zur Zahl zu lesen.

Die Ursache lag am Ende woanders, und das gehört zur Ehrlichkeit dieser Kette dazu: Die ursprüngliche Messung hatte mit *einer* Zahl gleichzeitig die Übertragungsgröße, den Speicherpuffer und ein Feld auf dem Stapelspeicher dimensioniert.
Sie konnte gar keine Aussage über eine einzelne Ursache tragen.
Als die drei getrennt wurden, kamen alle Größen durch — von 720 bis 21 600 Bytes.
Das Quelltextlesen hat nicht die Ursache gefunden.
Es hat eine falsche ausgeschlossen, bevor auf ihr aufgebaut wurde, und das in einer Stunde.

## Die Kreuzprobe

Am Ende dieses Teils steht die Regel, die aus den drei Ketten folgt und die für alles Weitere gilt.

Herstellerpapier — Datenblatt, Schaltplan, Beispielcode — ist eine gute **Hypothese** und keine Messung.
Es beschreibt, was jemand beim Entwurf vorhatte, und der Entwurf kann sich geändert haben, das Blatt kann eine Revision zu alt sein, der Beispielcode kann von einer Schwesterplatine stammen.
Nichts davon ist Böswilligkeit; es ist die normale Halbwertszeit von Dokumentation.

Praktisch heißt das zweierlei.

**Erstens**: Papier taugt hervorragend, um Kandidaten zu erzeugen und Suchräume zu verkleinern.
Die Pinbelegung aus dem Schaltplan hat die spätere Suche nach der Speicherkarte von „alle Pins" auf „diese sieben" verkürzt — und die Suche selbst hat dann das Gerät beantwortet.

**Zweitens**: Papier taugt nicht, um eine Frage zu schließen.
Bei den 23 vermessenen Pins stimmen 20 mit dem Plan überein — das ist eine gute Quote und es ist trotzdem keine Begründung, den einundzwanzigsten ungeprüft zu glauben.
Die drei Abweichungen sind nicht dort aufgetreten, wo man mit Abweichungen rechnet, sondern genau bei den drei Funktionen, die man wissen wollte.

Der nächste Teil geht eine Stufe weiter: weg vom Papier, hin zu dem, was tatsächlich auf dem Gerät liegt — den beiden Firmware-Abbildern, die vor dem ersten eigenen Schreibzugriff gesichert wurden.
Ein Abbild lügt nicht über seine Absicht.
Es enthält, was ausgeführt wird.
