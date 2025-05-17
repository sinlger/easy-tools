# Documentation utilisateur du décodeur Outlook Safelink

## 1. Présentation de l'outil
Le **décodeur Outlook Safelink** est un outil conçu pour décoder les liens générés par le service de messagerie Microsoft Outlook sous le nom de SafeLink. Cet outil permet de transformer les liens chiffrés produits par Outlook SafeLink en leurs URL d'origine, facilitant ainsi aux utilisateurs l'identification du véritable destinataire de ces liens.

## 2. Description des fonctionnalités
La principale fonctionnalité de cet outil est de décoder les liens Outlook Safelink, c'est-à-dire convertir les liens chiffrés et redirigés créés par Microsoft Outlook en adresses web originales.

## 3. Instructions d'utilisation

### Entrée
Collez dans le champ d'entrée le lien Safelink Outlook que vous souhaitez décoder. Ce lien a été chiffré par Microsoft Outlook à des fins de sécurité et possède un format spécifique.

### Sortie
Après avoir cliqué sur le bouton "Decode", l'outil traitera le lien saisi et affichera dans la zone de sortie l'URL originale décodée. Si le lien n'est pas correctement formaté ou ne peut pas être reconnu, un message d'erreur s'affichera : "Error: Invalid SafeLinks URL provided" (Erreur : Lien SafeLinks non valide fourni).

## 4. Exemples d'utilisation

### Exemple 1
Entrée (lien Safelink) :
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Résultat après décodage :
`https://example.com`

### Exemple 2
Entrée (lien Safelink) :
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Résultat après décodage :
`https://microsoft.com`

### Exemple 3
Entrée d'un lien invalide ou mal formaté :
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Message d'erreur :
`Error: Invalid SafeLinks URL provided`

## 5. Remarques importantes
- Vérifiez que le lien saisi est un lien complet Outlook Safelink.