# Documentation du Convertisseur Docker Run vers Docker-Compose

## 1. Présentation de l'Outil

Le convertisseur Docker Run vers Docker-Compose est un outil en ligne pratique qui aide les développeurs à transformer des commandes "docker run" en fichiers Docker-Compose. Cela simplifie le processus de configuration d'orchestration des conteneurs et améliore l'efficacité du développement.

## 2. Fonctions Principales

1. **Conversion des Commandes**
   * Les utilisateurs peuvent coller des commandes Docker complexes, telles que "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx", dans un champ d'entrée dédié.
   * L'outil analyse automatiquement tous les paramètres de la commande "docker run", notamment le mappage des ports ("-p 80:80"), le montage des volumes ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), les politiques de redémarrage ("--restart always"), les options de journalisation ("--log-opt max-size=1g") et le nom de l'image ("nginx").

2. **Génération des Fichiers Docker-Compose**
   * À partir des paramètres extraits de la commande "docker run", l'outil génère le contenu correspondant du fichier Docker-Compose.
   * Le fichier YAML produit inclut la déclaration de version (par exemple "version: '3.9'"), les définitions de services ("services"), la spécification de l'image ("image"), la configuration du journal ("logging" avec "options"), les paramètres de redémarrage ("restart"), les montages de volumes ("volumes") et les mappages de ports ("ports"). Ainsi, toutes les informations nécessaires pour orchestrer les conteneurs sont présentées de manière complète, permettant aux utilisateurs de les utiliser directement ou de les modifier selon leurs besoins.

3. **Téléchargement du Fichier**
   * Un bouton intitulé "Download docker-compose.yml" permet aux utilisateurs de télécharger facilement le fichier Docker-Compose généré sur leur machine locale, ce qui facilite son utilisation dans des environnements réels de projets.