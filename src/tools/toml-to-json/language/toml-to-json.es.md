# Documentación del usuario del convertidor TOML a JSON en línea

## 1. Descripción de la herramienta

TOML a JSON es una herramienta en línea práctica que analiza datos en formato TOML y los convierte en formato JSON. Los usuarios pueden pegar o introducir fácilmente datos TOML en el campo de entrada izquierdo, y el resultado correspondiente en formato JSON se generará automáticamente en el área derecha.

## 2. Descripción detallada de las funciones

### 1. Entrada de datos TOML

* En el campo de texto izquierdo "Your TOML", los usuarios pueden pegar o introducir manualmente datos en formato TOML. Este campo de texto soporta la entrada de texto multilínea, ofreciendo suficiente espacio para introducir información de configuración TOML más compleja.

### 2. Salida del resultado JSON

* Una vez que se introducen datos TOML en el campo de texto izquierdo, la herramienta realiza automáticamente el análisis y la conversión. Los datos JSON convertidos aparecerán en el campo de texto derecho "JSON from your TOML". Los usuarios pueden visualizarlos, copiarlos o procesarlos posteriormente.

## 3. Pasos para su uso

1. Abra la página de la herramienta ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. En el campo de texto izquierdo "Your TOML", pegue o introduzca los datos TOML que desee convertir.
3. El sistema realizará automáticamente la conversión, y el resultado aparecerá en el campo de texto derecho "JSON from your TOML".

## 4. Características principales

* Sencillez y facilidad de uso: La interfaz es clara e intuitiva, el proceso de operación es sencillo, no requiere configuraciones complejas, lo que permite a los usuarios comenzar a usarla rápidamente.
* Conversión en tiempo real: Una vez introducidos los datos TOML, la herramienta realiza automáticamente la conversión y muestra el resultado, sin necesidad de hacer clic manualmente en un botón de conversión, lo que mejora la eficiencia del proceso.
* Uso en línea: No es necesario instalar ningún software. Con solo disponer de un dispositivo con acceso a Internet, podrá utilizar esta herramienta para convertir TOML a JSON en cualquier momento y lugar.

## 5. Ejemplos

### Ejemplo 1: Conversión sencilla de TOML a JSON

Supongamos que tenemos los siguientes datos en formato TOML:
```toml
title = "TOML Example"
owner = "John Doe"
```

Al pegar estos datos en el campo de texto izquierdo "Your TOML", la herramienta los convertirá automáticamente al siguiente formato JSON:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Ejemplo 2: Conversión de TOML a JSON con estructura anidada

Tenemos datos TOML más complejos:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Después de introducirlos en la herramienta, obtendremos los siguientes datos JSON:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}