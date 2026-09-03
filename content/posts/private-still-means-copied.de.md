---
title: "Auch privat wird kopiert: Wo die Notizen liegen dürfen, die noch niemand lesen soll"
date: 2026-09-03T02:00:00+02:00
draft: true
tags: ["claude-code", "obsidian", "syncthing", "privacy", "workflow"]
summary: "Ich wollte meine halbfertigen Ideen in Obsidian auf dem Telefon haben und am Schreibtisch Claude Code daran. Die Verbindung der beiden war am Ende gar keine technische Frage — und das Prüfskript, das ich danach schrieb, fand einen Fehler in dem, was gerade erst entstanden war."
---

## Kurzfassung

- Meine Ideen für Blogbeiträge liegen in Obsidian, und ich wollte Claude Code mit mir daran arbeiten lassen.
- Die Claude-App auf dem Telefon kommt an einen lokalen Obsidian-Vault nicht heran.
  Es gibt drei Wege drumherum, und jeder davon ist technisch sauber.
- Zwei fielen aus Gründen weg, die mit Technik nichts zu tun haben.
- Ein *privates* Repository wird trotzdem auf eine Maschine kopiert, die mir nicht gehört.
  Die Sichtbarkeitseinstellung war nie der Punkt.
- Was schließlich funktionierte, lief seit Jahren in meinem privaten Netzwerk.
  Niemand hatte es für diesen Zweck angesehen.
- Danach schrieb ich ein kleines Prüfskript für die Notizen, und der allererste Lauf fand einen Fehler in dem, was ich gerade gebaut hatte.

---

## Der Teil, den ich für schwierig hielt

Eine Idee für einen Beitrag kommt selten am Schreibtisch.
Sie kommt beim Spazierengehen, in der Schlange an der Kasse, mitten in einem Satz über etwas ganz anderes.
Deshalb liegen die Ideen in Obsidian, das ich auf dem Telefon dabeihabe.

Claude Code dagegen läuft am Schreibtisch.
Er liest Dateien, führt Befehle aus und kann einen halbgaren Gedanken so lange durchsprechen, bis er entweder trägt oder auseinanderfällt.
Genau das braucht eine Idee — und es fand an einem anderen Ort statt als dort, wo die Ideen lagen.

Ich nahm an, der schwierige Teil wäre die Verbindung der Systeme.
War er nicht.
Für die Verbindung der Systeme gibt es mehrere gute Antworten.
Der schwierige Teil war eine Frage, die ich mir gar nicht gestellt hatte: **Wo bin ich eigentlich bereit, diese Notizen liegen zu lassen?**

## Kommt Claude an meinen Obsidian-Vault? Nein.

Fang mit dem Naheliegenden an.
Es gibt eine Claude-App fürs Telefon.
Der Obsidian-Vault ist ein Verzeichnis voller Markdown-Dateien auf demselben Telefon.

Die App kann es nicht öffnen.
Sie hat kein eigenes Dateisystem zum Stöbern, keine Möglichkeit, ein Hilfsprogramm neben sich laufen zu lassen, und keinen Mechanismus, über den Obsidian ihr einen Ordner überreichen könnte.
Was sie kann: eine Datei entgegennehmen, die du ihr von Hand über den System-Dialog anhängst, eine nach der anderen.
Das ist kein Arbeiten an einem Vault.
Das ist eine Mail an sich selbst mit Anhang.

Der direkte Weg ist also zu.
Und damit fängt das Interessante an, denn es gibt drei indirekte.

## Weg eins: den Vault in ein Repository legen

Claude Code arbeitet gut auf Code-Repositories, und ein Vault voller Markdown-Dateien ist strukturell genau das.
Lade ihn zu einem Hoster hoch, und du kannst vom Telefon aus eine Sitzung darauf starten: Claude Code klont das Repository in eine Sandbox, arbeitet dort und schiebt einen Branch zurück.
Keine Kosten über mein bestehendes Abo hinaus, keine Schlüssel zu verwalten, und das Telefon wird zur echten Fernbedienung.

Ich kam bis zu dem Gedanken „dann mache ich es eben privat“, bevor der eigentliche Einwand ankam.

Ein privates Repository ist kein Ort, an dem meine Notizen *bleiben*.
Es ist ein Ort, an dem sie *liegen* — und jede Sitzung **klont sie anschließend in eine virtuelle Maschine, die jemand anderem gehört**.
Die Sichtbarkeitseinstellung regelt, wer die Seite im Browser aufrufen darf.
Über den Verbleib der Arbeitskopie sagt sie nichts.

