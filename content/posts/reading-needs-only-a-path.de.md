---
title: "Lesen braucht nur einen Pfad: Wofür ein Agent mit Shell ein MCP braucht und wofür nicht"
date: 2026-09-24T18:00:00+02:00
tags: ["claude-code", "mcp", "linux", "privacy", "workflow", "Field Notes"]
themen: ["daten"]
summary: "Ich wollte wissen, ob eine Support-Anfrage erledigt ist, und Claude beantwortete es aus neun Jahren Mail, ohne das Postfach im Netz anzufassen. Das Ticket schließen konnte es danach nicht. Dieselbe Sitzung zeigt, wo die Grenze zwischen Shell und MCP verläuft: zwischen Lesen und Handeln."
---

## Kurzfassung

- Ein Agent mit Shell liest, was auf der Platte liegt, und dort liegt viel: Mail, Browserverlauf, Notizen, Konfiguration.
  Dafür braucht er nur einen Pfad, kein Passwort und kein MCP.
- An einem Tag beantwortete Claude eine Frage an mein Postfach allein aus Thunderbirds lokaler Kopie.
  1203 Nachrichten aus fast neun Jahren, durchsucht in Sekunden, ohne eine Verbindung zum Mailserver.
- Im selben Auftrag sollte es das Ticket schließen, und das ging nicht.
  Senden und Klicken brauchen Zugangsdaten, eine Sitzung oder eine API.
- Die Grenze verläuft zwischen Lesen und Handeln.
  Ein MCP hätte hier das Senden gekonnt, das Lesen hätte es nicht besser gemacht.

## Eine Frage an das Postfach

Ich hatte bei GitHub eine Support-Anfrage zu einer Aufräumarbeit an einem Repository gestellt.
Die Antworten kamen per Mail, und irgendwann wusste ich nicht mehr, ob die Sache erledigt war.
Also fragte ich Claude Code, ob die Anfrage in meinem Gmail-Postfach abgeschlossen sei.

Claude hat keinen Zugang zu Gmail.
Es gibt in dieser Umgebung kein MCP für Mail, also keinen Dienst, über den ein Agent nach einem festen Protokoll mit einem Postfach sprechen könnte.
Es gibt aber Thunderbird, und Thunderbird hält eine vollständige Kopie des Postfachs auf der Platte.

## Der Leseweg

Die erste Annahme war falsch.
Das Profil lag nicht dort, wo Thunderbird es klassisch ablegt, und auch nicht unter dem Namen, den die Flatpak-App früher trug.
Sie heißt inzwischen `net.thunderbird.Thunderbird`, gefunden hat Claude das mit `flatpak list`.

Die zweite Stelle, an der man hängen bleibt, ist `profiles.ini`.
Das Profil, das dort als Standard markiert ist, war eine leere Hülle vom Tag der Installation.
Welches Profil Thunderbird wirklich benutzt, stand in einem anderen Abschnitt derselben Datei.

Danach war es Handwerk.
In `prefs.js` führt eine Kette von Einträgen vom Konto über die Identität zur Adresse und vom Konto über den Server zum Ordner.
Erst diese Kette belegt, welcher Ordner zu welcher Adresse gehört.
Der Ordner selbst ist eine mbox, eine einzige Textdatei mit allen Nachrichten hintereinander, hier 80 MB groß.

`grep` gab die Größenordnung: 1203 Nachrichten, zwei relevante Absender.
Die eigentliche Auswertung lief über das Modul `mailbox` aus Pythons Standardbibliothek.
Zwei Fallen gab es dabei: Umlaute im Betreff stehen kodiert im Kopf und müssen erst dekodiert werden, und der Text einer Nachricht ist oft Base64, solange man ihn nicht ausdrücklich mit seinem Zeichensatz auspackt.

Nicht passiert ist dabei eine Verbindung zum Mailserver.
Claude hat kein Passwort gebraucht und Thunderbirds Passwortspeicher nicht angefasst, es hat keine Erweiterung installiert und kein MCP benutzt.
Es hat Dateien gelesen.

Die Mail war allerdings nur die Quelle und noch nicht der Beweis.
Ob die Aufräumarbeit wirklich erledigt war, belegte erst ein `curl` auf die alten Adressen: 404 über die Webseite, 422 über die API.

