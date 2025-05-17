# Documentation des Codes HTTP

## 1. Introduction

Les codes d'état HTTP sont des codes numériques à trois chiffres envoyés par le serveur en tant que partie de la réponse HTTP au client (généralement un navigateur web). Ils indiquent l'état d'une requête et permettent de comprendre si celle-ci a réussi, si une redirection est nécessaire ou si une erreur s'est produite.

## 2. Principales Catégories des Codes d'État HTTP

### 1xx : Réponses Informatives

Ces codes signalent que la requête a été comprise et que le serveur continue de traiter. Exemples :
- **100 Continue** - Le client devrait poursuivre sa requête.
- **101 Switching Protocols** - Le client a demandé un changement de protocole de communication, par exemple passer de HTTP à WebSocket.

### 2xx : Requête Réussie

Ces codes signifient que la requête a été correctement reçue, interprétée et acceptée. Exemples :
- **200 OK** - La requête a abouti et les données demandées ont été trouvées et transmises.
- **201 Created** - Une ressource a été créée avec succès, souvent après une requête POST.
- **204 No Content** - La requête a été exécutée avec succès, mais il n'y a aucun contenu à renvoyer.