Dieser Unterschied rutscht leicht durch, weil „privates Repo“ klingt, als hättest du damit bereits eine Entscheidung über Vertraulichkeit getroffen.
Hast du nicht.
Du hast eine über das Publikum einer Webseite getroffen.

Und hier war das wichtiger, als es bei Quelltext gewesen wäre.
Halbfertige Ideen sind kein Quelltext.
Manche sind auf eine Art falsch, die ich lieber nicht dokumentiert hätte.
Manche handeln von Menschen.
Manche werde ich vielleicht nie veröffentlichen.
Genau das ist der Sinn eines Orts für unfertige Gedanken: Er muss irgendwo sein, wo dir niemand zusieht.

## Weg zwei: Claude in Obsidian holen

Es gibt ein Community-Plugin — Vault Companion for Claude —, das ein Chatfenster direkt in Obsidian legt, auf dem Telefon wie am Rechner, mit echtem Zugriff auf die Notizen: lesen, suchen, anlegen, ändern, mit einer Freigabekarte für jeden Schreibvorgang.
Das ist ziemlich genau die Form dessen, was ich mir ursprünglich vorgestellt hatte.

Es hat zwei Betriebsarten.
Die eine leitet über einen Rechner mit installiertem Claude Code weiter; dafür wollte sie Hardware, die ich nicht habe.
Die andere spricht direkt mit dem Anbieter, über **einen eigenen API-Schlüssel**, abgerechnet nach Token.

Und dort war Schluss, aus einem Grund, der langweilig und vollkommen ausschlaggebend ist: Ich zahle bereits ein monatliches Abo, und ich hatte keine Vorstellung davon, was eine zweite, verbrauchsabhängige Abrechnung daneben mit meinen Kosten machen würde.
Nicht „ich habe es geschätzt und es war zu teuer“ — ich konnte es überhaupt nicht schätzen.
Der Tokenverbrauch für Gespräche lässt sich vorab ehrlich schlecht vorhersagen, und die aufrichtige Antwort auf „was kostet mich das im Monat?“ war ein Schulterzucken.

Eine zweite Art, zur Kasse gebeten zu werden, deren Höhe du nicht abschätzen kannst, führt man nicht mal eben an einem Dienstagabend für ein Hobbyprojekt ein.

## Weg drei: Claude Code zu Hause lassen

Der dritte Weg gefiel mir am besten, und ich habe ihn trotzdem nicht genommen.

Claude Code kann eine Sitzung, die **auf deinem eigenen Rechner** läuft, so bereitstellen, dass du sie vom Telefon oder aus dem Browser steuerst.
Die Arbeit passiert lokal: dein Dateisystem, deine Werkzeuge, deine Dateien, nichts davon wird irgendwohin kopiert.
Es ist in allen Tarifen enthalten, braucht weder API-Schlüssel noch Repository-Hoster, und verbunden wird es, indem du einen QR-Code scannst.

Für die Vertraulichkeitsfrage ist das die gute Antwort.
Nichts wird geklont.
Nichts wird gehostet.
Die Dateien bleiben genau dort, wo sie waren.

Zwei Dinge haben mich abgehalten, und nur eines davon ist technisch.

Das technische: Eine Sitzung muss *laufen*, auf einem Rechner, der *wach und erreichbar* ist, in dem Moment, in dem ich irgendwo stehe und eine Idee habe.
Mein Laptop ist zugeklappt, solange ich unterwegs bin.
Das bedeutet einen Rechner im Dauerbetrieb, von außen erreichbar — ein kleines Infrastrukturprojekt für sich.

Das nichttechnische gehört deutlich gesagt, weil es die ehrliche Grenze dieses ganzen Ansatzes ist: Die Dateien gehen nicht raus, aber **das Gespräch schon**.
Alles, was Claude Code liest und mit mir bespricht, geht wie jede andere Eingabe zum Anbieter.
Das ist dieselbe Preisgabe, die ich am Schreibtisch ohnehin akzeptiere, also kein neues Problem — aber „die Dateien bleiben auf meiner Maschine“ ist ein engeres Versprechen, als es zunächst klingt, und ich sage es lieber, als es mitschwingen zu lassen.

## Was ohnehin schon lief

Jetzt der ernüchternde Teil.

Das Verzeichnis, in dem alle meine Obsidian-Vaults liegen, wird von **Syncthing** zwischen meinen Geräten abgeglichen, und zwar seit Jahren.
Es arbeitet direkt zwischen den Geräten, läuft auf meiner eigenen Hardware, hat keinen Cloud-Anteil — und kopierte genau dieses Verzeichnis längst auf mein Telefon, jedes Mal, wenn ich zur Tür hereinkam.

