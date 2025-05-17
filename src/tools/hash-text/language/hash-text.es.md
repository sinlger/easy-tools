# Documentación del Generador de Hash de Texto de A Toolio

## 1. Descripción de la herramienta

El generador de hash de texto de A Toolio es una herramienta en línea conveniente que puede procesar cadenas de texto mediante múltiples algoritmos hash. Soporta muchos algoritmos hash como MD5, SHA1, SHA256, SHA224, SHA512, SHA384, SHA3 y RIPEMD160, satisfaciendo las necesidades de diferentes escenarios en cuanto a encriptación de textos y verificación de integridad de datos.

## 2. Acceso a la herramienta

1. **Introducir URL** - Introduce <https://atoolio.com/hash-text> en la barra de direcciones del navegador y pulsa Enter para acceder a la página de la herramienta.
2. **Carga de la página** - Espera a que la página se cargue completamente, asegurando que los campos de entrada, opciones y botones relacionados con el hash puedan mostrarse correctamente.

## 3. Guía de operación

### (1) Ingresar texto

Encuentra el campo de entrada "Your text to hash" en la página, haz clic y escribe el texto que deseas procesar con hash. Puede ser una cadena corta o un párrafo más largo. Al introducirlo, asegúrate de que sea preciso, ya que cualquier diferencia mínima en el texto dará lugar a resultados de hash completamente distintos.

### (2) Seleccionar función hash

La página muestra una lista de varias opciones de funciones hash, incluyendo MD5, SHA1, SHA256, SHA224, SHA512, SHA384, SHA3 y RIPEMD160. Haz clic en la opción correspondiente a la función hash que desees usar. Los diferentes algoritmos hash generan valores hash con longitudes y niveles de seguridad distintos. Por ejemplo, MD5 genera un valor hash de 128 bits, mientras que SHA256 genera uno de 256 bits. Generalmente, cuantos más bits tenga el valor hash, menor será la probabilidad de colisión y mayor su nivel de seguridad.

### (3) Seleccionar codificación del resumen (Digest encoding)

En el menú desplegable "Digest encoding", puedes seleccionar el formato de codificación del valor hash, esto determinará la forma final en que se presenta el valor hash. Las opciones incluyen:

* **Hexadecimal (base 16)** - Convierte el arreglo de bytes del valor hash en una cadena hexadecimal. Cada byte corresponde a dos caracteres hexadecimales. Este formato es intuitivo y fácil de leer, adecuado para representar y revisar valores hash en texto.
* **Binario (base 2)** - Representa el valor hash como un arreglo binario de bytes. Es conveniente para el procesamiento interno por computadora, pero complicado para mostrarlo y manejarlo en interfaces de texto.
* **Base64 (base 64)** - Es un método de codificación que usa 64 caracteres imprimibles para representar datos binarios. La codificación Base64 transforma tres bytes de datos binarios en cuatro bytes de caracteres de texto, facilitando así la transmisión de datos binarios dentro de protocolos de texto.
* **Base64url (base 64 con caracteres seguros para URLs)** - Similar a la codificación Base64, pero utiliza un conjunto de caracteres compatibles con URLs durante el proceso de codificación, evitando posibles problemas de escape en URLs.

### (4) Generar el valor hash

Una vez completadas la selección de la función hash, el texto de entrada y la configuración de codificación del resumen, la herramienta procesará automáticamente el texto según la función y codificación seleccionadas y mostrará el resultado del hash correspondiente junto a la opción elegida en la página.

### (5) Copiar el valor hash

A la derecha de cada resultado mostrado hay un ícono de copia; hacer clic en él permitirá copiar el valor hash al portapapeles para poder pegarlo donde sea necesario, como almacenamiento en base de datos, escenarios de verificación de seguridad, etc.

## 4. Explicación del significado de los parámetros

### (1) Your text to hash

