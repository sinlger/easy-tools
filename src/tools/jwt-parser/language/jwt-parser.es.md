# A Toolio - Documentación del Analizador de JWT

## 1. Descripción de la herramienta

A Toolio - El analizador de JWT es una herramienta en línea práctica que puede analizar y decodificar tokens web JSON (JWT) y mostrar claramente su contenido. Proporciona a los desarrolladores una forma rápida de ver los detalles de un JWT, lo que facilita la depuración, validación y aprendizaje.

## 2. Descripción de las funciones

### (A) Función de entrada

* **Campo de entrada JWT** : El usuario puede pegar el JWT que desea analizar en este campo de entrada. La capacidad del campo es amplia y puede contener JWTs de diversas longitudes, ofreciendo así una entrada flexible.

### (B) Función de análisis

* **Análisis del encabezado (Header)** : Puede analizar con precisión la información del encabezado del JWT, incluyendo los siguientes campos:
  * **alg (Algorithm)** : Muestra el algoritmo de cifrado utilizado por el JWT, por ejemplo, HS256 indica el uso del algoritmo HMAC con SHA-256.
  * **typ (Type)** : Muestra el tipo de JWT, generalmente "JWT".

* **Análisis de la carga útil (Payload)** : Puede analizar en detalle la parte de carga útil del JWT y mostrar varias declaraciones (claims) incluidas, por ejemplo:
  * **sub (Subject)** : Identifica al usuario o entidad para quien se emitió el JWT.
  * **name (Full name)** : Muestra el nombre completo del usuario.
  * **iat (Issued At)** : Indica el momento en que se emitió el JWT, normalmente mostrado como una marca de tiempo, y puede convertirse en un formato de fecha y hora específico.

### (C) Función de visualización

* **Presentación estructurada** : Los contenidos del JWT analizados se presentan claramente en forma de tabla estructurada, facilitando al usuario la comprensión rápida de cada campo y su valor, haciendo que la información sea más intuitiva y fácil de leer.

## 3. Pasos de uso

1. **Acceder a la URL** : Abra un navegador e ingrese a [https://atoolio.com/jwt-parser](https://atoolio.com/jwt-parser) para acceder a la página del analizador de JWT.
2. **Ingresar el JWT** : Pegue el JWT que desea analizar en el campo de entrada.
3. **Hacer clic en analizar** : Haga clic en el botón de análisis (generalmente junto a "JWT to decode", la descripción exacta dependerá de la interfaz), el sistema automáticamente analizará el JWT introducido.
4. **Ver resultados** : Consulte en el área inferior los resultados analizados, tanto del encabezado como de la carga útil, para comprender detalladamente el contenido del JWT.

## 4. Notas importantes

* Asegúrese de que el JWT introducido tenga un formato correcto; de lo contrario, podría provocar fallos en el análisis o resultados inexactos.
* Esta herramienta solo sirve para analizar y ver el contenido del JWT, no garantiza un análisis completamente correcto para todos los tipos de JWT, especialmente aquellos que utilizan algoritmos de cifrado especiales o formatos no estándar.
* Durante el uso, si encuentra problemas o necesita ayuda, puede contactar a través de los canales de soporte proporcionados por el sitio web (por ejemplo, "Buy me a coffee" podría implicar que puede contactar al desarrollador a través de esa opción).

La presente documentación tiene como objetivo ayudarle a entender y utilizar mejor esta herramienta, con el fin de manejar eficientemente las tareas relacionadas con JWT.