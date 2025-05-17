# Documentation utilisateur du convertisseur TOML en YAML

## Aperçu

TOML en YAML est un outil en ligne qui permet aux utilisateurs de convertir facilement des fichiers de configuration au format TOML (Tom's Obvious, Minimal Language) en format YAML (YAML Ain't Markup Language). Cet outil est particulièrement utile pour les développeurs souhaitant migrer des configurations entre différents systèmes ou intégrer plusieurs technologies.

## Conception de l'interface

L'interface de l'outil est simple et intuitive, comprenant principalement les éléments suivants :

1. Champ de texte gauche : il s'agit de la zone où les utilisateurs peuvent saisir ou coller du texte au format TOML, intitulé "Votre TOML".
2. Champ de texte droit : utilisé pour afficher le texte converti au format YAML, intitulé "YAML à partir de votre TOML".
3. Bouton de conversion central : après avoir saisi le texte TOML, les utilisateurs peuvent cliquer sur ce bouton pour effectuer la conversion.

## Description des fonctionnalités

### Saisie du texte TOML

- Les utilisateurs peuvent saisir directement du texte de configuration au format TOML dans le champ de texte de gauche.
- Ils peuvent également copier du texte TOML depuis d'autres fichiers ou éditeurs et le coller dans ce champ de texte.

### Opération de conversion

- Une fois le texte TOML saisi ou collé, cliquez sur le bouton de conversion central. Le système analysera immédiatement le texte TOML saisi et le convertira en format YAML.
- Une fois la conversion terminée, le texte YAML résultant s'affichera dans le champ de texte de droite.

### Visualisation du résultat YAML

- Le champ de texte de droite affiche intégralement le texte YAML converti.
- À cet endroit, les utilisateurs peuvent vérifier si le résultat de la conversion est précis et si la structure du texte YAML correspond à leurs attentes.

### Copie du texte YAML

- Les utilisateurs peuvent sélectionner et copier l'intégralité du texte YAML présent dans le champ de texte de droite, ce qui est pratique pour l'utiliser ailleurs, par exemple en le collant dans des fichiers de configuration ou en l'envoyant à d'autres personnes.

## Exemples

### Exemple 1 : Conversion basique

**Entrée au format TOML :**

```toml
# Ceci est un exemple simple de TOML
title = "Exemple de TOML"

[author]
name = "Zhang San"
age = 28
e-mail = "zhangsan@example.com"
```

**Sortie au format YAML :**

```yaml
# Ceci est l'exemple converti en YAML
title: Exemple de TOML

author:
  name: Zhang San
  age: 28
  e-mail: zhangsan@example.com
```

### Exemple 2 : Conversion de structures complexes

**Entrée au format TOML :**

```toml
# Exemple de TOML avec une structure plus complexe
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**Sortie au format YAML :**

```yaml
# Exemple de YAML avec une structure plus complexe
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Remarques importantes

- Si le format TOML saisi n'est pas correct, la conversion pourrait échouer et le système pourrait afficher des messages d'erreur.
- L'outil prend en charge la plupart des structures syntaxiques TOML courantes, mais pour certains éléments de syntaxe spéciaux ou peu utilisés, une conversion parfaite pourrait ne pas être possible.
- Le texte YAML généré peut présenter de légères différences de format selon la version et les spécifications de YAML utilisées.