Der Grund, warum es nie aufkam: Ich hatte gefragt „wie verbinde ich Claude Code mit meinem Telefon?“
Die richtige Frage lautete „wo müssen die Notizen liegen, damit wir beide sie erreichen?“
Und die Antwort war: genau dort, wo sie schon lagen.

Claude Code erreicht sie am Schreibtisch, weil sie ein Ordner auf meiner Platte sind.
Ich erreiche sie auf dem Telefon, weil der Ordner abgeglichen wird.
Es war nichts Neues nötig.
Ich habe einen neuen Vault in ein Verzeichnis gelegt, das ohnehin schon herumkopiert wurde, und das war die ganze Anbindung.

Aufgegeben habe ich die Unmittelbarkeit.
Schreibe ich im Café eine Idee auf, erreicht sie meinen Schreibtisch erst, wenn ich zu Hause bin.
Ich habe ungefähr zehn Sekunden gebraucht, um das in Ordnung zu finden.
Eine Idee ist kein Deployment.
Nichts hängt daran, dass sie binnen einer Stunde ankommt, und der Druck, Notizen sofort synchronisieren zu müssen, ist größtenteils aus Werkzeugen geborgt, bei denen Verzögerung tatsächlich zählt.

## Eine single source of truth, und keine zweite

Die Entwurfsentscheidung, die mir den meisten Ärger erspart hat, war der Verzicht auf Cleverness.

Es gibt genau **einen** Ort, an dem die Notizen liegen: den Vault.
Eine *single source of truth* — eine Fassung, die gilt, und daneben keine zweite, die still danebendriftet.
Der Projektordner mit den Werkzeugen enthält einen Symlink darauf und sonst nichts, was auseinanderlaufen könnte.
Kein Spiegel, kein Exportschritt, kein Skript, das Notizen hin- und herkopiert und hinterher abgleicht.

Das ist wichtig wegen einer Eigenschaft, die alle Abgleichwerkzeuge teilen: **Sie führen nicht zusammen.**
Ändert sich dieselbe Datei zwischen zwei Abgleichen an zwei Stellen, bekommst du weder eine kombinierte Fassung noch eine Fehlermeldung.
Du bekommst eine zweite Datei mit `sync-conflict` und einem Zeitstempel im Namen, die still neben dem Original liegt — und dort liegen bleibt, bis jemand hinsieht.

Bei einer single source of truth und einem Bearbeiter zur Zeit ist dieser Fall selten.
Mit Spiegel und Kopierskript hätte ich ihn planmäßig hergestellt.

## Und dann habe ich geprüft, was gerade entstanden war

Als der Vault stand — eine Vorlage für neue Notizen, ein Index, ein paar Konventionen im Kopfbereich der Dateien — schrieb ich ein Skript, das ihn prüft.

Das mag übertrieben klingen für einen Haufen Markdown-Dateien.
Die Überlegung war: Die Regeln existieren nur in meinem Kopf und in einer README, einige der Prüfungen sind schlicht stumpfsinnig (steht jede Notiz im Index? zeigt jeder Verweis irgendwohin? ist jeder Statuswert einer, den ich definiert habe?), und eine davon ist unsichtbar, bis sie weh tut — nämlich die Konfliktdateien von oben.
Eine kollidierte Notiz meldet sich nicht.
Sie liegt einfach da, während ich die veraltete Fassung lese.

Der erste Lauf schlug fehl.

Nicht an meinen alten Notizen.
Er schlug an der **Vorlage fehl, die ich zwanzig Minuten vorher geschrieben hatte** — der, aus der jede künftige Notiz entstehen sollte.

Die Vorlage trägt das Anlagedatum automatisch ein, mit der Platzhalter-Schreibweise von Obsidian:

```yaml
angelegt: {{date:YYYY-MM-DD}}
```

Diese Zeile ist kein gültiges YAML.
Geschweifte Klammern eröffnen eine Zuordnung, der Parser liest also eine Struktur, verschluckt sich am Doppelpunkt darin und gibt den ganzen Kopfbereich verloren.
Jede aus dieser Vorlage erzeugte Notiz hätte mit Metadaten begonnen, die der Editor nicht lesen kann.

Die Reparatur sind zwei Anführungszeichen.
Um die Reparatur geht es nicht.

Es geht darum, dass diese Zeile geschrieben, gegengelesen und von zweien im Vorbeigehen angesehen worden war — und *völlig in Ordnung aussah*, weil sie aussieht wie jeder andere Vorlagen-Platzhalter auf der Welt.
Es brauchte ein Programm, das nicht weiß, was die Zeile bedeuten soll, und nur prüft, ob sie sich lesen lässt.

