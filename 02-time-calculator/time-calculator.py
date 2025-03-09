def add_time(start, duration, start_day= None):
    
    datos_inicio = start.replace(' ', ':').split(':')
    datos_duracion = duration.split(':')
    
    t_inicial = {
        'hora': int(datos_inicio[0]),
        'minutos': int(datos_inicio[1]),
        'am-pm': datos_inicio[2],
        'dias': 0
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
        if t_inicial['minutos'] < 10:
            t_inicial['minutos'] = f"0{t_inicial['minutos']}"
        if t_inicial['hora'] > 11 and t_inicial['am-pm'] == "PM":
            t_inicial["dias"] += 1
            t_inicial['am-pm'] = "AM"
            
    t_inicial['hora'] += t_duracion['hora']
    
    while t_inicial['hora'] > 12:
        if t_inicial['hora'] > 11:
            if t_inicial['am-pm'] == "PM":
                t_inicial['am-pm'] = "AM"
                t_inicial["dias"] += 1
            else:
                t_inicial['am-pm'] = "PM"
        if t_inicial['hora'] > 12:
            t_inicial['hora'] -= 12
    
    new_time = f"{t_inicial['hora']}:{t_inicial['minutos']} {t_inicial['am-pm']}"
    
    # dias de la semana:
    if start_day != None:
        start_day = start_day.capitalize()
        days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        if t_inicial['dias'] > 0:
            n = days_week.index(start_day) + t_inicial['dias']
            while n > 6:
                n -= 7
            day_week_result = days_week[n]
        else:
            day_week_result = start_day
        
        new_time += f", {day_week_result}"
    
    # dias  
    if t_inicial['dias'] == 1:
        new_time += " (next day)"
    elif t_inicial['dias'] > 1:
        new_time += f" ({t_inicial['dias']} days later)"
          

    return new_time
    
    
# add_time('3:00 PM', '3:10')
# # Returns: 6:10 PM
# texto = '3:00 PM'
# inicio = texto.replace(' ', ':').split(':')
# tiempo_inicial = {
#         'hora': int(inicio[0])
#     }

# tests
print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00') )
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))

# print(add_time('3:00 PM', '3:10', 'mondAy'))
