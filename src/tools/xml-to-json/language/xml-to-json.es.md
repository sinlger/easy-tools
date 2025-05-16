# Herramienta de Conversión de XML a JSON

## 1. Introducción
Esta es una herramienta en línea para convertir datos con formato XML a formato JSON. Mejora la eficiencia del desarrollo y es adecuada para escenarios donde se requiere la conversión entre formatos de datos XML y JSON.

## 2. Funciones Principales

### (1) Entrada de Contenido XML
Pega o escribe los datos XML que deseas convertir en el área de entrada. Por ejemplo, puedes ingresar el siguiente contenido XML:
```
<a x="1.234" y="It's"/>
```

### (2) Salida de Datos JSON
Después de hacer clic en el botón de conversión, la herramienta mostrará los datos formateados en JSON correspondientes en el área de salida. Por ejemplo, el XML anterior se convertirá en los siguientes datos JSON:
```json
{
  "a": {
    "_atributos": {
      "x": "1.234",
      "y": "It's"
    }
  }
}
```

### (3) Función de Copiado
En el área de salida de datos JSON, puedes hacer clic en el botón de copiar para transferir los datos JSON generados al portapapeles, facilitando su uso en otros lugares.