# Dokumentasjon for RSA-nøkkelpar-generator

## 1. Verktøybeskrivelse

Dette online verktøyet lar deg enkelt generere tilfeldige RSA-privatnøkler og offentlige PEM-sertifikater. Det er ideell for utviklere som trenger å raskt lage et RSA-nøkkelpar under utviklingsprosessen.

## 2. Funksjonsbeskrivelse

### (1) **Nøkkel lengdeinnstilling**

* **Funksjon**: Brukeren kan sette nøkkelens lengde (i bits) innenfor et definert område.
* **Handling**: Skriv inn ønsket nøkkel lengde i inputfeltet etter "Bits", f.eks. vanligvis brukt 2048 bits. Verktøyet støtter et spesifikt bitområde, slik at den genererte nøkkelen oppfyller sikkerhets- og brukskrav.
* **Formål**: Jo lengre nøkkel, jo høyere sikkerhet, men kryptering og dekryptering kan bli tregere. En avveining basert på faktisk bruksområde må derfor gjøres.

### (2) **Oppdater nøkkelsett**

* **Funksjon**: Genererer nytt tilfeldig RSA-nøkkelsett raskt.
* **Handling**: Klikk på "Refresh key-pair"-knappen. Systemet vil basert på nåværende nøkkelengde konfigurert, generere et nytt sett med privat- og offentlig nøkkel.
* **Formål**: Når du har behov for å teste eller bruke flere forskjellige nøkkelsett, så trenger du ikke manuelt justere andre parametre. Et trykk på Refresh-knappen gir deg raskt nye nøkler og øker arbeidseffektiviteten din.

### (3) **Offentlig nøkkel - Visning og administrasjon**

* **Funksjon**: Viser den genererte offentlige RSA-nøkkelen og gir brukeren praktiske funksjoner for å bruke den.
* **Visning**: I feltet "Public key" vises nøkkelen i standard PEM-format inkludert "-----BEGIN PUBLIC KEY-----" og "-----END PUBLIC KEY-----". Denne kan direkte brukes i applikasjoner.
* **Kopieringsfunksjon**: En kopieringsknapp ved siden av lar brukeren kopiere offentlig nøkkel til utklippstavlen med ett klikk, slik at den lett kan limes inn andre steder, som konfigurasjonsfiler eller kodeblokker.

### (4) **Privat nøkkel - Visning og administrasjon**

* **Funksjon**: Viser den genererte private RSA-nøkkelen og tilbyr enkel håndtering for bruk.
* **Visning**: Under "Private key" brukes også standard PEM-format, identifisert med "-----BEGIN RSA PRIVATE KEY-----" og "-----END RSA PRIVATE KEY-----". Dette tillater brukeren å benytte nøkkelen til operasjoner som kryptering, dekryptering og digitale signaturer.
* **Kopieringsfunksjon**: Kopieringsknappen rett ved siden av gjør det lett å kopiere den private nøkkelen slik at den kan brukes i sikre miljøer, f.eks. lagring på servere eller konfigurasjon i applikasjoner.

## 3. Eksempler på bruksområder

1. Når utviklere trenger testnøkler under utvikling av applikasjoner basert på RSA-krypteringsalgoritmen, kan dette verktøyet brukes til å velge passende nøkkelengde og generere nøkkelsett med "Refresh"-knappen. Offentlig nøkkel kan da brukes til kryptering, mens privat nøkkel egner seg for dekrypteringstesting.
2. Ved oppsett av sikre kommunikasjonsprotokoller (som SSL/TLS), hvor selvsignerte sertifikater eller testmiljønøkler kreves, kan disse genereres her og plasseres deretter på relevante posisjoner hos både server og klient.