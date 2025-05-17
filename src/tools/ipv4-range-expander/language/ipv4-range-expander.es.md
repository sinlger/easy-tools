# Documentación del Expansor de Rango IPv4

## 1. Introducción a la Herramienta

El Expansor de Rango IPv4 calcula redes IPv4 efectivas basándose en direcciones IPv4 iniciales y finales proporcionadas. Esto incluye bloques de red válidos (representados en notación CIDR), rangos de direcciones y la cantidad total de direcciones dentro del rango.

## 2. Descripción de las Funciones

### (A) Función Básica de Entrada

1. **Entrada de la Dirección Inicial** - En el campo "Start address", ingrese una dirección IPv4 que servirá como punto inicial, por ejemplo "192.168.1.1".
2. **Entrada de la Dirección Final** - En el campo "End address", ingrese una dirección IPv4 que servirá como punto final, por ejemplo "192.168.6.255".

### (B) Procesamiento Automático y Visualización de Resultados

1. **Ajuste del Rango de Direcciones** - La herramienta ajustará automáticamente las direcciones inicial y final para obtener un rango más adecuado. Por ejemplo, "192.168.1.1" se ajustará a "192.168.0.0" y "192.168.6.255" se convertirá en "192.168.7.255".
2. **Cálculo de la Cantidad de Direcciones** - Se calculará la cantidad total de direcciones IPv4 disponibles en el nuevo rango, por ejemplo, aumentando de "1.535" a "2.048", mejorando así la eficiencia en el uso de direcciones.
3. **Generación de Notación CIDR** - Se mostrará la notación CIDR correspondiente al nuevo rango de direcciones, como "192.168.0.0/21", lo cual facilita la gestión y configuración de la red.

## 3. Notas Importantes

Asegúrese de que las direcciones inicial y final introducidas sigan el formato correcto de direcciones IPv4, con el fin de garantizar el correcto funcionamiento de la herramienta y la precisión de los resultados.