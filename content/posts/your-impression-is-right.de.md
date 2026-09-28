---
title: "Dein Eindruck stimmt: Wie ich mit einem Agenten rede"
date: 2026-09-28T10:45:00+02:00
draft: false
tags: ["claude-code", "language", "workflow", "Essay"]
themen: ["agent"]
summary: "Zweimal habe ich einen Agenten gebeten, die Schatten in meiner App zu prüfen. Beim ersten Mal bekam ich eine Bestätigung, eine Zahl und eine Erklärung, und die Erklärung war falsch. Beim zweiten Mal bekam ich eine Messung. Das Modell war dasselbe, der Satz ein anderer."
---

## Kurzfassung

- Ich hatte den Eindruck, dass die Karten in einem Menü meiner App stärkere Schatten werfen als die übrigen, und bat den Agenten, das zu prüfen.
- Die Antwort begann mit „Dein Eindruck stimmt“, lieferte eine Erklärung und eine Zahl. Gemessen hatte er im Emulator, gesehen hatte ich es auf dem Telefon.
- Knapp fünf Stunden später stellte ich dieselbe Aufgabe noch einmal, diesmal mit Gerät, Umfang, kritischer Stelle, Methode und einer Regel für den Befund. Das Ergebnis war eine Messung, und die Erklärung vom Morgen fiel dabei um.
- Was keine der beiden Anweisungen gefragt hatte, sah ich danach selbst: Zwei lange Seiten scrollten plötzlich zäh.
- Gelernt habe ich daraus weniger über Schatten als über meine Sätze. Ich versuche inzwischen vorher zu sehen, wo ein Missverständnis entstehen kann.

---

## Ein Eindruck

Die App, an der ich mit Claude Code arbeite, zeigt fast alles auf Karten: Listen, Einstellungen, Hilfeseiten.
Manche Menüs öffnen sich als Blatt, das von unten ins Bild fährt, ein sogenanntes Bottom Sheet.
Dort fielen mir die Schatten auf.

Ich schrieb:

> Prüfe visuell die Schatten der Karten auf den Bottom Sheets. Ich habe den Eindruck, dass diese stärker sind als die anderer Karten.

Die Antwort kam eine knappe halbe Stunde später und begann so:

> Dein Eindruck stimmt. Der Schatten selbst ist gleich stark, er dunkelt auf der Seite wie im Sheet um etwa 20 % ab. Im hellen Modus war das Sheet aber weiß wie die Karten […] Deshalb wirkte er schwerer.

Dazu kam eine Änderung, nach der „der Kantenverlauf dort jetzt derselbe wie auf der Seite“ war.
Das las sich gründlich: eine Bestätigung, eine Zahl, eine Ursache, ein Fix.

Gemessen hatte der Agent dabei im Emulator, einem simulierten Telefon auf dem Rechner.
Meinen Eindruck hatte ich auf dem echten Telefon in der Hand.
Für Prüfungen, die ohne meine Hand auskommen, hatte ich den Emulator sogar selbst festgelegt.
Wir hatten beide hingesehen, nur auf verschiedene Geräte.

Im Rückblick steckt in meinem Satz mehr Spielraum, als ich damals sah.
„Visuell“ sagt nicht, auf welchem Gerät.
„Ich habe den Eindruck“ lädt zur Bestätigung ein, und eine Bestätigung braucht nur eine plausible Erklärung.
Nach einer Messung hatte ich nicht gefragt.

## Derselbe Wunsch, noch einmal

Knapp fünf Stunden später schrieb ich:

> Vergleiche auf dem Telefon die Schattenwürfe aller Karten der Listen, Optionen, Settings, Seiten und der Bottom Sheets (und dort, wo ich es in dieser Aufzählung vergessen haben sollte). Schau dabei besonders den unteren Rand der untersten Karten an. Miss visuell, statt zu behaupten. Falls du Unterschiede feststellst, verwende den Schattenwurf der untersten Karte einer Liste für alle Karten.

Das ist dieselbe Bitte.
Nur steht jetzt darin, auf welchem Gerät, wo überall und mit welcher Lücke, welche Stelle die kritische ist, wie geprüft wird und was mit einem Befund geschieht, bevor es ihn gibt.
Der mittlere Satz ist ein Imperativ im grammatischen Sinn: Er lässt keine Antwort zu, die ohne Messung auskommt.

