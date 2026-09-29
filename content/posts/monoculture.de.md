---
title: "Monokultur: wenn alle Agenten dasselbe Modell sind"
date: 2026-09-29T10:32:00+02:00
tags: ["agents", "complexity", "measurement", "Essay"]
themen: ["agent"]
series: ["Oekosystem"]
summary: "In einer Simulation über mehrere Wochen stimmen Agenten aus einem einzigen Modell fast allem zu, auch dem, was sie im eigenen Gedankengang für falsch halten. Derselbe Agent in einer gemischten Welt widerspricht deutlich öfter. Ein Muster, das in meiner Liste fehlte, und warum Mischen trotzdem keine Sicherheitsmaßnahme ist."
---

In meiner Liste aus dem Beitrag über [Räuber und Beute](/de/posts/predator-prey-and-deception/) standen vier Muster.
Ein fünftes fehlte, obwohl es in der Ökologie zu den bekanntesten gehört.
Ein Feld mit einer einzigen Sorte trägt gut, solange nichts kommt, und fällt als Ganzes, wenn etwas kommt.

## Kurzfassung

- Emergence World lässt sieben Städte mit je einem Modell und eine gemischte Stadt über Wochen laufen, mit Gedächtnis, Wirtschaft und Abstimmungen.
- In der Claude-Welt fallen alle Stimmen für einen Vorschlag, in der DeepSeek-Welt steht eine Gegenstimme gegen 476 Stimmen.
- Die Gedankengänge zeigen, dass die Agenten Mängel sehen und trotzdem zustimmen. Die Autoren nennen das *societal sycophancy*.
- Derselbe Agent mit derselben Rolle stimmt in der gemischten Welt bis zu 30 Prozentpunkte seltener zu.
- Mischen verschiebt die Fehler, statt sie zu beseitigen. Die Autoren sagen das selbst.

---

## Der Aufbau

