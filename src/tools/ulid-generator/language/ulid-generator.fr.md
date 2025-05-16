# Documentation utilisateur du générateur ULID

## 1. Présentation de l'outil
Le générateur ULID permet de créer des identifiants universels uniques aléatoires triables lexicographiquement (ULID). Les identifiants générés sont à la fois uniques et triables, et sont largement utilisés dans les systèmes distribués, les identifiants d'enregistrements de bases de données, etc.

## 2. Description des fonctionnalités

### (1) Réglage de la quantité
L'option "Quantity" permet de définir le nombre d'ULID à générer. La valeur initiale est de 1, il est possible d'ajuster cette quantité en cliquant sur les boutons plus/moins situés à droite.

### (2) Choix du format
Deux formats de sortie sont proposés :
1. **Raw** : Affiche les ULID sous forme de texte brut, pratique pour une visualisation et utilisation directes.
2. **JSON** : Exporte les ULID générés au format JSON, ce qui facilite leur utilisation et analyse par des programmes.

### (3) Génération et opérations
Cliquez sur le bouton "Refresh" pour générer de nouveaux ULID ; cliquez sur "Copy" pour copier les ULID générés dans le presse-papier, vous permettant ainsi de les coller facilement ailleurs.

## 3. Exemples

### Exemple 1 : Générer un seul ULID (format Raw)
Réglez "Quantity" sur 1 et sélectionnez le format "Raw", puis cliquez sur "Refresh". Un ULID similaire à celui-ci sera généré :
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Exemple 2 : Générer plusieurs ULID (format JSON)
Réglez "Quantity" sur 3 et sélectionnez le format "JSON", puis cliquez sur "Refresh". Les ULID seront générés dans le format JSON suivant :
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}