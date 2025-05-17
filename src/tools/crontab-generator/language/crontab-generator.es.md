# Documentación del Generador de Expresiones Crontab

## 1. Descripción General de la Herramienta

El generador de expresiones Crontab es una herramienta en línea que ayuda a los usuarios a crear y validar fácilmente expresiones Crontab, así como a obtener descripciones legibles de las programaciones de cron.

## 2. Descripción de Funcionalidades

1. **Generación de Expresiones Crontab**

   * **Entrada Manual** - Introduzca directamente en el campo de entrada una expresión Crontab, por ejemplo "40 * * * *", la herramienta generará automáticamente la descripción correspondiente: "A las 40 minutos pasadas la hora, cada hora, cada día".
   * **Seleccionar Expresiones Preestablecidas** - La herramienta ofrece múltiples opciones predefinidas, tales como "@yearly", "@monthly", etc. Al hacer clic en una opción se genera rápidamente la expresión Crontab asociada.

2. **Validación de Expresiones Crontab**

   * Tras introducir una expresión Crontab personalizada, la herramienta verifica automáticamente si su formato es correcto. Si el formato es válido, muestra la descripción correspondiente; si hay errores, notifica al usuario para realizar correcciones.

3. **Obtener Descripción Legible**

   * Para cualquier expresión Crontab introducida o seleccionada, la herramienta genera descripciones comprensibles en lenguaje natural, facilitando así su interpretación.

4. **Configuraciones Personalizables**

   * **Modo Detallado (Verbose)** - Al activar esta opción se obtiene información más detallada en los registros.
   * **Usar Formato de Hora de 24 Horas** - Permite elegir si mostrar la hora en formato de 24 horas.
   * **Los Días Comienzan en 0** - Se puede seleccionar si los días deben contarse desde 0 o desde 1.

5. **Significado de los Símbolos Crontab**

   * **Asterisco (*)** - Representa cualquier valor, por ejemplo "* * * *" indica que la tarea se ejecuta cada minuto.
   * **Guión (-)** - Sirve para especificar un rango de valores, por ejemplo "1 - 10 * * *" significa que la tarea se ejecutará entre el minuto 1 y el 10.
   * **Coma (,)** - Se utiliza para listar múltiples valores, por ejemplo "1,10 * * *" implica que la tarea se ejecutará en los minutos 1 y 10.
   * **Barra Inclinada (/)** - Indica incrementos o intervalos, por ejemplo "*/10 * * *" quiere decir que la tarea se ejecutará cada 10 minutos.
   * **Símbolos Especiales (@)** - Incluye @yearly, @monthly, @weekly, @daily, @midnight, @hourly, @reboot, etc., que representan ejecuciones anuales, mensuales, semanales, diarias, a medianoche, cada hora y al reiniciar el sistema respectivamente.