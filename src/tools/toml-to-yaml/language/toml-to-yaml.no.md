# TOML til YAML konverteringsverktøy Brukerdokumentasjon

## Oversikt

TOML til YAML er et nettbasert verktøy som lar brukere enkelt konvertere konfigurasjonsfiler i TOML (Tom's Obvious, Minimal Language) format til YAML (YAML Ain't Markup Language) format. Dette er spesielt nyttig for utviklere som trenger å migrere konfigurasjoner mellom ulike systemer eller integrere flere teknologiplattformer.

## Grensesnittlayout

Verktøyet har et enkelt og intuitivt grensesnitt, hovedsakelig sammensatt av følgende deler:

1. Venstre tekstboks: Dette er området hvor brukere kan skrive inn eller lime inn TOML-formatert tekst, merket som "Your TOML".
2. Høyre tekstboks: Brukes til å vise den konverterte YAML-formaterte teksten, merket som "YAML from your TOML".
3. Midtre konverteringsknapp: Etter at brukeren har skrevet inn TOML-tekst, kan de klikke på denne knappen for å utføre konverteringen.

## Funksjonsbeskrivelse

### Inndata av TOML-tekst

- Brukere kan skrive inn TOML-formatert konfigurasjonstekst direkte i venstre tekstboks.
- De kan også kopiere TOML-tekst fra andre filer eller redigeringsprogrammer og lime det inn i denne tekstboksen.

### Konverteringsoperasjon

- Etter at TOML-teksten er skrevet inn eller limt inn, klikker du på midtre konverteringsknappen. Systemet analyserer umiddelbart den innskrevne TOML-teksten og konverterer den til YAML-format.
- Etter at konverteringen er fullført, vises den resulterende YAML-teksten i høyre tekstboks.

### Visning av YAML-resultat

- Høyre tekstboks viser hele den konverterte YAML-teksten.
- Her kan brukere sjekke om konverteringsresultatet er nøyaktig og om strukturen til YAML-teksten samsvarer med deres forventninger.

### Kopiering av YAML-tekst

- Brukere kan markere og kopiere hele YAML-teksten i høyre tekstboks, noe som er praktisk for å bruke den andre steder, som å lime den inn i konfigurasjonsfiler eller sende den til andre personer.

## Eksempler

### Eksempel 1: Grunnleggende konvertering

**TOML-inndata:**

```toml
# Dette er et enkelt TOML-eksempel
title = "TOML-eksempel"

[author]
name = "Zhang San"
age = 28
e-post = "zhangsan@example.com"
```

**YAML-utdata:**

```yaml
# Dette er det konverterte YAML-eksemplet
title: TOML-eksempel

author:
  name: Zhang San
  age: 28
  e-post: zhangsan@example.com
```

### Eksempel 2: Konvertering av komplekse strukturer

**TOML-inndata:**

```toml
# TOML-eksempel med mer kompleks struktur
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**YAML-utdata:**

```yaml
# YAML-eksempel med mer kompleks struktur
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Viktige notater

- Hvis det oppgitte TOML-formatet ikke er korrekt, kan konverteringen mislykkes og systemet kan vise feilmeldinger.
- Verktøyet støtter de mest vanlige TOML-syntaksstrukturene, men for noen spesielle eller sjeldent brukte syntakselementer, kan en perfekt konvertering kanskje ikke være mulig.
- Den genererte YAML-teksten kan ha små formateringsforskjeller avhengig av hvilken YAML-versjon og spesifikasjoner som brukes.