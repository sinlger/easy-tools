# Documentation du Générateur d'Expressions Crontab

## 1. Présentation Générale de l'Outil

Le générateur d'expressions Crontab est un outil en ligne qui aide les utilisateurs à créer facilement des expressions Crontab, à les valider et à obtenir des descriptions lisibles pour les planifications cron.

## 2. Description des Fonctionnalités

1. **Génération d'Expressions Crontab**

   * **Saisie Manuelle** - Saisissez directement une expression Crontab dans le champ d'entrée, par exemple "40 * * * *", l'outil générera automatiquement la description correspondante : "À 40 minutes après l'heure, toutes les heures, chaque jour".
   * **Sélectionner des Expressions Prédéfinies** - L'outil propose plusieurs options d'expressions prédéfinies telles que "@yearly", "@monthly", etc. En cliquant sur une option, vous pouvez rapidement générer l'expression Crontab correspondante.

2. **Validation d'Expressions Crontab**

   * Après avoir saisi une expression Crontab personnalisée, l'outil vérifie automatiquement si elle respecte le format correct. Si le format est valide, il affiche la description associée ; si le format est incorrect, il invite l'utilisateur à apporter des modifications.

3. **Obtenir une Description Lisible**

   * Pour toute expression Crontab saisie ou sélectionnée, l'outil génère une description compréhensible en langage naturel afin d'aider les utilisateurs à bien comprendre son fonctionnement.

4. **Paramètres Personnalisables**

   * **Mode Verbeux (Verbose)** - En activant cette option, vous obtenez des informations plus détaillées dans les journaux (logs).
   * **Utiliser le Format d'Heure sur 24 Heures** - Choisissez d'afficher l'heure au format 24 heures.
   * **Les Jours Commencent à 0** - Vous pouvez choisir si les jours doivent être comptés à partir de 0 ou de 1.

5. **Signification des Symboles Crontab**

   * **Astérisque (*)** - Représente n'importe quelle valeur, par exemple "* * * *" signifie que la tâche s'exécute chaque minute.
   * **Tiret (-)** - Utilisé pour spécifier une plage de valeurs, par exemple "1 - 10 * * *" indique que la tâche s'exécutera entre la minute 1 et la minute 10.
   * **Virgule (,)** - Employée pour lister plusieurs valeurs, par exemple "1,10 * * *" signifie que la tâche s'exécutera aux minutes 1 et 10.
   * **Barre Oblique (/)** - Indique des intervalles réguliers, par exemple "*/10 * * *" veut dire que la tâche s'exécutera toutes les 10 minutes.
   * **Symboles Spéciaux (@)** - Incluent @yearly, @monthly, @weekly, @daily, @midnight, @hourly, @reboot, etc., qui correspondent respectivement à une exécution annuelle, mensuelle, hebdomadaire, quotidienne, à minuit, chaque heure et au redémarrage du système.