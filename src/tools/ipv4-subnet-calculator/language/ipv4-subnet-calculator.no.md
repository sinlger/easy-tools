# IPv4 Subnett-kalkulator Dokumentasjon

IPv4 Subnett-kalkulatoren er et praktisk nettverktøy for å analysere IPv4 CIDR-blokker og hente detaljert informasjon om undernett. Under finner du en beskrivelse av funksjonene og bruksinstruksjoner:

## 1. Inndatafunksjon

I inndatafeltet kan brukeren skrive inn en IPv4-adresse, med eller uten nettmaske. For eksempel kan du skrive inn "192.168.0.1/24", og verktøyet vil utføre de nødvendige beregningene basert på denne adressen.

## 2. Beregningsresultater

1. **Nettmaske (Netmask)**
   * Viser kombinasjonen av IPv4-adressen og nettmasken i CIDR-format, som f.eks. "192.168.0.0/24", slik at brukeren tydelig kan se hvilket nettverk som behandles.

2. **Nettverksadresse (Network address)**
   * Gir nettverksadressen til undernettet, som er en spesiell adresse som representerer hele nettverket. F.eks. "192.168.0.0" angir startpunktet for dette undernettet.

3. **Nettverksmaske (Network mask)**
   * Viser nettmasken i desimalform, som f.eks. "255.255.255.0", og brukes til å avgrense nettverksdelen og host-delen av IP-adressen.

4. **Nettverksmaske i binær form (Network mask in binary)**
   * Presenterer nettmasken i binært format, som f.eks. "11111111.11111111.11111111.00000000", noe som hjelper på å bedre forstå hvordan nettmasken fungerer.

5. **CIDR-notation (CIDR notation)**
   * Viser CIDR-representasjonen av nettmasken, som f.eks. "/24", en kompakt måte å representere lengden på nettmasken, og gjør det lettere å forstå hvordan nettverket er delt opp.

6. **Wildcard-maske (Wildcard mask)**
   * Gir verdien til wildcard-masken, som f.eks. "0.0.0.255", en komplementær maske til standard nettmaske og ofte brukt i visse nettverksenheter og programvarekonfigurasjoner.

7. **Nettverksstørrelse (Network size)**
   * Informerer om den totale mengden IP-adresser tilgjengelig i undernettet, som f.eks. "256", slik at brukeren kjenner kapasiteten til undernettet.

8. **Første tilgjengelige adresse (First address)**
   * Viser den første adressen som kan tilordnes til en vertsmaskin (host) i undernettet, som f.eks. "192.168.0.1", som markerer begynnelsen på den tilgjengelige adresseblokken.

9. **Siste tilgjengelige adresse (Last address)**
   * Viser den siste adressen som kan tilordnes til en vertsmaskin (host) i undernettet, f.eks. "192.168.0.254", som markerer slutten på den tilgjengelige adresseblokken.

10. **Broadcast-adresse (Broadcast address)**
    * Gir broadcast-adressen for dette undernettet, som f.eks. "192.168.0.255", og som brukes til å sende meldinger til alle vertsnavn (hosts) i undernettet.

11. **IP-adresseklasse (IP class)**
    * Indikerer hvilken klasse IP-adressen tilhører, f.eks. "C", slik at brukeren lett kan identifisere klassifiseringen av denne IP-adressen.

## 3. Navigeringsfunksjonalitet

Det er inkludert to knapper merket som "Forrige blokk (Previous block)" og "Neste blokk (Next block)", som gjør det enkelt for brukeren å bytte mellom naboblokker og raskt få tilgang til informasjon om disse.