# IPv4-Subnetzrechner Benutzerdokumentation

Der IPv4-Subnetzrechner ist ein praktisches Online-Werkzeug, mit dem IPv4 CIDR-Blöcke analysiert und detaillierte Informationen über Subnetze abgerufen werden können. Im Folgenden finden Sie eine Beschreibung der Funktionen und Anweisungen zur Nutzung:

## 1. Eingabefunktion

In das Eingabefeld können Benutzer eine IPv4-Adresse eingeben, wobei diese mit oder ohne Subnetzmaske angegeben werden kann. Beispielsweise können Sie "192.168.0.1/24" eingeben, woraufhin das Werkzeug entsprechende Subnetzberechnungen durchführt.

## 2. Ergebnisse der Berechnung

1. **Netzmaske (Netmask)**
   * Zeigt die Kombination aus IPv4-Adresse und Subnetzmaske in CIDR-Notation an, z.B. "192.168.0.0/24", damit der Benutzer klar erkennt, wie der aktuelle Netzwerkbereich definiert ist.

2. **Netzwerkadresse (Network address)**
   * Gibt die Netzwerkadresse des Subnetzes an, eine spezielle Adresse, die das gesamte Netzwerk repräsentiert, beispielsweise "192.168.0.0". Diese zeigt den Startpunkt des Subnetzes.

3. **Subnetzmaske (Network mask)**
   * Stellt die Subnetzmaske in dezimaler Form dar, z.B. "255.255.255.0", um die Trennung zwischen Netzwerk- und Hostanteil innerhalb der IP-Adresse zu bestimmen.

4. **Subnetzmaske in Binärform (Network mask in binary)**
   * Zeigt die Subnetzmaske in binärer Schreibweise an, wie z.B. "11111111.11111111.11111111.00000000", was ein tieferes Verständnis der Funktionsweise einer Subnetzmaske ermöglicht.

5. **CIDR-Schreibweise (CIDR notation)**
   * Liefert die CIDR-Darstellung der Subnetzmaske, z.B. "/24". Dies ist eine kompakte Darstellungsform für die Länge der Subnetzmaske, welche rasche Einsicht in die Netzwerkunterteilung gewährt.

6. **Wildcard-Maske (Wildcard mask)**
   * Gibt den Wert der Wildcard-Maske an, z.B. "0.0.0.255". Diese ergänzt die Subnetzmaske und wird häufig bei bestimmten Netzwerkgeräten und Softwareanwendungen genutzt.

7. **Größe des Netzwerks (Network size)**
   * Informiert über die Gesamtanzahl der verfügbaren IP-Adressen im Subnetz, wie z.B. "256", sodass der Benutzer die Kapazität des Subnetzes kennt.

8. **Erste nutzbare Adresse (First address)**
   * Zeigt die erste Adresse im Subnetz, die einem Host zugewiesen werden kann, beispielsweise "192.168.0.1", was den Beginn des verfügbaren Adressbereichs markiert.

9. **Letzte nutzbare Adresse (Last address)**
   * Gibt die letzte Adresse im Subnetz an, die einem Host zugewiesen werden kann, wie z.B. "192.168.0.254", wodurch das Ende des verfügbaren Adressraums markiert wird.

10. **Broadcast-Adresse (Broadcast address)**
    * Liefert die Broadcast-Adresse dieses Subnetzes, z.B. "192.168.0.255", die verwendet wird, um Nachrichten an alle Hosts innerhalb des Subnetzes zu senden.

11. **IP-Klasse (IP class)**
    * Zeigt die Klasse, der die IP-Adresse angehört, beispielsweise "C", um dem Nutzer einen besseren Überblick über die Einordnung der IP-Adresse zu geben.