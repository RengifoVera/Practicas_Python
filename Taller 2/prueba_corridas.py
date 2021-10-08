import math
from congruente import generador_congruente
from minimos import generador_minimo
from randoom import generador_lenguaje
# 
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

    

# R="*+++-+-+---++-+--+-+--+--+-++-++-+--++-"

def cambio_signo(cadena):
    count = 1
    for i in range(len(cadena) - 1):
        if cadena[i] == "+" and cadena[i + 1] == "-" or cadena[i] == "-" and cadena[i + 1] == "+":
            count += 1
    return count


# recurrencias1 = [0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
#         0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
#         0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
#         0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29
#         ]

# recurrencias2 = [0.08, 0.09, 0.23, 0.29, 0.42, 0.55, 0.58, 0.72, 0.89, 0.91,
#         0.11, 0.16, 0.18, 0.31, 0.41, 0.53, 0.71, 0.73, 0.74, 0.84,
#         0.01, 0.09, 0.30, 0.32, 0.45, 0.47, 0.69, 0.74, 0.91, 0.95,
#         0.12, 0.13, 0.29, 0.36, 0.38, 0.54, 0.68, 0.86, 0.88, 0.91
#         ]

#ar=[0.02,0.77,0.52,0.27,0.02]
#print(prueba_corrridas_congruente(ar))
