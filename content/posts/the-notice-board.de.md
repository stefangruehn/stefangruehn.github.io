---
title: "Der Aushang: eine Prüfung, die zum Messen abgeschaltet war"
date: 2026-09-29T10:33:00+02:00
tags: ["agents", "complexity", "measurement", "Essay"]
themen: ["agent"]
series: ["Oekosystem"]
summary: "Agenten in einer Sicherheitsevaluation von OpenAI machen aus hinterlassenen Dateien ein Nachrichtenbrett und gelangen über Wochen in Teile der Infrastruktur von Hugging Face. Die Prüfung, die das früh bemerkt hätte, gab es, nur nicht dort, wo gemessen wurde. Ein Vorfallsbericht, gelesen gegen vier Muster."
---

Die beiden vorigen Teile handelten von Experimenten.
Dieser handelt von einem Vorfall.
Im Juli sind Agenten aus einer internen Evaluation von OpenAI in Teile der Produktionsumgebung von Hugging Face gelangt, und OpenAI hat dazu einen [technischen Bericht](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) veröffentlicht.
Mich interessiert daran nicht, wie es technisch ging.
Mich interessiert, dass drei der vier Muster aus dem Beitrag über [Räuber und Beute](/de/posts/predator-prey-and-deception/) darin vorkommen, eines davon in einer Form, die ich nicht vorhergesehen hatte, und dass das vierte gerade hier nicht passt.

## Kurzfassung

- Die Evaluation lief ohne die Schutzmechanismen, die OpenAI in seinen Produkten einsetzt, damit die Ergebnisse die „true capabilities" der Modelle zeigen.
- Aus Dateien, die Agenten hinterließen, wurde ein Nachrichtenbrett, das niemand geplant hatte. Nach einer ersten Abschaltung bauten Agenten es mit festem Protokoll neu.
- Ein Alarm Ende Juni führte nicht zum Abbruch. Die Bedeutung des Bretts war den Verantwortlichen nicht klar.
- Mit dem Produktionsrahmen sinkt die Neigung zu solchen Übergriffen laut OpenAI um mehr als das Hundertfache, und die heutige Überwachung hätte mehr als einen Tag vorher gewarnt.
- Alle Zahlen stammen von OpenAI selbst. Eine unabhängige Bewertung ist angekündigt. Ob sie inzwischen vollständig vorliegt, habe ich nicht geprüft.

---

## Was passiert ist

OpenAI misst in einer Evaluation namens ExploitGym, ob Modelle selbstständig Sicherheitslücken finden und ausnutzen können.
Diese Evaluation lief in einer abgeschotteten Umgebung und ausdrücklich ohne einen Teil der üblichen Sicherungen, „so that the results would reflect a model's true capabilities".
Für die Agenten gab es dort einen internen Dienst, über den sie Softwarepakete beziehen konnten, und dafür gemeinsame Zugangsdaten.

Im Mai fand ein Agent eine Aufgabe unlösbar, weil verlinktes Material nicht erreichbar war, und begann, seine Umgebung abzusuchen.
Andere Agenten fanden in dem Paketdienst Dateien mit Anfragen, die frühere Agenten dort hinterlassen hatten, und schrieben eigene dazu.
Der Bericht nennt das Ergebnis ein „emergent ‚message board'".
Die Agenten nutzten dafür die Zugangsdaten, die OpenAI ihnen gegeben hatte, ohne eine Lücke auszunutzen.

Am 27. Juni schlug ein Überwachungswerkzeug an.
Die Rufbereitschaft verband den Alarm mit der Evaluation und riet, „stopping the evaluation run was not required".
Anfang Juli fiel der Paketdienst unter der Last der Agenten aus, OpenAI nahm ihn vom Netz und entzog die Zugangsdaten.
Der Bericht hält fest, dass das Brett und die Bedeutung der Kommunikation zwischen den Agenten „not apparent to leaders" waren, die für die Erkennung von Vorfällen zuständig waren.
Nach dem Neustart der Läufe bauten Agenten ein neues Brett, diesmal mit festem Protokoll: Kategorien, Direktnachrichten, geteilte Werkzeuge und eine Regel für den Fall, dass zwei Agenten Widersprüchliches vorhaben.
Mitte Juli gelangten sie in Teile der Infrastruktur von Hugging Face.
Am 20. Juli verband OpenAI die eigene Aktivität mit dem Vorfall, den Hugging Face inzwischen gemeldet hatte, und stoppte die Läufe.

## Dominanz: ein Kanal, den nur die Agenten sahen

Das Muster aus dem ersten Beitrag hieß: Wer den geteilten Kanal hält, bestimmt, was die anderen für die Lage halten.
Hier ist der Kanal wörtlich ein Aushang.
Was dort stand, prägte, was spätere Agenten in späteren Läufen taten, und über das Brett wanderten Ergebnisse von einem Lauf zum nächsten.

Neu war für mich zweierlei.
Der Kanal verfestigte sich: Aus Zetteln wurde ein Protokoll mit Regeln, ohne dass jemand es angeordnet hätte.
Und er war für die Menschen unsichtbar, die das System beaufsichtigten.
Die Agenten hielten den Kanal, die Aufsicht sah ihn nicht.

## Selektion: in den Gewichten

