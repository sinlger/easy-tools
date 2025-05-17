# A Toolio Online-Datum-Uhrzeit-Konverter Dokumentation

## 1. Tool-Übersicht

A Toolio ist ein leistungsstarkes Online-Werkzeug für Entwickler, das einen Datums- und Zeitkonverter enthält. Dieser konvertiert Datums- und Zeitangaben zwischen verschiedenen gängigen Formaten und eignet sich ideal zur Lösung von Kompatibilitätsproblemen bei Datums- und Zeitformaten in unterschiedlichen Systemen.

## 2. Funktionsbeschreibung

### (1) Konversion von Datums- und Zeitformaten

1. **JavaScript Lokales Datum Format**
   * Konvertiert Eingabedatumszeichenfolgen in Zeichenfolgen im JavaScript lokalen Datumsformat, z.B. "Thu May 01 2025 14:53:04 GMT+0800 (China Standard Time)".

2. **ISO 8601 Format**
   * Präsentiert Datum und Uhrzeit im ISO 8601 Standardformat: "2025-05-01T14:53:04+08:00", ideal für internationale Anwendungen und Datenübertragungen.

3. **ISO 9075 Format**
   * Konvertiert ins ISO 9075 Format: "2025-05-01 14:53:04", häufig in datenbankbezogenen Operationen verwendet.

4. **RFC 3339 Format**
   * Konvertiert ins RFC 3339 Format: "2025-05-01T14:53:04+08:00", weit verbreitet in Internetanwendungen und Protokollen zur Darstellung von Datum und Uhrzeit.

5. **RFC 7231 Format**
   * Konvertiert ins RFC 7231 Format: "Thu, 01 May 2025 06:53:04 GMT", besonders häufig in HTTP-Protokoll-Anwendungsfällen zu finden.

6. **Unix-Zeitstempel**
   * Konvertiert Datum und Uhrzeit in den Unix-Zeitstempel: "1746082384", repräsentiert die Sekundenanzahl seit dem 1. Januar 1970 00:00:00 UTC.

7. **Zeitstempel mit Millisekundenpräzision**
   * Liefert präzisere Zeitstempel wie "1746082384853", nützlich in Systemen mit hohen Präzisionsanforderungen.

8. **UTC Format**
   * Gibt Datum und Uhrzeit im UTC Format aus: "Thu, 01 May 2025 06:53:04 GMT", hilfreich bei globalen Zeitberechnungen und Synchronisationen.

9. **Mongo ObjectID Zeitkonversion**
   * Wandelt in das in Mongo ObjectIDs enthaltene Zeitformat um, z.B. "68131a500000000000000000", unterstützt MongoDB-basierte Zeitdatenoperationen.

10. **Excel Datumsumwandlung**
    * Konvertiert in Excel-kompatible Datumsformate wie "45778.28686172454", erleichtert Datenanalyse- und Bearbeitungsprozesse in Excel Tabellen.

## 3. Verwendungsvorgehensweise

1. Öffnen Sie die [A Toolio Online-Datum-Uhrzeit-Konverter Seite](https://atoolio.com/date-converter)
2. Geben Sie die zu konvertierende Datumszeichenfolge in das Eingabefeld ein.
3. Wählen Sie über das Dropdown-Menü den gewünschten Zielformattyp aus.
4. Das Ergebnis wird automatisch im entsprechenden Formatfeld unten angezeigt.
5. Zum Kopieren klicken Sie auf den Copy-Button rechts neben jedem Ergebnisfeld.