# Analyseur d'URL

## 1. Aperçu de l'outil
L'analyseur d'URL est un outil en ligne permettant d'analyser les chaînes d'URL, capable de décomposer des URL complexes en plusieurs composants tels que le protocole, le nom d'utilisateur, le mot de passe, le nom d'hôte, le port, le chemin d'accès, les paramètres, etc., facilitant ainsi aux développeurs de comprendre rapidement la structure et les informations détaillées de l'URL, ce qui est pratique pour construire, déboguer et analyser des requêtes réseau.

## 2. Détails des fonctionnalités

  1. **Champ de saisie**
     * Fournit un champ de saisie dans lequel vous pouvez entrer la chaîne d'URL à analyser.

  2. **Affichage des résultats d'analyse**
     * **Protocole (Protocol)** : Affiche la partie du protocole de l'URL, par exemple "https:", indiquant le protocole de transmission réseau utilisé par l'URL.
     * **Nom d'utilisateur (Username)** : Si l'URL contient des informations sur le nom d'utilisateur, celles-ci seront affichées ici, utilisées pour identifier l'identité de l'utilisateur fournie dans l'URL.
     * **Mot de passe (Password)** : Affiche la partie du mot de passe dans l'URL, associée au nom d'utilisateur, utilisée pour l'authentification de l'identité de l'utilisateur.
     * **Nom d'hôte (Hostname)** : Affiche le nom de domaine correspondant à l'URL, par exemple "atoolio.com", représentant le nom du serveur cible.
     * **Port (Port)** : Affiche le numéro de port spécifié dans l'URL, utilisé pour déterminer le port spécifique sur le serveur où le service est disponible. Par défaut, différents protocoles ont des ports par défaut différents, par exemple le port 80 pour HTTP et le port 443 pour HTTPS.
     * **Chemin d'accès (Path)** : Affiche la partie du chemin d'accès dans l'URL, par exemple "/url-parser", pointant vers un emplacement spécifique de ressource ou de service sur le serveur.
     * **Paramètres (Params)** : Liste la partie des paramètres de requête dans l'URL, commençant par "?", suivie de plusieurs paires "clé-valeur" comme paramètres, par exemple "?key1=value&key2=value2", utilisés pour envoyer des informations supplémentaires et des instructions au serveur.
     * **Affichage détaillé des paramètres** : Chaque paire clé-valeur des paramètres de requête est affichée individuellement, montrant clairement le nom de chaque paramètre et sa valeur correspondante.

## 3. Étapes d'utilisation

  1. Ouvrez votre navigateur et visitez la page web [Analyseur d'URL](https://atoolio.com/url-parser).
  2. Dans le champ de saisie, entrez la chaîne d'URL que vous souhaitez analyser, par exemple "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Cliquez sur le bouton d'analyse (normalement, appuyer sur Entrée peut également déclencher l'analyse), l'outil analysera automatiquement l'URL saisie et affichera les informations détaillées de chaque composant ci-dessous.
  4. Consultez les résultats de l'analyse et, si nécessaire, copiez le contenu correspondant des composants pour l'utiliser dans des tâches ultérieures de développement, de débogage ou d'autres opérations.

## 4. Exemples

  1. **Exemple 1**
     * URL saisie : "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Résultat de l'analyse :
       * Protocole : http:
       * Nom d'utilisateur : user
       * Mot de passe : pass
       * Nom d'hôte : example.com
       * Port : 8080
       * Chemin d'accès : /page
       * Paramètres : ?param1=hello&param2=world
       * Affichage détaillé des paramètres :
         * param1 : hello
         * param2 : world

  2. **Exemple 2**
     * URL saisie : "https://www.google.com/s?wd=Analyseur d'URL"
     * Résultat de l'analyse :
       * Protocole : https:
       * Nom d'utilisateur : (aucun)
       * Mot de passe : (aucun)
       * Nom d'hôte : www.google.com
       * Port : (port par défaut 443, non affiché)
       * Chemin d'accès : /s
       * Paramètres : ?wd=Analyseur d'URL
       * Affichage détaillé des paramètres :
         * wd : Analyseur d'URL