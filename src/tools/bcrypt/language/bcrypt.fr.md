# Manuel d'utilisation de l'outil de chiffrement de texte

## 1. Présentation de l'outil

Cet outil de chiffrement de texte est un puissant logiciel basé sur l'algorithme bcrypt. Il permet de chiffrer des textes et de comparer les valeurs de hachage avec le texte original, ce qui peut être utilisé dans des scénarios liés à la sécurité tels que le stockage et la vérification de mots de passe.

## 2. Accès à l'outil

Saisissez l'URL de la page sur laquelle se trouve cet outil dans la barre d'adresse du navigateur, appuyez sur la touche "Entrée" pour accéder à la page et attendez que tous les éléments de la page soient entièrement chargés.

## 3. Guide d'utilisation

### (1) Chiffrer un texte

1. **Saisir le texte** : Dans la zone de saisie "Your string", entrez le contenu textuel que vous souhaitez chiffrer. Par exemple, le mot de passe défini par un utilisateur lors de son inscription.
2. **Configurer Salt count** : Cliquez sur les boutons "+" ou "-" à côté de "Salt count" pour régler le nombre d'itérations du sel (Salt). Le sel est une chaîne générée aléatoirement qui est ajoutée au texte original avant le chiffrement, afin d'améliorer la sécurité et d'éviter les attaques par tables arc-en-ciel. En général, il est recommandé de ne pas descendre en dessous de 10 itérations.
3. **Visualiser le résultat du chiffrement** : Une fois les paramètres ci-dessus effectués, l'outil chiffre automatiquement le texte saisi et affiche le hash résultant dans la case inférieure. Ce hash contient des informations sur l'algorithme de chiffrement utilisé, la valeur du sel et le texte chiffré. Par exemple : "$2a$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/Dk5Esl7bj1sXA.xK".