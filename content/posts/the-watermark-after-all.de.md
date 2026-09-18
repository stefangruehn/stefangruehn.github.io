---
title: "Das Wasserzeichen, das es doch gibt"
date: 2026-09-18T11:55:00+02:00
tags: ["claude-code", "writing", "authorship", "Essay"]
themen: ["autor"]
series: ["Autorschaft"]
summary: "Am 6. September fragte ich Claude, ob seine Texte ein Wasserzeichen tragen. Die Antwort war nein, und sie war falsch: Anthropic hatte das Wasserzeichen drei Wochen vorher angekündigt. Richtig war die zweite Hälfte der Antwort. Ein geändertes Wort löst im Text nichts aus. Nachweisbar ist jetzt etwas, aber nicht das, was die Frage wollte, und nicht für mich."
---

Am 6. September habe ich Claude eine Frage gestellt, die mir beim Gegenlesen gekommen war:

> Enthalten die von dir erzeugten oder überarbeiteten Texte Wasserzeichen? Dann würde die Änderung nur eines Wortes automatisch Nebeneffekte an anderen Stellen des Textes erzeugen, und das ließe sich mit einem Diff nachweisen, oder?

Die Antwort begann so:

> **Wasserzeichen (Punkt 6): nein — und die Beweisidee trüge auch dann nicht.** Anthropic bettet in Claudes Textausgabe kein Wasserzeichen ein, weder ein statistisches Sampling-Wasserzeichen (so etwas gibt es real, aber bei Google für Gemini: SynthID-Text) noch unsichtbare Zeichen.

Die erste Hälfte dieser Antwort war falsch.
Die zweite war richtig.
Dieser Beitrag handelt von beiden.

## Kurzfassung

- Anthropic hat am 14. August 2026 angekündigt, dass Claudes Text ein Wasserzeichen trägt.
  Die Antwort vom 6. September kam drei Wochen später und bestritt es.
- Ein solches Wasserzeichen ist ein Muster in der Wortwahl.
  Es wird beim Schreiben gelegt und liegt danach still im Text.
- Deshalb löst ein geändertes Wort an anderer Stelle nichts aus.
  Die Idee, das per Diff nachzuweisen, trägt nicht, auch jetzt nicht.
- Prüfen können nur berechtigte Stellen, ich nicht.
  Und das Ergebnis sagt, dass Claude beteiligt war, nicht welcher Satz von wem ist.
- Die englischen Fassungen dieses Blogs übersetzt Claude.
  Wenn hier etwas markiert ist, dann eher sie als die deutschen.
- Ohne Schlüssel bleibt nur der Stil, und der ist ein Indiz, kein Beweis.

---

## Was am 6. September schon bekannt war

