# Documentation du Convertisseur d'Adresses IPv4

## 1. Présentation de l'Outil

Le convertisseur d'adresses IPv4 est un outil en ligne permettant de convertir des adresses IPv4 dans différents systèmes numériques (décimal, hexadécimal, binaire) ainsi qu'en format IPv6. Cet outil est utile pour les développeurs et les techniciens réseau qui ont besoin d'obtenir rapidement différentes formes de représentation des adresses IPv4, ce qui facilite la configuration réseau, le développement logiciel ou encore l'analyse de sécurité informatique.

## 2. Description des Fonctions

### (A) Saisie de l'Adresse IPv4
- Dans le champ d'entrée de l'outil, l'utilisateur peut saisir directement une adresse IPv4 valide (par exemple : 192.168.1.1). Une fois la saisie effectuée, il suffit de cliquer sur le bouton "Convertir" ou d'appuyer sur la touche Entrée pour que l'outil lance automatiquement plusieurs conversions.

### (B) Conversion en Décimal
- **Fonction** : Convertir l'adresse IPv4 en un nombre décimal.
- **Méthode d'utilisation** : Après avoir saisi l'adresse IPv4, l'outil calcule automatiquement la valeur décimale correspondante. Cette valeur est obtenue en convertissant chacun des quatre octets de l'adresse IPv4 en nombres décimaux, puis en les combinant selon un schéma spécifique.

### (C) Conversion en Hexadécimal
- **Fonction** : Convertir l'adresse IPv4 en une chaîne hexadécimale.
- **Méthode d'utilisation** : Lorsque l'adresse IPv4 est saisie, chaque octet est transformé en un nombre hexadécimal à deux chiffres, puis assemblé en une chaîne complète. Par exemple, l'adresse IPv4 192.168.1.1 devient C0A80101 après conversion.

### (D) Conversion en Binaire
- **Fonction** : Transformer l'adresse IPv4 en une forme binaire.
- **Méthode d'utilisation** : Lors de la saisie de l'adresse IPv4, chaque octet est converti en un nombre binaire de 8 bits, puis les quatre octets sont reliés pour former une chaîne binaire de 32 bits. Ainsi, l'adresse IPv4 192.168.1.1 devient par exemple 11000000101010000000000100000001.

### (E) Conversion au Format IPv6
- **Fonction** : Convertir l'adresse IPv4 en représentation IPv6.
- **Méthode d'utilisation** : L'outil produit deux formats IPv6 :
  1. **Adresse IPv6 Complète** : Les 8 premiers octets sont remplis de zéros, les 8 derniers octets correspondent à la forme hexadécimale de l'adresse IPv4, avec l'ajout de "ffff" devant cette partie IPv4 comme identifiant. Exemple : À partir de l'adresse IPv4 192.168.1.1, on obtient l'adresse IPv6 complète suivante : 0000:0000:0000:0000:0000:ffff:c0a8:0101.