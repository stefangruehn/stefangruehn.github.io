---
title: "„baue einen blog mit hugo\": Der Auftrag, der seine eigene Antwort enthielt"
date: 2026-09-08T09:00:00+02:00
draft: false
tags: ["claude-code", "hugo", "CI", "werkzeuge", "messung", "selbstbezug", "Essay"]
themen: ["veroeffentlichen"]
summary: "Die erste Aufgabe an den Agenten bestand aus sechs Wörtern, und eines davon war bereits die Antwort. Das Werkzeug stand fest, bevor irgendwer gefragt hatte, und nachgemessen wurde nie. Hier wird es nachgeholt, mit dem unangenehmen Befund, dass Hugo je nach Rangliste auf Platz 2, auf Platz 1 oder überhaupt nicht steht."
---

*„baue einen blog mit hugo"*

Das war die Aufgabe.
Sechs Wörter, und eines davon war bereits die Antwort.

Der Agent hat nicht widersprochen.
Er hat gebaut.

## Kurzfassung

- Die allererste Aufgabe an den Agenten enthielt die Werkzeugentscheidung schon.
  Es gab keine Recherche, keinen Vergleich, keine Begründung, nur einen Namen im Auftrag.
- Das ist der wunde Punkt: Dieser Blog behauptet an zwei Stellen, dass hier **gemessen** und nicht behauptet wird.
  Ausgerechnet die Entscheidung, auf der alles Weitere steht, ist nie gemessen worden.
- Nachlesen lässt sich das durchaus, ohne selbst das halbe Web zu crawlen. Es gibt mindestens drei öffentliche Ranglisten.
- Nur misst keine zwei dasselbe. **Hugo steht auf Platz 2, auf Platz 1 und gar nicht**, je nachdem, welche man aufschlägt.
- Jede Rangliste bevorzugt strukturell eine Bauart: GitHub-Sterne belohnen Alter, das `generator`-Meta-Tag belohnt, wer es nicht abschaltet, npm-Downloads sehen nur, was aus npm kommt.
- Die Wahl war trotzdem richtig, und ich kann inzwischen sagen, woran ich das festmache, nämlich an vier Eigenschaften, die im Alltag tatsächlich getragen haben.
- Die vierte davon hat niemand gefordert: Weil die ganze Kette aus Textdateien und Kommandos besteht, ließe sie sich vollständig **von außen** bedienen, vom Telefon aus. Erprobt ist das nicht.

---

## Sechs Wörter, eines davon die Antwort

Ich habe „mit Hugo" in den Auftrag geschrieben, weil ich Hugo kannte.
Nicht, weil ich es verglichen hätte.
Der Agent hat die Vorgabe genommen, wie sie dastand, und angefangen zu bauen: Struktur, Theme, Zweisprachigkeit, Deployment.

Das ist erst einmal richtiges Verhalten.
Wer eine Werkzeugvorgabe im Auftrag stehen hat, soll sie nicht bei jeder Gelegenheit aufmachen. Ein Agent, der auf „baue X mit Y" mit einer Marktübersicht antwortet, ist anstrengend und meistens im Weg.

Trotzdem bleibt eine unangenehme Lücke.
Auf der [Themenübersicht](/de/themen/) dieses Blogs stehen zwei Leitthemen: dass KI-gestützte Werkzeuge Grundausstattung sind, und dass hier gemessen und nicht behauptet wird.
Das erste hat bei dieser Aufgabe sauber funktioniert.
Das zweite kam gar nicht erst zum Einsatz.

Also hole ich es nach.
Umwerfen will ich sie damit nicht, sie war gut.
Mich interessiert, was „gut" hier überhaupt heißen kann.

## Was hätte dastehen können

Die Sammlung bei Netlify listet über 500 statische Seitengeneratoren.
Ernsthaft in Frage gekommen wäre für einen zweisprachigen Textblog eine gute Handvoll, grob nach Bauart sortiert:

- **Ein Binary, keine Laufzeit:** Hugo (Go), Zola (Rust).
- **Die Urahnen:** Jekyll (Ruby), das GitHub Pages bis heute ohne Zutun baut, und Middleman.
- **Python:** Pelican, MkDocs mit dem Material-Theme, das faktisch der Standard für Dokumentation geworden ist.
- **JavaScript, contentorientiert:** Astro, Eleventy, Docusaurus, VitePress.
- **JavaScript, App-Frameworks mit Static-Export:** Next.js, Nuxt, SvelteKit, Gatsby.

Gatsby ist dabei das Lehrstück: 2023 von Netlify übernommen, seither in der Wartung stabil und in der Nutzung rückläufig.
Ein Werkzeug kann gepflegt sein und trotzdem verschwinden.

