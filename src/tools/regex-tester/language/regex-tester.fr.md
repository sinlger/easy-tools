# Documentation utilisateur du Regex Tester d'A Toolio

## 1. Présentation de l'outil

Le **Regex Tester d'A Toolio** est un outil en ligne permettant de tester des expressions régulières à travers l'entrée de textes d'exemple. Grâce à son interface claire et ses fonctions pratiques, il convient aussi bien aux débutants qu'aux développeurs expérimentés.

## 2. Description détaillée des fonctionnalités

### (1) Zone de saisie des expressions régulières

Saisissez dans le champ de texte l'expression régulière que vous souhaitez tester. Un lien vers une table de référence rapide pour les expressions régulières est également fourni pour vous aider pendant l'utilisation. Par exemple, l'expression régulière \w+ peut être utilisée pour trouver un ou plusieurs mots.

### (2) Options du Regex Tester

Les options disponibles sont : Recherche globale (g), Ignorer la casse (i), Mode multiligne (m), Mode monoligne (s), Support Unicode (u) et Support des jeux Unicode (v). Sélectionnez les options appropriées selon vos besoins spécifiques.

- Recherche globale (g) : Recherche toutes les occurrences dans l'ensemble du texte.
- Ignorer la casse (i) : Trouve des correspondances en ignorant les différences entre majuscules et minuscules.
- Mode multiligne (m) : Traite l'entrée comme un texte composé de multiples lignes, ce qui permet de rechercher au début et à la fin de chaque ligne.
- Mode monoligne (s) : Considère l'ensemble du texte comme une seule ligne, facilitant ainsi les recherches sur plusieurs lignes.
- Support Unicode (u) : Active le support des caractères Unicode.
- Support des jeux Unicode (v) : Prend en charge les jeux de caractères Unicode avancés.

Exemple : L'expression régulière \d{3}-\d{3}-\d{4} peut identifier plusieurs numéros de téléphone dans un texte lorsque la recherche globale est activée.

### (3) Zone de saisie du texte à analyser

Entrez dans le champ de texte le contenu dans lequel vous souhaitez trouver des correspondances. L'outil effectue la recherche en se basant sur l'expression régulière saisie et les options sélectionnées. Par exemple, en utilisant l'expression régulière \w+, vous pouvez extraire tous les mots individuels du texte "Trouver les mots dans ce texte".