# Documentation de l'analyseur d'agent utilisateur en ligne

## 1. Présentation de l'outil

L'analyseur d'agent utilisateur en ligne permet de détecter et analyser avec précision les informations concernant le navigateur, le moteur de rendu, le système d'exploitation, l'architecture du processeur (CPU) ainsi que le type/modèle de l'appareil à partir de la chaîne d'agent utilisateur. Cet outil aide les développeurs à obtenir rapidement des détails relatifs au client.

## 2. Description des fonctionnalités

### (1) Détection du navigateur

Il peut identifier précisément le type de navigateur utilisé par l'utilisateur ainsi que sa version exacte. Par exemple, si après avoir saisi une chaîne donnée, il affiche "Edge 135.0.0.0", cela signifie que le navigateur du client est Edge, et la version est 135.0.0.0.

### (2) Détection du moteur de rendu

Il présente clairement le moteur de rendu utilisé par le navigateur ainsi que sa version correspondante. Par exemple, "Blink 135.0.0.0" indique que le moteur de rendu est Blink, et la version est 135.0.0.0.

### (3) Détection du système d'exploitation

Il affiche en détail le nom du système d'exploitation et sa version. Par exemple, "Windows 10" signifie que le système d'exploitation est Windows, et la version est 10.

### (4) Détection des informations sur l'appareil

Il permet d'obtenir des informations telles que le type d'appareil, son modèle ou encore son fabricant (si disponibles). Certains appareils peuvent afficher leur modèle complet. Toutefois, dans certains cas, aucune information sur le modèle, le type ou le fabricant de l'appareil n'est disponible, et un message correspondant s'affichera alors : "No device model/type/vendor available".

### (5) Détection des informations sur le processeur (CPU)

Il permet également d'identifier les caractéristiques liées au processeur (CPU). Par exemple, si "amd64" s'affiche, cela indique que l'architecture du processeur est de type amd64.

## 3. Exemples d'utilisation

### Exemple 1 : Cas courant d'un navigateur sur ordinateur de bureau

Supposons que la chaîne d'agent utilisateur soit la suivante :
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Après avoir entré cette chaîne dans l'analyseur :

  * **Navigateur** : On identifie qu'il s'agit d'Edge 135.0.0.0.
  * **Moteur** : Il est reconnu comme étant Blink 135.0.0.0.
  * **Système d'exploitation** : Il s'agit de Windows 10.
  * **Appareil** : Aucun modèle, type ni fabricant spécifique de l'appareil n'est disponible, un message approprié s'affiche donc.
  * **Processeur (CPU)** : L'architecture est amd64.

### Exemple 2 : Navigateur sur appareil mobile

Prenons comme exemple la chaîne d'agent utilisateur suivante :
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Après l'avoir saisie dans l'analyseur :

  * **Navigateur** : On peut identifier le navigateur Safari sous iOS ainsi que sa version exacte (la version précise dépendra du résultat de l'analyse).
  * **Moteur** : Le moteur Webkit correspondant avec ses détails de version sera affiché.
  * **Système d'exploitation** : Il sera clairement identifié comme iOS, accompagné de son numéro de version (par exemple, 16_6_1).
  * **Appareil** : Des informations sur l'appareil pourront être obtenues, comme le fait qu'il s'agisse d'un iPhone (le modèle précis dépendra des résultats d'analyse).
  * **Processeur (CPU)** : L'architecture du processeur adaptée aux appareils mobiles sera affichée (si identifiable).