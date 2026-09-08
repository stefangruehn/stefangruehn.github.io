---
title: "Lokal grün, im Web kaputt: Die Baustufe, die niemand sieht"
date: 2026-09-08T05:00:00+02:00
draft: false
tags: ["claude-code", "hugo", "CI", "debugging", "deployment", "Technical Deep Dive"]
themen: ["veroeffentlichen"]
summary: "Die Übersichtsseite einer frisch veröffentlichten Serie war im Web zerlegt, lokal sah alles gut aus, und die Quelle war fehlerfrei. Schuld war ein einzelnes Anführungszeichen an einer Stelle, die niemand ansieht, und eine Baustufe, die nur im CI läuft."
---

Am 5. September, ein paar Stunden nach der Veröffentlichung der Serie [Codebuch](/de/series/codebuch/), sah ich mir die deutsche Übersichtsseite im Browser an.
Sie war kaputt.

## Kurzfassung

- Zwei Symptome: zwischen fettem und normalem Text fehlten Leerzeichen, und weiter unten legte sich Text übereinander.
  Beides sieht nach CSS aus.
  Es war kein CSS.
- Die Quelle war fehlerfrei.
  Im Markdown standen alle Leerzeichen, und lokal im Browser sah die Seite gut aus.
- Zwischen meiner Ansicht und der veröffentlichten Seite liegt eine Stufe, die es nur auf einer Seite gibt: Das CI baut mit `hugo --minify`, mein Rechner baut ohne — seit dem ersten Commit.
- Gefunden habe ich es nicht durch Lesen, es war ein Vergleich: zweimal bauen, den Text jeder Seite gegen den Text derselben Seite stellen.
- Die Ursache war **ein einzelnes Anführungszeichen** in der Beschreibung einer Grafik, an einer Stelle, die niemand ansieht, weil sie für Screenreader gedacht ist.
- Ab dieser Stelle verlor der Minifier die Spur: Leerzeichen an Inline-Tags fielen weg, schließende Tags ebenfalls.
  Ein nie geschlossener Anker, der über einer ganzen Beitragskachel liegt, nahm alles Folgende in sich auf, das war der überlagernde Text.
- Die englische Fassung derselben Grafik blieb heil.
  Nicht, weil sie besser war.
  Sie benutzte zwei gerade Anführungszeichen: gerade Anzahl, kein Bruch.
- **Nichts daran ist blogtypisch.** Es braucht dafür weder Hugo noch Markdown noch eine agentische KI, die einen Blog baut.
  Es genügt eine Pipeline, in der ein Schritt nur im CI läuft, dort heißt er dann Bundler, Kompression oder Image-Build.
- Der Fix ist nicht das Anführungszeichen.
  Der Fix ist, die Asymmetrie abzuschaffen: Die CI-Stufe läuft jetzt auch auf meinem Rechner, vor jedem Deploy.

---

## Zwei Symptome

Das erste fiel im Fließtext auf.
Wo ein fett gesetztes Satzende in normalen Text überging, klebten die Wörter aneinander: `…rechts unten` und `sind der Grund` ohne Leerzeichen dazwischen.
Nicht überall, aber oft genug, um es nicht für einen Tippfehler zu halten.

Das zweite war gröber.
Weiter unten auf der Seite lagen Textblöcke übereinander, halb verdeckt, in einer Weise, die kein Browserfenster erklärt.

Beide Symptome haben dieselbe Handschrift: Sie sehen aus wie Layout.
Fehlende Abstände und überlagerte Blöcke, das ist die Sorte Schaden, die man bei CSS sucht.
Genau dort habe ich zuerst gesucht.

## Die plausible Erklärung, die nicht stimmt

Es war kein CSS.
Kein Theme-Update, keine geänderte Regel, keine Schriftart, die nicht geladen hätte.

Und dann kommt der Teil, an dem die Fehlersuche normalerweise stehenbleibt: Die Quelle ist fehlerfrei.
Im Markdown steht jedes Leerzeichen da, wo es hingehört.
Der lokale Hugo-Server zeigt die Seite so, wie sie gedacht ist: kein fehlender Abstand, keine Überlagerung, nichts.

