# Documentación del analizador de agentes de usuario en línea

## 1. Introducción a la herramienta

El analizador de agentes de usuario en línea puede detectar y analizar con precisión información sobre el navegador, motor de renderizado, sistema operativo, arquitectura de CPU y tipo/modelo del dispositivo desde la cadena del agente de usuario, lo que ayuda a los desarrolladores a obtener rápidamente detalles relacionados con el cliente.

## 2. Descripción de las funciones

### (1) Detección del navegador

Puede identificar con precisión el tipo de navegador utilizado por el usuario y su versión específica. Por ejemplo, cuando se introduce una cadena determinada, si aparece "Edge 135.0.0.0", esto indica que el navegador del cliente es Edge y la versión es 135.0.0.0.

### (2) Detección del motor de renderizado

Muestra claramente el motor de renderizado utilizado por el navegador y su correspondiente versión. Por ejemplo, "Blink 135.0.0.0" significa que el motor de renderizado es Blink y la versión es 135.0.0.0.

### (3) Detección del sistema operativo

Muestra detalladamente el nombre del sistema operativo y su versión. Por ejemplo, "Windows 10", lo cual implica que el sistema operativo es Windows y la versión es la 10.

### (4) Detección de información del dispositivo

Permite obtener información como el tipo de dispositivo, modelo y fabricante (si está disponible). Por ejemplo, algunos dispositivos pueden mostrar completamente el modelo, aunque también existen casos donde no hay disponible un modelo, tipo o fabricante del dispositivo, en cuyo caso se mostrará un mensaje indicativo: "No device model/type/vendor available".

### (5) Detección de información de la CPU

Puede identificar características relacionadas con la CPU. Por ejemplo, si se muestra "amd64", esto indica que la arquitectura de la CPU es de tipo amd64.

## 3. Ejemplos de uso

### Ejemplo uno: Caso habitual de navegador de escritorio

Supongamos que la cadena del agente de usuario es:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Tras introducir esta cadena en el analizador:

  * **Navegador**: Se reconoce que es Edge 135.0.0.0.
  * **Motor**: Se identifica como Blink 135.0.0.0.
  * **Sistema operativo**: Es Windows 10.
  * **Dispositivo**: No hay disponible un modelo, tipo ni fabricante específico del dispositivo, por lo tanto, se muestra el mensaje adecuado.
  * **CPU**: Su arquitectura es amd64.

### Ejemplo dos: Navegador en dispositivo móvil

Tomemos como ejemplo la siguiente cadena de agente de usuario:
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Después de introducirla en el analizador:

  * **Navegador**: Puede identificarse el navegador Safari junto con la versión correspondiente bajo el sistema iOS (la versión exacta dependerá del análisis real).
  * **Motor**: Se presenta el motor Webkit correspondiente con detalles de su versión.
  * **Sistema operativo**: Se identifica claramente como iOS, junto con su número de versión correspondiente (por ejemplo, 16_6_1).
  * **Dispositivo**: Se obtiene información del dispositivo, como que es un iPhone (con modelos específicos según los resultados del análisis).
  * **CPU**: Muestra la arquitectura de CPU correspondiente adaptada a dispositivos móviles (si hay parte claramente identificable).