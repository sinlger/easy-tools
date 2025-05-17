# Online IBAN-Validierer und Parser Benutzerdokumentation

## 1. Werkzeugbeschreibung

Dies ist ein Online-IBAN-Validierer (International Bank Account Number) und Parser, der IBAN-Codes überprüfen und analysieren kann, um festzustellen, ob eine IBAN gültig ist, und zusätzliche relevante Informationen bereitzustellen.

## 2. Funktionsbeschreibung

### IBAN Validierungsfunktion

1. **IBAN-Nummer eingeben** - Geben Sie in das Eingabefeld die zu überprüfende IBAN ein. Stellen Sie beim Eingeben sicher, dass die Nummer genau und vollständig ist.
2. **Validierungsergebnis** :
   * **Gültige IBAN** - Wenn die eingegebene IBAN gültig ist, zeigt das Werkzeug eine Erfolgsmeldung an und liefert gleichzeitig folgende detaillierte Informationen:
     * **Land** - Zeigt das Land an, dem die IBAN zugeordnet ist, beispielsweise Frankreich, Deutschland oder Großbritannien.
     * **BBAN** - Zeigt die Grundnummer des Bankkontos (BBAN), eine wichtige Information zur Identifizierung des Kundenkontos durch die Bank.
     * **QR-IBAN Prüfung** - Gibt an, ob es sich bei der IBAN um eine QR-IBAN handelt (eine spezielle Form der IBAN, die häufig für Zahlungen per QR-Code verwendet wird).
     * **Benutzerfreundliches IBAN-Format** - Konvertiert die IBAN in ein benutzerfreundlicheres Format, normalerweise durch Hinzufügen von Leerzeichen nach jeweils vier Ziffern, wodurch die Lesbarkeit verbessert wird.

   * **Ungültige IBAN** - Wenn die eingegebene IBAN ungültig ist, wird eine Fehlermeldung angezeigt, die besagt, dass die Nummer nicht bestanden hat und Probleme aufweist.

### IBAN Parsing Funktion

Wenn die eingegebene IBAN gültig ist, analysiert das Werkzeug automatisch folgende Details:

1. **Land** - Bestimmt das Land, dem die IBAN zugeordnet ist. Dies ist besonders wichtig für internationale Transaktionen und Geldflüsse, da es hilft, Herkunft und Ziel der Überweisung besser zu verstehen.
2. **BBAN (Basic Bank Account Number)** - Liefert die Grundnummer des Kontos, einen zentralen Bezeichner, den Banken verwenden, um Kundendaten eindeutig zu identifizieren und Transaktionen korrekt abzuwickeln.
3. **QR-IBAN Prüfung** - Analysiert, ob es sich um eine QR-IBAN handelt, was für bestimmte Anwendungsszenarien wie mobile oder digitale Zahlungen relevant sein kann.
4. **Benutzerfreundliches IBAN-Format** - Wandelt die IBAN in ein leserfreundlicheres Format um, welches das Handling vereinfacht und Fehlinterpretationen oder Fehler minimiert.

### Beispiele

Das Werkzeug stellt einige gültige IBAN-Beispiele bereit, anhand derer Sie die korrekte IBAN-Formatvorlage kennenlernen können. Einige davon sind unten aufgeführt:

1. **FR76 3000 6000 0112 3456 7890 189** - Dies ist ein Beispiel einer französischen IBAN, mit dem Länderkürzel "FR" und BBAN "30006000011234567890189", dies ist keine QR-IBAN.
2. **DE89 3704 0044 0532 0130 00** - Ein deutsches IBAN-Beispiel, Länderkürzel "DE", BBAN "370400440532013000", auch keine QR-IBAN.
3. **GB29 NWBK 6016 1331 9268 19** - Ein Beispiel aus Großbritannien, Länderkürzel "GB", BBAN "NWBK60161331926819", ebenfalls keine QR-IBAN.

Die Kopierfunktion neben jedem Beispiel erlaubt es Ihnen, die Beispieldaten direkt in das Eingabefeld einzufügen, sodass Sie schnell Validierung und Analyse durchführen können.

## 3. Verwendungsschritte

1. Öffnen Sie die Seite des Online IBAN-Validierers und Parsers.
2. Geben Sie im Eingabefeld die IBAN ein, die Sie prüfen möchten.
3. Klicken Sie auf den Knopf "Check for validity" (oder drücken Sie Enter), um die Prüfung zu starten.
4. Schauen Sie sich das Ergebnis an. Falls gültig, werden weitere Details wie Land, BBAN usw. angezeigt. Bei Ungültigkeit erhalten Sie Hinweise zum Problem; überprüfen und korrigieren Sie Ihre Eingabe entsprechend.
5. Für Referenzzwecke finden Sie auf der Seite bereits vorgefertigte gültige IBANs, welche Sie durch Klick auf den Copy-Button direkt in das Feld kopieren können.

## 4. Wichtige Hinweise

1. **Genauigkeit der Eingabe** - Stellen Sie sicher, dass die eingegebene IBAN korrekt ist. Jeder Tippfehler kann dazu führen, dass die Prüfung fehlschlägt. Falls Sie unsicher sind, vergleichen Sie die Nummer sorgfältig oder kontaktieren Sie Ihre Bank für Unterstützung.
2. **Internetverbindung erforderlich** - Da dieses Werkzeug online genutzt wird, benötigen Sie eine stabile Internetverbindung. Bei schlechter oder keiner Verbindung kann das Tool nicht genutzt werden.
3. **Datenschutz und Sicherheit** - Achten Sie darauf, keine sensiblen oder vertraulichen persönlichen oder Unternehmensdaten einzugeben, um Risiken durch Datenlecks vorzubeugen. Obwohl das Tool üblicherweise Daten sicher behandelt, sollten Sie sensible Informationen im Internetumfeld immer mit Vorsicht eingeben.