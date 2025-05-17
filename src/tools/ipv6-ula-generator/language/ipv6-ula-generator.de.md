# IPv6 ULA-Generator Benutzerdokumentation

**1. Werkzeugbeschreibung**

Der IPv6 ULA-Generator ist ein Online-Werkzeug, das Benutzern dabei hilft, lokale nicht-routingfähige IPv6-Adressen gemäß RFC4193 zu generieren. Es eignet sich zur Erstellung eindeutiger Netzwerkidentifikatoren innerhalb eines lokalen Netzwerks, die im Internet nicht geroutet werden können.

**2. Hauptfunktionen**

1. **Zufällige ULA-Generierung basierend auf verschiedenen Faktoren**
   * Dieses Werkzeug verwendet die vom IETF empfohlene erste Methode und kombiniert Zeitstempel und MAC-Adresse mit dem SHA1-Hash-Algorithmus. Anschließend werden die unteren 40 Bit extrahiert, um zufällige ULA-Adressen zu erzeugen. Dadurch wird eine hohe Zufälligkeit und Einzigartigkeit der generierten Adressen gewährleistet, wodurch das Risiko von Adresskonflikten verringert wird und für Geräte im lokalen Netzwerk verlässliche lokale Netzwerkidentifikatoren bereitgestellt werden.

2. **Eingabe und Verarbeitung von MAC-Adressen**
   * Die Benutzer können in einem dafür vorgesehenen Eingabefeld manuell MAC-Adressen eingeben. Das Eingabeformat entspricht dem Standard-MAC-Adressformat (z.B. "20:37:06:12:34:56"). Das Werkzeug nutzt diese eingegebene MAC-Adresse als einen wesentlichen Parameter für die Generierung der ULA-Adresse. Sie wird zusammen mit anderen Faktoren in den Berechnungsprozess einbezogen, um eine ULA-Adresse zu generieren, die mit dieser MAC-Adresse verknüpft ist.

3. **Generierung von ULA-Adressen und zugehörigen Routenblöcken**

   * **IPv6 ULA**: Das Werkzeug generiert eine vollständige IPv6 ULA-Adresse, welche mit "fd" beginnt und dem RFC4193-Standard für lokale ULA-Adressen entspricht. Zum Beispiel: "fd1d:dba9:6f7b::/48", wobei "/48" angibt, dass die Präfixlänge dieser ULA-Adresse 48 Bits beträgt. Damit wird für Geräte im lokalen Netzwerk eine eindeutige Netzwerkidentifikation bereitgestellt, die für Netzwerkkonfiguration und Kommunikation innerhalb des lokalen Netzes genutzt werden kann.
   * **First routable block**: Es wird der erste nutzbare Routenblock generiert, z.B. "fd1d:dba9:6f7b:0::/64". Diese Adresse repräsentiert den ersten Block innerhalb des ULA-Adressbereichs, der Hosts oder Subnetzen zugewiesen werden kann. Dadurch erhält der Benutzer Informationen über den Startbereich der verfügbaren Adressen, was bei der Netzplanung und Adressverwaltung hilft.
   * **Last routable block**: Es wird auch der letzte nutzbare Routenblock generiert, z.B. "fd1d:dba9:6f7b:ffff::/64". Damit wird der letzte Adressblock innerhalb des ULA-Adressbereichs angegeben, der für Hosts oder Subnetze zugewiesen werden kann. Der Nutzer erhält dadurch eine klare Vorstellung des verfügbaren Adressraums und kann entsprechend seiner Netzwerkplanung und Gerätekonfiguration vorgehen.

**3. Einsatzszenarien**

1. Für Unternehmensinterne lokale Netzwerke, um Geräten eindeutige lokale IPv6-Adressen zuzuweisen. So können Konflikte mit öffentlich erreichbaren IPv6-Adressen vermieden werden, während gleichzeitig die Kommunikation zwischen Geräten innerhalb des lokalen Netzes gesichert bleibt.
2. In Testumgebungen für Netzwerke, um lokale nicht-routingfähige ULA-Adressen zu generieren. Damit können verschiedene Szenarien simuliert, sowie Netzwerkkonfigurations- und Applikationstests durchgeführt werden, ohne offizielle IPv6-Adressressourcen aus dem Internet belegen zu müssen.
3. Im Heimnetzwerk, um Routern und intelligenten Geräten ULA-Adressen zuzuteilen. Auf diese Weise wird die Stabilität und Sicherheit des Netzwerks verbessert, da Zugriffe von externen Netzwerken verhindert werden.

**4. Bedienungsanleitung**

1. Rufen Sie die Webseite des IPv6 ULA-Generators auf [https://atoolio.com/ipv6-ula-generator](https://atoolio.com/ipv6-ula-generator).
2. Falls die MAC-Adresse des Geräts bekannt ist, geben Sie diese im entsprechenden Feld im Standardformat ein (z.B. "20:37:06:12:34:56"). Wenn keine MAC-Adresse vorliegt, kann dieses Feld zunächst leer gelassen werden. Das Werkzeug könnte dann entweder eine Standard-MAC-Adresse verwenden oder eine zufällig generierte MAC-Adresse nutzen (abhängig von der tatsächlichen Funktionsweise des Tools).
3. Klicken Sie auf den Schaltfläche zum Generieren (z.B. "Generate", ggf. abhängig von der Oberfläche des Werkzeugs). Basierend auf der eingegebenen oder standardmäßigen MAC-Adresse sowie dem aktuellen Zeitstempel berechnet das Werkzeug gemäß der IETF-Empfehlung die entsprechende IPv6 ULA-Adresse, den ersten und letzten routbaren Adressblock.
4. Überprüfen Sie die generierten Adressinformationen und setzen Sie diese je nach Anforderung für die Gerätekommunikation, Netzwerkplanung oder Netzwerktests ein.

**5. Wichtige Hinweise**

1. Die generierten ULA-Adressen sind ausschließlich für den Einsatz im lokalen Netzwerk gedacht und können nicht im Internet geroutet oder dort kommuniziert werden. Für Geräte, die mit dem Internet kommunizieren müssen, werden weiterhin global eindeutige IPv6-Adressen benötigt.
2. Stellen Sie sicher, dass die eingegebene MAC-Adresse korrekt ist. Andernfalls kann dies Auswirkungen auf die Einzigartigkeit und Zuordnung der generierten ULA-Adresse haben und letztlich zu Problemen bei der Netzwerkkonfiguration führen.
3. Innerhalb des lokalen Netzes sollten ULA-Adressen immer eindeutig sein. Eine doppelte Nutzung gleicher ULA-Adressen sollte unbedingt vermieden werden, um Netzwerkkonflikte zu vermeiden, die die normale Kommunikation beeinträchtigen könnten.