Wer an dieser Stelle weitersucht, sucht in der Quelle nach einem Fehler, der nicht drinsteht.
Man kann das lange tun.

## Die Stufe, die man nicht sehen kann

Der Denkfehler steckt in einem Satz, den ich mir selbst mehrfach gesagt hatte: *Lokal sieht es gut aus.*

Lokal baut Hugo den Blog so, wie ich ihn geschrieben habe.
Das CI baut ihn mit `--minify`: Der Minifier wirft Leerraum weg, kürzt Attribute und lässt schließende Tags aus, wo HTML sie ohnehin nicht verlangt.
Das ist der Standardweg für Produktionsbuilds und keine exotische Einstellung, und in diesem Blog stand er seit dem ersten Commit im Deploy-Workflow.

Damit sind es zwei verschiedene Ausgaben.
Die Seite, die ich mir ansehe, ist nicht die Seite, die im Web steht.
„Lokal geprüft" ist eine Aussage über eine andere Datei.

Das ist die These dieses Beitrags, und sie ist unbequemer als der Bug: Jede Stufe, die nur auf einer Seite läuft, ist ungetestet — egal wie oft man auf die andere Seite schaut.

## Ein Zeichen

Gefunden habe ich die Stelle nicht durch Lesen, sondern durch Vergleichen.
Zweimal bauen, einmal mit `--minify` und einmal ohne, und dann für jede Seite den reinen Text der einen gegen den reinen Text der anderen stellen.
Wo beide auseinanderlaufen, liegt der Schaden, und man muss vorher nicht wissen, wie die Seite aussehen sollte.

Der Text lief in der Grafik auseinander, die über der Serienübersicht steht.
Sie ist ein Inline-SVG, und in ihrer Beschreibung stand ein Satz, in dem etwas „wächst weiter" sollte.

```text
„wächst weiter"
```

Vorne das deutsche Anführungszeichen unten, hinten ein gerades.
Für einen Menschen ein Schönheitsfehler.
Für einen Parser ein einzelnes ungepaartes `"`, eines, dem das zweite fehlt.

Die englische Fassung derselben Grafik blieb heil.
Dort steht `"keeps growing"`: zwei gerade Anführungszeichen, gerade Anzahl, alles paart sich.
Und das zweite Schema in derselben Serie hatte denselben Fehler sogar zweimal, und überlebte aus genau demselben Grund.

Der Fehler war also nicht selten.
Er war nur zufällig meistens unauffällig.

## Wie ein Zeichen einen Anker öffnet

Ab dem ungepaarten Anführungszeichen verliert der Minifier die Spur.
Er hält für Attributwert, was Text ist, und ab da stimmt seine Vorstellung vom Dokument nicht mehr mit dem überein, was tatsächlich dasteht.

Der erste Schaden ist harmlos und erklärt Symptom eins: An den Rändern von Inline-Elementen fällt Leerraum weg, den der Browser gebraucht hätte.
Deshalb klebten fettes Satzende und normaler Text aneinander.
Es traf auch den Footer, der plötzlich behauptete, die Seite sei „Powered byHugo&PaperMod".

Der zweite Schaden erklärt Symptom zwei, und für ihn braucht es eine Regel, die man kennen muss.
Ein Element, das sich selbst schließt, also der Schrägstrich vor der spitzen Klammer, funktioniert in SVG wirklich.
In HTML ist derselbe Schrägstrich wirkungslos: Ein Anker, der so geschrieben wird, gilt als geöffnet und nicht als geschlossen.

Genau das geschah mit den Ankern der drei Beitragskacheln auf der Übersichtsseite.
Ihr schließendes Tag fiel weg, der Schrägstrich stand da wie ein Abschluss und war keiner, und der Anker blieb offen.

