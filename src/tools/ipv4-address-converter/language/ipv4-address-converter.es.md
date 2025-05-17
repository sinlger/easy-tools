# Documentación del Conversor de Direcciones IPv4

## 1. Descripción de la Herramienta

El Conversor de Direcciones IPv4 es una herramienta en línea diseñada para convertir direcciones IPv4 en diferentes sistemas numéricos (decimal, hexadecimal, binario) y también al formato IPv6. Esta herramienta ayuda a desarrolladores y técnicos de redes a obtener rápidamente distintas representaciones de las direcciones IPv4, facilitando tareas como la configuración de redes, el desarrollo de software o el análisis de seguridad informática.

## 2. Descripción de Funciones

### (A) Introducción de Direcciones IPv4
- En el campo de entrada del programa, el usuario puede introducir directamente una dirección IPv4 válida (por ejemplo: 192.168.1.1). Una vez completada la entrada, haga clic en el botón "Convertir" o presione Enter, y la herramienta realizará automáticamente varias conversiones.

### (B) Conversión a Decimal
- **Función**: Convierte la dirección IPv4 a un número decimal.
- **Método de Uso**: Tras introducir la dirección IPv4, la herramienta calculará automáticamente su valor decimal correspondiente. El valor decimal se obtiene convirtiendo cada uno de los cuatro bytes de la dirección IPv4 a números decimales y combinándolos según un cálculo específico.

### (C) Conversión a Hexadecimal
- **Función**: Convierte la dirección IPv4 a una cadena hexadecimal.
- **Método de Uso**: Después de ingresar la dirección IPv4, la herramienta transformará automáticamente cada byte en dos dígitos hexadecimales y los combinará en una cadena hexadecimal completa. Por ejemplo, la dirección IPv4 192.168.1.1 se convertirá en C0A80101.

### (D) Conversión a Binario
- **Función**: Transforma la dirección IPv4 en una representación binaria.
- **Método de Uso**: Al introducir la dirección IPv4, la herramienta convertirá cada byte en un número binario de 8 bits, conectando posteriormente los cuatro bytes en una cadena binaria de 32 bits. Por ejemplo, la dirección IPv4 192.168.1.1 se convertirá en 11000000101010000000000100000001.

### (E) Conversión al Formato IPv6
- **Función**: Cambia la dirección IPv4 a una representación en formato IPv6.
- **Método de Uso**: La herramienta convertirá la dirección IPv4 a dos formatos IPv6:
  1. **Dirección IPv6 Completa**: Los primeros 8 bytes se rellenan con ceros, mientras que los últimos 8 bytes contienen la forma hexadecimal de la dirección IPv4, añadiendo "ffff" antes de la parte IPv4 como identificador. Por ejemplo, la dirección IPv4 192.168.1.1 se convertirá a la forma IPv6 completa 0000:0000:0000:0000:0000:ffff:c0a8:0101.