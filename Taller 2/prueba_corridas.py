import math
from minimos import generador_minimo

def prueba_corrridas(x,a,m):
    Z1 = 1.96
    Z2 = -1.96
    L_corrida=list()
    corrida = "*"
    recurrencias,min=generador_minimo(x,a,m)
    recurrencias.pop()
    media = round((2 * len(recurrencias) - 1) / 3, 2)
    varianza = math.sqrt((16 * len(recurrencias) - 29) / 90)
    for i in range(len(recurrencias) - 1):
        if recurrencias[i + 1] > recurrencias[i]:
            corrida += "+"

        else:
            corrida += "-"
    count = 1
    for i in range(len(corrida) - 1):
        if corrida[i] == "+" and corrida[i + 1] == "-" or corrida[i] == "-" and corrida[i + 1] == "+":
            count += 1
    return corrida
    # for i in corrida:
    #     L_corrida.append(i)
    # return (L_corrida)

    Z_observado = (count - media) / varianza
    
    
    if Z_observado >= Z2 and Z_observado <= Z1:
        print( Z_observado, "se encuentra en el intervalo", "[", Z1, Z2, "]")
    else:
        print (Z_observado, "no se encuentra en el intervalo", "[", Z1, Z2, "]")
    

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


# print(prueba_corrridas(recurrencias1))
