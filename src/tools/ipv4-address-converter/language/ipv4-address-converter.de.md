# IPv4-Adresskonverter Benutzerdokumentation

## 1. Werkzeugbeschreibung

Der IPv4-Adresskonverter ist ein Online-Werkzeug, das dazu dient, IPv4-Adressen in verschiedene Zahlensysteme (Dezimal, Hexadezimal, Binär) sowie in IPv6-Format umzuwandeln. Es hilft Entwicklern und Netzwerktechnikern dabei, schnell unterschiedliche Darstellungsformen einer IPv4-Adresse zu erhalten, was bei Netzwerkkonfiguration, Programmierung oder Sicherheitsanalysen von Vorteil ist.

## 2. Funktionsbeschreibung

### (A) Eingabe einer IPv4-Adresse
- In das Eingabefeld des Werkzeugs kann der Nutzer direkt eine gültige IPv4-Adresse eingeben (z.B.: 192.168.1.1). Nach der Eingabe klickt man entweder auf den "Konvertieren"-Button oder drückt die Enter-Taste, woraufhin das System automatisch mehrere Konvertierungen durchführt.

### (B) Dezimale Umrechnung
- **Funktion**: Wandelt die IPv4-Adresse in eine dezimale Zahl um.
- **Anwendung**: Nach Eingabe der IPv4-Adresse berechnet das Werkzeug automatisch den entsprechenden Dezimalwert. Der Dezimalwert ergibt sich aus den vier Bytes der IPv4-Adresse, die jeweils in Dezimalzahlen umgewandelt werden und anschließend nach einem bestimmten Schema zusammengestellt werden.

### (C) Hexadezimale Umrechnung
- **Funktion**: Konvertiert die IPv4-Adresse in eine hexadezimale Darstellung.
- **Anwendung**: Nach Eingabe der IPv4-Adresse wandelt das System jedes Byte in eine zweistellige Hexadezimalzahl um und verbindet diese zu einer vollständigen Zeichenkette. Beispielsweise wird die IPv4-Adresse 192.168.1.1 in C0A80101 umgewandelt.

### (D) Binäre Umrechnung
- **Funktion**: Verwandelt die IPv4-Adresse in eine binäre Form.
- **Anwendung**: Bei Eingabe der IPv4-Adresse konvertiert das Werkzeug jedes Byte in eine 8-stellige Binärzahl, welche dann zu einer 32-stelligen Binärzeichenkette zusammengefügt wird. Die IPv4-Adresse 192.168.1.1 erscheint so beispielsweise als 11000000101010000000000100000001.

### (E) Umwandlung in IPv6-Format
- **Funktion**: Konvertiert die IPv4-Adresse in eine IPv6-Darstellung.
- **Anwendung**: Das Werkzeug erzeugt zwei verschiedene IPv6-Formate:
  1. **Vollständige IPv6-Adresse**: Die ersten 8 Bytes werden mit Nullen aufgefüllt, die letzten 8 Bytes bestehen aus der hexadezimalen Form der IPv4-Adresse. Vor dem IPv4-Anteil wird außerdem "ffff" als Kennzeichnung hinzugefügt. Beispiel: Aus der IPv4-Adresse 192.168.1.1 wird die vollständige IPv6-Adresse 0000:0000:0000:0000:0000:ffff:c0a8:0101.