# A Toolio Online HMAC-Generator Dokumentation

## 1. Werkzeugbeschreibung

Der online HMAC-Generator von A Toolio berechnet mithilfe eines Schlüssels und einer Hash-Funktion einen Hash-basierten Message-Authentifizierungscode (HMAC), der für Entwickler geeignet ist, die in verschiedenen Entwicklungszenarien schnell HMACs generieren müssen.

## 2. Funktionsbeschreibung

### Eingabebereich

1. **Plain Text** - Geben Sie den Klartext ein, dessen Hash berechnet werden soll.
2. **Secret Key** - Geben Sie den geheimen Schlüssel ein, der zur Erzeugung des HMAC verwendet wird.
3. **Hashing Function** - Wählen Sie eine Hash-Funktion aus. Standardmäßig ist SHA256 eingestellt, andere Hash-Funktionen können nach Bedarf ausgewählt werden.
4. **Output Encoding** - Wählen Sie das Ausgabecodierungsformat. Voreinstellung ist Hexadezimal (Basis 16), andere Formate sind ebenfalls wählbar.

### Ausgabebereich

1. **HMAC of your text** - Zeigt den generierten HMAC-Wert an. Ein Kopierbutton erleichtert das Übertragen des Ergebnisses.

## 3. Verwendungsschritte

**Schritt 1: Eingabe von Klartext und Schlüssel**

Geben Sie in das Feld "Plain Text" den Text ein, für den ein Hash berechnet werden soll. Danach geben Sie im Feld "Secret Key" den Schlüssel ein, der zur Generierung des HMAC benötigt wird. Diese Basisdaten müssen korrekt eingegeben werden.

**Schritt 2: Auswahl der Hash-Funktion**

Wählen Sie aus dem Dropdown-Menü "Hashing Function" die gewünschte Hash-Funktion aus, z.B. SHA256 oder SHA1. Verschiedene Hash-Funktionen liefern unterschiedliche HMAC-Ergebnisse.

**Schritt 3: Auswahl des Ausgabecodierungsformats**

Wählen Sie im Menü "Output Encoding" das benötigte Codierungsformat aus, z.B. Hexadezimal (Basis 16) oder Base64. Dies bestimmt die Darstellungsform des generierten HMAC-Werts.

**Schritt 4: HMAC erzeugen und anzeigen**

Nach Eingabe aller Daten und Auswahl der Parameter berechnet das System automatisch den HMAC-Wert, der im Bereich "HMAC of your text" angezeigt wird. Das Ergebnis kann direkt angesehen werden.

**Schritt 5: HMAC kopieren**

Falls Sie diesen HMAC-Wert verwenden möchten, klicken Sie auf den Copy-Button neben dem Ergebnis, um den Wert in die Zwischenablage zu kopieren und an anderen Stellen einzufügen.