Der Agent machte Bildschirmfotos auf dem Telefon und las die Helligkeit Pixel für Pixel vom Kartenrand nach außen ab.
Ergebnis: Im Bottom Sheet war der Schatten doppelt so dunkel wie auf den Seiten.
Die Ursache lag darin, dass das Sheet technisch ein eigenes Fenster ist, für das Android Schatten nach anderen Regeln zeichnet.
Mein Eindruck vom Morgen war also richtig, die Erklärung dazu falsch, und die „20 %“ stimmten nur für die Seite.
Die Regel aus meinem letzten Satz entschied den Fix gleich mit: Alle Karten bekamen den Schatten der untersten Listenkarte.

## Was keine Messung gefragt hatte

Danach nahm ich das Telefon wieder in die Hand und schrieb:

> Terms und Changelog scrollen bei allen Karten ausgeklappt nun sehr träge und ruckeln dabei, so als wenn etwas unnötigerweise ständig neu gezeichnet wird. Alle anderen Seiten mit langen Inhalten scheinen mir so schnell wie vorher zu scrollen, prüfe dies aber trotzdem selbst.

Bildschirmfotos zeigen Standbilder.
Wie sich Scrollen anfühlt, sieht man auf keinem davon, und danach hatte meine Anweisung auch nicht gefragt.
Der Agent maß daraufhin, wie lange das Telefon beim Wischen für jedes Einzelbild brauchte: auf den beiden Seiten rund 350 Millisekunden statt eines Bruchteils davon.
Der neue Schatten wurde für jede Karte als Grafik in ihrer ganzen Größe berechnet, und diese Grafik wanderte bei jedem Einzelbild neu zur Grafikeinheit.
Meine Vermutung stimmte bis in die Formulierung.
Nach einem zweiten Umbau waren die Seiten so schnell wie vorher, die Schatten blieben gleich.

Der Nachsatz „prüfe dies aber trotzdem selbst“ hat sich dabei gelohnt.
Ich gab den Befund und den Verdacht, ließ die Gegenprobe aber offen.
Sie ergab, dass ein kleiner Rest an Langsamkeit auf diesen Seiten schon vorher da war und vom Text kommt, nicht vom Schatten.

## Was ich dabei gelernt habe

Das Modell war an beiden Tageszeiten dasselbe.
Geändert hat sich mein Satz.

Zwei Dinge nehme ich mit.
Das erste ist Sprachdisziplin: Ort, Maßstab und eine Entscheidungsregel gehören in die Anweisung, bevor es ein Ergebnis gibt, und ein Wort wie „Eindruck“ gehört dazu, wenn ich eine Bestätigung will, und nicht, wenn ich einen Befund will.
Das zweite wiegt schwerer: vorher zu sehen, wo ein Missverständnis entstehen kann.
Emulator oder echtes Telefon, Standbild oder Scrollen, das waren beide Male Unterschiede, die mir klar waren und dem Agenten nicht, weil ich sie nicht ausgesprochen hatte.

Inzwischen lese ich jeden Satz, bevor ich ihn abschicke, so, wie ein Agent ihn lesen würde.
Ein Mensch neben mir hätte gewusst, dass ich das Telefon in der Hand halte.
Der Agent weiß nur, was dasteht, und was fehlt, ergänzt er mit dem, was er gerade zur Hand hat.

Vor gut einer Woche habe ich [über diese Veränderung meiner Sprache geschrieben](/de/posts/language-follows-suit/), damals eher als Beobachtung.
Der Schattentag hat daraus eine Arbeitsweise gemacht.

## Und deine Sätze?

Wenn du mit einem Agenten arbeitest, lohnt sich ein Blick zurück auf deine eigenen Anweisungen.
Welche Wörter in deinen Sätzen lassen Spielraum, den du selbst nicht bemerkst, weil du die Antwort schon kennst?
Hat sich die Art, wie du Aufgaben formulierst, in den letzten Monaten verändert, und in welche Richtung?
Und schreibst du inzwischen auch an Menschen anders?
