# Dokumentasjon for Docker Run til Docker-Compose-konvertereren

## 1. Verktøyoversikt

Docker Run til Docker-Compose-konvertereren er et praktisk online verktøy som hjelper utviklere med å gjøre om kommandolinjer "docker run" til Docker-Compose-filer. Dette forenkler konfigurasjonsprosessen for container-orchestration og øker utviklingseffektiviteten.

## 2. Hovedfunksjoner

1. **Kommando-konvertering**
   * Brukere kan lime inn komplekse Docker-kommandoer, som f.eks. "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx", i et spesielt inndatafelt.
   * Verktøyet analyserer automatisk alle parametrene fra "docker run"-kommandoen, inkludert port-mapping ("-p 80:80"), volum-montering ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), omstartspolitikk ("--restart always"), loggvalg ("--log-opt max-size=1g") og bildetnavn ("nginx").

2. **Generering av Docker-Compose-filer**
   * Basert på de analyserte parameterne fra "docker run"-kommandoen, genererer verktøyet tilhørende Docker-Compose-filinnhold.
   * Den genererte YAML-filen inneholder versjonserklæring (f.eks. "version: '3.9'"), tjenestedefinisjoner ("services"), bildeangivelse ("image"), loggkonfigurasjon ("logging" med "options"), omstartsinstruksjoner ("restart"), volumtilordninger ("volumes") og port-mapping ("ports"). Dermed blir hele informasjonen om container-orchestration presentert fullstendig, slik at brukerne enkelt kan bruke eller viderejustere filen.

3. **Filnedlasting**
   * En knapp merket "Download docker-compose.yml" lar brukerne laste ned den genererte Docker-Compose-filen lokalt med ett klikk. Dette gjør det lett å anvende og administrere containertjenester i reelle prosjektmiljøer.