# Documentation du Calculateur de Sous-réseaux IPv4

Le calculateur de sous-réseaux IPv4 est un outil en ligne pratique qui permet d'analyser des blocs CIDR IPv4 et d'obtenir des informations détaillées sur les sous-réseaux. Voici une présentation de ses fonctionnalités et des instructions d'utilisation :

## 1. Fonction d'entrée

Dans la zone de saisie, l'utilisateur peut entrer une adresse IPv4 avec ou sans masque de sous-réseau. Par exemple, il peut taper "192.168.0.1/24", et l'outil effectuera les calculs nécessaires à partir de cette donnée.

## 2. Résultats des calculs

1. **Masque réseau (Netmask)**
   * Affiche la combinaison de l'adresse IPv4 et de son masque sous la forme CIDR, comme "192.168.0.0/24", permettant à l'utilisateur de comprendre clairement le périmètre du réseau.

2. **Adresse réseau (Network address)**
   * Indique l'adresse du réseau au sein du sous-réseau, une adresse spéciale représentant tout le réseau. Par exemple, "192.168.0.0" montre le point de départ du sous-réseau.

3. **Masque réseau (Network mask)**
   * Présente le masque de sous-réseau sous forme décimale, comme "255.255.255.0", pour identifier la limite entre la partie réseau et la partie hôte dans l'adresse IP.

4. **Masque réseau en binaire (Network mask in binary)**
   * Représente le masque de sous-réseau en format binaire, par exemple "11111111.11111111.11111111.00000000", ce qui facilite la compréhension de son fonctionnement.

5. **Notation CIDR (CIDR notation)**
   * Fournit la représentation CIDR du masque de sous-réseau, comme "/24", une écriture concise indiquant sa longueur, utile pour comprendre rapidement comment le réseau est segmenté.

6. **Masque générique (Wildcard mask)**
   * Donne la valeur du masque générique, tel que "0.0.0.255", complémentaire du masque de sous-réseau, souvent utilisé dans certaines configurations de matériel et logiciel réseau.

7. **Taille du réseau (Network size)**
   * Informe du nombre total d'adresses IP disponibles dans le sous-réseau, par exemple "256", permettant à l'utilisateur de connaître sa capacité globale.

8. **Première adresse utilisable (First address)**
   * Montre la première adresse pouvant être attribuée à un hôte dans le sous-réseau, comme "192.168.0.1", marquant ainsi le début de la plage d'adresses disponibles.

9. **Dernière adresse utilisable (Last address)**
   * Présente la dernière adresse pouvant être assignée à un hôte dans le sous-réseau, par exemple "192.168.0.254", définissant ainsi la fin de la plage d'adresses disponibles.

10. **Adresse de diffusion (Broadcast address)**
    * Fournit l'adresse de diffusion du sous-réseau, telle que "192.168.0.255", utilisée pour envoyer des messages à tous les hôtes présents sur le sous-réseau.

11. **Classe de l'adresse IP (IP class)**
    * Indique la classe à laquelle appartient l'adresse IP, comme "C", facilitant ainsi la compréhension de sa classification.

## 3. Fonctionnalité de Navigation

Des boutons intitulés "Bloc précédent (Previous block)" et "Bloc suivant (Next block)" sont mis à disposition pour permettre à l'utilisateur de passer facilement d'un bloc adjacent à l'autre et d'en visualiser les données.