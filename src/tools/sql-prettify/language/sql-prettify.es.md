# Documentación del usuario para la herramienta de formateo y embellecimiento SQL

## 1. Descripción general de la herramienta

La herramienta de formateo y embellecimiento SQL es una plataforma en línea utilizada para formatear y mejorar visualmente las sentencias SQL escritas. Soporta múltiples dialectos SQL, ayudando a los desarrolladores a leer y escribir código SQL de manera más clara.

## 2. Descripción de las funciones

### (1) **Funciones básicas**

1. **Embellecimiento SQL**: Convierte consultas SQL desordenadas en un formato estructurado y fácil de entender. Ejemplo:

* Consulta original:
```sql
select field1,field2,field3 from my_table where my_condition;
```

* Después del embellecimiento:
```sql
SELECT
    field1,
    field2,
    field3
FROM
    my_table
WHERE
    my_condition;
```


### (2) **Opciones de configuración**

1. **Selección de dialecto (Dialect)**: Se ofrecen múltiples dialectos SQL como Standard SQL, MySQL, PostgreSQL, SQL Server, etc. Seleccione el dialecto apropiado para su base de datos, asegurando que las sentencias SQL formateadas cumplan con las normas sintácticas específicas de dicha base de datos.
2. **Mayúsculas/minúsculas de palabras clave (Keyword case)**: Las palabras clave SQL pueden mostrarse en mayúsculas (UPPERCASE), minúsculas (lowercase) o con letra capital (Capitalized), logrando así un estilo uniforme del código. Ejemplos:

* Consulta original:
```sql
select * from table;
```

* Tras activar letras mayúsculas:
```sql
SELECT * FROM table;
```

* Tras activar letras minúsculas:
```sql
select * from table;
```

* Tras seleccionar primera letra en mayúscula:
```sql
Select * From table;
```


3. **Estilo de sangría (Indent style)**: Puede elegir entre distintos estilos de sangrado como estándar, 2 espacios (2 spaces), 4 espacios (4 spaces). Esto permite adaptarse a preferencias personales o al estilo interno del equipo. Ejemplos:

* Sangría estándar:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* Sangría de 2 espacios:
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* Sangría de 4 espacios:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **Área de entrada y salida**

1. **Área de entrada**: En el cuadro de texto del lado izquierdo puede pegar o escribir directamente su consulta SQL que desea formatear.
2. **Área de salida**: El cuadro de texto del lado derecho muestra en tiempo real el resultado del formateo y embellecimiento. Además, dispone de un botón de copiado que facilita transferir la consulta ya embellecida al portapapeles para usarla posteriormente donde sea necesario.

## 3. Pasos para su uso

1. Abra la [página web de la herramienta SQL](https://atoolio.com/sql-prettify).
2. Pegue o escriba su consulta SQL en el área de entrada.
3. Seleccione según sus necesidades las opciones adecuadas dentro de Dialecto, Mayúsculas/Minúsculas de palabras clave y Estilo de sangría.
4. Revise el resultado formateado en el área de salida derecha. Si le satisface, haga clic en el botón de copiar para guardarlo en el portapapeles.