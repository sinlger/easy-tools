# Documentación del usuario para el decodificador de enlaces seguros de Outlook

## 1. Introducción a la herramienta
El **decodificador de enlaces seguros de Outlook** es una herramienta diseñada para descifrar los enlaces generados por el servicio de correo electrónico Microsoft Outlook denominados SafeLink. Esta herramienta permite transformar los enlaces cifrados por Outlook SafeLink en sus URLs originales, facilitando así a los usuarios identificar el destino real de estos enlaces.

## 2. Descripción de las funciones
La principal función de esta herramienta es descifrar los enlaces de Outlook SafeLink, es decir, convertir los enlaces cifrados y redirigidos generados por Microsoft Outlook en direcciones web originales.

## 3. Instrucciones de uso

### Entrada
Pegue en el campo de entrada el enlace SafeLink de Outlook que desea descifrar. Este enlace ha sido cifrado por Microsoft Outlook por razones de seguridad y tiene un formato específico.

### Salida
Después de hacer clic en el botón "Decode", la herramienta procesará el enlace introducido y mostrará en el campo de salida la URL original descifrada. Si el enlace no está correctamente formateado o no puede ser reconocido, aparecerá un mensaje de error: "Error: Invalid SafeLinks URL provided" (Error: Se proporcionó una URL de SafeLinks inválida).

## 4. Ejemplos de uso

### Ejemplo 1
Entrada (enlace SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Salida después de la decodificación:
`https://example.com`

### Ejemplo 2
Entrada (enlace SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Salida después de la decodificación:
`https://microsoft.com`

### Ejemplo 3
Entrada de un enlace inválido o con formato incorrecto:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Mensaje de error:
`Error: Invalid SafeLinks URL provided`

## 5. Notas importantes
- Asegúrese de que el enlace introducido sea un enlace completo de Outlook SafeLink.