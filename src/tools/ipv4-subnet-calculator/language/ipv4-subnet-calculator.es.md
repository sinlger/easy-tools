# Documentación del Calculador de Subred IPv4

El calculador de subred IPv4 es una herramienta en línea conveniente que permite analizar bloques CIDR IPv4 y obtener información detallada sobre las subredes. A continuación se presenta una descripción de sus funciones y cómo utilizarla:

## 1. Función de Entrada

En el campo de entrada, los usuarios pueden introducir una dirección IPv4, con o sin máscara de subred. Por ejemplo, al ingresar "192.168.0.1/24", la herramienta realizará los cálculos correspondientes basados en esta entrada.

## 2. Resultados del Cálculo

1. **Máscara de red (Netmask)**
   * Muestra la combinación de la dirección IPv4 y su máscara de subred, como "192.168.0.0/24", permitiendo al usuario comprender claramente el rango actual de la red.

2. **Dirección de red (Network address)**
   * Proporciona la dirección de la red dentro del subred, que es una dirección especial utilizada para identificar toda la red. Por ejemplo, "192.168.0.0", representa el punto inicial de dicha subred.

3. **Máscara de red (Network mask)**
   * Presenta la máscara de subred en formato decimal, por ejemplo "255.255.255.0", útil para determinar la separación entre la parte de red y la parte de host en la dirección IP.

4. **Máscara de red en formato binario (Network mask in binary)**
   * Muestra la máscara de subred en forma binaria, como "11111111.11111111.11111111.00000000", lo cual ayuda a entender más profundamente el funcionamiento de la máscara de subred.

5. **Notación CIDR (CIDR notation)**
   * Indica la representación CIDR de la subred, como "/24", una forma concisa de expresar la longitud de la máscara de subred, facilitando así la rápida comprensión de la segmentación de la red.

6. **Máscara comodín (Wildcard mask)**
   * Ofrece el valor de la máscara comodín, por ejemplo "0.0.0.255", complementaria a la máscara de subred, comúnmente usada en configuraciones de ciertos dispositivos y softwares de red.

7. **Tamaño de la red (Network size)**
   * Informa sobre la cantidad total de direcciones IP disponibles en la subred, como por ejemplo "256", ayudando al usuario a conocer la magnitud de dicha subred.

8. **Primera dirección utilizable (First address)**
   * Muestra la primera dirección IP disponible para asignarse a un host dentro de la subred, por ejemplo "192.168.0.1", marcando el inicio del rango de direcciones utilizables.

9. **Última dirección utilizable (Last address)**
   * Presenta la última dirección IP disponible para asignarse a un host dentro de la subred, tal como "192.168.0.254", indicando el final del rango de direcciones utilizables.

10. **Dirección de difusión (Broadcast address)**
    * Proporciona la dirección de difusión de esta subred, como "192.168.0.255", empleada para enviar mensajes a todos los hosts dentro de la subred.

11. **Clase de la dirección IP (IP class)**
    * Indica la clase a la que pertenece la dirección IP, por ejemplo "C", ayudando al usuario a reconocer cómo se clasifica dicha dirección.

## 3. Funcionalidad de Navegación

Se ofrecen botones denominados "Bloque anterior (Previous block)" y "Siguiente bloque (Next block)", que facilitan al usuario el rápido acceso a bloques de subred adyacentes para revisarlos.