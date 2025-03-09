def add_time(start, duration):
    
    datos_inicio = start.replace(' ', ':').split(':')
    datos_duracion = duration.split(':')
    
    t_inicial = {
        'hora': int(datos_inicio[0]),
        'minutos': int(datos_inicio[1]),
        'am-pm': datos_inicio[2],
    }
    
    t_duracion = {
        'hora': int(datos_duracion[0]),
        'minutos': int(datos_duracion[1])
    }

    # Sumar minutos
    t_inicial['minutos'] += t_duracion['minutos']
    if t_inicial['minutos'] > 59:
        t_inicial['minutos'] -= 60
        t_inicial['hora'] += 1
        if t_inicial['hora'] > 12:
            t_inicial['hora'] = 1
        if t_inicial['hora'] > 11:
            if t_inicial['am-pm'] == "AM":
                t_inicial['am-pm'] = "PM"
            else:
                t_inicial['am-pm'] = "AM"
    
    
    new_time = f"{t_inicial['hora']}:{t_inicial['minutos']} {t_inicial['am-pm']}"

    return new_time
    
    
# add_time('3:00 PM', '3:10')
# # Returns: 6:10 PM
# texto = '3:00 PM'
# inicio = texto.replace(' ', ':').split(':')
# tiempo_inicial = {
#         'hora': int(inicio[0])
#     }


print(add_time('12:20 PM', '3:58'))
print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM