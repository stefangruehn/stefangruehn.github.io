---
title: "Der falsche Paragraf: die Angst sitzt am anderen Ende der Kette"
date: 2026-09-06T14:20:00+02:00
draft: true
tags: ["claude-code", "hardware", "recht", "schreiben", "meta", "Essay"]
themen: ["autor"]
summary: "Beim Schreiben über Hardware-Forensik kam die Frage, ob man sich damit strafbar macht. Die Antwort war überraschend: Der gefürchtete Paragraf greift aus drei Gründen nicht — und die einzige Handlung, bei der man wirklich etwas falsch machen kann, fühlt sich vollkommen harmlos an."
---

Als hier eine dreiteilige Serie über [Forensik an einer undokumentierten Platine](/de/series/jede-frage-ihre-eigene-kette/) entstand, kam mitten im Bauen die Frage: Machen wir uns strafbar, wenn wir das veröffentlichen?

Die Frage ist berechtigt und die Antwort war für mich überraschend.
Nicht, weil sie beruhigend ausfiel — sondern weil sie an einer ganz anderen Stelle beruhigend ausfiel, als ich vermutet hatte.

> **Das hier ist keine Rechtsberatung.**
> Ich bin kein Jurist. Was folgt, ist die Prüfung, die ich für meinen eigenen Fall angestellt habe, mit den Fundstellen, an denen ich sie festgemacht habe.
> Wer dieselbe Frage für sich beantworten muss, sollte jemanden fragen, der dafür haftet.

## Kurzfassung

- Der „Hackerparagraf" § 202c StGB erfasst **keine Texte**, sondern Passwörter und Computerprogramme.
  Eine Verfahrensbeschreibung fällt nicht darunter.
- Ihm fehlt hier außerdem die Vortat: Es ist meine eigene Platine, Secure Boot und Flash-Verschlüsselung sind ab Werk aus.
  Es gibt keine Sicherung, die überwunden werden könnte.
- Die einzige Handlung mit echtem Risiko ist die, die sich am harmlosesten anfühlt: **die 16-MB-Datei weitergeben**, die beim Sichern entsteht.
- Auslesen und Disassemblieren sind nicht bloß geduldet, sie sind im Urheberrecht **ausdrücklich privilegiert** — für Interoperabilität und für Fehlerbehebung.
- Protokollaufbau und Registerwerte sind Fakten und damit publizierbar; fremde Schaltplanbilder sind es nicht.
- Der eigentliche Gedanke: **Die Intuition folgt dem Vokabular, nicht der Rechtslage.**
  „Disassemblieren" klingt nach Einbruch, „Backup" klingt nach Ordnung — und genau andersherum liegt das Risiko.

---

## Der gefürchtete Paragraf trifft nicht zu

§ 202c StGB heißt im Volksmund Hackerparagraf und hat einen schlechten Ruf, den er sich verdient hat: Bei seiner Einführung 2007 war ernsthaft unklar, ob er Sicherheitsforschung im Nebenberuf kriminalisiert.

Nur trifft er auf einen Beitrag über die eigene Platine aus drei Gründen nicht zu, und jeder einzelne trägt allein.

**Erstens erfasst er keine Texte.**
Strafbar ist das Herstellen und Verbreiten von *Passwörtern und Sicherungscodes* oder von *Computerprogrammen, deren Zweck die Begehung einer Tat* nach § 202a oder § 202b ist.
Ein Aufsatz, der ein Verfahren beschreibt, ist beides nicht.
Wissen ist kein Werkzeug im Sinne der Norm — das Bundesverfassungsgericht hat sie 2009 in diese Richtung eng ausgelegt und Werkzeuge mit doppeltem Verwendungszweck im Grundsatz herausgenommen.

**Zweitens fehlt die Tat, die vorbereitet würde.**
§ 202c ist ein Vorbereitungsdelikt; ohne mögliche Haupttat läuft er leer.
§ 202a verlangt Daten, die *nicht für den Täter bestimmt* und *gegen unberechtigten Zugang besonders gesichert* sind.
Beide Merkmale fehlen hier, und zwar nicht knapp: Die Platine gehört mir, und ihr Flash-Speicher ist unverschlüsselt, weil der Hersteller Secure Boot nie eingeschaltet hat.
Es gibt nichts zu überwinden.
§ 202b, das Abfangen von Daten, scheitert an derselben Stelle — mitgehört wurde ein Gespräch zwischen zwei Chips, die beide mir gehören.

**Drittens fehlt der Vorsatz**, eine solche Tat vorzubereiten.

Dasselbe gilt für die Nachbarparagrafen.
Datenveränderung und Computersabotage (§ 303a, § 303b) setzen fremde Daten voraus.
Und § 108b UrhG, das Umgehen technischer Schutzmaßnahmen, bräuchte eine *wirksame technische Maßnahme* — die es nachweislich nicht gibt.

Bemerkenswert daran ist, wie wenig davon eine Auslegungsfrage ist.
Ich hatte mit Abwägung gerechnet und fand Tatbestandsmerkmale, die schlicht nicht vorliegen.

## Wo die Grenze wirklich verläuft

Sie verläuft im Urheberrecht, und sie verläuft an genau einer Stelle.

Der erste Schritt jeder Firmware-Forensik ist, das Auslieferungsabbild zu sichern, bevor irgendetwas geschrieben wird.
Bei diesem Board sind das 16 Megabyte für den einen Mikrocontroller und 4 für den anderen.
Diese beiden Dateien sind fremde Software.
Sie tragen keine Lizenz, sie sind nicht zur Weitergabe bestimmt, und daran ändert sich nichts dadurch, dass ich das Gerät gekauft habe.

Die Sicherung selbst ist erlaubt — § 69d Abs. 2 UrhG gibt dem berechtigten Nutzer das Recht auf eine Sicherungskopie, und dieses Recht kann vertraglich nicht ausgeschlossen werden.
Was nicht erlaubt ist, ist die Weitergabe.

Das ist die ganze Grenze.
Sie ist scharf, sie ist leicht einzuhalten, und im Repository zu diesem Projekt besteht sie aus einer Zeile:

```
# Flash-Abbilder der Werksfirmware — 16 MB Binaries, nichts für Git.
backup/*.bin
```

Der Kommentar darüber ist wichtiger als die Zeile selbst.
Eine `.gitignore`-Regel ohne Begründung überlebt keine Aufräumaktion.

## Drei Dinge, die erlaubt sind und sich verboten anfühlen

**Disassemblieren.**
Das Urheberrecht privilegiert es ausdrücklich.
§ 69d Abs. 3 erlaubt, ein Programm zu beobachten, zu untersuchen und zu testen, um die zugrunde liegenden Ideen zu ermitteln.
§ 69e erlaubt die Dekompilierung, wenn sie nötig ist, um **Interoperabilität** herzustellen — genau der Fall, wenn man herausfinden will, wie der eine Chip mit dem anderen spricht.
Und der Europäische Gerichtshof hat 2021 entschieden, dass ein rechtmäßiger Erwerber auch dekompilieren darf, um **Fehler zu beheben**.
Beide Zwecke lagen bei mir vor: mit dem zweiten Mikrocontroller reden, und ein Bild reparieren, das nach zwei Sekunden verblasste.

**Ein Protokoll rekonstruieren und veröffentlichen.**
Der Europäische Gerichtshof hat 2012 im Fall *SAS Institute* festgehalten, dass die Funktionalität eines Programms, seine Programmiersprache und seine Dateiformate **nicht** urheberrechtlich geschützt sind.
Geschützt ist der Ausdruck, nicht die Idee.
Ein Rahmenformat mit vier Bytes Kopf, eine Baudrate, die Nummerierung von Paketen: Das sind Fakten über eine Schnittstelle, und Fakten gehören niemandem.

**Rohe Gewalt über einen Suchraum.**
In Teil drei der Serie probiert ein Programm 840 Pinbelegungen durch, bis eine Speicherkarte antwortet.
Das klingt nach Angriff und ist keiner: Es fragt ein Gerät, das mir gehört, nach seiner eigenen Verdrahtung.
Ein Passwort wird dabei nicht geraten, ein Zugang nicht überwunden.

## Das Papier, das man nicht nachdruckt

Zwei Quellen aus Teil eins verdienen eine genauere Betrachtung, weil sie unterschiedlich zu behandeln sind.

**Der Schaltplan** liegt frei auf der Herstellerseite — aber *frei zugänglich* heißt nicht *frei verwendbar*.
Es steht keine Lizenz dabei, und ohne Lizenz gilt: alle Rechte vorbehalten.
Ein Schaltplan ist als Darstellung technischer Art geschützt.
Geschützt ist allerdings die **Darstellung**, nicht ihr Inhalt.
Dass an GPIO13 der Takt des Bildschirms hängt, ist eine Tatsache über ein Stück Kupfer und lässt sich in einer eigenen Tabelle wiedergeben.
Das Blatt selbst nachzudrucken wäre etwas anderes — und deshalb enthält die Serie kein einziges Bild.

