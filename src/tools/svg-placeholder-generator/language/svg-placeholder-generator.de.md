# SVG-Platzhaltergenerator Benutzerdokumentation

## 1. Einführung in das Tool

Der SVG-Platzhaltergenerator ist ein praktisches Online-Tool zur schnellen Erstellung von benutzerdefinierten SVG-Platzhalterbildern. Diese Platzhalter können während des Entwicklungsprozesses von Anwendungen als vorläufige Bilder verwendet werden, um bei der Gestaltung und Vorschau der Oberfläche zu helfen, wenn noch keine echten Bilddaten vorhanden sind.

## 2. Funktionsbeschreibung

### (1) **Größeneinstellungen**

* **Breite und Höhe**: Die Breite und Höhe des Platzhalters (in Pixeln) kann jeweils über Eingabefelder festgelegt werden. Zudem stehen "+" und "-" Schaltflächen zur schnellen Größenanpassung zur Verfügung.
* **Exakte Größe verwenden**: Wenn diese Option aktiviert ist, wird sichergestellt, dass das generierte SVG-Bild exakt der angegebenen Breite und Höhe entspricht.

### (2) **Farbanpassung**

* **Hintergrundfarbe**: Durch Eingabe eines Hexadezimal-Farb-Codes (z. B. "#cccccc") kann die Hintergrundfarbe des Platzhalters individuell angepasst werden.
* **Textfarbe**: Ebenfalls mithilfe eines Hexadezimal-Farb-Codes (z. B. "#333333") lässt sich die Farbe des auf dem Platzhalter dargestellten Textes bestimmen.

### (3) **Textkonfiguration**

* **Schriftgröße**: Geben Sie einen numerischen Wert ein und wählen Sie eine passende Einheit (z. B. Pixel), um die Schriftgröße des angezeigten Textes anzupassen.
* **Eigener Text**: Tragen Sie den gewünschten Text in das entsprechende Feld ein. Standardmäßig wird dabei die Formatierung "Breite x Höhe" angezeigt (z. B. "600x350").

### (4) **Vorschau und Export**

* **Live-Vorschau**: Im rechten Vorschaubereich lässt sich live der Effekt des gemäß der eingestellten Parameter generierten SVG-Platzhalters verfolgen.
* **SVG HTML Element**: Zeigt den generierten SVG-Code an, welcher direkt kopiert und in Webentwicklungen eingebunden werden kann.
* **SVG in Base64**: Stellt den SVG-Platzhalter als Base64-kodierten String bereit, was für Szenarien nützlich ist, in denen spezielle Kodierungsformate erforderlich sind.

## 3. Bedienungsschritte

1. Öffnen Sie die [Website des SVG-Platzhaltergenerators](https://atoolio.com/svg-placeholder-generator).
2. Legen Sie die gewünschte Breite und Höhe des Platzhalters fest. Möchten Sie z. B. einen Platzhalter mit einer Breite von 800 Pixeln und einer Höhe von 450 Pixeln erstellen, geben Sie in das Feld "Width (in px)" den Wert "800" und in das Feld "Height (in px)" den Wert "450" ein.
3. Passen Sie die Hintergrund- und Textfarbe nach Wunsch an. Soll der Hintergrund hellblau (z. B. "#e6f7ff") und der Text dunkelblau (z. B. "#1890ff") sein, geben Sie die entsprechenden Farbcodes in die dafür vorgesehenen Felder ein.
4. Bestimmen Sie Schriftgröße und individuellen Text. Angenommen, die Schriftgröße soll 20 Pixel betragen und der angezeigte Text "Sample" lauten, dann tragen Sie in das Feld "Font size" den Wert "20" ein und in das Feld "Custom text" den Text "Sample".
5. Überprüfen Sie im rechten Vorschaubereich, ob das generierte Platzhalterbild den Vorstellungen entspricht.
6. Abhängig vom konkreten Verwendungszweck können Sie entweder den unter "SVG HTML element" angezeigten Code oder den Base64-kodierten String kopieren und in Ihr Entwicklungsprojekt einfügen. Alternativ klicken Sie auf den Button "Download svg", um das erzeugte SVG-Bild direkt herunterzuladen.