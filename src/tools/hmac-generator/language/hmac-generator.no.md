# A Toolio Online HMAC-generator Dokumentasjon

## 1. Verktøybeskrivelse

Den online HMAC-generatoren fra A Toolio beregner hash-baserte meldingsautentiseringskoder (HMAC) ved hjelp av en nøkkel og en hash-funksjon, egnet for utviklere som trenger å generere HMAC-koder raskt i ulike utviklingsscenarier.

## 2. Funksjonsbeskrivelse

### Inndataområde

1. **Klartekst** - Skriv inn teksten du ønsker å beregne hash-verdien for.
2. **Hemmelig nøkkel** - Skriv inn den hemmelige nøkkelen som skal brukes til å generere HMAC.
3. **Hash-funksjon** - Velg ønsket hash-funksjon. Som standard er SHA256 satt, men andre hash-funksjoner kan velges etter behov.
4. **Output Encoding** - Velg ønsket kodingsformat for output. Standard er heksadesimal (base 16), men andre formater er også tilgjengelige.

### Output-område

1. **HMAC of your text** - Viser den genererte HMAC-verdien. En kopiknapp forenkler overføringen av resultatet.

## 3. Brukstrinn

**Trinn 1: Skriv inn klartekst og nøkkel**

Skriv inn teksten du vil behandle i feltet "Klartekst", og deretter skriver du inn den hemmelige nøkkelen i det tilhørende feltet. Disse grunnleggende dataene må tastes inn korrekt.

**Trinn 2: Velg hash-funksjon**

Velg den nødvendige hash-funksjonen fra nedtrekksmenyen "Hash-funksjon", som SHA256, SHA1 osv., avhengig av dine spesifikke behov. Forskjellige hash-funksjoner gir forskjellige HMAC-resultater.

**Trinn 3: Velg output-kodingsformat**

Velg ønsket kodingsformat gjennom menyen "Output Encoding", slik som heksadesimal (base 16) eller Base64. Dette bestemmer hvordan den genererte HMAC-verdien blir presentert.

**Trinn 4: Generer og vis HMAC**

Når du har fylt ut alle felt og gjort de nødvendige valgene, beregner systemet automatisk HMAC-verdien og viser den i seksjonen "HMAC of your text". Du kan se resultatet direkte.

**Trinn 5: Kopier HMAC**

Hvis du trenger å bruke denne HMAC-verdien, klikker du på kopiknappen ved siden av resultatet for å kopiere verdien til utklippstavlen og deretter lime den inn hvor som helst annet sted.