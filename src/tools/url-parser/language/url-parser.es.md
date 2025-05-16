# Analizador de URL

## 1. Descripción de la herramienta
El analizador de URL es una herramienta en línea para analizar cadenas de URL, capaz de descomponer URLs complejas en múltiples componentes, incluyendo protocolo, nombre de usuario, contraseña, nombre del host, puerto, ruta, parámetros, etc., facilitando a los desarrolladores comprender rápidamente la estructura y la información detallada de la URL, lo cual es conveniente para construir, depurar y analizar solicitudes de red.

## 2. Detalles de las funciones

  1. **Campo de entrada**
     * Proporciona un campo de entrada donde se puede ingresar la cadena de URL que desea analizar.

  2. **Mostrar resultados del análisis**
     * **Protocolo (Protocol)** : Muestra la parte del protocolo de la URL, por ejemplo "https:", indicando el protocolo de transmisión de red utilizado por la URL.
     * **Nombre de usuario (Username)** : Si la URL contiene información del nombre de usuario, esta se mostrará aquí, utilizada para identificar la identidad del usuario proporcionada en la URL.
     * **Contraseña (Password)** : Muestra la parte de la contraseña en la URL, junto con el nombre de usuario, utilizada para la autenticación de identidad del usuario.
     * **Nombre del host (Hostname)** : Muestra el nombre de dominio correspondiente a la URL, por ejemplo "atoolio.com", que representa el nombre del servidor de destino.
     * **Puerto (Port)** : Muestra el número de puerto especificado en la URL, utilizado para determinar el puerto específico en el servidor donde se ofrece el servicio. Por defecto, diferentes protocolos tienen distintos puertos predeterminados, por ejemplo, el puerto 80 para HTTP y el puerto 443 para HTTPS.
     * **Ruta (Path)** : Muestra la parte de la ruta en la URL, por ejemplo "/url-parser", apuntando a una ubicación específica de recursos o servicios en el servidor.
     * **Parámetros (Params)** : Lista la parte de los parámetros de consulta en la URL, comenzando con "?", seguido de varios pares "clave-valor" como parámetros, por ejemplo "?key1=value&key2=value2", utilizados para enviar información adicional e instrucciones al servidor.
     * **Muestra detallada de parámetros** : Cada par clave-valor de los parámetros de consulta se muestra individualmente, mostrando claramente el nombre de cada parámetro y su valor correspondiente.

## 3. Pasos de uso

  1. Abra el navegador y visite la página web [Analizador de URL](https://atoolio.com/url-parser).
  2. En el campo de entrada, ingrese la cadena de URL que desea analizar, por ejemplo "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Haga clic en el botón de análisis (normalmente, presionar Enter también puede activar el análisis), la herramienta analizará automáticamente la URL introducida y mostrará la información detallada de cada componente debajo.
  4. Revise los resultados del análisis y, según sea necesario, copie el contenido correspondiente de los componentes para utilizarlos en posteriores tareas de desarrollo, depuración u otras operaciones.

## 4. Ejemplos

  1. **Ejemplo 1**
     * URL ingresada: "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Resultado del análisis:
       * Protocolo: http:
       * Nombre de usuario: user
       * Contraseña: pass
       * Nombre del host: example.com
       * Puerto: 8080
       * Ruta: /page
       * Parámetros: ?param1=hello&param2=world
       * Muestra detallada de parámetros:
         * param1: hello
         * param2: world

  2. **Ejemplo 2**
     * URL ingresada: "https://www.google.com/s?wd=Analizador de URL"
     * Resultado del análisis:
       * Protocolo: https:
       * Nombre de usuario: (ninguno)
       * Contraseña: (ninguna)
       * Nombre del host: www.google.com
       * Puerto: (puerto predeterminado 443, no mostrado)
       * Ruta: /s
       * Parámetros: ?wd=Analizador de URL
       * Muestra detallada de parámetros:
         * wd: Analizador de URL