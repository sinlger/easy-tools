# Dokumentasjon for verktøy for grunnleggende autentisering

## Funksjonsbeskrivelse

Grunnleggende autentiseringsgenerator er et verktøy som genererer Base64-kodete autorisasjonshoder for HTTP-grunnautentisering. Ved å oppgi et brukernavn og passord kan verktøyet raskt generere tilhørende autorisasjonshode som kan brukes i utviklingsprosessen.

## Bruksanvisning

### Skriv inn brukernavn

Skriv inn ønsket brukernavn i inndatafeltet "Username". Det kan være hvilket som helst navn du ønsker å bruke for autentisering.

### Skriv inn passord

Skriv inn passordet som svarer til brukernavnet i feltet "Password". Under skriving blir passordet automatisk skjult for å sikre passordsikkerheten din.

### Se på generert autorisasjonshode

Når du har skrevet inn brukernavn og passord, genererer verktøyet automatisk den tilsvarende autorisasjonshoden. Denne hoden vises i følgende format:

```
Authorization header:
Authorization: Basic [Base64-kodet streng]
```

Her betyr "Basic" at grunnleggende autentiseringsmetode brukes, og den etterfølgende strengen er resultatet av Base64-koding av brukernavn og passord i formatet "brukernavn:passord".

### Kopier autorisasjonshoden

Hvis du trenger å bruke den genererte autorisasjonshoden et annet sted, kan du klikke på knappen "Copy header" for å kopiere den til utklippstavlen. På denne måten kan du enkelt lime den inn i filer eller kode hvor det er nødvendig.