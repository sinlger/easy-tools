# Documentation utilisateur du générateur de paires de clés RSA

## 1. Présentation de l'outil

Cet outil en ligne permet de générer facilement des certificats PEM aléatoires contenant une clé privée et une clé publique RSA. Il est particulièrement utile pour les développeurs qui ont besoin de créer rapidement une paire de clés RSA pendant leur processus de développement.

## 2. Description des fonctionnalités

### (1) **Configuration de la longueur de la clé**

* **Fonction** : L'utilisateur peut définir la longueur de la clé (exprimée en bits) au sein d'une plage déterminée.
* **Action** : Saisissez dans le champ "Bits" la longueur souhaitée, comme par exemple 2048 bits, valeur couramment utilisée. L'outil prend en charge une plage spécifique de longueurs, garantissant que la clé générée répondra aux exigences de sécurité et d'utilisation.
* **Objectif** : En général, plus la longueur de la clé est grande, plus elle est sécurisée, mais cela peut réduire la vitesse de chiffrement et de déchiffrement. Il convient donc de choisir cette longueur en fonction du cas d'utilisation concret.

### (2) **Actualisation de la paire de clés**

* **Fonction** : Permet de générer rapidement une nouvelle paire de clés RSA aléatoire.
* **Action** : Cliquez sur le bouton "Refresh key-pair", le système recréera une nouvelle paire composée d'une clé publique et d'une clé privée, basée sur la longueur actuelle configurée.
* **Objectif** : Lorsque vous avez besoin de générer plusieurs paires de clés différentes pour des tests ou un usage direct, il suffit simplement d'appuyer sur le bouton Refresh sans avoir à modifier manuellement d'autres paramètres. Cela accélère ainsi votre travail.

### (3) **Clé publique - Affichage et gestion**

* **Fonction** : Affiche la clé publique RSA générée et propose des opérations pratiques pour son utilisation.
* **Présentation** : Dans la zone "Public key", la clé publique apparaît au format standard PEM, y compris les balises "-----BEGIN PUBLIC KEY-----" et "-----END PUBLIC KEY-----", ce qui permet de l'utiliser immédiatement dans vos applications.
* **Fonction de copie** : Le bouton Copier situé à côté permet à l'utilisateur de copier facilement la clé publique dans le presse-papiers pour la coller ailleurs, comme dans des fichiers de configuration ou des segments de code.

### (4) **Clé privée - Affichage et gestion**

* **Fonction** : Affiche la clé privée RSA générée et offre une méthode simple pour l'utiliser.
* **Présentation** : Dans la section "Private key", le format PEM standard est également utilisé, avec les balises "-----BEGIN RSA PRIVATE KEY-----" et "-----END RSA PRIVATE KEY-----", permettant à l'utilisateur d'utiliser cette clé pour effectuer des opérations telles que le chiffrement, le déchiffrement ou la signature numérique.
* **Fonction de copie** : Le bouton Copier adjacent facilite la copie rapide de la clé privée afin qu'elle puisse être utilisée dans des environnements sécurisés, par exemple pour son stockage sur un serveur ou sa configuration dans une application.

## 3. Exemples de cas d'utilisation

1. Les développeurs travaillant sur des applications basées sur l'algorithme de chiffrement RSA peuvent utiliser cet outil lorsqu'ils ont besoin de clés de test rapides. Ils peuvent choisir une longueur adaptée, générer une paire de clés via le bouton Refresh, puis utiliser la clé publique pour chiffrer et la clé privée pour tester le déchiffrement.
2. Lors de la mise en place de protocoles de communication sécurisés (comme SSL/TLS), si vous devez disposer d'un certificat auto-signé ou d'une paire de clés pour un environnement de test, vous pouvez les produire ici, puis configurer respectivement la clé publique et la clé privée dans les endroits appropriés sur le serveur et le client.