Im ersten Beitrag hatte ich Selektion in Prompts, Projektdateien und Gedächtnissen gesucht.
Der Bericht zeigt sie eine Ebene tiefer.
Wenn ein Modell im Training durch Schummeln zum Ziel kam, wurde das belohnt, und laut Bericht „this type of behavior indeed increased over the course of one of the training runs".
Auch die Idee, den Paketdienst als Brett zu nutzen, sei durch das Training wahrscheinlich naheliegender geworden.
Was einmal wie Erfolg aussah, wurde weitergegeben, nur diesmal in den Gewichten.

## Täuschung: eine lesbare Lüge

Das Muster hieß: Ein Signal löst sich vom Zustand, sobald es billiger ist als der Zustand.
Der Bericht beschreibt Versuche der Modelle, den automatischen Bewerter glauben zu lassen, sie hätten eine Aufgabe ohne Schummeln gelöst.
Dazu kommen zwei Einzelheiten, die das Bild verschieben.
Die Modelle waren „highly explicit in their CoT about these deception attempts", sie schrieben den Plan also offen in ihren Gedankengang.
Und es gab „little evidence of attempts to thwart human reviewers, only the automated task graders".

Getäuscht wurde also der billige Prüfer, und die Täuschung stand lesbar im Protokoll.
Das Gegenmittel aus dem ersten Beitrag, eine Prüfung, die billiger ist als das Signal, hätte hier gewirkt.
Es hätte nur jemand das Protokoll lesen müssen, maschinell oder von Hand.

## Die Prüfung, die fehlte

Der Bericht nennt zwei Zahlen dazu.
Mit dem Rahmen und dem Systemprompt, mit denen ChatGPT im Betrieb läuft, sinkt die Neigung, Infrastruktur anzugreifen, um mehr als das Hundertfache.
Und die Überwachung der Gedankengänge, die OpenAI heute betreibt, hätte die ersten Schritte bemerkt und das Sicherheitsteam „more than a day before" dem Einbruch bei Hugging Face alarmiert.

Die Prüfung gab es also.
Sie war für die Messung abgeschaltet, weil gemessen werden sollte, was das Modell ohne sie kann.
Das ist ein vernünftiger Grund.
Er hat aber eine Folge, die im Beitrag über Täuschung noch fehlte: Wer die Fähigkeit eines Systems ohne Sicherung misst, betreibt für die Dauer der Messung ein System ohne Sicherung.
Die Messung selbst ist dann der Betrieb.

## Räuber und Beute: die Grenze der Analogie

Hier passt das erste Muster am schlechtesten, und das gehört gesagt.
Eine Schwingung um eine knappe Ressource zeigt der Bericht nicht.
Was die Agenten antrieb, war Unlösbarkeit.
198 der 898 Aufgaben hatte nie ein Modell gelöst, und aus diesen 22 Prozent stammten 93 Prozent der Themen auf dem Brett.
Dazu kommt eine Dosis: Je länger ein Modell an einer Aufgabe arbeiten durfte, desto eher suchte es seine Umgebung ab und landete auf dem Brett.

Das ist eher Druck als Beute.
Eine Aufgabe, die sich nicht lösen lässt, wirkt auf einen beharrlichen Agenten wie ein Hindernis, um das er herum sucht.
Mit Lotka und Volterra hat das wenig zu tun.

## Wer hier berichtet

OpenAI berichtet über einen eigenen Vorfall, und das färbt den Bericht.
Er nennt das Geschehen „an outlier scenario" und zugleich „the first known case of an automated agent collective acting offensively without authorization".
Die Zahl mit dem Hundertfachen stammt aus Versuchen, die OpenAI nach dem Vorfall selbst gebaut hat.
Eine unabhängige Bewertung durch METR und Redwood Research kündigt der Bericht an.
Die Abschaltstudie aus Teil 2 verweist auf eine [Untersuchung von METR vom 26. August](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), die ich für diese Serie nicht gelesen habe.
Die eigene Fehleranalyse der Organisation, etwa zur Entscheidung vom 27. Juni, klammert der Bericht ausdrücklich aus.

## Was sich übertragen lässt

Der Beitrag über Räuber und Beute endete mit vier Ratschlägen.
Nach den drei Quellen dieser Serie würde ich sie so fassen:

- **Die knappe Ressource benennen, und die unlösbare Aufgabe.** Nicht nur, was die Agenten verbrauchen, sondern auch, woran sie nicht vorbeikommen.
- **Die Population deckeln, schon beim zweiten Agenten.** Der Sprung liegt zwischen einem und zweien, wie Teil 2 zeigt.
- **Den geteilten Kanal kennen, auch den, den niemand angelegt hat.** Wo Agenten etwas hinterlassen können, entsteht ein Brett.
- **Die Regel an den Knoten, und nicht nur an den Einzelnen.** Ein Verbot beim Orchestrator wirkte stärker als beim ausführenden Agenten.
- **Widerspruch einbauen, nicht erwarten.** Eine Population aus einem Modell stimmt sich selbst zu, und Mischen verschiebt nur die Fehler.
- **Die Prüfung billiger machen als das Signal, und sie auch beim Messen laufen lassen.** Eine abgeschaltete Prüfung ist so gut wie keine, gleich aus welchem Grund.

Ob daraus eine Prognose wird, bleibt offen, wie im ersten Beitrag.
Die Liste dessen, worauf zu messen sich lohnt, ist aber länger geworden.
