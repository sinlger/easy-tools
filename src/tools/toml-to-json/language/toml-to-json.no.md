# Dokumentasjon for bruk av online-verktøyet for konvertering fra TOML til JSON

## 1. Verktøybeskrivelse

TOML til JSON er et praktisk online-verktøy som analyserer data i TOML-format og konverterer dem til JSON-format. Brukere kan enkelt lime inn eller skrive inn TOML-data i inndatafeltet på venstre side, og det tilsvarende JSON-resultatet genereres automatisk på høyre side.

## 2. Detaljert beskrivelse av funksjoner

### 1. Inndata av TOML-data

* I tekstfeltet på venstre side merket som "Your TOML" kan brukere lime inn eller manuelt skrive inn data i TOML-format. Tekstfeltet støtter flerlinjetekstinput og gir brukerne tilstrekkelig plass til å skrive inn mer komplekse TOML-konfigurasjonsinformasjoner.

### 2. Utdata av JSON-resultat

* Så snart TOML-data blir skrevet inn eller limt inn i tekstfeltet på venstre side, utfører verktøyet automatisk analyse og konvertering. De konverterte JSON-dataene vises i tekstfeltet på høyre side merket som "JSON from your TOML". Brukerne kan se på, kopiere eller viderebehandle disse dataene.

## 3. Brukerveiledning

1. Åpne verktøyets nettside ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. I tekstfeltet på venstre side merket som "Your TOML", lim inn eller skriv inn de TOML-data du ønsker å konvertere.
3. Systemet vil automatisk utføre konverteringen, og resultatet vises i tekstfeltet på høyre side merket som "JSON from your TOML".

## 4. Hovedfunksjoner

* Enkel og intuitiv brukergrensesnitt: Grensesnittet er klart og lett å bruke, med en enkel operasjonsprosess som ikke krever kompliserte innstillinger eller konfigurasjoner, noe som gjør at brukerne raskt kan ta i bruk verktøyet.
* Echtid-konvertering: Etter at TOML-dataene er skrevet inn, utfører verktøyet automatisk konvertering og viser resultatet, uten å måtte klikke manuelt på en konverteringsknapp, noe som øker konverteringseffektiviteten.
* Online-bruk: Ingen programvare trenger å installeres. Så lenge du har en enhet med internett-tilgang, kan du bruke dette verktøyet når som helst og hvor som helst for å konvertere TOML til JSON.

## 5. Eksempler

### Eksempel 1: Enkel TOML-til-JSON-konvertering

Anta at vi har følgende data i TOML-format:
```toml
title = "TOML Example"
owner = "John Doe"
```

Ved å lime inn disse dataene i tekstfeltet på venstre side merket som "Your TOML", vil verktøyet automatisk konvertere dem til følgende JSON-format:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Eksempel 2: TOML-til-JSON-konvertering med nøstet struktur

Vi har mer komplekse TOML-data:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Etter å ha skrevet dem inn i verktøyet, får vi følgende JSON-data:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}