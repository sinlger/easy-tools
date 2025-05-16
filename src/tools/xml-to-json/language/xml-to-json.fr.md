# Outil de Conversion XML en JSON

## 1. Introduction
Cet outil en ligne permet de convertir des données au format XML en format JSON. Il améliore l'efficacité du développement et convient aux scénarios nécessitant une conversion entre les formats de données XML et JSON.

## 2. Fonctions Principales

### (1) Saisie du Contenu XML
Collez ou saisissez les données XML que vous souhaitez convertir dans la zone d'entrée. Par exemple, vous pouvez entrer le contenu XML suivant :
```
<a x="1.234" y="It's"/>
```

### (2) Résultat de Données JSON
Après avoir cliqué sur le bouton de conversion, l'outil affichera les données correspondantes au format JSON dans la zone de sortie. Par exemple, le XML ci-dessus sera converti en données JSON suivantes :
```json
{
  "a": {
    "_attributs": {
      "x": "1.234",
      "y": "It's"
    }
  }
}
```

### (3) Fonction de Copie
Dans la zone de sortie des données JSON, vous pouvez cliquer sur le bouton de copie pour transférer les données JSON générées vers le presse-papiers, ce qui facilite leur utilisation ailleurs.