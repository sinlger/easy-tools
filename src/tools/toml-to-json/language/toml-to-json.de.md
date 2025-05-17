# TOML zu JSON Online-Konverter Benutzerdokumentation

## 1. Einführung des Tools

TOML zu JSON ist ein praktisches Online-Tool, das Daten im TOML-Format analysiert und in das JSON-Format konvertiert. Benutzer können TOML-Daten einfach in das linke Eingabefeld einfügen oder eingeben, und das entsprechende JSON-Ergebnis wird automatisch im rechten Bereich generiert.

## 2. Detaillierte Funktionsbeschreibung

### 1. Eingabe von TOML-Daten

* Im linken Textfeld "Your TOML" können Benutzer TOML-Daten entweder einfügen oder manuell eingeben. Das Textfeld unterstützt die Eingabe von mehrzeiligem Text und bietet Benutzern ausreichend Platz, um komplexere TOML-Konfigurationsinformationen einzugeben.

### 2. Ausgabe des JSON-Ergebnisses

* Sobald TOML-Daten im linken Textfeld eingegeben wurden, führt das Tool automatisch eine Analyse und Konvertierung durch. Die konvertierten JSON-Daten werden im rechten Textfeld "JSON from your TOML" angezeigt. Benutzer können diese Daten ansehen, kopieren oder weiter verarbeiten.

## 3. Verwendungsschritte

1. Öffnen Sie die Tool-Seite ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. Fügen Sie im linken Textfeld "Your TOML" die zu konvertierenden TOML-Daten ein oder geben Sie sie ein.
3. Das System führt automatisch die Konvertierung durch, und das Ergebnis wird im rechten Textfeld "JSON from your TOML" angezeigt.

## 4. Funktionseigenschaften

* Benutzerfreundlich: Die Oberfläche ist übersichtlich und intuitiv gestaltet, der Bedienablauf ist einfach, es sind keine komplexen Einstellungen oder Konfigurationen erforderlich, sodass Benutzer schnell mit dem Tool arbeiten können.
* Echtzeit-Konvertierung: Nachdem TOML-Daten eingegeben wurden, führt das Tool automatisch die Konvertierung durch und zeigt das Ergebnis an, ohne dass manuell auf einen Konvertierungsbutton geklickt werden muss. Dies erhöht die Effizienz der Konvertierung.
* Online-Nutzung: Es muss keine Software installiert werden. Solange ein internetfähiges Gerät vorhanden ist, kann das Tool jederzeit und überall für die Konvertierung von TOML nach JSON verwendet werden.

## 5. Beispiele

### Beispiel 1: Einfache TOML-zu-JSON-Konvertierung

Angenommen, wir haben folgende TOML-Daten:
```toml
title = "TOML Example"
owner = "John Doe"
```

Wenn wir diese Daten in das linke Textfeld "Your TOML" einfügen, konvertiert das Tool sie automatisch in folgende JSON-Daten:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Beispiel 2: TOML-zu-JSON-Konvertierung mit verschachtelter Struktur

Wir haben komplexere TOML-Daten:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Nach der Eingabe in das Tool erhalten wir folgende JSON-Daten:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}