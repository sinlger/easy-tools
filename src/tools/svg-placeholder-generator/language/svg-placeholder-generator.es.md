# Documentación del usuario para el generador de marcadores de posición SVG

## 1. Introducción a la herramienta

El generador de marcadores de posición SVG es una herramienta en línea conveniente para crear rápidamente imágenes de marcador de posición SVG personalizadas. Estos marcadores de posición se pueden utilizar durante el proceso de desarrollo de aplicaciones para mostrar imágenes temporales, ayudando a los desarrolladores a diseñar y visualizar el diseño de la interfaz antes de tener contenido de imagen real.

## 2. Descripción de las funciones

### (1) **Configuración del tamaño**

* **Ancho y alto**: Puedes establecer el ancho y el alto del marcador de posición (en píxeles) mediante cuadros de entrada, además hay botones '+' y '-' para ajustar rápidamente las dimensiones.
* **Usar tamaño exacto**: Al activar esta opción, se garantiza que el marcador de posición SVG generado se muestre estrictamente según el ancho y alto especificados.

### (2) **Personalización del color**

* **Color de fondo**: Introduce un código de color hexadecimal (por ejemplo, "#cccccc") para personalizar el color de fondo del marcador de posición.
* **Color del texto**: De manera similar, introduce un código de color hexadecimal (por ejemplo, "#333333") para establecer el color del texto mostrado en el marcador de posición.

### (3) **Configuración del texto**

* **Tamaño de fuente**: Introduce un valor numérico y selecciona una unidad adecuada (como píxeles) para ajustar el tamaño del texto mostrado en el marcador de posición.
* **Texto personalizado**: Escribe el contenido que desees mostrar en el cuadro de texto; por defecto se muestra "ancho x alto" (por ejemplo, "600x350").

### (4) **Vista previa y salida**

* **Vista previa en tiempo real**: En el área de vista previa del lado derecho, puedes ver en tiempo real el efecto del marcador de posición SVG generado según los parámetros configurados.
* **Elemento HTML SVG**: Muestra el código SVG generado, que puede copiarse directamente y utilizarse en el desarrollo web.
* **SVG en Base64**: Ofrece la posibilidad de convertir la imagen SVG en una cadena codificada en Base64, útil en escenarios que requieren este formato especial.

## 3. Pasos para usar la herramienta

1. Abre el sitio web [Generador de marcadores de posición SVG](https://atoolio.com/svg-placeholder-generator).
2. Configura el ancho y el alto del marcador de posición según tus necesidades. Por ejemplo, si deseas generar un marcador de 800 píxeles de ancho y 450 píxeles de alto, introduce "800" en el campo "Width (in px)" y "450" en el campo "Height (in px)".
3. Personaliza el color de fondo y el color del texto. Si deseas que el fondo sea azul claro (por ejemplo, "#e6f7ff") y el texto azul oscuro (por ejemplo, "#1890ff"), introduce los códigos de color correspondientes en sus campos respectivos.
4. Ajusta el tamaño de fuente y el texto personalizado. Supongamos que el tamaño de fuente es 20 píxeles y quieres mostrar el texto "Sample", introduce "20" en el campo "Font size" y "Sample" en el campo "Custom text".
5. Revisa el área de vista previa del lado derecho para confirmar que la imagen del marcador de posición cumple con tus expectativas.
6. Según tus necesidades reales, elige copiar el código proporcionado por "SVG HTML element", o bien copiar la cadena codificada en Base64, y pégala en tu proyecto de desarrollo correspondiente. También puedes hacer clic en el botón "Download svg" para descargar directamente el archivo SVG generado.