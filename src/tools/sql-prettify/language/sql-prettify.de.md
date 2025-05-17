# SQL-Formatierungs- und Aufbereitungstool Benutzerdokumentation

## 1. Toolübersicht

Das SQL-Formatierungs- und Aufbereitungstool ist eine Online-Plattform, die verwendet wird, um geschriebene SQL-Abfragen zu formatieren und aufzubereiten. Es unterstützt verschiedene SQL-Dialekte und hilft Entwicklern, SQL-Code übersichtlicher zu lesen und zu schreiben.

## 2. Funktionsbeschreibung

### (1) **Grundfunktionen**

1. **SQL-Aufbereitung**: Konvertiert unübersichtliche SQL-Abfragen in ein formatiertes und leicht verständliches Format. Beispiel:

* Originalabfrage:
```sql
select field1,field2,field3 from my_table where my_condition;
```

* Nach der Aufbereitung:
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


### (2) **Einstellungsoptionen**

1. **Dialektwahl (Dialect)**: Verschiedene SQL-Dialekte wie Standard SQL, MySQL, PostgreSQL, SQL Server usw. sind verfügbar. Wählen Sie den passenden Dialekt für Ihre Datenbank aus, um sicherzustellen, dass die formatierten SQL-Befehle den Syntaxregeln Ihrer Datenbank entsprechen.
2. **Schlüsselwortgroß-/kleinschreibung (Keyword case)**: Die SQL-Schlüsselwörter können entweder in Großbuchstaben (UPPERCASE), Kleinbuchstaben (lowercase) oder mit großem Anfangsbuchstaben (Capitalized) angezeigt werden, um ein einheitliches Codestyle zu gewährleisten. Beispiele:

* Originalabfrage:
```sql
select * from table;
```

* Nach Einstellung auf Großschreibung:
```sql
SELECT * FROM table;
```

* Nach Einstellung auf Kleinschreibung:
```sql
select * from table;
```

* Nach Einstellung auf Anfangsgroßbuchstabe:
```sql
Select * From table;
```


3. **Einrückungsstil (Indent style)**: Wählen Sie zwischen verschiedenen Einrückungsvarianten wie Standard, 2 Leerzeichen (2 spaces), 4 Leerzeichen (4 spaces). Dadurch können persönliche oder teaminterne Formatvorlieben berücksichtigt werden. Beispiele:

* Standardmäßige Einrückung:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* Mit 2 Leerzeichen eingerückt:
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* Mit 4 Leerzeichen eingerückt:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **Eingabe- und Ausgabebereich**

1. **Eingabebereich**: Fügen Sie im linken Textfeld Ihre zu formatierende SQL-Abfrage per Copy & Paste ein oder geben Sie diese direkt ein.
2. **Ausgabebereich**: Im rechten Textfeld wird das Ergebnis nach der Formatierung in Echtzeit angezeigt. Ein Kopierbutton erlaubt es Ihnen, das formatierte SQL direkt in die Zwischenablage zu übernehmen, damit Sie es problemlos an anderen Stellen weiterverwenden können.

## 3. Verwendungsvorgehensweise

1. Öffnen Sie die [Webseite des SQL-Formatierers](https://atoolio.com/sql-prettify).
2. Fügen Sie Ihre SQL-Abfrage im Eingabebereich ein oder geben Sie sie direkt ein.
3. Wählen Sie nach Bedarf im Bereich Dialekt, Schlüsselwort-Groß-/Kleinschreibung und Einrückstil die gewünschten Optionen aus.
4. Prüfen Sie das Ergebnis im rechten Ausgabebereich. Falls zufrieden, klicken Sie auf den Copy-Button, um die formatierte Version zu kopieren.