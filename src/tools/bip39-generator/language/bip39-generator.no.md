# A Toolio - BIP39-passordfrasegenerator Dokumentasjon

## 1. Verktøybeskrivelse

BIP39-passordfrasegeneratoren er et online verktøy som kan generere BIP39-passordfraser fra eksisterende eller tilfeldige minnedeviser, og støtter også henting av minnedeviser fra passordfraser. Dette verktøyet gir utviklere praktiske passordrelaterte operasjoner, egnet for flere anvendelsesområder.

## 2. Funksjonsmoduler og bruksanvisning

### 1. **Språkvalg**
   * **Funksjon**: Brukeren kan velge mellom ulike språkalternativer i en nedtrekksliste etter behov. For øyeblikket støttes "Chinese simplified" osv., for å sette språktypen til minnedevisa.
   * **Brukstrinn**: Klikk på språkvalgsboksen og velg det ønskede språket for minnedevisene i den visuelle nedtrekkslisten, slik som kinesisk (forenklet) osv.

### 2. **Generering av minnepassord**
   * **Funksjon**: Basert på entropi-strengen som angis av brukeren eller som genereres tilfeldig, genererer verktøyet den tilsvarende BIP39-minnefrasen i henhold til det valgte språket, og gir brukeren en huskemodell for lagring og videre bruk.
   * **Brukstrinn**:
     1. Skriv inn ønsket entropi-streng i tekstboksen "Entropy (seed):". Hvis du ikke ønsker manuell innskriving, kan du klikke på ikonet "Tilfeldig" ved siden av feltet for å generere en tilfeldig entropi.
     2. Velg språk for minnedevisa (allerede beskrevet i språkvalgsmodulen) og klikk på "Generer"-knappen. Tekstboksen "Passphrase (mnemonic):" nedenfor vil automatisk generere den korresponderende minnefrasen.