# IPv4-adressekonverteringsverktøy Dokumentasjon

## 1. Verktøybeskrivelse

IPv4-adressekonverteringsverktøyet er et nettbasert verktøy som konverterer IPv4-adresser til ulike tallsystemer (desimal, heksadesimal, binær) og også til IPv6-format. Dette verktøyet hjelper utviklere og nettverksteknikere med å raskt få tak i forskjellige representasjoner av IPv4-adresser, noe som forenkler nettverkskonfigurasjon, programvareutvikling og sikkerhetsanalyser.

## 2. Funksjonsbeskrivelse

### (A) Inndata av IPv4-adresse
- I inndatafeltet kan brukeren skrive inn en gyldig IPv4-adresse direkte (f.eks. 192.168.1.1). Etter at adressen er skrevet inn, klikk på "Konverter"-knappen eller trykk Enter for å starte konverteringsprosessen automatisk.

### (B) Konvertering til Desimalformat
- **Funksjon**: Gjør om IPv4-adressen til en desimalverdi.
- **Bruk**: Når IPv4-adressen er skrevet inn, beregner verktøyet den tilsvarende desimalverdien automatisk. Denne verdien oppnås ved å konvertere hver av de fire oktettene i IPv4-adressen til desimalform og deretter kombinere dem etter en bestemt metode.

### (C) Konvertering til Heksadesimalformat
- **Funksjon**: Gjør om IPv4-adressen til en heksadesimal streng.
- **Bruk**: Når IPv4-adressen er skrevet inn, blir hvert oktett konvertert til to sifre i heksadesimalform og sammenføyd til en komplett heksadesimalstreng. For eksempel blir IPv4-adressen 192.168.1.1 konvertert til C0A80101.

### (D) Konvertering til Binært Format
- **Funksjon**: Transformerer IPv4-adressen til binær form.
- **Bruk**: Ved å legge inn IPv4-adressen konverteres hver byte til et 8-biters binærtall, som så slås sammen til en 32-bits binærstreng. For eksempel blir IPv4-adressen 192.168.1.1 til 11000000101010000000000100000001 i binærform.

### (E) Konvertering til IPv6-format
- **Funksjon**: Gjør om IPv4-adressen til en representasjon i IPv6-format.
- **Bruk**: Verktøyet produserer to forskjellige IPv6-formater:
  1. **Full IPv6-adresse**: De første 8 byte fylles med nuller, mens de siste 8 byte inneholder den heksadesimale representasjonen av IPv4-adressen, med tillegget "ffff" foran IPv4-delen som identifikasjon. Eksempel: Fra IPv4-adressen 192.168.1.1 blir det generert en fullversjon av IPv6-adressen: 0000:0000:0000:0000:0000:ffff:c0a8:0101.