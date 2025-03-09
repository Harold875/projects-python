# Instrucciones para realizar el proyecto (ES)
Escriba una función llamada add_time que acepte dos parámetros obligatorios y un parámetro opcional:

una hora de inicio en el formato de reloj de 12 horas (que termina en AM o PM)

• Una duración que indica el número de horas y minutos

• (opcional) Un día de inicio de la semana, sin distinción de mayúsculas

La función debe agregar el tiempo de duración al tiempo de inicio y devolver el resultado.

Si el resultado será al día siguiente, debería aparecer (día siguiente) después de la hora.

Si el resultado será más de un día después, debe mostrarse (n días después) después de la hora, donde "n" es el número de días después.

Si se le asigna a la función el parámetro opcional de día de inicio de la semana, la salida debe mostrar el día de la semana del resultado. El día de la semana en la salida debe aparecer después de la hora y antes del número de días posteriores.

A continuación se muestran algunos ejemplos de diferentes casos que la función debe manejar. Preste especial atención al espaciado y la puntuación de los resultados.

```py
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
```


**IMPORTANTE**
No importe ninguna biblioteca de Python. Suponga que las horas de inicio son horas válidas. Los minutos en el tiempo de duración serán un número entero menor que 60, pero la hora puede ser cualquier número entero.

Nota: abra la consola del navegador con F12 para ver un resultado más detallado de las pruebas.


# Instructions for carrying out the project (EN):
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
Una duración que indica el número de horas y minutos
(opcional) Un día de inicio de la semana, sin distinción de mayúsculas
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

```py
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
```

**IMPORTANT**
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

Note: open the browser console with F12 to see a more verbose output of the tests.