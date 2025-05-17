# Documentación del Generador HMAC de A Toolio

## 1. Descripción de la herramienta

El generador HMAC en línea proporcionado por A Toolio permite calcular códigos de autenticación de mensajes basados en hash (HMAC) mediante una clave y una función hash, ideal para desarrolladores que necesitan generar rápidamente HMACs en diversos escenarios de desarrollo.

## 2. Descripción de las Funciones

### Sección de Entrada

1. **Texto plano** - Introduzca el texto sin cifrar que desee procesar.
2. **Clave secreta** - Ingrese la clave secreta utilizada para generar el HMAC.
3. **Función Hash** - Seleccione la función hash deseada. Por defecto se encuentra SHA256, aunque también puede elegir otras funciones hash según sus necesidades.
4. **Codificación de salida** - Elija el formato de codificación de salida deseado. La opción predeterminada es hexadecimal (base 16), pero también se pueden seleccionar otros formatos.

### Sección de Salida

1. **HMAC of your text** - Muestra el valor HMAC generado, con un botón de copia que facilita su transferencia.

## 3. Pasos de Uso

**Paso 1: Ingrese el texto plano y la clave**

En el campo "Texto plano", escriba el contenido cuyo hash desea calcular. Posteriormente, introduzca la "Clave secreta" en el campo correspondiente. Esta información básica debe ser ingresada correctamente.

**Paso 2: Seleccione la función hash**

Seleccione la función hash requerida desde el menú desplegable "Función Hash", como SHA256, SHA1, etc., dependiendo de sus necesidades específicas. Diferentes funciones hash producirán distintos resultados HMAC.

**Paso 3: Seleccione el formato de codificación de salida**

Elija el formato de codificación deseado a través del menú "Codificación de salida", tal como formato hexadecimal (base 16) o Base64. Esto definirá cómo se presentará el valor HMAC generado.

**Paso 4: Genere y visualice el HMAC**

Tras completar los campos anteriores y realizar las selecciones pertinentes, el sistema calculará automáticamente el valor HMAC, mostrándolo en la sección "HMAC of your text". Podrá ver directamente el resultado.

**Paso 5: Copie el HMAC**

Si necesita usar este valor HMAC, haga clic en el botón de copiado junto al resultado para guardarlo en el portapapeles y poder pegarlo posteriormente donde sea necesario.