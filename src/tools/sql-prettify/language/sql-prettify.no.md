# Dokumentasjon for SQL-formaterings- og oppryddingsverktøyet

## 1. Verktøybeskrivelse

SQL-formaterings- og oppryddingsverktøyet er en plattform på nettet som brukes til å formatere og rydde opp i SQL-spørringer du har skrevet. Det støtter flere SQL-dialekter, og hjelper utviklere med å lese og skrive SQL-kode på en klarere måte.

## 2. Funksjonsbeskrivelse

### (1) **Grunnfunksjoner**

1. **SQL-opprydding**: Gjør uoversiktlige SQL-spørringer om til et strukturert og lettleselig format. Eksempel:

* Opprinnelig spørring:
```sql
select field1,field2,field3 from my_table where my_condition;
```

* Etter opprydding:
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


### (2) **Innstillingsalternativer**

1. **Dialektvalg (Dialect)**: Flere forskjellige SQL-dialekter er tilgjengelige, blant annet Standard SQL, MySQL, PostgreSQL, SQL Server osv. Velg riktig dialekt for databasen din for å sikre at den formaterede SQL-koden følger korrekt syntaks for nettopp denne databasen.
2. **Størrelse på bokstaver i nøkkelord (Keyword case)**: Nøkkelordene i SQL-koden kan vises i STORE BOKSTAVER (UPPERCASE), små bokstaver (lowercase) eller med stor forbokstav (Capitalized). Dette gjør det mulig å ha en enhetlig stil i koden. Eksempler:

* Opprinnelig spørring:
```sql
select * from table;
```

* Store bokstaver:
```sql
SELECT * FROM table;
```

* Små bokstaver:
```sql
select * from table;
```

* Forbokstav stor:
```sql
Select * From table;
```


3. **Innrykkstype (Indent style)**: Du kan velge mellom ulike typer innrykk, som standard, 2 mellomrom (2 spaces), 4 mellomrom (4 spaces), slik at du kan tilpasse det etter dine eller teamets preferanser. Eksempler:

* Standard innrykk:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* Innrykk med 2 mellomrom:
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* Innrykk med 4 mellomrom:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **Inndata- og utdataområder**

1. **Inndatafelt**: I tekstfeltet til venstre kan du lime inn eller skrive direkte inn din SQL-spørring som du ønsker å formatere.
2. **Utdatafelt**: Tekstfeltet til høyre viser resultatet av formateringen i sanntid. Det finnes også en kopieringsknapp som gjør det enkelt å overføre den rydde SQL-koden til utklippstavlen, slik at du raskt kan bruke den andre steder.

## 3. Trinnvis bruksanvisning

1. Åpne [nettsiden til SQL-verktøyet](https://atoolio.com/sql-prettify).
2. Lim inn eller skriv inn din SQL-spørring i inndatafeltet.
3. Velg de alternativene du trenger fra nedtrekksmenyene under Dialekt, Nøkkelord-stil og Indent-type.
4. Kontroller hvordan den formaterede versjonen ser ut i utdatafeltet til høyre. Hvis du er fornøyd, klikker du på kopieringsknappen for å lagre det i utklippstavlen.