Diese Anker sind kein gewöhnlicher Link im Text.
Sie liegen absolut positioniert über der gesamten Kachel, damit die ganze Fläche klickbar ist.
Ein Anker, der nie geschlossen wird, nimmt alles Folgende in sich auf: Der Rest der Seite wandert in ein Element, das über einer Kachel liegen soll, und legt sich mit ihm über den Text darunter.

Das ist die Überlagerung.
Ein Anführungszeichen, drei Kacheln, eine zerlegte Seite.

## Der Text, den niemand sieht

Das Zeichen lag in einem `<desc>`-Element.
Das ist die Beschreibung, die ein Screenreader vorliest, wenn er auf die Grafik trifft, auf dem Bildschirm ist sie unsichtbar.

Es ist damit ungefähr der letzte Ort auf der Seite, an dem jemandem ein schiefes Anführungszeichen auffällt.
Wer die Seite ansieht, sieht ihn nicht.
Wer sie liest, liest ihn nicht.
Er steht da für Leserinnen, die die Grafik nicht sehen können, und wird deshalb von allen anderen nie geprüft.

Unsichtbarer Text hat die sichtbare Seite zerstört.

Das ist mehr als eine Pointe.
Barrierefreie Ergänzungen sind fast immer Text ohne Publikum im eigenen Alltag: Alternativtexte, Beschreibungen, Beschriftungen, die man selbst nie zu Gesicht bekommt.
Was niemand ansieht, korrigiert auch niemand nebenbei.
Für [dieselbe Sorte Aufmerksamkeit](/de/posts/shortcuts-as-an-input-aid/) habe ich an anderer Stelle argumentiert, dass sie sich für alle auszahlt.
Hier zahlte sich ihr Fehlen für alle aus.

## Derselbe Verdächtige, drei Tage vorher

Am 2. September hatte `--minify` schon einmal etwas zerlegt.
Damals traf es den JSON-LD-Block, in einem Testlauf mit anderer Basis-URL.

Der Produktionsbuild war nicht betroffen, und deshalb wurde der Befund als Eigenart des Prüfaufbaus abgehakt.
Der Minifier hatte seine Zähne gezeigt, und ich habe ihn weiterlaufen lassen.

Das ist der Teil, den ich ungern schreibe, und der Grund, warum er hier steht: Es war nicht fehlende Sorgfalt.
Drei Tage vorher lag der Hinweis vor, und er wurde korrekt eingeordnet, als Sonderfall eines Prüfaufbaus.
Was fehlte, war nicht Aufmerksamkeit, sondern eine Stelle, an der dieser Verdacht regelmäßig überprüft wird.
Genau das leistet ein Mensch nicht, der schon dreimal hingesehen hat.

## Wer die Zeile geschrieben hat

Die fehlerhafte Zeile stammt nicht von mir.
Das Shortcode für die Grafik hat mein Agent gebaut, samt Beschreibung für Screenreader.
Der Commit ist von ihm, der Push auch, und der Linkchecker lief auf demselben Commit grün durch: 52 Sekunden, kein Fehler.
Er prüfte Links, und die Links waren in Ordnung.

Aufgefallen ist es einem Menschen, der eine Seite im Browser ansah.

Ich schreibe das nicht als Vorwurf.
Ein deutsches Anführungszeichen in einem deutschen Satz ist genau richtig.
An einer Stelle, die durch einen Minifier läuft, ist es der Bruch.
Interessant ist die Kombination: Die Zeile entstand schnell, sie war plausibel, sie war grün geprüft, und der einzige Prüfschritt, der sie erwischt hätte, lief nur auf der anderen Seite.

## Ein Test ohne Soll

Der Fix ist nicht das Anführungszeichen.
Das war eine Minute Arbeit.

Der Fix ist `tools/check-minify.py`: Er baut den Blog zweimal, mit und ohne `--minify`, und vergleicht für jede Seite den reinen Text und die Tag-Bilanz.
145 Seiten in unter einer Sekunde.
Er hängt im Deploy-Workflow vor dem Veröffentlichungs-Build und läuft lokal vor jeder Veröffentlichung.
Die Stufe, die vorher nur im CI lief, läuft jetzt auf beiden Seiten.

