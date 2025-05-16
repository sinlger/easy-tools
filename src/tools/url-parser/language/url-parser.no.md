# URL Parser Brukerveiledning

## 1. Verktøyoversikt
URL Parser er et nettverktøy for å analysere URL-strenger, som kan dekomponere komplekse URL-er til flere komponenter, inkludert protokoll, brukernavn, passord, vertsnavn, port, bane, parametere osv., noe som gjør det enklere for utviklere å raskt forstå URL-ens struktur og detaljert informasjon, og letter bygging, feilsøking og analyse av nettverksforespørsler.

## 2. Funksjonsdetaljer

  1. **Inndatafelt**
     * Gir et inndatafelt der du kan skrive inn URL-strengen som skal analyseres.

  2. **Resultatvisning etter analyse**
     * **Protokoll (Protocol)** : Viser protokoll-delen av URL-en, f.eks. "https:", som indikerer nettverksprotokollen som brukes av URL-en.
     * **Brukernavn (Username)** : Hvis URL-en inneholder informasjon om brukernavn, vil dette bli vist her, brukt til å identifisere brukeridentiteten gitt i URL-en.
     * **Passord (Password)** : Viser passorddelen i URL-en, sammen med brukernavnet brukt til brukerautentisering.
     * **Vertsnavn (Hostname)** : Viser domenenavnet som svarer til URL-en, f.eks. "atoolio.com", som representerer navnet på målserveren.
     * **Port (Port)** : Viser portnummeret spesifisert i URL-en, brukt til å bestemme den spesifikke porten på serveren hvor tjenesten er tilgjengelig. Som standard har ulike protokoller ulike standardporter, f.eks. port 80 for HTTP og port 443 for HTTPS.
     * **Bane (Path)** : Viser bane-delen av URL-en, f.eks. "/url-parser", som peker til en spesifikk ressurs- eller tjenesteplassering på serveren.
     * **Parametere (Params)** : List opp forespørselsparameterdelen i URL-en, startende med "?", etterfulgt av flere "nøkkel-verdi" par som parametere, f.eks. "?key1=value&key2=value2", som brukes til å sende ekstra informasjon og instruksjoner til serveren.
     * **Detaljert visning av parametere** : Hvert nøkkel-verdi par av forespørselsparameterne vises individuelt, tydelig fremheving av hver parameters navn og tilhørende verdi.

## 3. Brukstrinn

  1. Åpne nettleseren din og besøk nettsiden [URL Parser](https://atoolio.com/url-parser).
  2. Skriv inn URL-strengen du ønsker å analysere i inndatafeltet, f.eks. "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Klikk på analyseknappen (vanligvis kan du også trykke Enter for å starte analysen), verktøyet vil automatisk analysere den angitte URL-en og vise detaljene til hver komponent nedenfor.
  4. Sjekk analyseresultatet og kopier ved behov den tilsvarende delen av komponentene for videre utvikling, feilsøking eller andre operasjoner.

## 4. Eksempler

  1. **Eksempel 1**
     * Innskrevet URL: "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Analyseresultat:
       * Protokoll: http:
       * Brukernavn: user
       * Passord: pass
       * Vertsnavn: example.com
       * Port: 8080
       * Bane: /page
       * Parametere: ?param1=hello&param2=world
       * Detaljert visning av parametere:
         * param1: hello
         * param2: world

  2. **Eksempel 2**
     * Innskrevet URL: "https://www.google.com/s?wd=URL Parser"
     * Analyseresultat:
       * Protokoll: https:
       * Brukernavn: (ingen)
       * Passord: (ingen)
       * Vertsnavn: www.google.com
       * Port: (standardport 443, ikke vist)
       * Bane: /s
       * Parametere: ?wd=URL Parser
       * Detaljert visning av parametere:
         * wd: URL Parser