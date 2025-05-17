# Documentation utilisateur de l'outil de mise en forme et d'embellissement SQL

## 1. Présentation générale de l'outil

L'outil de mise en forme et d'embellissement SQL est une plateforme en ligne utilisée pour formater et embellir les requêtes SQL écrites. Il prend en charge plusieurs dialectes SQL, aidant ainsi les développeurs à lire et écrire plus facilement du code SQL.

## 2. Description des fonctionnalités

### (1) **Fonctions de base**

1. **Embellissement SQL** : Convertit des requêtes SQL désordonnées en un format structuré et facile à comprendre. Exemple :

* Requête originale :
```sql
select field1,field2,field3 from my_table where my_condition;
```

* Après embellissement :
```sql
SELECT
    field1,
    field2,
    field3
FROM
    my_table
WHERE
    my_condition;
```


### (2) **Options de configuration**

1. **Choix du dialecte (Dialect)** : Plusieurs dialectes SQL sont disponibles, tels que Standard SQL, MySQL, PostgreSQL, SQL Server, etc. Sélectionnez le dialecte adapté à votre base de données afin de garantir que les requêtes SQL formatées respectent les règles syntaxiques spécifiques à cette dernière.
2. **Cas particulier des mots-clés (Keyword case)** : Les mots-clés SQL peuvent être affichés en majuscules (UPPERCASE), en minuscules (lowercase) ou avec une initiale majuscule (Capitalized), ce qui permet d'assurer une cohérence stylistique dans le code. Exemples :

* Requête originale :
```sql
select * from table;
```

* En majuscules :
```sql
SELECT * FROM table;
```

* En minuscules :
```sql
select * from table;
```

* Première lettre majuscule :
```sql
Select * From table;
```


3. **Style d'indentation (Indent style)** : Vous pouvez choisir entre différents styles d'indentation tels que standard, 2 espaces (2 spaces), 4 espaces (4 spaces). Cela permet de s'adapter aux préférences personnelles ou au style interne d'une équipe. Exemples :

* Indentation standard :
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* Indentation de 2 espaces :
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* Indentation de 4 espaces :
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **Zone d'entrée et de sortie**

1. **Zone d'entrée** : Dans la zone de texte située à gauche, vous pouvez coller ou taper directement la requête SQL que vous souhaitez formater.
2. **Zone de sortie** : La zone de texte à droite affiche en temps réel le résultat après formatage et embellissement. Un bouton de copie facilite également le transfert de la requête embellie vers le presse-papiers, pour l'utiliser ultérieurement ailleurs.

## 3. Étapes d'utilisation

1. Ouvrez la [page web de l'outil SQL](https://atoolio.com/sql-prettify).
2. Collez ou saisissez votre requête SQL dans la zone d'entrée.
3. Choisissez les options adaptées selon vos besoins, parmi Dialecte, Majuscules/Minuscules des mots-clés et Style d'indentation.
4. Vérifiez le résultat formaté dans la zone de sortie à droite. Si cela vous convient, cliquez sur le bouton de copie pour l'enregistrer dans le presse-papiers.