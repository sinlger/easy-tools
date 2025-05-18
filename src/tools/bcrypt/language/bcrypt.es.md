# Manual de Uso del Herramienta de Encriptación de Texto

## 1. Descripción General de la Herramienta

Esta es una herramienta poderosa para encriptar textos, basada principalmente en el algoritmo bcrypt. Permite encriptar textos y comparar los valores hash resultantes con el texto original, lo cual puede aplicarse a escenarios relacionados con seguridad, como almacenamiento y verificación de contraseñas.

## 2. Acceso a la Herramienta

Ingrese la URL de la página donde se encuentra esta herramienta en la barra de direcciones del navegador, pulse "Enter" para acceder a la página y espere a que se carguen completamente todos los elementos de la página.

## 3. Guía de Operación

### (1) Encriptar un Texto

1. **Introducir texto** : En el campo de entrada "Your string", ingrese el contenido textual que desee encriptar. Por ejemplo, la contraseña establecida por un usuario durante el registro.
2. **Configurar Salt count** : Pulse los botones "+" o "-" junto a "Salt count" para establecer la cantidad de iteraciones del valor Salt (sal). El Salt es una cadena aleatoriamente generada que se añade al texto original antes de la encriptación, mejorando la seguridad y previniendo ataques de tablas arcoíris. Se recomienda generalmente no utilizar menos de 10 iteraciones.
3. **Ver resultado de encriptación** : Una vez completados los pasos anteriores, la herramienta encriptará automáticamente el texto introducido y mostrará el hash resultante en el cuadro inferior. Este hash contiene información sobre el algoritmo de encriptación utilizado, el valor Salt y el texto encriptado. Por ejemplo: "$2a$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/Dk5Esl7bj1sXA.xK".