# Documentation utilisateur de l'outil en ligne de conversion TOML en JSON

## 1. Présentation de l'outil

TOML en JSON est un outil en ligne pratique qui analyse les données au format TOML et les convertit en format JSON. Les utilisateurs peuvent facilement coller ou saisir des données TOML dans le champ d'entrée à gauche, et le résultat correspondant au format JSON sera généré automatiquement à droite.

## 2. Description détaillée des fonctionnalités

### 1. Saisie des données TOML

* Dans le champ de texte à gauche intitulé "Your TOML", les utilisateurs peuvent coller ou saisir manuellement des données au format TOML. Ce champ de texte prend en charge la saisie de texte multiligne et offre suffisamment d'espace pour entrer des informations de configuration TOML plus complexes.

### 2. Affichage du résultat JSON

* Dès que des données TOML sont saisies dans le champ de texte à gauche, l'outil effectue automatiquement l'analyse et la conversion. Les données JSON converties s'affichent alors dans le champ de texte à droite intitulé "JSON from your TOML". Les utilisateurs peuvent visualiser ces données, les copier ou les traiter ultérieurement.

## 3. Étapes d'utilisation

1. Ouvrez la page de l'outil ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. Dans le champ de texte à gauche intitulé "Your TOML", collez ou saisissez les données TOML que vous souhaitez convertir.
3. Le système effectuera automatiquement la conversion, et le résultat s'affichera dans le champ de texte à droite intitulé "JSON from your TOML".

## 4. Fonctionnalités principales

* Interface simple et intuitive : L'interface est claire et facile à utiliser, avec un processus d'opération simple ne nécessitant aucune configuration complexe, ce qui permet aux utilisateurs de commencer rapidement à l'utiliser.
* Conversion en temps réel : Une fois les données TOML saisies, l'outil effectue automatiquement la conversion et affiche le résultat, sans avoir à cliquer manuellement sur un bouton de conversion, ce qui améliore l'efficacité de la conversion.
* Utilisation en ligne : Aucun logiciel n'a besoin d'être installé. Tant que vous disposez d'un appareil connecté à Internet, vous pouvez utiliser cet outil à tout moment et en tout lieu pour convertir des données TOML en JSON.

## 5. Exemples

### Exemple 1 : Conversion simple de TOML en JSON

Supposons que nous ayons les données suivantes au format TOML :
```toml
title = "TOML Example"
owner = "John Doe"
```

En collant ces données dans le champ de texte à gauche intitulé "Your TOML", l'outil les convertira automatiquement en format JSON comme suit :
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Exemple 2 : Conversion de TOML en JSON avec une structure imbriquée

Nous disposons de données TOML plus complexes :
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Après les avoir saisies dans l'outil, nous obtiendrons les données JSON suivantes :
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}