# Dokumentasjon for bruk av SVG-placeholdere

## 1. Verktøybeskrivelse

SVG-placeholdergeneratoren er et praktisk verktøy på nettet som brukes til å raskt generere tilpassede SVG-placeholdere. Disse placeholdere kan benyttes under utvikling av applikasjoner for midlertidig visning av bilder, og hjelper utviklere med å arbeide med grensesnittlayout og designforhåndsvisning før det faktiske bildeinnholdet er klart.

## 2. Funksjonsbeskrivelse

### (1) **Størrelsesinnstillinger**

* **Bredde og høyde**: Du kan sette bredde og høyde for placeholderen (i piksler) gjennom inndatafelt. Det er også "+" og "-" knapper for å justere størrelsen raskt.
* **Bruk eksakt størrelse**: Aktiver denne innstillingen for å sikre at den genererte SVG-placeholderen vises nøyaktig etter de angitte dimensjonene.

### (2) **Fargepersonliggjøring**

* **Bakgrunnsfarge**: Skriv inn en heksadesimal fargekode (som "#cccccc") for å tilpasse bakgrunnsfargen til placeholderen.
* **Tekstfarge**: Tilsvarende skrives en heksadesimal kode (som "#333333") for å bestemme fargen på teksten som vises på placeholderen.

### (3) **Tekstinndstillinger**

* **Fontstørrelse**: Skriv inn en numerisk verdi og velg passende enhet (som piksler) for å justere tekstens størrelse i placeholderen.
* **Egen tekst**: Skriv inn ønsket tekst i feltet. Som standard vises "Bredde x Høyde" (for eksempel "600x350").

### (4) **Forhåndsvisning og resultat**

* **Live-forhåndsvisning**: I forhåndsvisningsområdet til høyre kan du se effekten av SVG-placeholderen som blir generert basert på dine innstillinger i sanntid.
* **SVG HTML-element**: Viser den genererte SVG-koden som kan kopieres og direkte brukes i nettsidedeveloping.
* **SVG i Base64**: Gir muligheten til å konvertere SVG-bildet til en Base64-enkodet streng, nyttig i scenarier hvor spesielle kodingformater kreves.

## 3. Trinnvis bruksanvisning

1. Åpne [nettsiden for SVG-placeholdergeneratoren](https://atoolio.com/svg-placeholder-generator).
2. Sett bredde og høyde på placeholderen etter behov. For eksempel, hvis du ønsker å lage en placeholder på 800 piksler i bredde og 450 piksler i høyde, skriver du "800" i feltet "Width (in px)" og "450" i feltet "Height (in px)".
3. Tilpass bakgrunns- og tekstfarger. Dersom du ønsker en lyseblå bakgrunn (som "#e6f7ff") og mørkeblå tekst (som "#1890ff"), legger du inn de respektive fargekodene i de korrekte feltene.
4. Juster fontstørrelse og egentekst. La oss si at fontstørrelsen skal være 20 piksler og at teksten skal hete "Sample", da skriver du "20" i feltet "Font size" og "Sample" i feltet "Custom text".
5. Sjekk forhåndsvisningsområdet til høyre for å bekrefte at placeholderbildet ser ut som forventet.
6. Velg enten å kopiere koden fra "SVG HTML element", eller Base64-koden fra "SVG in Base64" og lim den inn i ditt aktuelle prosjekt. Alternativt kan du klikke på "Download svg" for å laste ned den genererte SVG-filen direkte.