## Wo es aufhörte

Im selben Auftrag sollte das Ticket geschlossen werden.
Das ging nicht.

Für eine Antwort per Mail fehlte ein Weg nach draußen.
Auf dem Rechner läuft kein Mailserver, der verschicken könnte, und Claude hätte das Gmail-Passwort aus Thunderbirds Speicher holen müssen.
Das war keine Option.

Das Support-Portal im Browser zu bedienen ging auch nicht.
Die Browsersteuerung war in dieser Sitzung nicht verfügbar, und das Portal hat keine API.
Das Token, mit dem Claude sonst über `gh` bei GitHub arbeitet, half nicht, weil die Tickets in einem anderen System liegen.

Neun Jahre Postfach in Sekunden durchsucht, und keine Zeile hinausgeschickt.
Das Ticket habe ich von Hand geschlossen.

## Die Grenze zwischen Lesen und Handeln

Aus diesem Tag ist mir eine Unterscheidung im Gedächtnis geblieben.
Sie trennt die Aufgaben nach ihrer Richtung, einfache und schwierige kommen auf beiden Seiten vor.

**Lesen braucht nur einen Pfad.**
Fast jedes Programm legt seinen Zustand in Dateien ab, deren Format dokumentiert ist: mbox, SQLite, JSON, INI, Markdown.
Dazu kommen Werkzeuge, die ohnehin angemeldet sind, bei mir `gh` und `git`, und `curl` auf öffentliche Adressen.
Browser führen ihren Verlauf zum Beispiel in einer SQLite-Datei, und für Kalender und Notizprogramme gilt Ähnliches.
Vorgeführt habe ich es für diesen Beitrag nur am Postfach.

**Handeln nach außen braucht mehr**, und dort verdient ein MCP sein Geld:

- Wo Zugangsdaten zu einem fremden Dienst nötig sind, die man nicht aus dem Passwortspeicher eines anderen Programms holen will.
- Wo in den Zustand eines laufenden Programms geschrieben wird: Thunderbirds Index zu lesen ist unbedenklich, ihn zu verändern riskant.
- Wo ein Dienst keine lokale Spur hat, weil er nur hinter einer Weboberfläche existiert.
- Wo ein fester Vertrag besser ist als ein erratenes Format.

Das ist keine Kritik an MCPs.
Sie sind für das Handeln gebaut, für das Nachsehen braucht ein Agent mit Shell sie selten.

## Die unbequeme Seite

Der Leseweg ist kein Trick und keine Sicherheitslücke.
So arbeitet ein Werkzeug, das im eigenen Benutzerkonto läuft: Es kommt an alles, woran ich auch komme.
Genau deshalb gehört es ausgesprochen.

Der Umfang gehört dazu.
Auf eine beiläufige Frage hin lagen 1203 Nachrichten von November 2017 bis September 2026 offen, vollständig durchsuchbar.
Wo meine Notizen hingehen dürfen, habe ich in [Auch privat wird kopiert](/de/posts/private-still-means-copied/) beschrieben.
Hier ging es um die andere Richtung: woran ein lokaler Agent ohnehin herankommt.

Und die Kopie auf der Platte ist nicht das Postfach auf dem Server.
Was nie synchronisiert wurde, fehlt in ihr, und gelöschte Nachrichten können eine Weile liegen bleiben.
Nachgesehen hat Claude das in diesem Fall: Von den 1203 Nachrichten trugen 639 überhaupt ein Statusfeld, und bei keiner stand es auf gelöscht.

## Was ich daraus mitnehme

- Bevor ich einen Agenten an einen Dienst anschließe, frage ich, ob der Dienst schon eine Spur auf meiner Platte hinterlässt.
  Oft tut er das.
- Lesen und Handeln sind verschiedene Fragen.
  Das eine braucht einen Pfad, das andere Zugangsdaten, und die will ich bewusst vergeben.
- Ein MCP lohnt sich dort, wo der Agent etwas tun soll, das ich sonst von Hand tue.
- Was der Agent lesen kann, ist ungefähr alles, was ich lesen kann.
  Das ist praktisch, und es ist der Grund, genauer hinzusehen.
