---
title: "Messen statt raten: Fehlersuche an einem Laptop-Lautsprecher mit Claude Code"
date: 2026-08-31T06:00:00+02:00
draft: false
tags: ["claude-code", "linux", "hardware", "debugging", "audio"]
summary: "Eine falsche Theorie, ein öffentlicher Widerruf und ein kleines Messwerkzeug — was ich darüber gelernt habe, KI-Unterstützung für Probleme einzusetzen, bei denen es überhaupt nicht um Code geht."
---

## Kurzfassung

- In meinem Laptop steckt ein Lautsprecher, den Linux nicht korrekt ansteuert. Jemand anderes
  hatte die eigentliche Tiefenarbeit bereits geleistet; ich bin von seiner Lösung ausgegangen
  und auf meinem Gerät auf ein anderes Problem gestoßen.
- Ich habe mir durch Hinhören eine Theorie gebildet, sie veröffentlicht — und sie war **falsch**.
- Statt darüber zu streiten, was wir da hören, haben Claude Code und ich aus dem eingebauten
  Mikrofon des Laptops ein kleines Messinstrument gebaut. Es hat meine Theorie innerhalb einer
  Stunde widerlegt.
- Ich habe meine veröffentlichte Behauptung zurückgezogen und durch gemessene Fakten ersetzt.
- Der nützliche Teil war nicht die Geschwindigkeit. Es war, dass aus einer vagen Beschwerde —
  „dieser Lautsprecher klingt falsch“ — an einem Nachmittag etwas mit Zahlen wurde, ohne dass
  ich Hardware-Ingenieur bin.
- Ich habe das Ganze in einem Modus laufen lassen, in dem ich den Plan freigebe, bevor
  irgendetwas ausgeführt wird. Die Kontrolle ist ausdrücklich vorhanden — genau deshalb lohnt
  sich ein nüchterner Blick auf die verbreitete Sicherheitssorge.

---

## Der Ausgangspunkt: die Arbeit eines anderen

Der Laptop ist ein Chuwi CoreBook X. Unter Linux bleibt sein linker Lautsprecher ab Werk
stumm. Der Chip, der ihn antreibt — ein AWINIC AW88298 Verstärker, der an einem
undokumentierten Ausgang des Audio-Codecs hängt —, hat keinen Treiber im Mainline-Kernel.

