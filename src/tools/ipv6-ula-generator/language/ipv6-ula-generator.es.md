# Documentación del Generador IPv6 ULA

**1. Descripción del Herramienta**

El generador IPv6 ULA es una herramienta en línea diseñada para ayudar a los usuarios a generar direcciones IPv6 no enrutables locales según el estándar RFC4193. Es adecuada para crear identificadores de red únicos dentro de una red local que no puedan ser enrutados en Internet.

**2. Funciones Principales**

1. **Generación Aleatoria de ULA basada en múltiples factores**
   * Esta herramienta utiliza el primer método recomendado por IETF, combinando la marca de tiempo actual y la dirección MAC mediante el algoritmo SHA1, y luego extrayendo los 40 bits inferiores para generar direcciones ULA aleatorias. Esto asegura una alta aleatoriedad y unicidad en las direcciones generadas, reduciendo significativamente el riesgo de conflictos de direcciones y proporcionando identificadores de red locales confiables para los dispositivos dentro de la red local.

2. **Entrada y Procesamiento de Direcciones MAC**
   * Los usuarios pueden introducir manualmente direcciones MAC en el campo designado siguiendo el formato estándar (por ejemplo, "20:37:06:12:34:56"). La herramienta utilizará esta dirección MAC como uno de los parámetros clave para la generación de la dirección ULA, incluyéndola junto con otros factores en el cálculo para producir una dirección ULA vinculada a dicha MAC.

3. **Generación de Direcciones ULA y Bloques de Enrutamiento Asociados**

   * **IPv6 ULA**: La herramienta genera una dirección IPv6 ULA completa que comienza con "fd", cumpliendo con el formato estándar RFC4193 para direcciones ULA locales. Por ejemplo, "fd1d:dba9:6f7b::/48", donde "/48" indica que la longitud del prefijo de esta dirección ULA es de 48 bits. Esto proporciona identificadores de red únicos para dispositivos en la red local, utilizables para configuraciones de red y comunicación dentro de la red privada.
   * **Primer bloque enrutable**: Se genera el primer bloque de direcciones asignable, como "fd1d:dba9:6f7b:0::/64", lo cual representa el primer bloque de direcciones dentro del rango ULA que puede ser asignado a hosts o subredes. Esto ayuda al usuario a comprender el rango inicial de direcciones disponibles, facilitando la planificación de redes y la asignación de direcciones.
   * **Último bloque enrutable**: Se produce también el último bloque de direcciones disponible, por ejemplo "fd1d:dba9:6f7b:ffff::/64", indicando el último bloque de direcciones dentro del rango ULA que se puede asignar a hosts o subredes. Con ello, el usuario tiene claridad sobre el rango final de direcciones disponibles, permitiendo un despliegue eficiente de la red y configuración de dispositivos.

**3. Escenarios de Aplicación**

1. En redes internas empresariales, asignar direcciones IPv6 locales únicas a los dispositivos. Esto evita conflictos con direcciones IPv6 públicas mientras garantiza la comunicación normal entre dispositivos dentro de la red local.
2. Para entornos de pruebas de redes, generar direcciones ULA locales no enrutables permite simular escenarios de red, realizar pruebas de configuración de equipos de red y aplicaciones sin necesidad de consumir recursos oficiales de direcciones IPv6 de Internet.
3. En redes domésticas, asignar direcciones ULA a routers y dispositivos inteligentes aumenta la estabilidad y seguridad de la red, previniendo accesos no autorizados desde redes externas.

**4. Instrucciones de Uso**

1. Acceda al sitio web del generador IPv6 ULA en [https://atoolio.com/ipv6-ula-generator](https://atoolio.com/ipv6-ula-generator).
2. Si ya conoce la dirección MAC del dispositivo, ingrésela en el campo "MAC address" siguiendo el formato estándar. Si no conoce la dirección MAC, puede dejar este campo vacío; la herramienta podría usar una dirección MAC predeterminada o generarla aleatoriamente (esto dependerá del funcionamiento interno real de la herramienta).
3. Haga clic en el botón de generación (como "Generate", aunque el nombre podría variar dependiendo de la interfaz de la herramienta). El programa calculará y generará la dirección IPv6 ULA correspondiente, el primer bloque enrutable y el último bloque enrutable, basándose en la dirección MAC ingresada (o predeterminada) y la marca de tiempo actual.
4. Revise la información de las direcciones generadas y aplíquelas según sea necesario para la configuración de dispositivos en la red local, planificación de redes o pruebas de conectividad.

**5. Notas Importantes**

1. Las direcciones ULA generadas son exclusivamente para uso en redes locales y no pueden enrutar ni comunicarse en Internet. Si se requiere conectividad con Internet, se deben configurar direcciones IPv6 unicast globales enrutables para los dispositivos.
2. Asegúrese de que la dirección MAC introducida sea correcta, ya que cualquier error podría afectar la unicidad y relación de la dirección ULA generada, causando posibles problemas en la configuración de red.
3. Las direcciones ULA deben mantenerse únicas dentro de la red local. Evite repetir el uso de la misma dirección ULA para prevenir conflictos de red que puedan afectar la comunicación normal de los dispositivos.