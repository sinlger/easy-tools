# Docker Run zu Docker-Compose-Konverter Dokumentation

## 1. Tool-Übersicht

Der Docker Run zu Docker-Compose-Konverter ist ein praktisches Online-Werkzeug, das Entwicklern dabei hilft, Befehlszeilen des Typs "docker run" schnell in Docker-Compose-Dateien umzuwandeln. Dadurch wird der Konfigurationsprozess für Container-Orchestrierung vereinfacht und die Entwicklungsproduktivität gesteigert.

## 2. Hauptfunktionen

1. **Befehlskonvertierung**
   * Benutzer können komplexe Docker-Befehle wie z.B. "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx" in ein vorgesehenes Eingabefeld einfügen.
   * Das Tool analysiert automatisch alle Parameter aus dem Docker-run-Befehl, einschließlich Port-Mappings ("-p 80:80"), Volume-Mounts ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), Restart-Richtlinien ("--restart always"), Log-Optionen ("--log-opt max-size=1g") und Image-Namen ("nginx").

2. **Erstellung von Docker-Compose-Dateien**
   * Basierend auf den analysierten Parametern des Docker-run-Befehls generiert das Tool den entsprechenden Inhalt für eine Docker-Compose-Datei.
   * Die erzeugte YAML-Datei enthält Deklarationen zur Version (z.B. "version: '3.9'"), Dienstedefinitionen ("services"), Angaben zum Image ("image"), Logging-Konfigurationen ("logging" mit "options"), Restart-Einstellungen ("restart"), Volume-Zuordnungen ("volumes") sowie Port-Mappings ("ports"). Damit wird die gesamte Container-Orchestrierungsinformation vollständig dargestellt, sodass Benutzer diese direkt verwenden oder weiter anpassen können.

3. **Dateidownload**
   * Ein "Download docker-compose.yml" Button ermöglicht es Benutzern, die generierte Docker-Compose-Datei mit nur einem Klick lokal herunterzuladen. Somit kann diese problemlos in realen Projektumgebungen angewandt und genutzt werden.