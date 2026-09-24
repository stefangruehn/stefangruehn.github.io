---
title: "Erst der Restore macht das Backup: Ein Agent sichert die Umgebung, in der er läuft"
date: 2026-09-24T07:00:00+02:00
tags: ["claude-code", "disaster-recovery", "workflow", "linux", "privacy", "Field Notes"]
themen: ["daten"]
summary: "Ich habe Claude die Sicherung genau der Arbeitsumgebung bauen lassen, in der es selbst läuft: Projekte, sein Gedächtnis, seine eigenen Sitzungsprotokolle. Das Backup war schnell geschrieben. Was es taugt, zeigte erst der Restore in eine leere Maschine, und die Fehler, die er fand, hatte kein Entwurf vorhergesehen."
---

## Kurzfassung

- Ich habe einen Agenten die Sicherung der Umgebung bauen lassen, in der er selbst arbeitet: Projekte, sein Gedächtnis, seine eigenen Sitzungsprotokolle.
- Das Archiv enthält auch die Sitzung, die es gebaut hat.
  Ihr Protokoll wuchs weiter, während es gepackt wurde.
- Die erste Probe, ein Entpacken in einen Nebenordner, war vollständig grün.
  Erst die zweite, in einen leeren Container, fand zwei abweichende Dateien: Das frisch installierte Claude Code hatte die Wiederherstellung verändert, bevor sie geprüft war.
- Die Passphrase ging nie durch den Agenten, und die SSH-Schlüssel darf er nicht lesen.
  Wie sie gesichert werden, hat er trotzdem gebaut und getestet.
- Einen Fehler fand nur die Benutzung, einen anderen nur die Überlegung.
  Vorhergesehen hatte beide kein Entwurf.

## Das Archiv, in dem es selbst steckt

Mein Rechner hat ein Systembackup.
Was fehlte, war eine Sicherung, mit der ich nach einer Neuinstallation sofort weiterarbeiten kann: die Projekte, das Arbeitsverzeichnis von Claude Code mit seinem Gedächtnis und allen Sitzungsverläufen, die Obsidian-Vaults, die Dotfiles und zuletzt auch die SSH- und GPG-Schlüssel.

Entworfen, gebaut und getestet hat das Claude, zuerst in einem Interview, dann in zwei Skripten.
Eines packt und verschlüsselt, das andere stellt wieder her, dazu kommt eine Anleitung für den Ernstfall.
Gezählt am 24. September umfasst die Sicherung 9929 Dateien, verschlüsselt 384 MiB.

Das Seltsame an dieser Aufgabe zeigt sich beim ersten echten Lauf.
Unter den Dateien, die gesichert werden, liegt das Protokoll der Sitzung, in der Claude das Skript geschrieben hat.
Diese Sitzung lief noch, als ich das Skript in einem eigenen Terminal startete, und sie schrieb weiter.
Für `tar` ist das eine Datei, die sich beim Lesen geändert hat.
Das Skript wertet es als Warnung, und das Manifest des Archivs vermerkt: „1 claude process(es) were running while packing“.

Die Sicherung enthält dieses Protokoll also bis zu der Zeile, an der `tar` es gerade las.
Für ein Backup ist das in Ordnung, die nächste Generation hat den Rest.
Es zeigt aber früh, worum es in diesem Beitrag geht: Dass ein Archiv entstanden ist, sagt noch nichts darüber, was aus ihm wieder wird.

## Die Passphrase geht nicht durch den Agenten

Verschlüsselt wird symmetrisch mit gpg, die Passphrase liegt in meinem Passwortmanager.
Sie geht nie durch Claude.
Jeder echte Lauf findet in meinem eigenen Terminal statt: Claude schreibt die Handgriffe hin, ich führe sie aus, danach prüft Claude die Ergebnisse auf der Platte.
Für seine eigenen Tests nimmt es eine Wegwerf-Passphrase aus einer Datei.

Bei den Schlüsseln geht das einen Schritt weiter.
Eine Regel in den Einstellungen von Claude Code verbietet ihm, `~/.ssh` zu lesen.
Es sollte die Schlüssel also sichern, ohne sie je zu sehen.
Getestet hat es das an einem künstlichen Home mit Test-Schlüsseldateien: ob sie im Archiv landen und ob sie mit den richtigen Rechten zurückkommen.
Die echten hat es nicht gelesen.

## Zwei Proben, eine grün

Die erste Probe entpackte das Archiv in einen Nebenordner und verglich jede Datei mit ihrer Prüfsumme.
Alles stimmte, alle Repositories standen auf dem gesicherten Commit, die Version von Claude Code war dieselbe.