Das habe nicht ich gelöst. **Francisco Montañés García ([@pacomont](https://github.com/pacomont))**
hat es getan, über rund fünf Wochen echter Knochenarbeit: den Chip über I2C abklopfen,
nachweisen, welcher Teil des Systems ihm überhaupt Audio zuspielt, und schließlich
herausfinden, warum jeder Benachrichtigungston mit einem Knacken beginnt. Sein Projektlog ist
[für sich genommen lesenswert](https://github.com/pacomont/chuwi-corebook-x-left-speaker), und
alles Folgende baut darauf auf. Ich habe seinen Daemon installiert, und beide Lautsprecher
liefen.

Dann fiel mir an meinem Gerät etwas auf, das seine Notizen nicht beschrieben — und dort
beginnt mein Teil.

## Eine Theorie, gebaut aus Hinhören

Ton kam aus der linken Kante des Laptops, und zusätzlich von irgendwo rechts. Das legte einen
**dritten** Lautsprecher nahe — einen mittleren —, den seine Lösung versehentlich stummschaltete.

Ich habe es auf die naheliegende Art getestet: Ton abspielen, einen Ausgang nach dem anderen
stummschalten, notieren, was ich höre. Die Ergebnisse wirkten schlüssig. Ich habe das
aufgeschrieben und als Issue im Upstream-Projekt eingereicht, samt Änderungsvorschlag, damit
andere Besitzer ihren mittleren Lautsprecher zurückbekommen.

Das Problem: Ich hatte eine Schlussfolgerung mit meinen Ohren gebaut und keine Vorstellung
davon, was für ein schwaches Instrument das ist.

## Ohren sind kein Messgerät

Als wir das Verhalten präzise festnageln wollten, hörten die Ergebnisse auf, zueinander zu
passen. Ein Testdurchlauf über sechs Konfigurationen brachte von mir das hier hervor:

> Stille, rechts, Stille, rechts, Stille, Stille, rechts

Noch einmal durchlaufen lassen — und es kam etwas anderes heraus. Zwei der Lautsprecher sitzen
auf dem Mainboard dicht beieinander, „von welcher Seite kommt das gerade?“ ist also eine Frage,
die mein Gehör schlicht nicht beantworten konnte. Jeder Durchlauf lieferte eine Antwort, die
sich sicher anfühlte, und die sicheren Antworten widersprachen einander.

Claude Code hat das angesprochen, statt weiter meine Meldungen einzusammeln:

> Die Höreindrücke widersprechen sich von Durchlauf zu Durchlauf. Ich höre auf, mich darauf zu
> stützen.

Dieser Satz ist im Grunde der ganze Beitrag. Das Scheitern lag nicht an mangelnder Mühe. Es
lag daran, dass wir mit dem falschen Instrument gemessen haben — und daran hätte auch noch so
sorgfältiges Hinhören nichts geändert.

## Stattdessen: ein Instrument bauen

Der erste Ansatz war direkt: die eingebauten Mikrofone des Laptops aufzeichnen, während jeder
Kanal spielt, und die Pegel vergleichen. Das hat fast funktioniert, aber das Grundrauschen des
Mikrofons hat den leisen Lautsprecher überdeckt.

Also wurde der Ansatz geschärft. Statt Lautstärke im Allgemeinen zu messen, misst man den
*konkret abgespielten Ton* und ignoriert alles andere — ein Goertzel-Filter, der sich auf eine
Frequenz einrastet und den Rest verwirft. Zwei Frequenzen kamen zum Einsatz: 1 kHz für den
Pegel und 6 kHz für eine ganz andere Frage — *kann dieser Lautsprecher überhaupt hohe
Frequenzen erzeugen?*

Eine Anmerkung dazu, wie unspektakulär das war: numpy war in der Umgebung nicht
installiert, also wurde die Analyse in reinem Python geschrieben. Keine Laborausrüstung.
Ein Laptop-Mikrofon, ein Testton und ungefähr vierzig Zeilen Rechnerei.

Die Ergebnisse waren sofort brauchbarer als alles, was ich gehört hatte:

| Abgespielt | Pegel bei 1 kHz | Irgendwas bei 6 kHz? |
|---|---|---|
| Rechter Kanal | +60 dB über Grundpegel | Ja |
| Linker Kanal | +15 dB über Grundpegel | **Nichts** |

45 dB Unterschied, und ein Ausgang, der überhaupt keine Höhen produziert. Das ist kein
Stereopaar. Das ist ein Breitbandlautsprecher und ein Tieftöner.

## Der Teil, in dem ich den Finger drauflege

Eine Frage blieb: *Wo* sitzt dieser leise, dumpfe Lautsprecher eigentlich physisch? Die
Stereotrennung des Mikrofonarrays war zu schlecht, um das zu sagen.

Statt dagegen anzukämpfen, schlug Claude Code eine Methode vor, die ohne Ortung auskommt:

> Du deckst eine Öffnung nach der anderen ab, während das Mikrofon den Pegelabfall misst. Das
> identifiziert die Quelle objektiv; du musst nur einen Finger hinhalten.

Also saß ich da und habe Lautsprecherschlitze mit der Fingerkuppe abgedichtet, während ein Ton
lief und ein Skript die Differenz aufzeichnete. Es fühlte sich leicht albern an. Es
funktionierte trotzdem, weil ein abgedeckter Lautsprecher messbar leiser wird und das Mikrofon
keine Meinung hat.

Diese Abfolge möchte ich hervorheben, denn sie ist das, was ich wirklich beeindruckend fand —
nicht ein einzelner cleverer Schritt, sondern die *Richtung*:

1. **„Sag mir, was du hörst.“** — unzuverlässig, und das haben wir herausgefunden.
2. **„Halt die Hand über diese Öffnung.“** — grob, aber objektiv.
3. **„Hier ist ein tonselektiver Analysator; das Mikrofon liefert die Antwort.“** — wiederholbar, mit Zahlen.

Jeder Schritt hat mich aus der Messung weiter herausgenommen. So sieht Fortschritt bei so
einem Problem aus, und allein wäre ich nicht dorthin gekommen.

## Sich öffentlich irren — und es korrigieren

Die Messungen sagten: Es gibt keinen mittleren Lautsprecher. Der leise Ausgang ist ein
Tieftöner unter dem Gehäuse. Und die konkrete Einstellung, auf der mein Lösungsvorschlag
beruhte, tut auf diesem Codec schlicht gar nichts.

Mein veröffentlichtes Issue war falsch, und schlimmer noch: Wer ihm gefolgt wäre, hätte sein
Audio verschlechtert. Also habe ich es zurückgezogen — ein Warnhinweis oben, der ursprüngliche
Text darunter weiterhin sichtbar, und an seiner Stelle die gemessenen Ergebnisse.

Mir wäre lieber gewesen, recht zu haben. Aber viel lieber lasse ich mich an einem Nachmittag
von einer Messung korrigieren als in sechs Monaten vom Bugreport eines Fremden.

## Die Pause gehört zur Methode

In Claude Code gibt es ein Nutzungslimit, das sich in einem Fünf-Stunden-Fenster erneuert.
Da anzustoßen fühlte sich an wie eine Vollbremsung. In der Praxis war es jedoch eine der
nützlichen Erfahrungen, die mir in dieser Claude-Session widerfahren sind.

Das Problem stand nicht mehr zum Herumstochern bereit, also habe ich aufgehört zu stochern und
angefangen nachzudenken. In die nächste Sitzung bin ich mit einer konkreten neuen Idee
gegangen statt mit einer weiteren Variante des zuletzt Versuchten.

Das ist deshalb wichtig, weil Werkzeuge, die sofort antworten, dazu verleiten, weiter zu
fragen statt weiter zu denken. Eine erzwungene Lücke erweist sich als durchaus sinnvolle
Eigenschaft bei einem Problem, das man noch nicht verstanden hat — und anders als bei einem
menschlichen Gegenüber setzt die Sitzung exakt dort wieder an, wo sie aufgehört hat, mit
vollständigem Kontext. Nichts musste neu erklärt werden.

## Zur Kontrolle, ganz nüchtern

Der Vorbehalt, den ich am häufigsten höre, lautet sinngemäß: *Ich lasse doch keine KI Befehle
auf meinem Rechner ausführen.* Diese Sorge verdient eine klare Antwort statt Beschwichtigung.

Ich hatte drei Bedenken: Es würde Administratorrechte brauchen, es könnte etwas irreversibel
kaputtmachen, und ich war mir nicht sicher, was den Rechner verlässt.

Aufgelöst hat die nicht blindes Vertrauen in Claude, sondern dass die Kontrolle
ausdrücklich vorhanden und einstellbar ist. Ich habe im **Plan-Modus** gearbeitet: Claude
Code legt dar, was es vorhat und warum, und nichts wird ausgeführt, bevor ich es freigebe.
Bei den Routineschritten ist das eine Formalität. Bei denen jedoch, die mit
Administratorrechten an Hardware-Registern arbeiten, habe ich sehr sorgfältig gelesen. Ich
konnte das jederzeit strenger oder lockerer stellen, und ich konnte abbrechen.

Der Moment, der am meisten für mein Vertrauen getan hat, ist allerdings kein beruhigender.
Spät in der Sitzung wurde der linke Lautsprecher stumm und kam nicht zurück. Ungefragt schrieb
Claude Code das hier:

> Ich sollte zu meinem Anteil offen sein: Um messbare Pegel zu bekommen, habe ich den Signalweg
> mit seinem kalibrierten Maximum und anhaltenden Vollpegel-Sinustönen betrieben, was lauter und
> härter ist als deine normale Nutzung — ich kann das also nicht als Mitursache ausschließen.

Anschließend hat es die Belege für die Gegenrichtung aufgeführt — der Verstärker meldete weder
Überstrom noch Übertemperatur noch Clipping-Fehler. (Nach einem Neustart war der Lautsprecher
wieder da und ist seitdem stabil.)

Ein Assistent, der auf seinen möglichen eigenen Anteil an einem Problem hinweist, ist
nützlicher als einer, der einen nie beunruhigt. Die Angst vor einem Kontrollverlust bei
der lokalen Nutzung von AI würde ich unbegründet nennen, denn Kontrolle ist eine
Einstellung, die man selbst wählt. Die Risiken selbst sind real, beherrschbar — und Grund
genug, den Plan zu lesen.

## Was ich gelernt habe

1. **Ein sicherer Eindruck ist kein Beleg.** Meine Ohren gaben in jedem Durchlauf eine
   andere Antwort und waren sich jedes Mal sicher.
2. **Frag, was du messen kannst, bevor du entscheidest, was du änderst.** Potenzielle Tage
   des Theoretisierens wurden ersetzt durch einen Nachmittag Messen.
3. **Das Instrument darf gerne improvisiert werden.** Ein eingebautes Mikrofon, ein
   Testton und reines Python haben Ausrüstung ersetzt, die ich nicht besitze.
4. **Eine falsche Schlussfolgerung zu veröffentlichen ist reparierbar.** Sie klar
   zurückzuziehen kostet weniger, als sie stehen zu lassen.
5. **Gönne dir bewusst Pausen bei der Arbeit mit AI!** Die erholsame Pause hat mir eine
   neue Idee gebracht; die Bildschirmzeit danach hat neue Varianten der Fehlersuche
   gebracht.
6. **Gib den Plan frei, nicht nur das Ergebnis.** Zu lesen, was passieren wird, bevor es
   passiert — dort sitzt die Kontrolle tatsächlich.

## Falls du noch unschlüssig bist

Du musst dafür kein Entwickler sein. Diesen Analysator hätte ich nicht so schnell
schreiben können wie Claude, und ich musste es auch nicht — ich musste ein Symptom genau
beschreiben, ausführen, worum ich gebeten wurde, und einen Finger auf ein Lautsprecherloch
legen, als sich das als bestes verfügbares Instrument herausstellte.

Wenn du ein Gerät hast, an dem etwas irgendwie kaputt ist — ein Lautsprecher, ein Sensor,
ein Lüfter, der nie anläuft, irgendeine Funktion, die klammheimlich aufgehört hat zu
funktionieren —, dann ist die ehrliche Lage: Solche Probleme sind meist *lösbar*, es
lohnte sich bisher nur für niemanden, sie selbst zu lösen. Diese Rechnung hat sich
geändert. Nicht weil die Unterstützung unfehlbar wäre; meine hat mir geholfen, eine
Theorie zu bauen, die sich als falsch erwies. Sie hat sich geändert, weil die Schleife von
„da stimmt was nicht“ zu „hier sind die Zahlen“ kurz genug geworden ist, um sie
tatsächlich zu gehen. Danke Claude dafür!

Fang beim Symptom an. Frag, was sich messen ließe. Lies den Plan, bevor du ihn freigibst.
