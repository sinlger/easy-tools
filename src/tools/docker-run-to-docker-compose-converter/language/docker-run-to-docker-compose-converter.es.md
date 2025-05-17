# Documentación del Convertidor de Docker Run a Docker-Compose

## 1. Descripción General de la Herramienta

El Convertidor de Docker Run a Docker-Compose es una herramienta en línea conveniente que ayuda a los desarrolladores a transformar comandos de línea "docker run" en archivos Docker-Compose. Esto simplifica el proceso de configuración de orquestación de contenedores y mejora la productividad durante el desarrollo.

## 2. Funciones Principales

1. **Conversión de Comandos**
   * Los usuarios pueden pegar comandos Docker complejos, como por ejemplo: "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx", en un campo de entrada designado.
   * La herramienta analiza automáticamente cada parámetro del comando "docker run", incluyendo mapeo de puertos ("-p 80:80"), montaje de volúmenes ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), políticas de reinicio ("--restart always"), opciones de registro ("--log-opt max-size=1g") y el nombre de la imagen ("nginx").

2. **Generación de Archivos Docker-Compose**
   * Con base en los parámetros extraídos del comando "docker run", genera el contenido correspondiente del archivo Docker-Compose.
   * El archivo YAML generado incluye declaraciones de versión (por ejemplo, "version: '3.9'"), definiciones de servicios ("services"), especificación de imágenes ("image"), configuración de registros ("logging" con "options"), políticas de reinicio ("restart"), asignaciones de volúmenes ("volumes") y mapeos de puertos ("ports"). De esta manera, se presenta completamente la información de orquestación de contenedores para que los usuarios puedan usarla directamente o realizar modificaciones adicionales.

3. **Descarga del Archivo**
   * Se proporciona un botón "Download docker-compose.yml" que permite a los usuarios descargar con un solo clic el archivo Docker-Compose generado a su computadora local. Esto facilita su aplicación y gestión en entornos reales de proyectos.