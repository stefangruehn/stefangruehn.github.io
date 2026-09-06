---
title: "Jede Frage ihre eigene Kette"
badge: "Technical Deep Dive"
summary: "Dreizehn kurze Werkzeugketten an einer Platine ohne brauchbare Dokumentation. Jede aus vorhandenen Standardteilen zusammengesteckt, jede endet in genau einer Tatsache — und der Unterschied zwischen ihnen ist nicht die Technik, sondern wer am Ende antwortet."
---

{{< serienbadge >}}

Drei Beiträge über dieselbe Platine: einen Drehknopf mit rundem Bildschirm, zwei Mikrocontrollern und einer Dokumentation, die aus einer Wiki-Seite und einem ZIP-Archiv besteht.

Sie gehören zusammen, weil sie einen Katalog aufteilen.
Dreizehn Ketten sind an diesem Gerät wirklich gelaufen, und sie sortieren sich danach, **wer am Ende antwortet**:
der erste Teil fragt Papier, der zweite Firmware-Abbilder, der dritte das Gerät selbst.

{{< kettenschema >}}

## Ob das etwas für dich ist

Der Weg von links nach rechts ist die Geschichte: eine Frage, eine Kette aus Werkzeugen, die ohnehin da sind, eine Tatsache, eine Datei.

**Der Pfeil zurück** ist der Grund, hier zu lesen.
Keine dieser Ketten ist neu — ein Datenblatt lesen, Firmware disassemblieren, eine Pinbelegung durchprobieren, das ist alles Jahrzehnte alt.
Neu ist der Preis: Eine Kette entsteht in Minuten, also lohnt sich eine eigene je Frage, statt einen festen Messplatz zu bauen und danach zu überlegen, was er beantworten kann.

> Wer gern zusieht, wie ein Herstellerdokument an einer Messung zerbricht, ist hier richtig.
> Der erste Teil beginnt mit einem Schaltplan, der dreimal widerlegt wurde — und jedes Mal genau in der Aussage, wegen der man ihn aufgeschlagen hatte.

**Die drei Kästen unten** sind die Gliederung, nicht eine Rangfolge.
Papier sagt, was jemand vorhatte; ein Abbild sagt, was ausgeführt wird; das Gerät sagt, was ist.
Alle drei werden gebraucht, und das Verwechseln ist teuer.

Vorausgesetzt wird kein ESP32-Wissen.
Register, Literal-Pool, nichtflüchtiger Speicher und der erste Befehl einer Speicherkarte werden im Nebensatz erklärt, und wer nie gelötet hat, kommt mit.
Befehlszeilen stehen darin, mit den echten Zahlen — aber als Beleg, nicht als Anleitung.
