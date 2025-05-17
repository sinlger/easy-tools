# Outlook Safelink Decoder Benutzerdokumentation

## 1. Einführung in das Tool
Der **Outlook Safelink Decoder** ist ein Tool zur Entschlüsselung von SafeLink-Links, die vom Microsoft Outlook-Mail-Dienst verwendet werden. Es kann verschlüsselte Links, die durch Outlook SafeLink generiert wurden, wieder in ihre ursprüngliche URL zurückverwandeln, sodass Nutzer leicht erkennen können, wohin diese Links wirklich führen.

## 2. Funktionsbeschreibung
Die Hauptfunktion dieses Tools besteht darin, Outlook-SafeLink-Links zu entschlüsseln, d.h., die von Microsoft Outlook generierten verschlüsselten Weiterleitungslinks in die ursprüngliche Webadresse zurückzuwandeln.

## 3. Verwendung

### Eingabe
Fügen Sie in das Eingabefeld den Outlook-SafeLink ein, den Sie entschlüsseln möchten. Dieser Link wurde von Microsoft Outlook aus Sicherheitsgründen verschlüsselt und hat ein spezifisches Format.

### Ausgabe
Nachdem Sie auf den "Decode"-Button geklickt haben, verarbeitet das Tool den eingegebenen Link und zeigt im Ausgabefeld die entschlüsselte Original-URL an. Falls der eingegebene Link nicht korrekt formatiert ist oder nicht erkannt werden kann, erscheint eine Fehlermeldung: "Error: Invalid SafeLinks URL provided".

## 4. Anwendungsbeispiele

### Beispiel 1
Eingabe (SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Ausgabe nach der Decodierung:
`https://example.com`

### Beispiel 2
Eingabe (SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Ausgabe nach der Decodierung:
`https://microsoft.com`

### Beispiel 3
Eingabe eines ungültigen oder falsch formatierten Links:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Fehlermeldung:
`Error: Invalid SafeLinks URL provided`

## 5. Wichtige Hinweise
- Stellen Sie sicher, dass der eingegebene Link ein vollständiger Outlook-SafeLink ist.