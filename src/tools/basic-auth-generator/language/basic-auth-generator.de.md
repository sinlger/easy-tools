# Grundlegende Authentifizierungsgenerator Dokumentation

## Funktionsübersicht

Der Basic Auth Generator ist ein Werkzeug zur Erzeugung von Base64-kodierten Authorization-Headern für die HTTP-Grundauthentifizierung. Durch Eingabe eines Benutzernamens und Passworts kann das Werkzeug schnell einen entsprechenden Authorization-Header generieren, der im Entwicklungsprozess verwendet werden kann.

## Verwendung

### Benutzernamen eingeben

Geben Sie in das Eingabefeld "Username" Ihren gewünschten Benutzernamen ein. Es kann ein beliebiger Name sein, der für die Authentifizierung verwendet werden soll.

### Passwort eingeben

Geben Sie in das Feld "Password" das entsprechende Passwort zu Ihrem Benutzernamen ein. Bei der Eingabe wird das Passwort automatisch versteckt, um Ihre Sicherheit zu gewährleisten.

### Generierten Authorization-Header ansehen

Nach Eingabe des Benutzernamens und Passworts generiert das Werkzeug automatisch den zugehörigen Authorization-Header. Dieser wird im folgenden Format angezeigt:

```
Authorization header:
Authorization: Basic [Base64 kodierter String]