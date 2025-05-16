# Online-Benutzeragentenanalysator - Bedienungsanleitung

## 1. Einführung zum Tool

Der Online-Benutzeragentenanalysator kann präzise Browser, Rendering-Engine, Betriebssystem, CPU-Architektur sowie Geräteinformationen (Gerätetyp/Modell) aus dem Benutzeragentenstring erkennen und analysieren. Dies hilft Entwicklern dabei, schnell relevante Informationen über den Client zu erhalten.

## 2. Funktionsbeschreibung

### (1) Browsererkennung

Es kann genau den verwendeten Brower-Typ sowie dessen konkrete Versionsnummer identifizieren. Wenn beispielsweise "Edge 135.0.0.0" angezeigt wird, bedeutet dies, dass der Client-Browser Edge ist und die Version 135.0.0.0 verwendet.

### (2) Erkennung der Engine

Die vom Browser genutzte Rendering-Engine samt zugehöriger Version wird klar dargestellt. Wird beispielsweise "Blink 135.0.0.0" angezeigt, heißt das, dass Blink als Rendering-Engine in der Version 135.0.0.0 zum Einsatz kommt.

### (3) Erkennung des Betriebssystems

Das auf dem Client verwendete Betriebssystem samt seiner Version wird detailliert angezeigt. Wird beispielsweise "Windows 10" angezeigt, heißt das, dass Windows als Betriebssystem in der Version 10 verwendet wird.

### (4) Geräteinformations-Erkennung

Informationen wie Gerätetyp, Modellbezeichnung und Hersteller können (sofern verfügbar) ermittelt werden. Bei einigen Geräten werden möglicherweise vollständige Modellbezeichnungen angezeigt. In manchen Fällen sind jedoch keine Angaben zu Gerätetyp, -modell oder -hersteller vorhanden. Dann erscheint die entsprechende Meldung: "No device model/type/vendor available".

### (5) CPU-Informations-Erkennung

CPU-relevante Eigenschaften können ebenfalls erkannt werden. Wird beispielsweise "amd64" angezeigt, bedeutet dies, dass eine CPU-Architektur des Typs amd64 vorliegt.

## 3. Anwendungsbeispiele

### Beispiel 1: Gängiger Desktop-Browser

Angenommen, der Benutzeragentenstring lautet:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Nachdem dieser String in den Analysator eingegeben wurde:

  * **Browser**: Es wurde Edge 135.0.0.0 erkannt.
  * **Engine**: Entsprechend erkannt als Blink 135.0.0.0.
  * **Betriebssystem**: Es handelt sich um Windows 10.
  * **Gerät**: Keine konkreten Gerätemodelle oder Typen bzw. Herstellerangaben verfügbar, es wird entsprechender Hinweis angezeigt.
  * **CPU**: Die Architektur ist amd64.

### Beispiel 2: Mobiles Gerät mit Browser

Beispielhaft nehmen wir folgenden Benutzeragentenstring:
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Nach Eingabe in den Analysator:

  * **Browser**: Es wird Safari unter iOS mit entsprechender Versionsangabe erkannt (genaue Version je nach Analyseergebnis).
  * **Engine**: Entsprechende Webkit-Engine mit Versionsdetails wird angezeigt.
  * **Betriebssystem**: Klar als iOS mit Versionsnummer (z.B. 16_6_1) identifizierbar.
  * **Gerät**: Gerätetyp iPhone wird erkannt (konkretes Modell je nach Ergebnis der Analyse).
  * **CPU**: Entsprechende CPU-Architektur für mobile Geräte wird (falls eindeutig erkennbar) angezeigt.