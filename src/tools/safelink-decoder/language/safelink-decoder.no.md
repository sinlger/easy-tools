# Outlook Safelink dekoder Brukerdokumentasjon

## 1. Introduksjon til verktøyet
**Outlook Safelink dekoderen** er et verktøy som er utformet for å dekode lenkene som blir generert av Microsoft Outlook e-posttjenesten under navnet SafeLink. Dette verktøyet lar deg omforme krypterte lenker laget av Outlook SafeLink tilbake til deres originale nettadresser (URL-er), noe som gjør det lettere for brukere å identifisere hvor disse lenkene faktisk fører til.

## 2. Funksjonsbeskrivelse
Hovedfunksjonen til dette verktøyet er å dekode Outlook Safelink-lenker, altså konvertere de krypterte og videresendte lenkene som blir opprettet av Microsoft Outlook tilbake til de opprinnelige webadressene.

## 3. Bruksanvisning

### Inndata
Lim inn Outlook Safelink-lenken du ønsker å dekode i inndatafeltet. Denne lenken har blitt kryptert av Microsoft Outlook av sikkerhetsgrunner og har et spesifikt format.

### Utdata
Etter at du har klikket på "Decode"-knappen, vil verktøyet behandle den innskrevne lenken og vise den opprinnelige URL-en i utdatafeltet. Hvis lenken ikke er riktig formatert eller ikke kan gjenkjennes, vil det vises en feilmelding: "Error: Invalid SafeLinks URL provided".

## 4. Eksempler på bruken

### Eksempel 1
Inndata (SafeLink-lenke):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Utdata etter dekoding:
`https://example.com`

### Eksempel 2
Inndata (SafeLink-lenke):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Utdata etter dekoding:
`https://microsoft.com`

### Eksempel 3
Inndata med ugyldig eller feilformatert lenke:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Feilmelding:
`Error: Invalid SafeLinks URL provided`

## 5. Viktige merknader
- Sørg for at lenken du skriver inn er en komplett Outlook Safelink.