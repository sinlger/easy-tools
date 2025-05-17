# IPv6 ULA-generator Dokumentasjon

**1. Verktøybeskrivelse**

IPv6 ULA-generatoren er et nettbasert verktøy som er utformet for å hjelpe brukere med å generere lokale, ikke-rutbare IPv6-adresser i henhold til RFC4193-standard. Den er egnet for å opprette unike nettverksidentifikatorer innenfor et lokalt nettverk som ikke kan rutes på Internett.

**2. Hovedfunksjoner**

1. **Tilfeldig generering av ULA-basert på flere faktorer**
   * Dette verktøyet bruker den første metoden anbefalt av IETF, og kombinerer tidsstempel og MAC-adresse via SHA1-hashalgoritmen, og trekker deretter ut de laveste 40 bitene for å generere tilfeldige ULA-adresser. Dette sikrer høy grad av tilfeldighet og unikhet i de genererte adressene, reduserer betydelig risikoen for adressekonflikter og gir pålitelige lokale nettverksidentifikatorer for enheter i det lokale nettverket.

2. **Inndata og behandling av MAC-adresser**
   * Brukere kan manuelt skrive inn MAC-adresser i det reserverte feltet etter standardformat (f.eks. "20:37:06:12:34:56"). Verktøyet vil bruke denne MAC-adressen som en viktig parameter i genereringen av ULA-adressen, sammen med andre faktorer i beregningen, og produsere en ULA-adresse knyttet til denne spesifikke MAC-adressen.

3. **Generering av ULA-adresser og tilhørende ruteblokker**

   * **IPv6 ULA**: Verktøyet genererer en fullstendig IPv6 ULA-adresse som starter med "fd", i samsvar med RFC4193-standard for lokale ULA-adresser. For eksempel "fd1d:dba9:6f7b::/48", hvor "/48" indikerer at prefikslengden for denne ULA-adressen er på 48 biter. Dette gir unike nettverksidentifikatorer for enheter i det lokale nettverket, som kan brukes til lokal nettverkskonfigurasjon og kommunikasjon.
   * **Første rutbare blokk**: Første blokk som kan tilordnes til vertsnavn eller undernett blir generert, f.eks. "fd1d:dba9:6f7b:0::/64". Dette representerer den første adressen innenfor ULA-adresseområdet som kan tilordnes. Brukeren får informasjon om startadresser, noe som gjør det lettere å planlegge nettverk og administrere adresser.
   * **Siste rutbare blokk**: Siste blokk som kan tilordnes til vertsnavn eller undernett blir også produsert, for eksempel "fd1d:dba9:6f7b:ffff::/64", som viser den siste adressen innenfor ULA-adresseområdet som kan tilordnes. På denne måten har brukeren tydelig oversikt over tilgjengelige adresserområder, noe som gjør det lettere å distribuere nettverk og konfigurere enheter.

**3. Bruksscenarier**

1. I interne bedriftsnettverk, for å tildele unike lokale IPv6-adresser til enheter. Dette unngår konflikter med offentlige IPv6-adresser og sikrer samtidig normal kommunikasjon mellom enheter innenfor det lokale nettverket.

2. I nettverkstestmiljøer, for å generere lokale ikke-rutbare ULA-adresser for å simulere nettverksscenarier, utføre test av nettverksutstyrskonfigurasjon og applikasjonsprøving uten å måtte bruke offisielle IPv6-adresser fra Internett.

3. I hjemmenettverk, for å tildele ULA-adresser til rutere og smarte enheter. Dette øker nettverkets stabilitet og sikkerhet, og hindrer uautorisert tilgang fra eksterne nettverk.

**4. Instruksjoner for bruk**

1. Gå til IPv6 ULA-generatorens nettsteder [https://atoolio.com/ipv6-ula-generator](https://atoolio.com/ipv6-ula-generator).
2. Hvis du kjenner din enhets MAC-adresse, skriv den inn i riktig format (f.eks. "20:37:06:12:34:56") i inndatafeltet "MAC address". Hvis MAC-adressen er ukjent, kan du la feltet stå tomt; verktøyet kan da enten bruke en standard-MAC-adresse eller generere en tilfeldig (avhengig av verktøyets faktiske logikk).
3. Klikk på genererknappen (som f.eks. "Generate", navnet kan variere litt avhengig av grensesnittet) slik at verktøyet kan beregne og generere de tilhørende IPv6 ULA-adressene, første og siste rutbare blokker basert på angitt (eller standard) MAC-adresse og nåværende tidsstempel.
4. Se gjennom de genererte adressene og bruk dem etter behov i konfigurasjon av enheter i ditt lokale nettverk, nettverksplanlegging eller nettverkstesting.

**5. Viktige merknader**

1. De genererte ULA-adressene er kun ment for bruk i lokale nettverk og kan hverken rutes eller kommuniseres på Internett. For enheter som skal kunne kommunisere med Internett, trenger du globale unicast IPv6-adresser som er rutbare.

2. Sørg for at den angitte MAC-adressen er korrekt. Feil her kan påvirke unikhetskarakteren og koblingen til ULA-adressen, og føre til nettverksproblemer.

3. ULA-adressene må være unike innenfor det lokale nettverket. Unngå duplisering av samme ULA-adresse for å forhindre nettverkskonflikter som kan påvirke enhetenes normale kommunikasjon.