# ULID-generator Brukerdokumentasjon

## 1. Verktøyoversikt
ULID-generatoren brukes til å opprette tilfeldige universelt unike leksikografisk sorterbare identifikatorer (ULID). De genererte identifikatorene er unike og sorterbare, og har bred bruk i distribuerte systemer, databaserekordidentifikatorer og lignende scenarier.

## 2. Funksjonsbeskrivelse

### (1) Mengdeinnstilling
Bruk "Quantity"-valget til å sette antallet ULID som skal genereres. Standardverdien er 1, og du kan justere mengden ved å klikke på pluss/minustastene til høyre.

### (2) Formatvalg
To outputformater er tilgjengelige:
1. **Raw**: Viser ULID-ene i ren tekstformat, praktisk for direkte visning og bruk.
2. **JSON**: Eksporterer de genererte ULID-ene i JSON-format, noe som gjør det lettere å kalle og analysere dem fra programmer.

### (3) Generering og operasjoner
Klikk på "Refresh"-knappen for å generere nye ULID; klikk på "Copy"-knappen for å kopiere de genererte ULID-ene til utklippstavlen, slik at du enkelt kan lime dem inn andre steder.

## 3. Eksempler

### Eksempel 1: Generer én ULID (rått format)
Sett "Quantity" til 1 og velg "Raw"-format, klikk deretter på "Refresh", en ULID lik følgende vil bli generert:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Eksempel 2: Generer flere ULID-er (JSON-format)
Sett "Quantity" til 3 og velg "JSON"-format, klikk deretter på "Refresh", ULID-ene vil bli generert i følgende JSON-format:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}