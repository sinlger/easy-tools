# IPv4-Bereichserweiterer Benutzerdokumentation

## 1. Einführung des Werkzeugs

Der IPv4-Bereichserweiterer berechnet basierend auf einer gegebenen Start- und End-IPv4-Adresse effektive IPv4-Netzwerke, einschließlich gültiger Netblocks (dargestellt in CIDR-Notation), Adressbereiche und die Anzahl der Adressen innerhalb des Bereichs.

## 2. Funktionsbeschreibung

### (A) Grundlegende Eingabefunktion

1. **Eingabe der Startadresse** - Geben Sie in das Feld "Start address" eine IPv4-Adresse als Startpunkt ein, z.B. "192.168.1.1".
2. **Eingabe der Endadresse** - Geben Sie in das Feld "End address" eine IPv4-Adresse als Endpunkt ein, z.B. "192.168.6.255".

### (B) Automatische Verarbeitung und Ergebnisdarstellung

1. **Anpassung des Adressbereichs** - Das Werkzeug passt die Start- und Endadressen automatisch an, um einen geeigneteren Bereich zu erhalten. Zum Beispiel wird "192.168.1.1" in "192.168.0.0" und "192.168.6.255" in "192.168.7.255" umgewandelt.
2. **Berechnung der Adressanzahl** - Die Gesamtanzahl der IPv4-Adressen im neuen Bereich wird berechnet, z.B. von "1.535" auf "2.048", wodurch die Effizienz der Adressnutzung verbessert wird.
3. **Erstellung der CIDR-Notation** - Es wird die entsprechende CIDR-Notation für den neuen Adressbereich angezeigt, z.B. "192.168.0.0/21", was die Netzwerkverwaltung und Konfiguration vereinfacht.

## 3. Wichtige Hinweise

Stellen Sie sicher, dass die eingegebenen Start- und Endadressen dem IPv4-Adressformat entsprechen, um eine korrekte Funktion des Tools und genaue Ergebnisse zu gewährleisten.