Damit war belegt, dass Verschlüsseln, Entpacken und Prüfen tragen.
Der Ernstfall war es nicht: ein leeres Home, in dem Pfade, Rechte und die Neuinstallation wirklich greifen müssen.

Ein Wegwerf-Benutzer taugt dafür nicht.
Claude Code legt die Ordner für Gedächtnis und Verläufe unter dem absoluten Pfad des Projekts ab, der Benutzername steht also im Ordnernamen.
Unter einem anderen Namen fänden die Erinnerungen nicht zu ihren Projekten, und das Restore-Skript lehnt jedes Home ab, das nicht dem gesicherten entspricht.
Die zweite Probe lief deshalb in einem Container: ein frisches System derselben Distribution, derselbe Benutzername, ein leeres Home.

Diesmal wichen zwei Dateien ab.
Die Konfigurationsdatei von Claude Code war verändert, und in seinem Ordner für eigene Sicherungskopien fehlte ein Eintrag.

Die Ursache lag in der Reihenfolge.
Das Skript bot an, Claude Code zu installieren, bevor es die Prüfsummen verglich.
Die Rückfrage wurde bestätigt, der Installer lief und fasste genau diese beiden Dateien an.
Das Werkzeug, das wiederhergestellt werden sollte, hatte die Wiederherstellung verändert, bevor sie geprüft war.
Den Beleg lieferte die erste Probe: Aus demselben Archiv, ohne Installer, hatten alle Dateien gestimmt.

Die Reparatur ist eine andere Reihenfolge, erst prüfen, dann installieren.
Die Wiederholung im Container war danach vollständig grün.

Am selben Prüfbericht fiel noch etwas auf.
Er erklärte die Abweichung als „expected for files kept by --skip-existing“, obwohl diese Option gar nicht gesetzt war.
Eine Meldung, die einen Fehler wegerklärt, führt weiter in die Irre als gar keine.
Sie erscheint jetzt nur noch, wenn die Option wirklich gesetzt ist.

## Was nur die Benutzung fand

Beim ersten echten Lauf öffnete gpg seinen Dialog für die Passphrase.
Er ist modal: Solange er offen ist, lässt sich kein anderes Fenster bedienen, auch der Passwortmanager nicht, in dem die Passphrase liegt.
Wer sie nicht vorher in die Zwischenablage kopiert hat, kommt nicht an sie heran, solange der Dialog wartet.

Das stand in keinem Entwurf, und Claudes Tests konnten es nicht zeigen, weil sie die Passphrase aus einer Datei lasen und nie einen Dialog öffneten.
Es kam aus der Benutzung.
Jetzt halten beide Skripte vor dem ersten Aufruf von gpg an und sagen, dass die Passphrase in die Zwischenablage gehört.

## Was nur die Überlegung fand

Den umgekehrten Fall gab es auch.
gpg legt beim ersten Aufruf sein eigenes Konfigurationsverzeichnis im Home an.
Auf einer frischen Maschine passiert das beim Entschlüsseln des Archivs, also bevor das gesicherte Verzeichnis zurückkommt.
Dann kollidiert beides: Das Restore-Skript findet eine Datei, die es schon gibt, und bricht ab.

Keine Probe hat diesen Fehler gezeigt, weil die Schlüssel erst nach den Proben in den Umfang kamen.
Gefunden hat ihn die Frage, was gpg auf einer leeren Maschine als Erstes tut.
Behoben ist er mit einem Wegwerf-Verzeichnis für gpg im Arbeitsordner des Skripts, geprüft am künstlichen Home.

Zu den Schlüsseln gehört noch eine Kleinigkeit mit Folgen.
Das Archiv enthält nur Dateien, keine Verzeichnisse.
Die Dateien kommen mit ihren Rechten zurück, die Schlüsselordner aber entstehen beim Entpacken neu und sind dann für andere Benutzer lesbar.
Das Restore-Skript setzt ihre Rechte jetzt nachträglich.

## Was ich daraus mitnehme

- Ein Backup ist eine Behauptung.
  Belegt ist es erst durch einen Restore unter den Bedingungen, für die es gedacht ist, und das heißt: in eine leere Maschine.
- Die erste grüne Probe war nicht falsch.
  Sie prüfte nur, woran ohnehin am wenigsten zu zweifeln war.
- Wer das Werkzeug sichert, mit dem er arbeitet, muss damit rechnen, dass es beim Wiederherstellen mitredet.
  Erst prüfen, dann installieren.
- Ein Agent kann sichern, was er nicht sehen darf.
  Er braucht dafür eine Attrappe, an der er testen kann, und einen Menschen, der den echten Lauf macht.
- Die Fehler kamen aus drei Richtungen: aus der Probe, aus der Benutzung und aus der Überlegung.
  Keine davon hätte allein gereicht.