**Das Datenblatt** wird zitiert, und das ist zulässig.
§ 51 UrhG erlaubt das Zitat, wenn es als Beleg für eine eigene Aussage dient, im Umfang durch den Zweck gerechtfertigt ist und die Quelle genannt wird.
Genau das leisten die Sätze in Teil eins: ein Satz aus dem Datenblatt, dazu die Seitenzahl und die Fundstelle, als Beleg für eine These über das Verblassen des Bildes.
Die Quellenangabe ist dabei keine Höflichkeit.
Sie ist die Bedingung, unter der das Zitat überhaupt erlaubt ist.

## Warum die Angst am falschen Ende sitzt

Und hier ist der Punkt, wegen dem ich das aufschreibe.

Alles, was sich bei dieser Arbeit gefährlich anfühlt, ist erlaubt.
Das Einzige, was verboten ist, fühlt sich nach Ordnung an.

Ich glaube, das liegt am Vokabular.
Die Tätigkeiten heißen *auslesen*, *disassemblieren*, *sniffen*, *brute force* — Wörter, die aus dem Umfeld von Einbruch und Angriff stammen und die man laut ausspricht, weil sie nach Können klingen.
Die riskante Handlung dagegen heißt *Backup*, *Anhang*, *ins Repo legen*.
Sie ist unsichtbar, sie dauert eine Sekunde, und sie hat kein Vokabular, das eine Warnlampe anschaltet.

Die Intuition folgt den Wörtern statt der Sache.

Das ist nicht auf Hardware beschränkt.
Beim Datenschutz ist es dasselbe Muster: Man ist unsicher, ob man die Daten *auswerten* darf, und exportiert währenddessen bedenkenlos eine CSV-Datei auf den Desktop.
Die Analyse ist sichtbar und wird geprüft, die Kopie ist beiläufig und wird es nicht.

Daraus folgt eine praktische Konsequenz, und sie ist der eigentliche Ertrag dieser ganzen Prüfung: **Die rechtliche Frage gehört nicht ans Ende.**
Wer sie sich vor dem Veröffentlichen stellt — „darf ich das schreiben?" —, stellt sie an der Stelle, an der ohnehin nichts passiert.
Sie gehört an die Stelle, an der die Datei entsteht.
Deshalb steht die Regel in diesem Projekt in der `.gitignore` und nicht in einer Checkliste, die niemand liest.

Ein Nachtrag dazu, der zeigt, dass die Prüfung sich nicht auf Recht beschränken sollte: In Teil drei stand die vollständige MAC-Adresse meines Boards.
Rechtlich völlig unbedenklich — mein Gerät, meine Kennung.
Sie steht jetzt trotzdem maskiert da, weil ein dauerhafter Gerätekennzeichner in einem öffentlichen Text nichts belegt, was er nicht auch mit drei `xx` belegen würde.
Nicht alles, was erlaubt ist, will man auch getan haben.

## Was ich nicht weiß

Die Ehrlichkeit gehört dazu, gerade bei diesem Thema.

Ich habe das nicht anwaltlich prüfen lassen.
Die Fundstellen sind nachgeschlagen und passen auf meinen Fall, aber ich habe keine Ausbildung darin, zu erkennen, welche Frage ich nicht gestellt habe.

§ 69e hat engere Voraussetzungen, als ich sie oben referiere: Die Dekompilierung muss unerlässlich sein, die Informationen dürfen nicht anders zugänglich sein, und das Ergebnis darf nicht für ein im Wesentlichen ähnliches Programm verwendet werden.
Für meinen Fall ist das unstrittig erfüllt.
Für den allgemeinen Satz „Reverse Engineering ist erlaubt" ist es das nicht.

Und der unangenehmste Punkt bleibt der Hersteller-Download ohne Lizenzangabe.
Bei den Schaltplanbildern ist die Konsequenz klar.
Bei den Demo-Quelltexten, aus denen die Serie einzelne Konstanten nennt, ist die Grenze zwischen Tatsache und Codeauszug fließend, und ich habe sie nach Gefühl gezogen.
