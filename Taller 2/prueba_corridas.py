import math
from congruente import generador_congruente
from minimos import generador_minimo
from randoom import generador_lenguaje
 
def prueba_corrridas(x,a,m,d):

    L_corrida=list()
    corrida = "*"
    recurrencias,min=generador_minimo(x,a,m,d)
    #recurrencias,min=generador_minimo(5,106,6075)
    recurrencias.pop()
    media = round((2 * len(recurrencias) - 1) / 3, 2)
    varianza = math.sqrt((16 * len(recurrencias) - 29) / 90)



    for i in range(len(recurrencias) - 1):
        if recurrencias[i + 1] > recurrencias[i]:
            corrida += "+"

        else:
            corrida += "-"
    count = 1
    Z_observado =0
    for i in range(len(corrida) - 1):
        if corrida[i] == "+" and corrida[i + 1] == "-" or corrida[i] == "-" and corrida[i + 1] == "+":
            count += 1
        Z_observado=(count - media) / varianza
        #print(corrida)
        return corrida,Z_observado
    
    
def prueba_corrridas_congruente(x,a,c,m):

    L_corrida=list()
    corrida = "*"
    recurrencias,min=generador_congruente(x,a,c,m)
    #recurrencias.pop()
    media = round((2 * len(recurrencias) - 1) / 3, 2)
    varianza = math.sqrt((16 * len(recurrencias) - 29) / 90)



    for i in range(len(recurrencias) - 1):
        if recurrencias[i + 1] > recurrencias[i]:
            corrida += "+"

        else:
            corrida += "-"
    


    count = 1
    Z_observado =0
    for i in range(len(corrida) - 1):
        if corrida[i] == "+" and corrida[i + 1] == "-" or corrida[i] == "-" and corrida[i + 1] == "+":
            count += 1
        Z_observado=(count - media) / varianza
    return(corrida,Z_observado)

def prueba_corrridas_lenguaje(m):

    L_corrida=list()
    corrida = "*"
    recurrencias,min=generador_lenguaje(m)
    #recurrencias.pop()
    media = round((2 * len(recurrencias) - 1) / 3, 2)
    varianza = math.sqrt((16 * len(recurrencias) - 29) / 90)



    for i in range(len(recurrencias) - 1):
        if recurrencias[i + 1] > recurrencias[i]:
            corrida += "+"

        else:
            corrida += "-"
    


    count = 1
    Z_observado =0
    for i in range(len(corrida) - 1):
        if corrida[i] == "+" and corrida[i + 1] == "-" or corrida[i] == "-" and corrida[i + 1] == "+":
            count += 1
        Z_observado=(count - media) / varianza
    return(corrida,Z_observado)

#funcion de sobrante
def cambio_signo(cadena):
    count = 1
    for i in range(len(cadena) - 1):
        if cadena[i] == "+" and cadena[i + 1] == "-" or cadena[i] == "-" and cadena[i + 1] == "+":
            count += 1
    return count


