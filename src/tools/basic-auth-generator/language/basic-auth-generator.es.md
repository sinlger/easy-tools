# Documentación del Generador de Autenticación Básica

## Descripción de las Funciones

El generador de autenticación básica es una herramienta que genera encabezados de autorización codificados en Base64 para la autenticación HTTP básica. Al proporcionar un nombre de usuario y contraseña, la herramienta puede generar rápidamente el encabezado de autorización correspondiente, facilitando su uso a los desarrolladores durante el proceso de desarrollo.

## Instrucciones de Uso

### Introducir Nombre de Usuario

En el campo de entrada "Username", introduzca su nombre de usuario deseado. Puede ser cualquier nombre que desee utilizar para la autenticación.

### Introducir Contraseña

Introduzca la contraseña correspondiente al nombre de usuario en el campo "Password". Durante la introducción, el campo de contraseña se ocultará automáticamente para proteger la seguridad de su contraseña.

### Verificar el Encabezado de Autorización Generado

Tras introducir el nombre de usuario y la contraseña, la herramienta generará automáticamente el encabezado de autorización correspondiente. Este encabezado se mostrará en el siguiente formato:

```
Authorization header:
Authorization: Basic [Cadena codificada en Base64]
```

Aquí, "Basic" indica que se utiliza el método de autenticación básica, y la cadena posterior es el resultado de codificar en Base64 el conjunto de nombre de usuario y contraseña siguiendo el formato "nombre de usuario:contraseña".

### Copiar el Encabezado de Autorización

Si necesita utilizar el encabezado de autorización generado en otro lugar, puede hacer clic en el botón "Copy header" para copiarlo al portapapeles. De esta manera, podrá pegarlo fácilmente en archivos o código donde sea necesario.