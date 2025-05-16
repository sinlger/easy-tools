# URL Parser

## 1. Tool Overview
URL Parser ist ein Online-Tool zum Parsen von URL-Zeichenfolgen, das komplexe URLs in mehrere Komponenten zerlegen kann, einschließlich Protokoll, Benutzername, Passwort, Hostname, Port, Pfad, Parameter usw. Jeder Teil erleichtert Entwicklern das schnelle Verständnis der URL-Struktur und der detaillierten Informationen, um den Aufbau, die Debugging und Analyse von Netzwerkanfragen zu vereinfachen.

## 2. Funktionsbeschreibung

  1. **Eingabefeld**
     * Bietet ein Eingabefeld, in dem die zu analysierende URL-Zeichenfolge eingegeben werden kann.

  2. **Ergebnisanzeige**
     * **Protokoll (Protocol)** : Zeigt den Protokollteil der URL an, z.B. "https:", was das verwendete Netzwerkübertragungsprotokoll angibt.
     * **Benutzername (Username)** : Wenn die URL Benutzernameinformationen enthält, werden diese hier angezeigt, um die im URL bereitgestellte Benutzeridentität zu kennzeichnen.
     * **Passwort (Password)** : Zeigt entsprechend den Passwortteil in der URL an, der zusammen mit dem Benutzernamen zur Benutzerauthentifizierung dient.
     * **Hostname (Hostname)** : Zeigt den Domänennamen der URL an, z.B. "atoolio.com", was den Namen des Zielserver darstellt.
     * **Port (Port)** : Zeigt die in der URL angegebene Portnummer an, um den spezifischen Port auf dem Server zu bestimmen, über den der Dienst bereitgestellt wird. Standardmäßig haben verschiedene Protokolle unterschiedliche Standardports, z.B. Port 80 für HTTP und Port 443 für HTTPS.
     * **Pfad (Path)** : Zeigt den Pfadteil der URL an, z.B. "/url-parser", welcher auf eine bestimmte Ressource oder Dienstposition auf dem Server verweist.
     * **Parameter (Params)** : Listet den Abfrageparameter der URL auf, beginnend mit "?", gefolgt von mehreren Parametern im Format "Schlüssel=Wert", wie z.B. "?key1=value&key2=value2", welche zusätzliche Informationen und Anweisungen an den Server übermitteln.
     * **Detaillierte Parameterdarstellung** : Jedes Schlüssel-Wert-Paar der Abfrageparameter wird einzeln angezeigt, um Name und Wert jedes Parameters übersichtlich darzustellen.

## 3. Verwendungsschritte

  1. Öffnen Sie einen Browser und rufen Sie die [URL Parser](https://atoolio.com/url-parser) Webseite auf.
  2. Geben Sie in das Eingabefeld die zu analysierende URL-Zeichenfolge ein, z.B. "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Klicken Sie auf den Analysebutton (normalerweise kann auch die Eingabetaste die Analyse auslösen), das Tool analysiert die eingegebene URL automatisch und zeigt unten die detaillierten Informationen jeder Komponente an.
  4. Überprüfen Sie das Analyseergebnis und kopieren Sie bei Bedarf den entsprechenden Inhalt der Komponenten für spätere Entwicklungs-, Debugging- oder andere Operationen.

## 4. Beispiele

  1. **Beispiel 1**
     * Eingegebene URL: "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Analyseergebnis:
       * Protokoll: http:
       * Benutzername: user
       * Passwort: pass
       * Hostname: example.com
       * Port: 8080
       * Pfad: /page
       * Parameter: ?param1=hello&param2=world
       * Detaillierte Parameterdarstellung:
         * param1: hello
         * param2: world

  2. **Beispiel 2**
     * Eingegebene URL: "https://www.google.com/s?wd=URL Parser"
     * Analyseergebnis:
       * Protokoll: https:
       * Benutzername: (keiner)
       * Passwort: (keines)
       * Hostname: www.google.com
       * Port: (Standardport 443, nicht angezeigt)
       * Pfad: /s
       * Parameter: ?wd=URL Parser
       * Detaillierte Parameterdarstellung:
         * wd: URL Parser