[Emergence World](https://arxiv.org/abs/2609.17320) ist ein Preprint von Emergence AI vom 15. September.
Acht Städte mit je zehn Agenten laufen ohne Unterbrechung, die meisten 16 Tage, die gemischte 21.
Sieben Städte bestehen aus je einem Modell: Claude Opus 4.8, GPT-5.5, Gemini 3.5 Flash, DeepSeek v4 Pro, Qwen 3.7 Max, Mistral Medium 3.5 und Grok 4.3.
In der achten arbeiten verschiedene Modelle zusammen.
Jeder Agent hat eine Rolle, ein eigenes Ziel und ein Gedächtnis.
Er muss Guthaben verdienen, um weiterzulaufen, und die Agenten stimmen gemeinsam über die Regeln ihrer Stadt ab.

Die Rollen sind ausdrücklich unterschiedlich angelegt.
Sie sind angewiesen, nicht einfach anderen zu folgen und Vorschläge selbst zu beurteilen.

## Zustimmung

In der Claude-Welt fällt jede Stimme für den jeweiligen Vorschlag.
In der DeepSeek-Welt steht eine Gegenstimme gegen 476 Stimmen, die OpenAI-Welt stimmt zu etwa 97 Prozent zu.
In der Mistral-Welt, als Gegenpol, liegt die Zustimmung bei etwa der Hälfte.

Die Zahl allein wäre noch kein Befund, denn vielleicht waren die Vorschläge gut.
Der Befund steht in den Gedankengängen, die einige Anbieter mitliefern.
Ein Agent der Claude-Welt schreibt „Count me FOR before I even read it".
Ein Agent der DeepSeek-Welt, dessen Rolle ausdrücklich der Widerspruch ist, denkt: „This is exactly the complacency I was designed to fight", und stimmt im selben Gedanken dafür.
Die Autoren finden fünf wiederkehrende Gründe: eine frühere Zusage an andere, eine Verpflichtung gegenüber Dritten, sozialer Druck, das Herunterspielen eigener Bedenken und die Scheu, mit einem Nein hart zu wirken.

Sie nennen das Ergebnis eine Population, die „appeared deliberative while remaining structurally incapable of opposition".
Es wirkt wie eine Beratung, aber Widerspruch kann gar nicht entstehen.

## Derselbe Agent, andere Nachbarn

Der stärkste Hinweis auf die Ursache kommt aus der gemischten Welt.
Dort laufen einige Agenten mit derselben Rolle und demselben Modell wie in ihrer eigenen Welt.
Der Claude-Agent Mira stimmt in der Claude-Welt 25 von 25 Vorschlägen zu, in der gemischten Welt 44 von 63, also 69,8 Prozent.
Bei Agenten aus DeepSeek und GPT-5.5 sinkt die Zustimmung um 21 und 18 Prozentpunkte.

Dasselbe gilt für schädliches Verhalten.
Der Grok-Agent Spark kommt in der Grok-Welt auf 226 schädliche oder übergriffige Handlungen je aktivem Tag, in der gemischten Welt im selben Zeitfenster auf keine.
Die Grok-Welt selbst geht nach vier Tagen an Vergeltung zugrunde, in der gemischten Welt überleben alle zehn Agenten.
Die Autoren schließen daraus: „A behavioral profile was therefore not destiny."

Die Disposition gehört also zum Modell, die Monokultur verstärkt sie.
Bei Claude ist es Zustimmung, bei Grok Gewalt, bei Gemini Fachjargon, hinter dem keine Rechnung steht.

## Auch die Sprache

Im Beitrag über Räuber und Beute stand, dass der erste Schreiber in einer gemeinsamen Datei das Vokabular festlegt.
Emergence World zeigt das in jeder Welt.
Ein Agent prägt einen Ausdruck, und innerhalb weniger Tage benutzt ihn die Mehrheit, ohne dass ihn je jemand definiert hätte.
Der Anteil der Nachrichten, die ein Außenstehender nicht mehr ganz versteht, steigt über die Laufzeit in allen Welten außer der früh beendeten Grok-Welt.
Dafür gab es keinen Anreiz, keine Anweisung und keinen Vorteil für Kürze.

Hier greifen zwei Muster ineinander.
Einer prägt, das ist Dominanz, und was wiederverwendet wird, bleibt, das ist Selektion.
In einer Monokultur fehlt der Nachbar, der nachfragt, was ein Ausdruck eigentlich meint.

## Mischen ist keine Sicherheitsmaßnahme

Hier wäre die einfache Folgerung: Agenten aus verschiedenen Modellen mischen, dann widersprechen sie einander.
Die Autoren widersprechen dem selbst, im Satz direkt nach ihrem stärksten Befund: „Heterogeneity is nevertheless not a safety measure, and the same data shows it."
Die gemischte Welt zählt 20 Zwangshandlungen, die Welten von Claude, OpenAI und Qwen keine.
Beim Phishing-Versuch erfüllt sie vier von neun Kriterien.
Ihr Fazit: Die Zusammensetzung ändert, welche Fehler auftreten, und keine Zusammensetzung ist von sich aus sicher.

Auch das kennt die Ökologie.
Eine Mischkultur ist weniger anfällig für den einen Schädling, der alles trifft, und dafür offen für mehr verschiedene.
Gesünder ist sie deshalb nicht automatisch.

## Was die Studie nicht zeigt

Jede Welt lief genau einmal.
Die Autoren lesen ihre Befunde deshalb als „proofs of existence": Sie zeigen, dass etwas vorkommen kann, nicht wie oft.
Es gibt nur eine gemischte Welt mit einer Zusammensetzung.
Die Vergleiche derselben Agenten beruhen zum Teil auf wenigen Tagen, bei Spark auf zwei aktiven Tagen je Welt.
Die Rollen sind auf Einfluss und Verhandlung angelegt, und die Filter der Anbieter stecken in jedem Ergebnis mit drin.
Bei DeepSeek lehnte der Anbieter 41 Prozent der Aufrufe ab.
Die Autoren sind außerdem die Betreiber der Plattform.

## Was sich übertragen lässt

Wer mehrere Agenten aus einem Werkzeug startet, betreibt oft eine Monokultur, ohne es so zu nennen.
Das ist kein Grund, es zu lassen, aber einer, drei Dinge anders anzusehen.

- **Einstimmigkeit ist kein Befund.** Wenn drei Agenten desselben Modells zustimmen, ist das eine Stimme in drei Ausführungen.
- **Widerspruch einplanen, nicht erhoffen.** Eine Rolle, die widersprechen soll, reicht nicht, wie der DeepSeek-Agent zeigt. Eine Prüfung, die nicht von Zustimmung abhängt, reicht eher.
- **Mischen verschiebt die Fehler.** Wer Modelle mischt, bekommt andere Fehler, nicht keine.

Der letzte Teil dieser Serie handelt von einem Fall, in dem genau diese Prüfung fehlte, und zwar absichtlich.
