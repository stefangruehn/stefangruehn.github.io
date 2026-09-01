---
title: "Messen statt raten: Fehlersuche an einem Laptop-Lautsprecher mit Claude Code"
date: 2026-08-31T06:00:00+02:00
draft: false
tags: ["claude-code", "linux", "hardware", "debugging", "audio"]
summary: "Eine falsche Theorie, ein öffentlicher Widerruf und ein kleines Messwerkzeug — was ich darüber gelernt habe, AI-Unterstützung für Probleme einzusetzen, bei denen es überhaupt nicht um Code geht."
---

## Kurzfassung

- In meinem Laptop steckt ein Lautsprecher, den Linux nicht korrekt ansteuert.
  Jemand anderes hatte die eigentliche Tiefenarbeit bereits geleistet;
  ich bin von seiner Lösung ausgegangen und dabei auf meinem Gerät auf ein weiteres Problem gestoßen.
- Ich habe mir durch Hinhören eine erste Theorie gebildet, sie veröffentlicht — und sie war **falsch**!
- Statt darüber zu streiten, was wir da hören, haben Claude Code und ich aus dem eingebauten Mikrofon des Laptops ein kleines Messinstrument gebaut.
  Es hat meine erste Theorie über das Problem innerhalb einer Stunde widerlegt.
- Ich habe meine veröffentlichte Behauptung zurückgezogen und durch gemessene Fakten ersetzt.
- Der nützlichste Teil dabei war nicht die Geschwindigkeit.
  Es war, dass aus einer vagen Beschwerde — „dieser Lautsprecher klingt falsch“ — an einem Nachmittag etwas Solides mit Zahlen wurde, ohne dass ich Hardware-Ingenieur in einem Messlabor bin.
- Ich habe das Ganze in einem sicheren Modus laufen lassen, in dem ich den Plan freigebe, bevor irgendetwas lokal ausgeführt wird.
  Die Kontrolle ist ausdrücklich vorhanden — genau deshalb lohnt sich ein nüchterner Blick auf eine verbreitete Sorge in Bezug auf agentische AI.

---

## Der Ausgangspunkt: die Arbeit eines anderen

Der Laptop ist ein Chuwi CoreBook X.
Unter Linux bleibt sein linker Lautsprecher ab Werk stumm.
Der Chip, der ihn antreibt — ein AWINIC AW88298 Verstärker, der an einem undokumentierten Ausgang des Audio-Codecs hängt —, hat keinen Treiber im Mainline-Kernel.

