# Textverschlüsselungswerkzeug Benutzerhandbuch

## 1. Werkzeugübersicht

Dies ist ein leistungsfähiges Textverschlüsselungswerkzeug, das hauptsächlich auf dem bcrypt-Algorithmus basiert und Texte verschlüsselt sowie die vergleichende Überprüfung von verschlüsselten Hashwerten mit Originaltexten unterstützt. Es kann in sicherheitsrelevanten Anwendungsszenarien wie Passwortverwaltung und -überprüfung eingesetzt werden.

## 2. Zugriff auf das Werkzeug

Geben Sie die URL der Seite, auf der sich dieses Werkzeug befindet, in die Adressleiste des Browsers ein, drücken Sie die Enter-Taste, um die Seite aufzurufen, und warten Sie, bis alle Seitenelemente vollständig geladen sind.

## 3. Bedienungsanleitung

### (1) Textverschlüsselung

1. **Text eingeben** : Geben Sie im Eingabefeld "Your string" den Text ein, der verschlüsselt werden soll. Zum Beispiel das Passwort, das ein Benutzer beim Registrieren festlegt.
2. **Salt count einstellen** : Klicken Sie auf die Schaltflächen "+" oder "-" neben "Salt count", um die Iterationsanzahl für den Salt-Wert einzustellen. Salt ist ein zufällig generierter String, der vor der Verschlüsselung zum Originaltext hinzugefügt wird, um die Sicherheit zu erhöhen und Angriffe wie Rainbow-Table-Angriffe zu verhindern. Die Iterationsanzahl sollte mindestens 10 betragen.
3. **Verschlüsselungsergebnis ansehen** : Nachdem die oben genannten Einstellungen abgeschlossen sind, verschlüsselt das Werkzeug automatisch den eingegebenen Text. Das Ergebnis wird unten angezeigt, beispielsweise "$2a$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/Dk5Esl7bj1sXA.xK".