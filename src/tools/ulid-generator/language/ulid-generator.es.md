# Documentación del usuario para el generador de ULID

## 1. Introducción a la herramienta
El generador de ULID se utiliza para crear identificadores únicos universales aleatorios que son ordenables lexicográficamente (ULID). Los identificadores generados son únicos y ordenables, y se utilizan ampliamente en sistemas distribuidos, como identificadores de registros en bases de datos, entre otros escenarios.

## 2. Descripción de funciones

### (1) Configuración de cantidad
Mediante la opción "Quantity", puede establecer la cantidad de ULID que desea generar. El valor predeterminado es 1. Puede ajustar esta cantidad utilizando los botones de aumento/disminución a la derecha.

### (2) Selección de formato
Se ofrecen dos formatos de salida:
1. **Raw**: Muestra los ULID en formato de texto plano, facilitando su visualización y uso directo.
2. **JSON**: Exporta los ULID generados en formato JSON, facilitando su llamada y análisis por programas.

### (3) Generación y operaciones
Haga clic en el botón "Refresh" para generar nuevos ULID; haga clic en el botón "Copy" para copiar los ULID generados al portapapeles y pegarlos fácilmente en otras ubicaciones.

## 3. Ejemplos

### Ejemplo 1: Generar un solo ULID (formato Raw)
Establezca "Quantity" en 1 y seleccione el formato "Raw", luego haga clic en "Refresh", se generará un ULID similar al siguiente:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Ejemplo 2: Generar múltiples ULID (formato JSON)
Establezca "Quantity" en 3 y seleccione el formato "JSON", luego haga clic en "Refresh", se generarán ULID en formato JSON como se muestra a continuación:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}