## Drei Ranglisten, drei verschiedene Größen

Die eigentliche Frage war, ob sich so etwas überhaupt *nachlesen* lässt, statt es selbst zu erheben.
Das geht, an mindestens drei Stellen, alle frei zugänglich, Stand 8. September 2026:

| Quelle | misst | Hugo steht dort |
|---|---|---|
| [jamstack.org/generators](https://jamstack.org/generators/) (Netlify, über 500 Einträge, nach GitHub-Sternen sortierbar) | **Aufmerksamkeit** | **Platz 2**, rund 82.900 Sterne, hinter Next.js (rund 133.900), vor Docusaurus (rund 61.400) |
| [W3Techs](https://w3techs.com/) | **tatsächlich ausgelieferte Websites** | **Platz 1** unter den Generatoren, in der Größenordnung von 0,0x Prozent aller Websites |
| npm-Downloads, etwa über npm trends | **Installationen in JavaScript-Projekten** | **gar nicht**, denn Hugo ist ein Go-Binary und kommt in npm schlicht nicht vor |

Drei Quellen, drei Ergebnisse, alle drei korrekt.
Sie widersprechen sich nicht, weil eine falsch wäre, sondern weil sie **verschiedene Dinge zählen**.

Und jede zählt so, dass sie eine Bauart bevorzugt:

**GitHub-Sterne sind kumulativ und werden praktisch nie zurückgegeben.**
Ein Stern von 2016 wiegt so viel wie einer von gestern.
Die Liste misst damit eher Lebensalter mal Sichtbarkeit als heutige Verwendung.

**W3Techs erkennt einen Generator im Wesentlichen an einem Meta-Tag.**
Hugo setzt `<meta name="generator" content="Hugo …">` von Haus aus, Jekyll ebenfalls, und zahlreiche Themes entfernen es wieder, aus Sparsamkeit oder Diskretion.
Wer das Tag abschaltet, verschwindet aus der Statistik.
Astro und Next.js hinterlassen dagegen Laufzeitartefakte im ausgelieferten HTML, die niemand versehentlich wegkonfiguriert.
Die Rangliste misst also nicht Nutzung, sondern **Sichtbarkeit der Nutzung**, und sie benachteiligt systematisch genau die Generatoren, deren Ergebnis am saubersten ist.

**npm-Downloads sind die ehrlichste und zugleich engste Zahl.**
Sie sind reproduzierbar und tagesaktuell, Astro etwa lag im Mai 2026 bei rund 2,7 Millionen Downloads pro Woche.
Nur misst sie das eigene Ökosystem und hält dessen Rand für den Rand der Welt.
Alles, was nicht als npm-Paket ausgeliefert wird, existiert dort nicht.

Dazu kommt eine vierte Sorte, die man beim Suchen als erstes findet: „Die 20 besten Static Site Generators 2026".
Die misst gar nichts.
Sie wird trotzdem am häufigsten zitiert, und sie ist der Grund, warum diese Frage als beantwortet gilt, obwohl sie es nicht ist.

Das ist der Befund, und er ist unbequemer als ein Ranking:
**Es gibt keine Zahl für „das beste Werkzeug", und es gibt nicht einmal eine für „das meistgenutzte".**
Es gibt drei Stellvertreter, die man nachlesen kann, wenn man dazusagt, welchen man meint.

## Warum die Wahl trotzdem trägt

Was man messen kann, ist die eigene Erfahrung, und die ist nach einigen Wochen und rund einem Dutzend Beiträgen deutlich genug.
Vier Eigenschaften haben tatsächlich getragen:

**Erstens: schnell.**
Der Build ist ein Tastendruck, keine Wartezeit.
Das klingt nach Bequemlichkeit und ist eine Verhaltensänderung: Ein Vorschauserver, der bei jedem Speichern neu rendert, macht das Gegenlesen im Browser zur Normalform statt zur Ausnahme.
Wer eine Minute auf den Build wartet, liest im Editor gegen und übersieht, was erst im Layout auffällt.

**Zweitens: leichtgewichtig.**
Ein einziges statisches Binary. Keine Laufzeit, kein `node_modules`, keine Lieferkette aus hunderten transitiven Paketen, die man weder liest noch aktualisiert.
Was hinten herauskommt, ist HTML, ohne Server, ohne Datenbank, ohne Angriffsfläche, die man pflegen müsste.

**Drittens: Zweisprachigkeit und Taxonomien sind eingebaut, nicht angebaut.**
Sprachvarianten je Datei, ein gemeinsamer `translationKey`, eigene Taxonomien und Serien, alles ohne ein einziges Plugin.
Daran hängt dieser Blog vollständig: Deutsch und Englisch sind hier die Grundeinheit, in der jeder Beitrag existiert, und kein Sonderfall.
Ein Generator, bei dem Mehrsprachigkeit ein Plugin von 2019 ist, wäre spätestens beim dritten Beitrag zum Problem geworden.

**Viertens: Prüfer sind billig, und Prüfer für Prüfer auch.**
Das ist der Punkt, den ich vorher nicht auf der Rechnung hatte, und der inzwischen der wichtigste ist.
Weil die Eingabe aus Textdateien besteht und die Ausgabe aus HTML ohne Laufzeit, ist ein Prüfer ein kurzes Skript.
Zweimal bauen und den Text jeder Seite gegen den Text derselben Seite stellen. Oder das Frontmatter aller Beiträge gegen eine Regel halten.
Kein Headless-Browser, keine Testumgebung, kein laufender Server.

Entstanden sind so, bis zum 7. September, fünf Prüfer und vier Selbsttests, die den Prüfern absichtlich Defekte unterschieben und rot werden müssen, sonst prüfen sie nichts.
Einer davon hat den Vorfall gefunden, von dem [der bislang einzige andere Beitrag in diesem Thema](/de/posts/green-locally-broken-on-the-web/) handelt: ein einzelnes Anführungszeichen, das den Minifier aus dem Tritt brachte und eine veröffentlichte Seite zerlegte, ohne dass lokal irgendetwas zu sehen war.

Hier laufen die beiden Leitthemen zusammen.
„Messen statt behaupten" bleibt eine Haltung, solange das Messen teuer ist.
Bei dieser Bauart kostet ein neuer Prüfer eine halbe Stunde und läuft danach in unter einer Sekunde vor jedem Deploy.
Das ist der Unterschied zwischen einem Vorsatz und einer Gewohnheit.

Der ehrliche Gegenposten gehört dazu: Hugos Template-Sprache ist sperrig, und das merkt man in dem Moment, in dem man selbst hineinfasst.
Wer viel am Layout arbeitet, wird damit weniger glücklich als jemand, der Text schreibt.

## Was niemand gefordert hat

Am Ende steht eine Kette, die vollständig aus Textdateien, Git und einem CI-Lauf besteht.
Kein Klickpfad, keine Oberfläche, kein Programm, das laufen muss, damit etwas passiert.

Daraus folgt eine Eigenschaft, die in keinem Auftrag stand: Die ganze Kette **ließe sich von außen bedienen**.
Idee notieren, Entwurf schreiben, Vorschau prüfen, Prüfer laufen lassen, veröffentlichen: alles davon sind Dateioperationen und Kommandos, und alles davon könnte fernbedient werden, über Claude Code Remote Control oder vom Telefon aus über die Claude-App.
Die einzige Voraussetzung wäre, dass die Maschine von außen erreichbar ist.

Konjunktiv, und der bleibt hier stehen: **Ich habe das nicht erprobt.**
Die Maschine ist bislang nicht von außen erreichbar, und solange das so ist, ist der Absatz eine Plausibilitätsüberlegung und keine Messung.
In einem Beitrag, dessen These „messen statt behaupten" lautet, gehört genau das dazugesagt.

Interessant ist es trotzdem, weil es zeigt, wie eine Werkzeugwahl weiterwirkt.
Eine Kette aus Dateien und Kommandos ist fernbedienbar.
Eine Kette aus Klicks ist es nicht.
Das war kein Kriterium bei der Entscheidung.
Es ist ein Nebenprodukt, und es ist wertvoller als die meisten Kriterien, die ich hätte aufschreiben können.

## Was bleibt

Die Werkzeugwahl war nie eine Wahl.
Sie stand im Auftrag, sie war richtig, und sie war ungeprüft — drei Dinge, die gleichzeitig wahr sein können.

Was ich mitnehme, ist weniger etwas über Hugo als über die Frage danach.
Wer wissen will, ob ein Werkzeug „führend" ist, kann das nachlesen, und zwar an mehreren Stellen ohne eigene Erhebung.
Er bekommt dann drei verschiedene Antworten und muss selbst entscheiden, welche Größe er eigentlich gemeint hat.
Das ist kein Mangel der Quellen. Das ist der Normalfall bei jeder Zahl, die man nicht selbst erhoben hat.

Und ja: Die Zahlen für diesen Beitrag hat derselbe Agent geholt, der damals nicht nachgefragt hat.
Ich habe die Quellen einzeln aufgeschlagen, bevor sie hier stehen.
Nachgeprüft gehört auch das, sonst wäre dieser Beitrag genau der Fehler, den er beschreibt.
