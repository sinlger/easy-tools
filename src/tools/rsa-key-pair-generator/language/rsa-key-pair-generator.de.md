# RSA-Schlüsselpaargenerator Benutzerdokumentation

## 1. Toolübersicht

Dieses Online-Tool ermöglicht das einfache Generieren von zufälligen RSA-Privat- und Public-Key-PEM-Zertifikaten. Es ist ideal für Entwickler, die während des Entwicklungsprozesses schnell ein RSA-Schlüsselpaar erstellen müssen.

## 2. Funktionsbeschreibung

### (1) **Schlüssellängeneinstellung**

* **Funktion**: Der Nutzer kann die Schlüssellänge innerhalb eines definierten Bereichs festlegen (in Bit).
* **Aktion**: Geben Sie in das Eingabefeld hinter "Bits" die gewünschte Schlüssellänge ein, wie z.B. 2048 Bit. Das Tool unterstützt einen bestimmten Bit-Bereich, um sicherzustellen, dass der generierte Schlüssel sicherheits- und anwendungsrelevanten Anforderungen entspricht.
* **Zweck**: Je länger die Schlüssellänge, desto höher ist in der Regel die Sicherheit, allerdings kann dadurch auch die Geschwindigkeit von Verschlüsselung und Entschlüsselung abnehmen. Eine sorgfältige Abwägung entsprechend dem konkreten Anwendungsfall ist daher wichtig.

### (2) **Schlüsselpaar erneuern**

* **Funktion**: Dient zum schnellen Erstellen eines neuen Zufallsschlüsselpaares.
* **Aktion**: Klicken Sie auf den "Refresh key-pair"-Knopf. Das System generiert basierend auf der aktuell eingestellten Schlüssellänge ein neues Schlüsselpaar mit öffentlichem und privatem Schlüssel.
* **Zweck**: Bei Bedarf für mehrere Testläufe unterschiedliche Schlüsselpaare zu generieren, können Sie einfach den Refresh-Knopf drücken, ohne manuelle Anpassungen vornehmen zu müssen. Damit wird die Arbeitsgeschwindigkeit erhöht.

### (3) **Öffentlicher Schlüssel - Anzeige & Verwaltung**

* **Funktion**: Zeigt den generierten öffentlichen RSA-Schlüssel an und bietet dem Benutzer praktische Handhabungsmöglichkeiten.
* **Anzeige**: Im Bereich "Public key" wird der öffentliche Schlüssel im Standard-PEM-Format angezeigt, inklusive der Kennzeichnung "-----BEGIN PUBLIC KEY-----" und "-----END PUBLIC KEY-----", sodass dieser direkt in Applikationen als Konfigurationsbasis genutzt werden kann.
* **Kopierfunktion**: Ein benachbarter Copy-Button erlaubt es dem Benutzer, den öffentlichen Schlüssel mit nur einem Klick in die Zwischenablage zu kopieren, um ihn bequem in anderen Stellen einzufügen, etwa in Konfigurationsdateien oder Codeabschnitte.

### (4) **Privater Schlüssel - Anzeige & Verwaltung**

* **Funktion**: Zeigt den generierten privaten RSA-Schlüssel an und stellt eine einfache Bedienung bereit.
* **Anzeige**: Im Bereich "Private key" wird ebenfalls das standardmäßige PEM-Format verwendet, gekennzeichnet durch "-----BEGIN RSA PRIVATE KEY-----" und "-----END RSA PRIVATE KEY-----". So können Benutzer den privaten Schlüssel direkt nutzen, um Vorgänge wie Verschlüsselung, Entschlüsselung oder digitale Unterschrift durchzuführen.
* **Kopierfunktion**: Der danebenliegende Copy-Button ermöglicht es, den privaten Schlüssel unkompliziert zu kopieren, damit er in sicheren Umgebungen genutzt werden kann, z.B. zur Speicherung auf Servern oder Konfiguration in Anwendungen.

## 3. Beispiele für Anwendungsfälle

1. Entwickler, die bei der Entwicklung von Anwendungen, die auf dem RSA-Verschlüsselungsalgorithmus basieren, schnell Testschlüsel benötigen, können hier die passende Schlüssellänge wählen und per Refresh-Taste ein Schlüsselpaar generieren. Danach lässt sich der öffentliche Schlüssel für den Verschlüsselungsteil und der private Schlüssel für Entschlüsselungstests verwenden.
2. Bei der Einrichtung von Sicherheitsprotokollen (wie SSL/TLS) können mithilfe dieses Tools selbstsignierte Zertifikate oder Testschlüsel für Umgebungsläufe generiert werden. Öffentlicher und privater Schlüssel lassen sich dann jeweils auf Servern und Clients platzieren.