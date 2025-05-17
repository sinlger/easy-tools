# TOML to YAML Konverter Benutzerdokumentation

## Überblick

TOML to YAML ist ein Online-Tool, das es Benutzern ermöglicht, TOML (Tom's Obvious, Minimal Language)-Konfigurationsdateien einfach in YAML (YAML Ain't Markup Language)-Format zu konvertieren. Dies ist besonders nützlich für Entwickler, die Konfigurationen zwischen verschiedenen Systemen migrieren oder mehrere Technologiestapel integrieren müssen.

## Oberflächendesign

Die Oberfläche des Tools ist einfach und intuitiv gestaltet, mit den folgenden Hauptkomponenten:

1. Linkes Textfeld: Dies ist der Bereich, in den Benutzer ihr TOML-Format-Text eingeben oder einfügen können, gekennzeichnet als "Ihr TOML".
2. Rechtes Textfeld: Wird verwendet, um den konvertierten YAML-Format-Text anzuzeigen, gekennzeichnet als "YAML aus Ihrem TOML".
3. Mittlerer Konvertierungsbutton: Nachdem Benutzer ihren TOML-Text eingegeben haben, können sie diesen Button klicken, um die Konvertierung durchzuführen.

## Funktionsbeschreibung

### Eingabe von TOML-Text

- Benutzer können direkt TOML-formatierten Konfigurationstext in das linke Textfeld eingeben.
- Sie können auch TOML-Text aus anderen Dateien oder Editoren kopieren und in dieses Textfeld einfügen.

### Konvertierungsvorgang

- Nachdem der TOML-Text eingegeben oder eingefügt wurde, klicken Sie auf den mittleren Konvertierungsbutton. Das System analysiert den eingegebenen TOML-Text sofort und konvertiert ihn in YAML-Format.
- Nach Abschluss der Konvertierung wird der resultierende YAML-Text im rechten Textfeld angezeigt.

### Anzeige des YAML-Ergebnisses

- Das rechte Textfeld zeigt den vollständig konvertierten YAML-Text an.
- Hier können Benutzer überprüfen, ob das Konvertierungsergebnis genau ist und ob die Struktur des YAML-Textes ihren Erwartungen entspricht.

### Kopieren des YAML-Textes

- Benutzer können den gesamten YAML-Text im rechten Textfeld auswählen und kopieren, was praktisch ist, um ihn an anderen Orten zu verwenden, z.B. in Konfigurationsdateien einzufügen oder an andere weiterzusenden.

## Beispiele

### Beispiel 1: Grundlegende Konvertierung

**Eingabe im TOML-Format:**

```toml
# Dies ist ein einfaches TOML-Beispiel
title = "TOML Beispiel"

[author]
name = "Zhang San"
age = 28
e-mail = "zhangsan@example.com"
```

**Ausgabe im YAML-Format:**

```yaml
# Dies ist das konvertierte YAML-Beispiel
title: TOML Beispiel

author:
  name: Zhang San
  age: 28
  e-mail: zhangsan@example.com
```

### Beispiel 2: Konvertierung komplexer Strukturen

**Eingabe im TOML-Format:**

```toml
# TOML-Beispiel mit komplexerer Struktur
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**Ausgabe im YAML-Format:**

```yaml
# YAML-Beispiel mit komplexerer Struktur
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Wichtige Hinweise

- Wenn das eingegebene TOML-Format nicht korrekt ist, kann die Konvertierung fehlschlagen und das System gibt möglicherweise Fehlermeldungen aus.
- Das Tool unterstützt die meisten gängigen TOML-Syntaxstrukturen, aber für einige spezielle oder selten verwendete Syntaxelemente ist eine perfekte Konvertierung möglicherweise nicht möglich.
- Der ausgegebene YAML-Text kann je nach unterschiedlichen YAML-Versionen und Spezifikationen kleine Formatunterschiede aufweisen.