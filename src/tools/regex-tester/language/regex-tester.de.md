# A Toolio - Regex-Tester Benutzerdokumentation

## 1. Einführung in das Tool

Der **A Toolio Regex-Tester** ist ein Online-Tool, das es ermöglicht, reguläre Ausdrücke durch die Eingabe von Beispieltexten zu testen. Mit seiner klaren Oberfläche und praktischen Funktionen eignet es sich sowohl für Lernende als auch für Entwickler.

## 2. Detaillierte Funktionsbeschreibung

### (1) Bereich zur Eingabe regulärer Ausdrücke

Geben Sie den regulären Ausdruck, den Sie testen möchten, in das Textfeld ein. Ein unten stehender Link bietet eine schnelle Referenztabelle für reguläre Ausdrücke, um Ihnen während der Nutzung zu helfen. Beispielsweise können Sie mit dem regulären Ausdruck \w+ ein oder mehrere Wortzeichen finden.

### (2) Optionen des Regex-Testers

Die verfügbaren Optionen sind: Globale Suche (g), Groß-/Kleinschreibung ignorieren (i), Mehrzeilenmodus (m), Einzelzeilenmodus (s), Unicode-Support (u) und Unterstützung für Unicode-Zeichensätze (v). Wählen Sie je nach Ihren Anforderungen die passenden Optionen aus.

- Globale Suche (g): Sucht nach allen Übereinstimmungen im gesamten Text.
- Groß-/Kleinschreibung ignorieren (i): Findet Übereinstimmungen unabhängig von der Schreibweise.
- Mehrzeilenmodus (m): Behandelt die Eingabe als mehrzeiligen Text, sodass am Anfang und Ende jeder Zeile gesucht werden kann.
- Einzelzeilenmodus (s): Betrachtet den gesamten Text als eine einzige Zeile, was bei der Suche über Zeilen hinweg hilft.
- Unicode-Support (u): Aktiviert Unterstützung für Unicode-Zeichen.
- Unterstützung für Unicode-Zeichensätze (v): Unterstützt erweiterten Unicode-Zeichensatz.

Beispiel: Der reguläre Ausdruck \d{3}-\d{3}-\d{4} kann bei aktivierter globaler Suche mehrere Telefonnummern in einem Text finden.

### (3) Bereich zur Eingabe von Text

Geben Sie den Text ein, in dem Sie mit Ihrem regulären Ausdruck übereinstimmende Muster finden möchten. Das Tool sucht anhand des eingegebenen regulären Ausdrucks und der gewählten Optionen nach Übereinstimmungen. Beispielsweise können Sie mit dem regulären Ausdruck \w+ alle Wörter im Text "Finde Wörter in diesem Text" finden.