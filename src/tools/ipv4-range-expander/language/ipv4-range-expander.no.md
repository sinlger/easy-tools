# IPv4 Områdesekspander Dokumentasjon

## 1. Verktøybeskrivelse

IPv4 Områdesekspander beregner effektive IPv4 nettverk basert på gitte start- og sluttpunkter for IPv4-adresser. Dette inkluderer gyldige nettblokker (vist i CIDR-notation), adresseområder og totalt antall adresser innenfor området.

## 2. Funksjonsdetaljer

### (A) Grunnleggende inndatafunksjon

1. **Inndata av Startadresse** - Skriv inn en IPv4-adresse i feltet "Start address" som skal brukes som utgangspunkt, f.eks. "192.168.1.1".
2. **Inndata av Sluttadresse** - Skriv inn en IPv4-adresse i feltet "End address" som skal brukes som sluttpunkt, f.eks. "192.168.6.255".

### (B) Automatisk behandling og resultatvisning

1. **Justering av adresseområde** - Verktøyet justerer automatisk start- og slutadressene til et mer passende område. For eksempel vil "192.168.1.1" bli justert til "192.168.0.0", og "192.168.6.255" blir "192.168.7.255".
2. **Beregning av antall adresser** - Totalt antall IPv4-adresser tilgjengelig i det nye området beregnes, for eksempel øker det fra "1.535" til "2.048", noe som forbedrer effektiviteten i bruken av adresseressurser.
3. **Generering av CIDR-notation** - Den tilhørende CIDR-notationen for det nye adresseområdet vises, som f.eks. "192.168.0.0/21", noe som forenkler nettverksadministrasjon og konfigurasjon.

## 3. Viktige Merknader

Sørg for at de oppgitte start- og slutadressene følger riktig IPv4-adresseformat for å sikre nøyaktig funksjon og resultater fra verktøyet.