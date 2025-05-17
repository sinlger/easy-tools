# Documentation du Générateur HMAC en Ligne d'A Toolio

## 1. Description de l'Outil

Le générateur HMAC en ligne d'A Toolio permet de calculer des codes d'authentification de messages basés sur le hachage (HMAC) à partir d'une clé secrète et d'une fonction de hachage. Cet outil est particulièrement utile pour les développeurs devant générer rapidement des HMAC dans divers contextes de développement.

## 2. Description des Fonctions

### Section d'Entrée

1. **Texte en clair** - Saisissez le texte que vous souhaitez utiliser pour le calcul de hachage.
2. **Clé secrète** - Entrez la clé secrète utilisée pour générer l'HMAC.
3. **Fonction de hachage** - Sélectionnez une fonction de hachage. Par défaut, SHA256 est sélectionné, mais vous pouvez choisir d'autres fonctions si nécessaire.
4. **Encodage de sortie** - Choisissez le format d'encodage souhaité. Par défaut, le format hexadécimal (base 16) est utilisé, mais d'autres formats sont également disponibles.

### Section de Sortie

1. **HMAC of your text** - Affiche la valeur HMAC générée. Un bouton de copie facilite le transfert du résultat.

## 3. Étapes d'Utilisation

**Étape 1 : Entrée du texte brut et de la clé**

Saisissez dans le champ "Texte en clair" le contenu dont vous souhaitez obtenir le haché, puis entrez dans le champ "Clé secrète" la clé utilisée pour générer l'HMAC. Ces données de base doivent être saisies avec précision.

**Étape 2 : Choisir la fonction de hachage**

Depuis le menu déroulant "Fonction de hachage", sélectionnez la fonction désirée comme SHA256 ou SHA1, en fonction de vos besoins spécifiques. Différentes fonctions produiront des résultats HMAC différents.

**Étape 3 : Choisir le format d'encodage de sortie**

Sélectionnez dans le menu "Encodage de sortie" le format d'encodage souhaité pour afficher la valeur HMAC générée, par exemple le format hexadécimal (base 16) ou Base64.

**Étape 4 : Générer et consulter l'HMAC**

Après avoir effectué les étapes ci-dessus, le système calcule automatiquement la valeur HMAC et l'affiche dans la zone "HMAC of your text". Vous pouvez visualiser directement le résultat.

**Étape 5 : Copier l'HMAC**

Si vous avez besoin d'utiliser cette valeur, cliquez sur le bouton de copie situé à côté du résultat pour la placer dans le presse-papiers et pouvoir la coller ailleurs.