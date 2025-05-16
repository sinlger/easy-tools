# Online brukeragentparser - Brukerdokumentasjon

## 1. Verktøyoversikt

Denne online-brukeragentparseren kan nøyaktig oppdage og analysere informasjon om nettleser, renderingsmotor, operativsystem, CPU-arkitektur og enhetstype/modell fra brukeragentstrengen. Dette hjelper utviklere med å raskt få detaljer om klienten.

## 2. Funksjonsbeskrivelse

### (1) Nettlesergjenkjenning

Den kan nøyaktig identifisere hvilken type nettleser brukeren bruker og den spesifikke versjonen. For eksempel, når en bestemt streng tastes inn, viser det "Edge 135.0.0.0", noe som indikerer at klientens nettleser er Edge og at versjonen er 135.0.0.0.

### (2) Motorgjenkjenning

Den viser tydelig renderingsmotoren brukt av nettleseren og den tilhørende versjonen. Hvis den viser "Blink 135.0.0.0", betyr dette at renderingsmotoren er Blink og versjonen er 135.0.0.0.

### (3) Operativsystemsgjenkjenning

Den viser i detalj navnet på operativsystemet og versjonen. For eksempel "Windows 10", som betyr at operativsystemet er Windows og versjonen er 10.

### (4) Enhetsinformasjonsdeteksjon

Den kan hente informasjon som enhetstype, modell og produsent (hvis tilgjengelig). For eksempel kan noen enheter vise modellnummer fullstendig, men det finnes også tilfeller der det ikke er noen tilgjengelige enhetsmodeller, typer eller produsenter. I slike tilfeller vil det være en melding: "No device model/type/vendor available".

### (5) Prosessorinformasjonsdeteksjon

Den kan identifisere prosessorrelaterte egenskaper. Hvis "amd64" vises, betyr det at CPU-arkitekturen er av typen amd64.

## 3. Brukseksempler

### Eksempel én: Vanlig desktop-nettleser

Anta at brukeragentstrengen er:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Etter å ha skrevet inn denne strengen i parseren:

  * **Nettleser**: Det blir identifisert som Edge 135.0.0.0.
  * **Motor**: Den blir identifisert som Blink 135.0.0.0.
  * **Operativsystem**: Det er Windows 10.
  * **Enhet**: Det er ingen spesifikk enhetsmodell, type eller produsent tilgjengelig, så en passende melding blir vist.
  * **CPU**: Arkitekturen er amd64.

### Eksempel to: Mobilnettleser

La oss ta følgende brukeragentstreng som eksempel:
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Etter å ha skrevet inn dette i parseren:

  * **Nettleser**: Den kan identifisere at det er Safari under iOS og tilhørende versjonsinformasjon (den nøyaktige versjonen avhenger av faktiske analyseresultater).
  * **Motor**: Den viser den tilhørende Webkit-motoren med versjonsdetaljer.
  * **Operativsystem**: Det blir tydelig identifisert som iOS og tilhørende versjonsnummer (for eksempel 16_6_1 osv.).
  * **Enhet**: Det kan hentes informasjon om enheten, for eksempel at det er en iPhone (det konkrete modellnummeret avhenger av analysens resultater).
  * **CPU**: Den viser tilpasset CPU-arkitektur for mobile enheter (hvis deler tydelig kan identifiseres).