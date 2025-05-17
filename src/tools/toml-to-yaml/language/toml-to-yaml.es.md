# Documentación del usuario del convertidor de TOML a YAML

## Descripción general

TOML a YAML es una herramienta en línea que permite a los usuarios convertir fácilmente archivos de configuración en formato TOML (Tom's Obvious, Minimal Language) a formato YAML (YAML Ain't Markup Language). Esto es especialmente útil para desarrolladores que necesitan migrar configuraciones entre diferentes sistemas o integrar múltiples tecnologías.

## Diseño de la interfaz

La interfaz de la herramienta es sencilla e intuitiva, con las siguientes componentes principales:

1. Campo de texto izquierdo: Es el área donde los usuarios pueden ingresar o pegar texto en formato TOML, identificado como "Su TOML".
2. Campo de texto derecho: Se utiliza para mostrar el texto convertido en formato YAML, identificado como "YAML desde su TOML".
3. Botón de conversión central: Después de ingresar el texto TOML, los usuarios pueden hacer clic en este botón para realizar la conversión.

## Descripción de funciones

### Ingreso de texto TOML

- Los usuarios pueden ingresar directamente texto de configuración en formato TOML en el campo de texto izquierdo.
- También pueden copiar texto TOML desde otros archivos o editores y pegarlo en este campo de texto.

### Operación de conversión

- Una vez que se ingresa o pega el texto TOML, haga clic en el botón de conversión central. El sistema analizará inmediatamente el texto TOML ingresado y lo convertirá al formato YAML.
- Una vez completada la conversión, el texto YAML resultante se mostrará en el campo de texto derecho.

### Visualización del resultado YAML

- El campo de texto derecho muestra completamente el texto YAML convertido.
- Aquí, los usuarios pueden verificar si el resultado de la conversión es preciso y si la estructura del texto YAML cumple con sus expectativas.

### Copiado del texto YAML

- Los usuarios pueden seleccionar y copiar todo el texto YAML en el campo de texto derecho, lo cual es conveniente para usarlo en otros lugares, como pegarlo en archivos de configuración o enviarlo a otras personas.

## Ejemplos

### Ejemplo 1: Conversión básica

**Entrada en formato TOML:**

```toml
# Este es un ejemplo simple de TOML
title = "Ejemplo de TOML"

[author]
name = "Zhang San"
age = 28
e-mail = "zhangsan@example.com"
```

**Salida en formato YAML:**

```yaml
# Este es el ejemplo convertido a YAML
title: Ejemplo de TOML

author:
  name: Zhang San
  age: 28
  e-mail: zhangsan@example.com
```

### Ejemplo 2: Conversión de estructuras complejas

**Entrada en formato TOML:**

```toml
# Ejemplo de TOML con estructura más compleja
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**Salida en formato YAML:**

```yaml
# Ejemplo de YAML con estructura más compleja
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Notas importantes

- Si el formato TOML introducido no es correcto, la conversión podría fallar y el sistema podría mostrar mensajes de error.
- La herramienta soporta la mayoría de las estructuras de sintaxis TOML comunes, pero para algunos elementos de sintaxis especiales o poco utilizados, quizás no sea posible una conversión perfecta.
- El texto YAML producido puede presentar pequeñas diferencias de formato dependiendo de la versión y especificación de YAML utilizadas.