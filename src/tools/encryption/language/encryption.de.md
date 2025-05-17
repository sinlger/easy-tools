# A Toolio Online-Verschlüsselungs-/Entschlüsselungswerkzeug Dokumentation

## Funktionsübersicht

Das von A Toolio bereitgestellte Online-Verschlüsselungs- und Entschlüsselungswerkzeug unterstützt die Verschlüsselung und Entschlüsselung von Texten mit verschiedenen Algorithmen (wie AES, TripleDES, Rabbit oder RC4). Benutzer können bequem Klartexte verschlüsseln oder Geheimtexte entschlüsseln, um alltägliche Anforderungen in Entwicklung oder Studium zu erfüllen.

## Verschlüsselungsfunktion

1. **Klartext-Eingabe** - Geben Sie im Eingabefeld "Your text" des "Encrypt"-Bereichs den zu verschlüsselnden Klartext ein. Zum Beispiel "Lorem ipsum dolor sit amet".
2. **Schlüssel festlegen** - Legen Sie im Feld "Your secret key" einen Schlüssel zur Verschlüsselung fest, z.B. "my secret key". Der Schlüssel ist ein wesentlicher Parameter im Verschlüsselungsprozess, der sicher aufbewahrt werden muss.
3. **Verschlüsselungsalgorithmus auswählen** - Wählen Sie über das Dropdown-Menü "Encryption algorithm" den gewünschten Algorithmus wie AES, TripleDES, Rabbit oder RC4 aus. Unterschiedliche Algorithmen haben unterschiedliche Sicherheits- und Leistungsmerkmale, sodass Sie je nach Bedarf wählen können.
4. **Verschlüsselungsergebnis ansehen** - Nach Abschluss der obigen Einstellungen zeigt das Werkzeug automatisch den verschlüsselten Geheimtext im Bereich "Your text encrypted" an, z.B. "U2FsdGVkX19wCAAvFjYehC+Haqkp3/xRGF4yN17gt6/FgnlHRvikeCuOvDyAIBvG".

## Entschlüsselungsfunktion

1. **Geheimtext eingeben** - Geben Sie im "Decrypt"-Bereich im Feld "Your encrypted text" den zu entschlüsselnden Geheimtext ein, z.B. "U2FsdGVkX1/EC3+6P5dbbkZ3e1kQ5o2yzuU0NHTjmrKnLBEwreV489Kr0DIB+uBs".
2. **Schlüssel eingeben** - Geben Sie im Feld "Your secret key" denselben Schlüssel wie bei der Verschlüsselung ein: "my secret key". Der korrekte Schlüssel ist entscheidend für eine erfolgreiche Entschlüsselung.
3. **Verschlüsselungsalgorithmus auswählen** - Wählen Sie über das Menü "Encryption algorithm" denselben Algorithmus wie bei der Verschlüsselung, z.B. AES.
4. **Ergebnis der Entschlüsselung ansehen** - Das Werkzeug zeigt im Bereich "Your decrypted text" den entschlüsselten Klartext an, z.B. "Lorem ipsum dolor sit amet".

## Weitere Hinweise

* **Sicherheit** - Obwohl dieses Werkzeug bequem und schnell ist, empfiehlt es sich, bei der Verarbeitung sensibler Informationen ein sicheres Netzwerkumfeld zu nutzen und den Schutz des Schlüssels sicherzustellen, um eine unbefugte Offenlegung zu verhindern.
* **Algorithmenwahl** - Unterschiedliche Verschlüsselungsalgorithmen sind für verschiedene Szenarien geeignet. AES ist derzeit einer der weit verbreiteten und vertrauenswürdigen Algorithmen; TripleDES ist relativ alt, wird aber immer noch in bestimmten Systemen genutzt; Rabbit und RC4 haben ebenfalls ihre eigenen Merkmale und Einsatzbereiche. Nutzer können je nach tatsächlichen Anforderungen und Sicherheitsbedürfnissen wählen.