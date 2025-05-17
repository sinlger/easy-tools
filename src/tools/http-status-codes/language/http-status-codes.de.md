# HTTP-Statuscodes Dokumentation

## 1. Einführung

HTTP-Statuscodes sind dreistellige numerische Codes, die vom Server als Teil der HTTP-Antwortnachricht an den Client (normalerweise einen Webbrowser) gesendet werden. Sie geben den Status einer Anfrage wieder und helfen dabei zu verstehen, ob eine Anfrage erfolgreich war, ob Umleitungen nötig sind oder ob Fehler aufgetreten sind.

## 2. Hauptkategorien von HTTP-Statuscodes

### 1xx: Informationsantwort

Diese Codes zeigen an, dass die Anfrage verstanden wurde und der Server weiterhin arbeitet. Beispiele:
- **100 Continue** - Der Client sollte mit der Anfrage fortfahren.
- **101 Switching Protocols** - Der Client hat angefordert, das Kommunikationsprotokoll zu wechseln, z.B. von HTTP zu WebSocket.

### 2xx: Erfolgreiche Anfrage

Diese Codes bedeuten, dass die Anfrage erfolgreich empfangen, verstanden und akzeptiert wurde. Beispiele:
- **200 OK** - Die Anfrage war erfolgreich, und die gewünschten Daten wurden gefunden und übermittelt.
- **201 Created** - Eine Ressource wurde erfolgreich erstellt, oft nach einem POST-Request.
- **204 No Content** - Die Anfrage war erfolgreich, aber es gibt keine zurückzugebenden Inhalte.