Es gibt eine Fassung dieses Abends, in der ich das Prüfskript nicht schreibe und stattdessen Wochen später auf dem Telefon davon erfahre, wenn eine frisch angelegte Notiz ihre eigenen Metadaten als Fließtext anzeigt.

Ob dieses Prüfskript selbst etwas taugt, ist eine andere Frage, und ich möchte sie mir ordentlich ansehen — ein Test, der nicht fehlschlagen kann, ist nichts wert, und dieser hier war in derselben Sitzung von denselben Händen geschrieben worden wie das, was er prüft.
Das ist ein eigener Beitrag.

## Was ich gelernt habe

1. **Frag zuerst, wo die Daten liegen dürfen, und erst dann, wie du irgendetwas verbindest.**
   Jeder Weg, den ich angesehen habe, war technisch in Ordnung.
   Die beiden, die wegfielen, fielen an Vertraulichkeit und an Abrechnung.
   Hätte ich mit der Verbindung der Systeme angefangen, hätte ich das Falsche kompetent gebaut.
2. **„Privat“ beschreibt eine Webseite, keinen Arbeitsablauf.**
   Ein privates Repository wird trotzdem bei jeder Sitzung in fremde Infrastruktur kopiert.
   Wenn dir das bei deinen Inhalten etwas ausmacht, hilft dir die Einstellung nicht — und man hält sie leicht für eine Entscheidung, die man getroffen hat.
3. **Unabschätzbare Kosten sind ein echter Einwand, kein fauler.**
   „Ich kann das nicht einschätzen“ ist ein legitimer Grund, eine zweite Abrechnung abzulehnen.
   Man muss ihn nicht als technisches Bedenken verkleiden.
4. **Sieh nach, was ohnehin schon läuft.**
   Die Antwort spiegelte genau dieses Verzeichnis seit Jahren auf mein Telefon.
   Ich hätte beinahe einen zweiten Mechanismus neben einen funktionierenden gestellt, weil meine Frage um ein Produkt herum gebaut war statt um meine Dateien.
5. **Asynchron reicht meistens.**
   Ideen müssen nicht binnen einer Minute ankommen.
   Ein Großteil des Drucks zum sofortigen Abgleich ist aus Werkzeugen geerbt, bei denen Verzögerung wirklich zählt — und er ist nicht umsonst, denn genau er treibt dich zuerst in gehostete Ablagen.
6. **Eine single source of truth.**
   Keine Spiegel, keine Exportschritte.
   Abgleichwerkzeuge führen nicht zusammen; sie legen eine Konfliktdatei ab und sagen nichts.
   Stell die Bedingungen dafür nicht absichtlich her.
7. **Prüfe das, was du gerade gebaut hast, nicht nur das, was du schon hattest.**
   Der Fehler saß in der neuesten, kleinsten und offensichtlich korrektesten Datei des Projekts.
   Neuer Code ist der Code, den noch niemand angesehen hat — auch nicht die Person, die ihn vor zehn Minuten geschrieben hat.

## Wenn du noch unschlüssig bist

Wenn du Notizen führst und dich fragst, ob du Claude Code an sie heranlassen sollst, ist das Nützlichste, was ich anbieten kann, keine Einrichtungsanleitung.
Es ist die Reihenfolge der Fragen.

Fang damit an, was tatsächlich in deinen Notizen steht.
Nicht „ist das sensibel“ im Allgemeinen, sondern: Steht hier etwas, bei dem es mir unangenehm wäre, wenn es auf eine Maschine kopiert würde, die ich nicht kontrolliere — und sei es kurz, und sei es privat?
Bei einer Rezeptsammlung vermutlich nicht, und dann sind die gehosteten Wege ausgezeichnet und du solltest sie nehmen.
Bei allem Halbfertigen, Persönlichen oder von anderen Handelnden ändert sich die Antwort — und zwar *bevor* du bei den Werkzeugen ankommst.

Sieh dir dann an, was du schon betreibst.
Dateiabgleich, ein Heimserver, ein Gerät, das ohnehin läuft — das ist unspektakulär und taucht in keiner Integrationsanleitung auf, und genau deshalb übersieht man es leicht.

Und nimm die langweilige Lösung, wenn sie die richtige ist.
Was ich gebaut habe, ist ein Ordner in einem Verzeichnis, das ohnehin kopiert wurde, plus ein Symlink, plus ein Skript, das etwas YAML liest.
Es ist nicht clever.
Es hat keinen Cloud-Anteil, keine zweite Rechnung und keine laufenden Entscheidungen.
Gekostet hat es einen Abend, von dem der größte Teil dafür draufging herauszufinden, was ich eigentlich will — was, wie üblich, die eigentliche Arbeit war.
