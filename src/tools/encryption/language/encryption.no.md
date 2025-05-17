# A Toolio Online Krypterings-/Dekrypteringsverktøy Dokumentasjon

## Funksjonsbeskrivelse

A Toolios online krypterings- og dekrypteringsverktøy lar deg kryptere og dekryptere tekst med flere algoritmer (slik som AES, TripleDES, Rabbit eller RC4). Brukerne kan enkelt kryptere klartekst eller dekryptere kryptert tekst for å møte daglige behov i utvikling eller læring.

## Krypteringsfunksjon

1. **Inndata av klartekst** - I "Encrypt"-seksjonen skriver du inn teksten du ønsker å kryptere i feltet "Your text", for eksempel: "Lorem ipsum dolor sit amet".
2. **Angi hemmelig nøkkel** - I feltet "Your secret key" setter du en nøkkel som skal brukes til kryptering, f.eks. "my secret key". Nøkkelen er en viktig parameter under krypteringsprosessen og må lagres forsvarlig.
3. **Velg krypteringsalgoritme** - Gjennom nedtrekksmenyen "Encryption algorithm" velger du en passende algoritme slik som AES, TripleDES, Rabbit eller RC4. Forskjellige algoritmer har forskjellige sikkerhets- og ytelsesegenskaper, så du kan velge etter dine spesifikke behov.
4. **Vis krypteringsresultat** - Etter at stegene ovenfor er fullført viser verktøyet automatisk den krypterte teksten i seksjonen "Your text encrypted", for eksempel: "U2FsdGVkX19wCAAvFjYehC+Haqkp3/xRGF4yN17gt6/FgnlHRvikeCuOvDyAIBvG".

## Dekrypteringsfunksjon

1. **Skriv inn kryptert tekst** - I "Decrypt"-seksjonen skriver du inn den krypterte teksten du vil dekryptere i feltet "Your encrypted text", for eksempel: "U2FsdGVkX1/EC3+6P5dbbkZ3e1kQ5o2yzuU0NHTjmrKnLBEwreV489Kr0DIB+uBs".
2. **Skriv inn hemmelig nøkkel** - Skriv inn samme nøkkel som ble brukt under krypteringen, "my secret key", i feltet "Your secret key". Riktig nøkkel er avgjørende for vellykket dekryptering.
3. **Velg krypteringsalgoritme** - Velg gjennom nedtrekksmenyen "Encryption algorithm" samme algoritme som ble brukt under kryptering, for eksempel: AES.
4. **Vis dekrypteringsresultat** - Verktøyet vil vise den dekrypterte teksten i seksjonen "Your decrypted text" (din dekrypterte tekst), for eksempel: "Lorem ipsum dolor sit amet".

## Viktige merknader

* **Sikkerhet** - Selv om dette verktøyet er praktisk og raskt anbefales det å bruke det i et sikkert nettverksmiljø når du håndterer sensitiv informasjon. Sørg også for å beskytte nøkkelen din for uautorisert eksponering.
* **Algoritmevalg** - Forskjellige krypteringsalgoritmer egner seg for ulike scenarier. AES er for tiden en av de mest brukte og sikre algoritmene; TripleDES er relativt gammel men fortsatt i bruk i noen systemer; Rabbit og RC4 har også sine egne karakteristika og bruksområder. Du kan velge basert på faktiske behov og sikkerhetskrav.