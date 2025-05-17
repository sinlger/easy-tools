# A Toolio - Regex Tester Brukerdokumentasjon

## 1. Introduksjon til verktøyet

**A Toolio Regex Tester** er et online verktøy som lar deg teste regulære uttrykk ved å skrive inn eksempeltekst. Med sitt klare grensesnitt og praktiske funksjoner egner det seg både for nybegynnere og utviklere.

## 2. Detaljert beskrivelse av funksjoner

### (1) Inndatafelt for regulære uttrykk

Skriv inn det regulære uttrykket du ønsker å teste i tekstboksen. En lenke til en hurtigreferansetabell for regulære uttrykk er også inkludert for din letthet under bruk. For eksempel kan du bruke det regulære uttrykket \w+ for å finne ett eller flere ord.

### (2) Valg for Regex Tester

Tilgjengelige valg inkluderer: Global søk (g), Ignorer store/små bokstaver (i), Flere linjer-modus (m), Enkel linje-modus (s), Unicode-støtte (u) og Støtte for Unicode-tegnsett (v). Velg de passende alternativene basert på dine spesifikke behov.

- Global søk (g): Søker etter alle treff i hele teksten.
- Ignorer store/små bokstaver (i): Finner treff uavhengig av bokstavens storhet.
- Flere linjer-modus (m): Behandler inndata som flere linjer, slik at du kan søke ved begynnelsen og slutten av hver linje.
- Enkel linje-modus (s): Behandler hele teksten som én enkelt linje, noe som hjelper når du søker over flere linjer.
- Unicode-støtte (u): Aktiverer støtte for Unicode-tegn.
- Støtte for Unicode-tegnsett (v): Støtter avanserte Unicode-tegnsett.

Eksempel: Det regulære uttrykket \d{3}-\d{3}-\d{4} kan finne flere telefonnumre i en tekst når global søk er aktivert.

### (3) Inndatafelt for sammenligningstekst

Skriv inn innholdet der du ønsker å finne treff. Verktøyet søker etter mønstre basert på det regulære uttrykket og valgte alternativer. For eksempel kan du lokalisere alle individuelle ord i teksten "Finn ord i denne teksten" ved å bruke det regulære uttrykket \w+.