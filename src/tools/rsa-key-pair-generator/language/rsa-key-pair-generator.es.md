# Documentación del usuario para el generador de pares de claves RSA

## 1. Descripción general de la herramienta

Esta herramienta en línea permite generar fácilmente certificados PEM aleatorios de clave privada y pública RSA. Es ideal para desarrolladores que necesitan crear rápidamente un par de claves RSA durante el proceso de desarrollo.

## 2. Descripción de las funciones

### (1) **Configuración de la longitud de la clave**

* **Función**: El usuario puede establecer la longitud de la clave dentro de un rango definido (en bits).
* **Acción**: Introduzca en el campo de entrada junto a "Bits" la longitud deseada para la clave, como por ejemplo los habituales 2048 bits. La herramienta soporta un rango determinado de bits, asegurando así que la clave generada cumpla con los requisitos de seguridad y aplicación.
* **Propósito**: Cuanto más larga sea la longitud de la clave, mayor será normalmente su seguridad, aunque puede disminuir la velocidad de cifrado y descifrado. Por ello es importante realizar una elección equilibrada según el caso práctico de uso.

### (2) **Actualizar el par de claves**

* **Función**: Sirve para generar rápidamente un nuevo par de claves RSA aleatorio.
* **Acción**: Haga clic en el botón "Refresh key-pair", el sistema regenerará un nuevo par de claves público-privadas basándose en la longitud actual configurada de la clave.
* **Propósito**: Cuando se requiera generar múltiples pares de claves distintos para pruebas o uso directo, simplemente pulse el botón Refresh sin tener que realizar ajustes manuales adicionales, lo cual aumenta la eficiencia laboral.

### (3) **Clave pública - Visualización y gestión**

* **Función**: Muestra la clave pública RSA generada y ofrece opciones cómodas al usuario para utilizarla.
* **Presentación**: En la sección "Public key", la clave pública aparece mostrada en el formato estándar PEM, incluyendo "-----BEGIN PUBLIC KEY-----" y "-----END PUBLIC KEY-----", permitiendo usarla directamente en aplicaciones.
* **Función de copiado**: El botón de copia adyacente permite al usuario copiar rápidamente la clave pública en el portapapeles para insertarla fácilmente donde sea necesario, como archivos de configuración o fragmentos de código.

### (4) **Clave privada - Visualización y gestión**

* **Función**: Muestra la clave privada RSA generada y proporciona una forma sencilla de utilizarla.
* **Presentación**: En la sección "Private key", también se utiliza el formato PEM habitual, identificado por "-----BEGIN RSA PRIVATE KEY-----" y "-----END RSA PRIVATE KEY-----", lo que permite al usuario emplear esta clave para operaciones como cifrado, descifrado o firmas digitales.
* **Función de copiado**: El botón de copia colocado al lado facilita al usuario la copia rápida de la clave privada, para poder usarla en entornos seguros, tales como almacenamiento en servidores o configuración dentro de aplicaciones.

## 3. Ejemplos de escenarios de aplicación

1. Los desarrolladores que necesiten claves de prueba cuando desarrollan aplicaciones basadas en el algoritmo de cifrado RSA pueden usar esta herramienta para configurar una longitud adecuada de clave y generar un par de claves mediante el botón Refresh. Posteriormente, pueden emplear la clave pública para el cifrado y la privada para realizar pruebas de descifrado.
2. Al configurar protocolos de comunicación segura (como SSL/TLS), si se precisa un certificado autofirmado o un par de claves para un entorno de prueba, se puede generar aquí y colocar cada clave (pública y privada) en su posición correspondiente en el servidor y cliente.