Das habe nicht ich gelöst.
**Francisco Montañés García ([@pacomont](https://github.com/pacomont))** hat es getan, über rund fünf Wochen echter Knochenarbeit: den Chip über I2C abklopfen, nachweisen, welcher Teil des Systems ihm überhaupt Audio zuspielt, und schließlich herausfinden, warum jeder Benachrichtigungston mit einem Knacken beginnt.
Sein Projektlog ist [für sich genommen lesenswert](https://github.com/pacomont/chuwi-corebook-x-left-speaker), und alles Folgende baut darauf auf.

Ich habe seinen Daemon installiert und beide Lautsprecher liefen.
Dann fiel mir an meinem Gerät jedoch etwas auf, das seine Notizen nicht beschrieben — und dort beginnt mein Beitrag zu diesem Thema.

## Eine Theorie, gebaut durch Hinhören

Ton kam für mich sowohl klar aus der linken, vorderen Kante des Laptops, als auch von irgendwo unten rechts hinten.
Das legte einen **dritten** Breitbandlautsprecher nahe, wobei seine Lösung diesen statt des rechten vorderen Lautsprechers benutzte.

Ich habe es auf die naheliegende Art getestet: Ton abspielen, einen Ausgang nach dem anderen stummschalten, notieren, was ich höre.
Die Ergebnisse wirkten schlüssig.
Ich habe das aufgeschrieben und als Issue im Upstream-Projekt eingereicht, samt Änderungsvorschlag, damit andere Besitzer ihren dritten Lautsprecher zurückbekommen.

Das Problem: Ich hatte eine Schlussfolgerung „mit meinen Ohren“ gebaut und keine Vorstellung davon, was für ein schwaches Instrument das ist.

## Ohren sind kein Messgerät

Als Claude und ich das Verhalten später präziser festnageln wollten, hörten die Ergebnisse auf, zueinander zu passen.
Ein Testdurchlauf über sechs Konfigurationen brachte von mir das hier hervor:

> Stille, rechts, Stille, rechts, Stille, Stille, rechts

Noch einmal durchlaufen lassen — und es kam etwas anderes heraus.
Zwei der Lautsprecher sitzen auf dem Mainboard dicht beieinander, „woher kommt das gerade?“ ist also eine Frage, die mein Gehör schlicht nicht beantworten konnte.
Jeder Durchlauf lieferte eine Antwort, die sich für mich sicher anfühlte, aber die vermeintlich sicheren Antworten widersprachen einander.

Claude Code hat das angesprochen, statt weiter meine Meldungen einzusammeln:

> Die Höreindrücke widersprechen sich von Durchlauf zu Durchlauf.
> Ich höre auf, mich darauf zu stützen.

Unser gemeinsames Scheitern an diesem Punkt der Sitzung lag wohl nicht an mangelnder Mühe meinerseits.
Es lag vielmehr daran, dass wir mit dem falschen Instrument gemessen haben — und daran hätten auch noch so sorgfältiges Hinhören oder jüngere Ohren nichts geändert.

## Stattdessen: ein Instrument bauen

Der nächste Ansatz war, die Signale der eingebauten Mikrofone des Laptops aufzuzeichnen, während jeder Kanal Rauschen abspielt, und die Pegel zu vergleichen.
Das hat auch fast funktioniert, aber das Grundrauschen des Mikrofons hat den leisen Lautsprecher überdeckt.

Also wurde der Ansatz geschärft.
Statt die Lautstärke im Allgemeinen zu messen, misst man den *konkret abgespielten Ton* und ignoriert alles andere — ein Goertzel-Filter, der sich auf eine Frequenz einrastet und den Rest verwirft.
Zwei Frequenzen kamen zum Einsatz: 1 kHz für den Pegel und 6 kHz für eine ganz andere Frage — *kann dieser Lautsprecher überhaupt hohe Frequenzen erzeugen?*

Eine Anmerkung dazu, wie verblüffend flexibel das von Claude gelöst wurde: numpy, eine Python-Bibliothek zur Signalanalyse, war in der Umgebung nicht installiert, also wurde die Analyse kurzerhand in reinem Python geschrieben.
Keine Laborausrüstung nötig.
Nur ein Laptop-Mikrofon, ein Testton und ungefähr vierzig Zeilen Rechnerei auf den gemessenen Daten.

Die Ergebnisse waren sofort brauchbarer als alles, was ich vermeintlich gehört hatte:

| Abgespielt | Pegel bei 1 kHz | Irgendwas bei 6 kHz? |
|---|---|---|
| Rechter Kanal | +60 dB über Grundpegel | Ja |
| Linker Kanal | +15 dB über Grundpegel | **Nichts** |

45 dB Unterschied und ein Ausgang, der überhaupt keine Höhen produziert.
Das ist kein Stereopaar.
Das ist ein Breitbandlautsprecher und ein Tieftöner.

## Der Teil, in dem ich den Finger drauflege

Eine Frage blieb: *Wo* sitzt dieser leise, dumpfe Lautsprecher eigentlich physisch im Gehäuse?
Die Stereotrennung des Mikrofonarrays war zu schlecht, um das zu sagen.

Statt dagegen anzukämpfen, schlug Claude Code eine Methode vor, die ohne Ortung auskommt:

> Du deckst eine Öffnung nach der anderen ab, während das Mikrofon den Pegelabfall misst.
> Das identifiziert die Quelle objektiv; du musst nur einen Finger hinhalten.

Also saß ich da und habe Lautsprecherschlitze mit dem Finger abgedichtet, während ein Ton lief und ein Skript die Differenz aufzeichnete.
Nebenbei: Es fühlte sich leicht albern an.
Es funktionierte trotzdem, weil ein abgedeckter Lautsprecher messbar leiser wird und ein Mikrofon nun mal keine eigene Meinung hat.

Diese Abfolge möchte ich hervorheben, denn sie ist das, was ich wirklich beeindruckend fand — nicht nur ein einzelner cleverer Schritt, sondern die logische *Richtung*, in der sich unsere Erkenntnisse entwickelten:

1. **„Sag mir, was du hörst.“** — unzuverlässig, und das haben wir schnell herausgefunden.
2. **„Halt die Hand über diese Öffnung.“** — grob und handfest, aber für Claude objektiv messbar.
3. **„Hier ist ein tonselektiver Analysator; das Mikrofon liefert die Antwort.“** — wiederholbar, mit Zahlen.

Jeder Schritt hat mich als „Bioware“ aus der Messung weiter herausgenommen.
So sieht echter Fortschritt bei so einem Problem aus.
Allein wäre ich nicht so weit gekommen.

## Sich öffentlich irren — und es korrigieren

Nun wussten wir: Es gibt keinen dritten Breitbandlautsprecher.
Der dritte Schallwandler ist ein Tieftöner am Lüftungsschlitz auf der Unterseite, hinten rechts — 45 dB leiser und bei 6 kHz stumm.
Genau deshalb klang er wie „ein leiser Lautsprecher auf dem linken Kanal“.
Und die Einstellung, auf der mein erster Vorschlag im Upstream-Issue beruhte, ist nicht wirkungslos, wie ich dachte, sondern schädlich:
Meine Beobachtung hatte nur den rechten vorderen Lautsprecher im Blick, und wenn man diese Einstellung auf null setzt, verstummt der linke vordere Lautsprecher komplett.

Das Issue, das ich upstream veröffentlicht hatte, war also falsch, und schlimmer noch: Wer ihm gefolgt wäre, hätte sein Audio verschlechtert.
Also habe ich es zurückgezogen.
Oben einen Warnhinweis eingefügt, der ursprüngliche Text darunter blieb weiterhin sichtbar, und darunter die aktuell gemessenen Ergebnisse als Kommentar eingefügt.

Mir wäre lieber gewesen, recht zu haben.
Aber viel lieber lasse ich mich an einem Nachmittag von einer Messung korrigieren als in sechs Monaten vom Bugreport eines Fremden.

## Die Pause gehört zur Methode

In Claude Code gibt es ein Nutzungslimit, das sich in einem Fünf-Stunden-Fenster erneuert.
Zum ersten Mal daran zu stoßen fühlte sich für mich an wie eine Vollbremsung.
Es war jedoch eine der besten Erfahrungen, die ich in dieser Claude-Session gemacht habe.

Das Problem stand nicht mehr zum Herumstochern bereit, also habe ich aufgehört zu stochern und angefangen nachzudenken.
In die nächste Sitzung mit Claude bin ich mit einer konkreten neuen Idee gegangen statt mit einer weiteren Variante des zuletzt Versuchten.

Das ist deshalb wichtig, weil Werkzeuge, die sofort antworten, uns dazu verleiten können, sofort weiter zu fragen, statt erst einmal weiter nachzudenken.
So sind wir Menschen sozial konditioniert, und einer agentischen AI nicht sofort zu antworten, fühlt sich erst einmal komisch an.

Eine erzwungene Pause erweist sich aber als durchaus sinnvoll bei einem Problem, das man noch nicht verstanden hat — und anders als bei einem menschlichen Gegenüber setzt die Sitzung exakt dort wieder an, wo sie aufgehört hat, mit vollständigem Kontext.
Nichts musste Claude neu erklärt werden.

## Die Kontrolle behalten

Ein Vorbehalt, den ich im Zusammenhang mit agentischer AI oft höre, lautet sinngemäß: *Ich lasse AI doch keine Befehle auf meinem Rechner ausführen!*
Diese Sorge verdient eine klare Antwort statt Beschwichtigung.

Ich hatte in diesem Projekt anfangs drei Bedenken: Es würde Administratorrechte brauchen, es könnte etwas irreversibel kaputtmachen und ich war mir nicht sicher, was den Rechner an Daten verlässt.

Aufgelöst hat diese Bedenken nicht blindes Vertrauen in Claude, sondern dass die Kontrolle ausdrücklich vorhanden und einstellbar ist.
Ich habe im **Plan-Modus** gearbeitet: Claude Code legt dar, was es vorhat und warum, und nichts wird ausgeführt, bevor ich es freigebe.
Bei den Routineschritten ist das leicht zu entscheiden und kann bei erneutem Vorkommen in der Session auch automatisiert werden.
Bei denen jedoch, die mit Administratorrechten an Hardware-Registern arbeiten, habe ich Claudes Plan sehr sorgfältig gelesen.
Ich konnte das jederzeit strenger oder lockerer stellen, und ich konnte abbrechen.

Der Moment in dieser Sitzung, der am meisten für mein Vertrauen getan hat, ist folgender.
Spät in der Sitzung wurde der linke Lautsprecher erst sehr laut und dann stumm und kam nicht zurück.
Ungefragt schrieb Claude Code das hier:

> Ich sollte zu meinem Anteil offen sein: Um messbare Pegel zu bekommen, habe ich den Signalweg mit seinem kalibrierten Maximum und anhaltenden Vollpegel-Sinustönen betrieben, was lauter und härter ist als deine normale Nutzung —
> ich kann das also nicht als Mitursache ausschließen.

Anschließend hat es auch die Belege für die Gegenrichtung aufgeführt — der Verstärker meldete weder Überstrom noch Übertemperatur noch Clipping-Fehler.
Nach einem Neustart des Rechners war der Lautsprecher übrigens wieder da und ist seitdem stabil.

Ein Assistent, der proaktiv auf seinen möglichen eigenen Anteil an einem akuten Problem hinweist, ist nützlicher als einer, der einen nie beunruhigen möchte und deshalb Informationen vorenthält.
Die Angst vor einem Kontrollverlust bei der lokalen Nutzung von agentischer AI empfinde ich als unbegründet.
Denn Kontrolle ist zuerst eine Frage der Haltung zum Problem, die man selbst in der Hand hat.
Die technischen Risiken sind zwar real, aber beherrschbar, wenn man zuerst den Plan liest und sich dann entscheidet.

## Was ich gelernt habe

1. **Ein sicherer Eindruck ist kein Beleg.**
   Meine Ohren gaben in jedem Durchlauf eine andere Antwort und waren sich jedes Mal sicher.
2. **Frag, was du messen kannst, bevor du entscheidest, was du änderst.**
   Potenzielle Tage gemeinsamen Theoretisierens wurden ersetzt durch einen Nachmittag gemeinsames Messen.
3. **Ein Messinstrument darf gerne improvisiert werden.**
   Ein eingebautes Mikrofon, ein Testton und reines Python haben Laborausrüstung ersetzt, die ich nicht besitze.
4. **Eine falsche Schlussfolgerung zu veröffentlichen ist reparierbar.**
   Sie klar zurückzuziehen kostet letztendlich weniger, als sie öffentlich stehen zu lassen.
5. **Gönne dir bewusst Pausen bei der Arbeit mit AI!**
   Die erholsame Pause hat mir eine neue Idee geschenkt und die Bildschirmzeit danach hat neue Varianten der Fehlersuche gebracht.
6. **Gib den Plan frei, nicht nur das Ergebnis.**
   Zu lesen, was passieren wird, bevor es passiert, und dann entscheiden — dort sitzt die Kontrolle tatsächlich.

## Falls du noch unschlüssig bist

Du musst dafür kein Entwickler sein.
Diesen Ton-Analysator hätte ich nicht so schnell in Python schreiben können wie Claude, und ich musste es auch nicht — ich musste nur ein Symptom genau beschreiben und ausführen, worum ich von Claude gebeten wurde.
Und einen Finger auf ein Lautsprecherloch legen, der sich in diesem Moment als das beste verfügbare Instrument herausstellte. :-)

Wenn du ein Gerät hast, an dem etwas irgendwie kaputt ist — ein Lautsprecher, ein Sensor, ein Lüfter, der nie anläuft, irgendeine Funktion, die klammheimlich aufgehört hat zu funktionieren —,
dann ist es doch so: Solche Probleme sind meist *lösbar*, es lohnte sich bisher nur für niemanden, sie selbst zu lösen.
Diese Rechnung hat sich klar erkennbar geändert.
Nicht weil die Unterstützung durch agentische AI unfehlbar wäre.
Meine hat mir anfangs geholfen, eine Theorie über das Problem zu bauen, die sich später als falsch erwies.
Die Rechnung hat sich geändert, weil die Schleife von „da stimmt was nicht“ hin zu „hier ist etwas Solides mit Zahlen“ kurz genug geworden ist, um sie tatsächlich auch zu gehen.
Danke dafür, Claude!

Fang beim Symptom an.
Frag, was sich messen ließe.
Lies den Plan, bevor du ihn freigibst.
