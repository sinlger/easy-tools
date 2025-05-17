# Crontab-Ausdruckgenerator Benutzerdokumentation

## 1. Tool-Übersicht

Der Crontab-Ausdruckgenerator ist ein Online-Werkzeug, das Benutzern hilft, Crontab-Ausdrücke einfach zu erstellen und zu validieren sowie lesbare Beschreibungen für cron-Jobs zu generieren.

## 2. Funktionsbeschreibung

1. **Crontab-Ausdruck-Erstellung**

   * **Manuelle Eingabe** - Geben Sie direkt im Eingabefeld einen Crontab-Ausdruck ein, z.B. "40 * * * *", das Tool generiert automatisch die entsprechende Beschreibung: "Bei 40 Minuten nach der Stunde, jede Stunde, jeden Tag".
   * **Voreinstellungen auswählen** - Das Tool stellt mehrere vordefinierte Ausdrucksoptionen bereit, wie z.B. "@yearly", "@monthly" usw. Klicken Sie auf eine Option, um schnell den entsprechenden Crontab-Ausdruck zu generieren.

2. **Crontab-Ausdruck-Validierung**

   * Nachdem Sie einen benutzerdefinierten Crontab-Ausdruck eingegeben haben, überprüft das Tool automatisch, ob dieser dem korrekten Format entspricht. Bei gültigem Format wird die entsprechende Beschreibung angezeigt, bei ungültigem Format wird eine Korrektur empfohlen.

3. **Lesbare Beschreibung erhalten**

   * Für eingegebene oder ausgewählte Crontab-Ausdrücke generiert das Tool verständliche natürlichsprachliche Beschreibungen, um Benutzern das Verständnis zu erleichtern.

4. **Anpassbare Einstellungen**

   * **Ausführliche Modus (Verbose)** - Aktivieren Sie diese Option, um detailliertere Protokollinformationen zu erhalten.
   * **24-Stunden-Zeitformat verwenden** - Wählen Sie, ob die Zeit im 24-Stunden-Format angezeigt werden soll.
   * **Tage beginnen bei 0** - Legen Sie fest, ob Tage bei 0 oder bei 1 gezählt werden sollen.

5. **Crontab-Symbolerklärung**

   * **Stern (*)** - Steht für jeden Wert, z.B. bedeutet "* * * *", dass der Job jede Minute ausgeführt wird.
   * **Bindestrich (-)** - Dient zur Angabe eines Wertebereichs, z.B. "1 - 10 * * *" bedeutet, dass der Job zwischen Minute 1 und 10 ausgeführt wird.
   * **Komma (,)** - Wird verwendet, um mehrere Werte anzugeben, z.B. "1,10 * * *" steht für die Ausführung in Minute 1 und 10.
   * **Schrägstrich (/)** - Dient zur Festlegung von Schrittwerten, z.B. "*/10 * * *" bedeutet, dass der Job alle 10 Minuten ausgeführt wird.
   * **Spezialsymbole (@)** - Enthält @yearly, @monthly, @weekly, @daily, @midnight, @hourly, @reboot usw., welche jährlich, monatlich, wöchentlich, täglich, um Mitternacht, stündlich bzw. beim Systemstart die Ausführung eines Jobs anstoßen.