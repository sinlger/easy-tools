# HTTP-statuskoder Dokumentasjon

## 1. Introduksjon

HTTP-statuskoder er tresifrede numeriske koder som sendes av serveren som en del av HTTP-svaret til klienten (vanligvis en nettleser). De indikerer statusen på en forespørsel og hjelper med å forstå om forespørselen var vellykket, om omdirigering er nødvendig eller om det oppstod feil.

## 2. Hovedkategorier av HTTP-statuskoder

### 1xx: Informasjonsrespons

Disse kodene indikerer at forespørselen ble forstått og at serveren fortsetter å arbeide. Eksempler:
- **100 Continue** - Klienten bør fortsette med forespørselen.
- **101 Switching Protocols** - Klienten har bedt om å endre kommunikasjonsprotokoll, f.eks. fra HTTP til WebSocket.

### 2xx: Vellykket forespørsel

Disse kodene betyr at forespørselen ble mottatt, forstått og akseptert. Eksempler:
- **200 OK** - Forespørselen var vellykket, og de ønskede data ble funnet og overført.
- **201 Created** - En ressurs ble opprettet, ofte etter en POST-forespørsel.
- **204 No Content** - Forespørselen var vellykket, men det er ingen innhold å returnere.