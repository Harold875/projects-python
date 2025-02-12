# formateador aritmetico

def cantidad_chars(datos):
    for dato in datos:
        chars = []
        for n in range(len(dato)):
            if n == 1:
                continue
            chars.append(len(dato[n]))
        dato.append(chars)
    return datos


def resultado(n1,n2,signo):
    if "+" in signo:
        return n1 + n2
    else:    
        return n1 - n2
    



def mensaje(datos, show=False):
    # mensaje = ""
    linea_superior = ""
    linea_media = ""
    linea_inferior = ""
    linea_resultado = ""
    for i in range(len(datos)):
        chars_sup = datos[i][3][0]
        chars_inf = datos[i][3][1]
        n1 = int(datos[i][0])
        n2 = int(datos[i][2])
        signo = datos[i][1]
        r = resultado(n1,n2,signo)
        if chars_sup >= chars_inf:
            diferencia = chars_sup - chars_inf
            linea1 = "  " + f"{datos[i][0]}"
            linea2 = f"{datos[i][1]} " + (" "*diferencia) + f"{datos[i][2]}"
            linea3 = "--" + "-"*chars_sup
            dif_resultad = 2 + chars_sup
            linea4 = (" "*(dif_resultad - len(str(r)))) + f"{r}"
            if  (i + 1) != len(datos):
                linea_superior += linea1 + " "*4
                linea_media += linea2 + " "*4
                linea_inferior += linea3 + " "*4
                linea_resultado += linea4 + " "*4
            else:
                linea_superior += linea1
                linea_media += linea2
                linea_inferior += linea3
                linea_resultado += linea4
        else:
            diferencia = chars_inf - chars_sup
            linea1 = "  " + (" "*diferencia) + f"{datos[i][0]}"
            linea2 = f"{datos[i][1]} " + f"{datos[i][2]}"
            linea3 = "--" + "-"*chars_inf
            dif_resultad = 2 + chars_inf
            linea4 = (" "*(dif_resultad - len(str(r)))) + f"{r}"
            if  (i + 1) != len(datos):
                linea_superior += linea1 + " "*4
                linea_media += linea2 + " "*4
                linea_inferior += linea3 + " "*4
                linea_resultado += linea4 + " "*4
            else:
                linea_superior += linea1
                linea_media += linea2
                linea_inferior += linea3
                linea_resultado += linea4
    
    # mensaje
    mensaje_final = linea_superior + "\n" + linea_media + "\n" + linea_inferior
    if not show:
        return mensaje_final
    else:
        mensaje_final += "\n" + linea_resultado 
        return mensaje_final


def errores(elements):
    #  5 maximo
    if len(elements) > 5:
        return 'Error: Too many problems.' 

    for el in elements:
        # cobormacion de signos '+' y '-' 
        if el[1] != "+":
            if el[1] != "-": 
                return "Error: Operator must be '+' or '-'."
            
        # comprobar si son datos numericos
        if not el[0].isnumeric() or not el[2].isnumeric():
            return 'Error: Numbers must only contain digits.'
        
        # comprobar si contienen mas de 4 digitos
        if len(el[0]) > 4 or len(el[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
    
    return None


def arithmetic_arranger(elements, show_answers=False):
    
    #validacion del segundo argumento
    if not isinstance(show_answers, bool):
        return "Error: Invalid second argument. Only True or False are allowed."
    
    
    elements_orden = [element.split(" ") for element in elements]
    
    # control de errores
    error = errores(elements_orden)
    if error != None:
        return error

    # funcionamiento
    elements_chars  = cantidad_chars(elements_orden)
    if show_answers:
        mensaje_ = mensaje(elements_chars, True)
    else:
        mensaje_ = mensaje(elements_chars)
        
    return mensaje_ 




# tests
print(arithmetic_arranger(["3801 + 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))



# completado :3
