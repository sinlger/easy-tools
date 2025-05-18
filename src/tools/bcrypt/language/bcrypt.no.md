# Tekstkrypteringsverktøy Brukerhåndbok

## 1. Verktøyets beskrivelse

Dette er et kraftig tekstkrypteringsverktøy som hovedsakelig er basert på bcrypt-algoritmen og støtter tekstkryptering samt sammenligningsverifikasjon av de krypterte hash-verdiene med originalteksten. Det kan brukes i sikkerhetsrelaterte anvendelsesområder som passordlagring og verifisering.

## 2. Tilgang til verktøyet

Skriv inn URL-en til siden der dette verktøyet befinner seg i nettleserens adressefelt, trykk "Enter" for å åpne siden og vent til alle sidens elementer er fullstendig lastet.

## 3. Betjeningsveiledning

### (1) Kryptering av tekst

1. **Skriv inn teksten** : Skriv inn den teksten du ønsker å kryptere i inndatafeltet merket "Your string". For eksempel passordet som en bruker har satt under registrering.
2. **Sett Salt count** : Trykk på knappene "+" eller "-" ved siden av "Salt count" for å justere antall iterasjoner for saltverdien. Salt er en tilfeldig generert streng som legges til originalteksten før krypteringen for å forbedre sikkerheten og hindre angrep som regnbueangrep. Generelt anbefales det å bruke minst 10 iterasjoner.
3. **Vis krypteringsresultat** : Etter at de ovennevnte innstillingene er fullført, vil verktøyet automatisk kryptere den angitte teksten og vise den resulterende hash-verdien i feltet nedenfor. Denne hash-verdien inneholder informasjon om algoritmen som ble brukt, saltverdien og den krypterte teksten.