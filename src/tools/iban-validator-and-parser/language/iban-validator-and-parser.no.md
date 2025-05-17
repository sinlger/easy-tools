# Online IBAN-validerings- og analysator Dokumentasjon

## 1. Verktøybeskrivelse

Dette er ein online IBAN-validerings- og analyseverktøy (International Bank Account Number) som kan verifisere og analysere IBAN-nummer for å hjelpe brukarane med å sjekke om eit IBAN-nummer er gyldig, og få relevant informasjon.

## 2. Funksjonsbeskrivelse

### IBAN Valideringsfunksjon

1. **Skriv inn IBAN-nummer** - Skriv inn det IBAN-nummeret du vil validere i tilhøyrande inndatafelt. Når du skriv inn, må du vere sikker på at nummeret er nøyaktig og komplett.
2. **Resultat frå valideringa** :
   * **Gyldig IBAN** - Dersom det skrivne IBAN-nummeret er gyldig, vil verktøyet vise ei suksessmelding og gje følgjande detaljerte informasjonar:
     * **Land** - Viser landet som IBAN høyrer til, t.d. Frankrike, Tyskland eller Storbritannia.
     * **BBAN** - Viser grunnlagsnummeret for bankkontoen (BBAN), ei viktig informasjon som bankar nyttar for å identifisere kundekonti.
     * **QR-IBAN sjekk** - Gir beskjed om dette IBAN-nummeret er ein QR-IBAN (eit spesifikt format av IBAN som ofte blir brukt i scenarier som betaling gjennom QR-koder).
     * **Brukervennleg IBAN-format** - Konverterer IBAN-nummeret til eit meir lesbart format, vanlegvis ved å leggje til mellomrom etter kvart fjerde siffer, noko som gjer det enklare å lesa og bruka.

   * **Ugyldig IBAN** - Dersom det skrivne IBAN-nummeret ikkje er gyldig, vil verktøyet vise ei feilmelding og seie at nummeret har problem og ikkje består valideringa.

### IBAN Analysefunksjon

Når det skrivne IBAN-nummeret er gyldig, vil verktøyet automatisk analysere ut følgjande detaljerte informasjonar:

1. **Land** - Bestemmer kva land IBAN-nummeret høyrer til, noko som er særskild viktig for internasjonale transaksjonar og pengestrøymingar, og som hjelper brukarane med å forstå korleis pengar flytast og kva område som er involvert.
2. **BBAN (Basic Bank Account Number)** - Leverer grunnlagsnummeret for bankkontoen, ein sentral identifikator som bankar nyttar for å identifisere kundekonton, avgjerande for å fullføre transaksjonar og finansavvikling.
3. **QR-IBAN sjekk** - Identifiserer om IBAN-nummeret er ein QR-IBAN, og gjer det mogleg for brukaren å vite om det samsvarar med visse krav for spesielle betalingscenario som betaling gjennom QR-kode og andre nye betalingsmåtar.
4. **Brukervennleg IBAN-format** - Gjer om IBAN-nummeret til eit lettlesbart format, slik at det blir enklare å sjå og bruke, og reduserer misforståingar eller feil som kjem av formatproblem.

### Eksempelreferanse

Verktøyet leverer nokre gyldige IBAN-eksempler som brukarane kan ta referanse frå for å forstå korrekt format på eit IBAN-nummer. Under følgjer nokre døme:

1. **FR76 3000 6000 0112 3456 7890 189** - Dette er eit døme på ein fransk IBAN, med landskode "FR" og BBAN "30006000011234567890189", og det er ikkje ein QR-IBAN.
2. **DE89 3704 0044 0532 0130 00** - Dette er eit døme på ein tysk IBAN, med landskode "DE" og BBAN "370400440532013000", også her er det ikkje ei QR-IBAN.
3. **GB29 NWBK 6016 1331 9268 19** - Dette er eit britisk IBAN-døme, med landskode "GB" og BBAN "NWBK60161331926819", også dette er ikkje ei QR-IBAN.

Brukarane kan klikke på kopieringsknappen ved sida av kvart døme for å kopiere eksemplet IBAN-nummer til inndatafeltet og raskt utføre validering og analyseoperasjonar.

## 3. Bruksteg

1. Opne sida til den online IBAN-valideraren og analysatoren.
2. Skriv inn IBAN-nummeret du vil validere i inndatafeltet.
3. Klikk på "Check for validity" (eller trykk Enter) for å starte valideringa.
4. Sjå på resultatet av valideringa; viss det er gyldig får du tilleggjande informasjon som land, BBAN osv., viss det ikkje er gyldig så må du sjekke og rette opp IBAN-nummeret ifølgje meldinga frå verktøyet.
5. Viss du treng referanse, kan du sjå på dei gyldige IBAN-eksempla på sida og klikke på kopieringsknappen for å lime inn eksemplet i inndatafeltet og utføre handlingar.

## 4. Viktige Merknadar

1. **Nøyaktig inndata** - Sørg for at IBAN-nummeret som blir skrive inn er nøyaktig og utan feil. Ein feil i ein einaste teikn kan føre til at valideringa misslår. Viss du ikkje er sikker på om IBAN-nummeret er korrekt, så dobbeltsjekk det nøye eller kontakt relevante finansinstitusjon for å stadfeste det.
2. **Nettverkskobling krevd** - Dette verktøyet er nettbasert og krev stabil nettverkskobling. Ved ustabil nettverksforbindelse eller ingen tilgang til internett, vil ikkje dette verktøyet kunna brukast til validering og analyse.
3. **Personvern og sikkerheit** - I løpet av bruken må du vere sikker på at informasjonen til det IBAN-nummeret ikkje involverer sensitive eller konfidensielle personlege eller bedriftsfinansielle data, for å unngå risiko ved informasjonslekkasje. Selv om verktøyet normalt behandler data sikkert, bør du vere forsiktig når du skriv inn og sender sensitiv informasjon over Internett.