Este es el área destinada a ingresar el texto que desea someter a tratamiento hash. El texto ingresado servirá como parámetro de entrada a la función hash y tras su procesamiento generará un valor hash único. Pequeñas variaciones en el texto, como un espacio adicional o diferencias entre mayúsculas y minúsculas, provocarán cambios totalmente diferentes en el valor hash, esta es una de las características básicas de los algoritmos hash, lo cual garantiza la funcionalidad de verificación de integridad de datos.

### (2) Digest encoding

Como se explicó anteriormente, se usa para especificar el formato de codificación del valor hash generado. Diferentes formatos tienen sus propias características y aplicaciones:

* **Hexadecimal (base 16)** - Ampliamente utilizado en muchos lenguajes de programación y sistemas, por ejemplo, cuando se representa el valor hash MD5 frecuentemente se emplea la codificación hexadecimal. Sus ventajas son legibilidad y almacenamiento sencillo, además no contiene caracteres especiales que puedan causar problemas de transmisión o almacenamiento. Por ejemplo, el texto simple "hello" después del procesamiento con MD5 y codificado en hexadecimal podría dar un resultado similar a "5d41402abc4b2a76b9719d911017c592".
* **Binario (base 2)** - Es la forma básica de procesamiento interno de datos en computadoras, representando el valor hash como un arreglo binario de bytes. Puede usarse en ciertos escenarios que requieren integración con procesamiento de datos de bajo nivel o algoritmos criptográficos específicos, pero es menos conveniente para mostrarlo y manejarlo en interfaces de texto normales.
* **Base64 (base 64)** - Usado comúnmente para transmitir datos binarios en forma de texto, por ejemplo, adjuntos binarios en correos electrónicos o protocolos HTTP. Pues convierte cualquier dato binario en solo 64 caracteres básicos (como letras, números y '+' '/') evitando errores causados por caracteres no imprimibles o de control en la transmisión. Por ejemplo, el mismo "hello" tras el procesamiento MD5 y codificado en Base64 podría obtenerse aproximadamente como "XYBkfZP2jh Buchanan" (resultado de ejemplo, el real debe calcularse mediante una herramienta específica).
* **Base64url** - Una variante de Base64, cuya principal diferencia radica en que reemplaza '+' y '/' por '-' y '_', respectivamente, evitando problemas de análisis de caracteres especiales en URLs o nombres de archivos. Cuando los valores hash deben insertarse en parámetros de URL o utilizarse como nombre de archivo, Base64url ofrece ventajas, pues su cadena resultante es más estable y segura en URLs sin problemas de análisis de caracteres especiales.

### (3) Opciones de funciones hash (MD5, SHA1, SHA256, SHA224, SHA512, SHA384, SHA3, RIPEMD160)

Estas son diversas opciones de algoritmos hash disponibles, cada uno con características únicas y aplicaciones específicas:

* **MD5** - Un algoritmo hash ampliamente utilizado que calcula un valor hash de 128 bits (16 bytes) a partir de datos de entrada, normalmente mostrado como 32 caracteres hexadecimales. MD5 es rápido, pero se han descubierto vulnerabilidades por colisión (es decir, diferentes entradas pueden producir el mismo hash), por lo que no se recomienda su uso en escenarios con altos requisitos de seguridad (como almacenamiento de contraseñas, comunicaciones seguras). Sin embargo, sigue siendo útil como método rápido de verificación de integridad en datos no críticos.
* **SHA1** - Diseñado por la NSA (Agencia de Seguridad Nacional de EE.UU.), produce un valor hash de 160 bits (20 bytes). De manera similar a MD5, también se ha descubierto que es vulnerable a ataques de colisión, aunque su dificultad es algo mayor. Ha sido progresivamente abandonado en aplicaciones de seguridad crítica, pero aún puede estar presente en sistemas heredados o escenarios con requisitos de seguridad moderados.
* **SHA256, SHA224, SHA512, SHA384** - Todos pertenecen a la familia SHA-2 (Secure Hash Algorithm 2), sucesora de SHA-1, con mayor seguridad. Entre ellas:
   * **SHA224** - Produce un valor hash de 224 bits (28 bytes), adecuada para ciertos protocolos de seguridad o sistemas que requieran este tamaño específico.
   * **SHA256** - Produce un valor hash de 256 bits (32 bytes), ampliamente usado en muchos protocolos de seguridad y sistemas criptográficos, como la tecnología blockchain en monedas digitales como Bitcoin. Su seguridad es alta, hasta ahora no se han encontrado casos reales de colisión, por lo que se ha convertido en una opción predilecta en nuevos sistemas y aplicaciones.
   * **SHA384** - Produce un valor hash de 384 bits (48 bytes), adecuada para escenarios con mayores requisitos de seguridad, reduciendo aún más la probabilidad de colisión.
   * **SHA512** - Produce un valor hash de 512 bits (64 bytes), proporciona mayor seguridad y resistencia a colisiones, usada en escenarios que procesan grandes volúmenes de datos o exigen un alto nivel de seguridad, tales como algunos sistemas de cifrado gubernamentales o certificaciones de seguridad.
* **SHA3** - SHA3 (Algoritmo de Hash Seguro 3) es otro estándar de hash posterior a SHA-2, adopta una estructura interna y diseño matemático diferente al de SHA-2, ofreciendo mayor capacidad contra ataques nuevos. Es adecuado para desarrollo de futuros sistemas de seguridad y aplicaciones extremadamente exigentes en términos de seguridad, como almacenamiento criptográfico avanzado y preparativos para criptografía en la era de computación cuántica.
* **RIPEMD160** - Desarrollado por el proyecto europeo RACE financiado por la UE, genera un valor hash de 160 bits (20 bytes), tiene ciertas características de diseño diferentes en comparación con SHA-1. Aún se usa en algunas aplicaciones criptográficas específicas, por ejemplo, en la generación de direcciones de Bitcoin, combinándose frecuentemente con SHA256 para generar direcciones de Bitcoin más cortas manteniendo cierta seguridad.

## 5. Notas importantes

1. **Seguridad de datos** - Aunque esta herramienta es conveniente y rápida, debes proteger información sensible durante su uso. Evita realizar hash sobre textos que contengan privacidad personal, secretos empresariales u otra información altamente confidencial para prevenir riesgos potenciales derivados del posible filtrado de valores hash. Si realmente necesitas realizar hash sobre textos sensibles, te recomendamos hacerlo en entornos de red interna seguros, complementándolo con medidas adicionales de cifrado y protección.
2. **Adecuación de las funciones hash** - Las distintas funciones hash presentan características en seguridad y eficiencia de cálculo. En aplicaciones prácticas, debes seleccionar la función hash adecuada según tus necesidades específicas. Por ejemplo, en escenarios con altos requisitos de seguridad (almacenamiento de contraseñas, verificación de integridad de datos), se recomienda priorizar el uso de funciones hash más seguras como SHA256 o SHA512, en lugar de funciones con vulnerabilidades conocidas como MD5.
3. **Verificación de resultados** - Si tienes dudas sobre el resultado generado o necesitas verificar su exactitud, puedes compararlo con otras herramientas confiables o bibliotecas de programación para asegurar consistencia y precisión.
4. **Influencia del formato de codificación en los resultados** - Diferentes métodos de codificación harán que el mismo valor hash se muestre como formas textuales distintas. Por lo tanto, al utilizar los valores hash para verificación de datos o almacenamiento, debes mantener la coherencia del formato de codificación, evitando incompatibilidades debido a diferencias en la codificación. Por ejemplo, el valor hash SHA256 codificado en Base64 en el sistema A no coincide con el mismo valor codificado en hexadecimal en el sistema B, incluso si ambos provienen del mismo texto original.