# ULID-Generator Benutzerdokumentation

## 1. Einführung in das Tool
Der ULID-Generator dient zur Erstellung zufälliger, universell eindeutiger lexikographisch sortierbarer Identifikatoren (ULIDs). Die generierten Kennzeichner sind eindeutig und sortierbar und finden breite Anwendung in verteilten Systemen, als Datensatzidentifikatoren in Datenbanken usw.

## 2. Funktionsbeschreibung

### (1) Mengeneinstellung
Über die Option "Quantity" lässt sich die Anzahl der zu generierenden ULIDs festlegen. Der Standardwert ist 1. Mit den Plus-/Minus-Schaltflächen auf der rechten Seite kann die Anzahl angepasst werden.

### (2) Formatwahl
Es stehen zwei Ausgabeformate zur Verfügung:
1. **Raw**: Zeigt ULIDs im Klartextformat an, was eine direkte Ansicht und Verwendung erleichtert.
2. **JSON**: Gibt die generierten ULIDs im JSON-Format aus, was den Aufruf und die Verarbeitung durch Programme vereinfacht.

### (3) Generierung & Operationen
Klicken Sie auf die Schaltfläche "Refresh", um neue ULIDs zu generieren. Klicken Sie auf "Copy", um die generierten ULIDs in die Zwischenablage zu kopieren und anschließend an anderen Stellen einzufügen.

## 3. Beispiele

### Beispiel 1: Einzelne ULID generieren (Raw-Format)
Legen Sie "Quantity" auf 1 fest und wählen Sie das Format "Raw" aus. Nach Klick auf "Refresh" wird eine ULID ähnlich wie folgt generiert:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Beispiel 2: Mehrere ULIDs generieren (JSON-Format)
Legen Sie "Quantity" auf 3 fest und wählen Sie das Format "JSON" aus. Nach Klick auf "Refresh" werden ULIDs im folgenden JSON-Format generiert:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}