# A Toolio - BIP39-Passphrase-Generator Dokumentation

## 1. Werkzeugübersicht

Der BIP39-Passphrase-Generator ist ein Online-Werkzeug, das aus vorhandenen oder zufällig generierten Merksätzen BIP39-Passphrasen erzeugt und auch Merksätze aus Passphrasen ableiten kann. Dieses Werkzeug bietet Entwicklern bequeme Passwortoperationen mit vielfältigen Anwendungsmöglichkeiten.

## 2. Funktionsmodule und Bedienungsanleitung

### 1. **Sprachauswahl**
   * **Funktion**: Der Benutzer kann über ein Dropdown-Menü verschiedene Sprachoptionen auswählen. Derzeit werden mehrere Sprachen wie "Chinese simplified" unterstützt, um den Sprachtyp der Merksätze festzulegen.
   * **Bedienungsschritte**: Klicken Sie auf das Sprachauswahlfeld und wählen Sie im angezeigten Dropdown-Menü die gewünschte Sprache für die Merksätze, z.B. Chinesisch (vereinfacht).

### 2. **Generierung von Merksätzen**
   * **Funktion**: Auf Basis der vom Benutzer eingegebenen Zufallszahl (Entropie) oder einer zufällig generierten Zufallszahl erstellt das Werkzeug entsprechend der ausgewählten Sprache einen passenden BIP39-Merksatz. So erhält der Benutzer eine Eselsbrücke, die sich leicht speichern und verwenden lässt.
   * **Bedienungsschritte**:
     1. Geben Sie im Textfeld "Entropy (seed):" Ihre gewünschte Entropie-Zeichenkette ein. Falls Sie diese nicht manuell eingeben möchten, können Sie das Symbol "Zufallsgenerator" neben dem Feld anklicken, um eine zufällige Entropie zu erzeugen.
     2. Wählen Sie die gewünschte Sprache für den Merksatz (wie bereits unter Sprachauswahl beschrieben). Klicken Sie anschließend auf den "Generieren"-Knopf. Das Textfeld "Passphrase (mnemonic):" darunter generiert automatisch den entsprechenden Merksatz.