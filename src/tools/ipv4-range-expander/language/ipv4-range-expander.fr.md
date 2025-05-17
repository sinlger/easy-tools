# Documentation de l'outil Étendeur de Plage IPv4

## 1. Présentation de l'Outil

L'Étendeur de Plage IPv4 permet de calculer des réseaux IPv4 efficaces à partir d'une adresse IPv4 initiale et d'une adresse IPv4 finale données. Cela inclut des blocs réseau valides (exprimés en notation CIDR), les plages d'adresses, ainsi que le nombre total d'adresses disponibles dans cette plage.

## 2. Détails des Fonctionnalités

### (A) Fonction d'Entrée de Base

1. **Saisie de l'Adresse Initiale** - Dans le champ "Start address", entrez une adresse IPv4 qui servira de point de départ, par exemple "192.168.1.1".
2. **Saisie de l'Adresse Finale** - Dans le champ "End address", entrez une adresse IPv4 qui agira comme point final, comme "192.168.6.255".

### (B) Traitement Automatique et Affichage des Résultats

1. **Ajustement de la Plage d'Adresses** - L'outil ajuste automatiquement les adresses initiale et finale pour obtenir une plage plus adaptée. Par exemple, "192.168.1.1" sera converti en "192.168.0.0", et "192.168.6.255" deviendra "192.168.7.255".
2. **Calcul du Nombre d'Adresses** - Le nombre total d'adresses IPv4 disponibles dans la nouvelle plage est calculé, passant par exemple de "1.535" à "2.048", ce qui améliore l'efficacité d'utilisation des adresses.
3. **Génération de la Notation CIDR** - La notation CIDR correspondante à la nouvelle plage d'adresses est affichée, telle que "192.168.0.0/21", facilitant ainsi la gestion et la configuration réseau.

## 3. Remarques Importantes

Assurez-vous que les adresses initiale et finale saisies respectent le format correct des adresses IPv4 afin de garantir un fonctionnement approprié de l'outil et des résultats précis.