Am 14. August 2026 hat Anthropic erklärt, [wie Claudes Wasserzeichen funktioniert](https://www.anthropic.com/news/claude-text-watermark).
Der erste Satz lautet: „Future Claude models will generate text that contains a watermark.“
Anlass ist der AI Act der EU.
Anthropic hat im Juli 2026 einen Verhaltenskodex der EU unterschrieben, der Anbieter verpflichtet, KI-erzeugten Text zu markieren.
Ein [Hilfeartikel](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) führt die Modelle auf, für die das gilt.

Die Antwort, die ich bekam, stammte von Claude Opus 5.
Für dieses Modell nennt der Hilfeartikel die Markierung ausdrücklich.
Ob die Antwort selbst markiert war, kann ich nicht prüfen.

Warum die Antwort falsch war, lässt sich trotzdem sagen.
Sie kam aus dem, was das Modell beim Training gelernt hatte, und die Ankündigung war jünger.
Nachgesehen hat in dem Moment niemand, weder Claude noch ich.
Die falsche Hälfte klang genauso sicher wie die richtige.

## Wie das Zeichen in den Text kommt

Ein Sprachmodell schreibt Wort für Wort.
An jeder Stelle hat es eine Liste möglicher nächster Wörter, und oft passen mehrere gleich gut.
Ein Wasserzeichen nutzt genau diese Wahlmöglichkeiten.

Das Grundverfahren haben John Kirchenbauer und Kollegen [2023 beschrieben](https://arxiv.org/abs/2301.10226).
Vor jedem Wort wird aus den vorangehenden Wörtern und einem geheimen Schlüssel eine zufällige „grüne“ Hälfte des Wortschatzes bestimmt.
Das Modell bevorzugt dann leicht die grünen Wörter.
Wer den Schlüssel hat, zählt hinterher, wie viele Wörter eines Textes grün sind.
Bei einem Menschen ist es ungefähr die Hälfte, bei einem markierten Text deutlich mehr.
Ab einem festgelegten Abstand gilt der Text als markiert, und die Wahrscheinlichkeit, dabei einen menschlichen Text falsch einzuordnen, liegt im Beispiel des Papers bei drei zu hunderttausend.

Anthropic beschreibt dasselbe Prinzip.
Der Schlüssel und die paar Wörter davor entscheiden, welches Wort das Modell unter gleichwertigen wählt.
„Nothing is added to the text and there are no hidden characters.“
Google markiert auf diese Weise seit 2024 die Antworten von Gemini, mit einem Verfahren namens SynthID-Text, [beschrieben in Nature](https://www.nature.com/articles/s41586-024-08025-4).

## Warum ein geändertes Wort nichts auslöst

Meine Frage vom 6. September steckte in einem Bild: dass ein Wasserzeichen die Stellen eines Textes miteinander verknüpft wie eine Prüfsumme, sodass eine Änderung an einer Stelle an anderen Stellen etwas nach sich zieht.

So funktioniert es nicht.
Das Zeichen ist ein Muster in Wahlen, die beim Schreiben einmal getroffen wurden.
Danach rechnet der Text nicht mehr.
Wer ein Wort ändert, ändert die Zählung an dieser Stelle und bei den wenigen folgenden Wörtern, deren grüne Liste von ihm abhing.
Anderswo passiert nichts.
Um das Zeichen aus einem langen Text zu entfernen, muss man nach Kirchenbauer ungefähr ein Viertel der Wörter ändern.
Anthropic sagt es für den eigenen Fall ähnlich: Leichtes Bearbeiten entfernt es wahrscheinlich nicht, ein vollständiges Umschreiben schon.

Der Effekt, den ich im Diff gesehen hatte, war trotzdem echt.
Er hat nur eine andere Ursache.
Wer einen Satz überarbeitet, fasst die Nachbarsätze mit an, weil Rhythmus und Anschluss sonst nicht mehr passen.
Im Diff sieht diese Überarbeitung aus wie eine Fernwirkung.
Diese Hälfte der alten Antwort gilt weiter.

## Wer prüfen kann, und was dabei herauskommt

Anthropic gibt die Prüfung über eine Schnittstelle heraus, die im September 2026 in einer geschlossenen Vorschau läuft.
Zugang haben Stellen, die das EU-Recht vorsieht: Aufsichtsbehörden, Strafverfolgung, Medien, Faktenprüfer, Forschende, Bildungseinrichtungen und zivilgesellschaftliche Gruppen.
Ich gehöre nicht dazu.
Ich kann an meinen eigenen Texten nicht nachsehen, ob und wie stark sie markiert sind.

Und wer nachsehen kann, erfährt weniger, als meine Frage wollte.
Das Zeichen zeigt nach Anthropics eigener Beschreibung nur, dass Claude „at some point“ wahrscheinlich beteiligt war.
„It cannot distinguish ‚Claude wrote this‘ from ‚Claude heavily edited this.‘“
Bei kurzen Texten ist das Signal schwach, bei Tatsachen auch, weil es dort wenig gleichwertige Wortwahl gibt.

Im [zweiten Teil](/de/posts/retouched-by-my-hand/) dieser Serie ging es um die Stufen des Auktionskatalogs.
Das Wasserzeichen liefert eine davon: „Werkstatt“.
Welche Hand welche Fläche gemalt hat, liefert es nicht.

## Welche Fassung dieses Blogs markiert wäre

Auf den Einstiegsseiten steht, dass der Schreibstil der deutschen Seiten meiner ist und die englischen Fassungen daraus übersetzt sind.
Übersetzt werden sie von Claude.

Dazu schreibt Anthropic: „A translation produced by Claude carries a watermark, because in this case every word is chosen by Claude.“
Auch die deutschen Seiten entstehen mit Claude.
Aber was ich beim Gegenlesen umstelle und neu formuliere, schwächt ein Zeichen, wenn es eines gibt.
Die englische Fassung zieht Claude nach jeder Änderung nach, und jedes ihrer Wörter hat Claude gewählt.

Wenn in diesem Blog etwas markiert ist, dann also eher die Fassung, die meinem Stil nur so weit folgt, wie es das Englische zulässt.
Der Inhalt ist in beiden derselbe.
Ob die Modelle, mit denen hier gearbeitet wird, auf dem Weg, den ich benutze, tatsächlich markieren, lässt sich von außen nicht prüfen.
Das ist der Stand vom 18. September.

## Ohne Schlüssel bleibt der Stil

Wer den Schlüssel nicht hat, kann nur auf den Stil sehen.
Anthropic grenzt das in derselben Erklärung ab: Erkennungsdienste achten auf verräterische Wendungen, etwa die Figur „this isn't [X], it's [Y]“ oder das Wort „quietly“.
„Picking up on these patterns is fundamentally different from checking for a watermark.“

Das ist ein altes Verfahren.
Der Kunsthistoriker Giovanni Morelli hat im 19. Jahrhundert Gemälde an Nebensachen zugeschrieben, an der Form von Ohren und Fingernägeln, die ein Fälscher nicht beachtet.
Er selbst hat allerdings widersprochen, als man ihm nachsagte, er erkenne einen Maler allein am Ohr.
In der [englischen Ausgabe](https://archive.org/details/gri_33125000150405) heißt es, die Formen „aid us in distinguishing the works of a master from those of his imitators“.
Sie helfen, sie entscheiden nicht.

Für Text sind die Zahlen ernüchternd.
OpenAI hat seinen eigenen Erkenner für KI-Text im Juli 2023 [zurückgezogen](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/).
Er hatte 26 Prozent der KI-Texte erkannt und 9 Prozent der menschlichen Texte fälschlich als KI-Text eingestuft.
Eine [Studie in Patterns](https://doi.org/10.1016/j.patter.2023.100779) ließ sieben Erkenner auf Aufsätze aus der Englischprüfung TOEFL los, geschrieben von Menschen, die nicht mit Englisch aufgewachsen sind.
Im Mittel hielten sie 61,3 Prozent davon für maschinell.

## Was bleibt

Am 6. September bekam ich zwei Antworten in einem Absatz.
Die eine war falsch, die andere richtig, und beide klangen gleich.
Der [erste Teil](/de/posts/who-built-the-chain/) dieser Serie verlangt Prüfbarkeit, wenn der Stoff nicht von mir kommt.
Eine Aussage darüber, was ein Anbieter heute tut, gehört dazu, auch wenn sie von dessen eigenem Modell kommt.
Das Modell weiß nicht, was nach seinem Training angekündigt wurde, und sagt das nicht von selbst dazu.

Die Serie hat mit der Frage angefangen, wer hier schreibt.
Nachweisen lässt sich jetzt etwas, aber nicht für mich und nicht auf Satzebene.
Die Naht zwischen meiner Hand und der von Claude bleibt am Text unsichtbar.
Sichtbar wird sie nur dort, wo jemand sie angibt.

Dies ist der dritte und letzte Teil der Serie [Autorschaft](/de/series/autorschaft/).