Das Bemerkenswerte an diesem Prüfer ist, was er *nicht* weiß.
Er hat kein Soll.
Er kennt keine Regel dafür, wie die Seite auszusehen hat, und er würde ein hässliches Layout nie bemängeln.
Er verlangt nur, dass zwei Bauergebnisse, die gleich sein müssen, auch gleich sind.

Ein Differenztest braucht kein Orakel.
Das ist der übertragbarere Teil als der Anführungszeichen-Bug, und es ist der Grund, warum sich so ein Prüfer in einer Stunde schreiben lässt statt in einer Woche.

Zwei Fallen lagen trotzdem darin, und beide zeigen, dass ein Prüfer selbst erst geprüft werden muss:

- In SVG schließt ein selbstschließendes Element wirklich, in HTML nicht.
  Ohne diese Unterscheidung meldete die Strukturprüfung 89 Fehlalarme aus den Grafiken.
- Pythons `HTMLParser` hält einen selbstschließenden Anker für geschlossen — Browser tun das nicht.
  Wäre das so geblieben, wäre genau der Befund durchgefallen, der die Überlagerung verursacht hat.

Gegengeprüft habe ich den Prüfer, indem der Defekt zurückgebaut wurde: das Anführungszeichen wieder hinein, Prüfer laufen lassen, Befund da.
Ein Test, der nicht nachweislich anschlägt, hat nichts bewiesen.

## Was ich gelernt habe

- **„Lokal geprüft" ist eine Aussage über eine andere Datei**, sobald zwischen lokal und veröffentlicht eine Stufe liegt, die nur eine Seite kennt.
- **Ein Fehler in der Ausgabe muss nicht in der Quelle stehen.** Wer nur die Quelle liest, findet ihn nie, und hält die Sache irgendwann für Magie.
- **Zufällig unauffällig ist nicht selten.** Derselbe Fehler stand mehrfach in denselben Dateien, sichtbar wurde er nur dort, wo die Anzahl ungerade war.
- **Was niemand ansieht, korrigiert auch niemand nebenbei.** Beschreibungen für Screenreader sind der blindeste Fleck einer Seite, im Wortsinn.
- **Ein grüner Prüflauf beweist nur, was er prüft.** Der Linkchecker hatte recht: Die Links waren in Ordnung.
- **Ein Vergleich schlägt eine Erwartung.** Ein Test ohne Soll braucht niemanden, der vorher weiß, wie es aussehen soll, und findet trotzdem den Bruch.

## Was sich übertragen lässt

Die Geschichte sieht aus wie eine Blog-Geschichte, ist aber keine.
Kein Teil davon hängt an Hugo, an Markdown oder daran, dass hier eine agentische KI mitschreibt, die kommt nur darin vor, weil sie den Fehler mitgesucht hat.
Er hängt an einer einzigen Eigenschaft der Pipeline: **Ein Schritt läuft nur auf einer Seite.**

Wer lokal `npm run dev` startet und im CI `npm run build` fährt, hat sie.
Wer sein Container-Image im CI mit anderen Flags baut als auf dem Laptop, hat sie.
Wer Assets erst beim Deploy komprimiert, minifiziert, signiert oder umschreibt, hat sie.
Das defekte Zeichen ist austauschbar, die Asymmetrie ist es nicht.

Sieh nach, welche Stufen deiner Veröffentlichung nur auf einer Seite laufen.
Fast jedes Projekt hat mindestens eine: ein Minifier, ein Bundler, eine Kompression, ein Optimierungsschritt, der lokal ausgeschaltet ist, weil er die Entwicklung langsam macht.

Diese Stufe ist ungetestet, und zwar dauerhaft.
Nicht, weil sie schlecht wäre.
Weil niemand ihr Ergebnis regelmäßig ansieht.

Der Handgriff, der sich lohnt, ist kleiner als ein Test: Baue einmal beides und vergleiche die Ergebnisse gegeneinander.
Du musst nicht wissen, was herauskommen soll.
Es genügt zu verlangen, dass zweimal dasselbe herauskommt.
