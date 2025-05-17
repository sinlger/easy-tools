# Documentación del usuario para el Regex Tester de A Toolio

## 1. Introducción a la herramienta

El **Regex Tester de A Toolio** es una herramienta en línea que permite probar expresiones regulares mediante la introducción de textos de ejemplo. Su interfaz clara y sus funciones prácticas lo hacen adecuado tanto para aprendices como para desarrolladores que trabajan con expresiones regulares.

## 2. Descripción detallada de las funciones

### (1) Área de entrada para expresiones regulares

Introduzca en el campo de texto la expresión regular que desee probar. Se proporciona un enlace a una tabla de referencia rápida para expresiones regulares, útil durante su uso. Por ejemplo, la expresión regular \w+ puede utilizarse para encontrar una o más palabras.

### (2) Opciones del Regex Tester

Las opciones incluyen: Búsqueda global (g), Ignorar mayúsculas/minúsculas (i), Modo multilínea (m), Modo de una sola línea (s), Soporte Unicode (u) y Soporte de conjunto Unicode (v). Seleccione las opciones según sus necesidades específicas.

- Búsqueda global (g): Busca todas las coincidencias en el texto completo.
- Ignorar mayúsculas/minúsculas (i): Encuentra coincidencias ignorando diferencias de mayúsculas y minúsculas.
- Modo multilínea (m): Trata la entrada como un texto multilínea, permitiendo buscar al inicio y final de cada línea.
- Modo de una sola línea (s): Trata todo el texto como una única línea, facilitando búsquedas que atraviesan múltiples líneas.
- Soporte Unicode (u): Habilita soporte para caracteres Unicode.
- Soporte de conjunto Unicode (v): Soporta conjuntos avanzados de caracteres Unicode.

Ejemplo: La expresión regular \d{3}-\d{3}-\d{4} puede encontrar múltiples números telefónicos cuando la búsqueda global está activa.

### (3) Área de entrada del texto a comparar

Introduzca en el campo de texto el contenido donde desea encontrar coincidencias. La herramienta buscará patrones basándose en la expresión regular introducida y las opciones seleccionadas. Por ejemplo, al usar la expresión regular \w+ en el texto "Encuentra palabras en este texto", podrá localizar todas las palabras individuales.