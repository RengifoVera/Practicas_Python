from minimos import generador_minimo

recurrencia,min=generador_minimo(5,106,6075)

chi_critico=36.42
matriz =  []
matriz_chicuadrado=[]
for i in range(5):
    matriz.append([0]*5)
for i in range(5):
    matriz_chicuadrado.append([0]*5)

#arr=[0.09, 0.25, 0.26, 0.57, 0.28, 0.19, 0.72, 0.99, 0.78, 0.53, 0.36, 0.04, 0.01, 0.4, 0.96, 0.16, 0.1, 0.56, 0.98, 0.47, 0.82, 0.46, 0.51, 0.74, 0.61, 0.21, 0.33, 0.42, 0.58, 0.59, 0.9, 0.62, 0.52, 0.05, 0.32, 0.11, 0.87, 0.69, 0.37, 0.35, 0.73, 0.3, 0.49, 0.43, 0.89, 0.31, 0.8, 0.15, 0.79, 0.84, 0.07, 0.94, 0.54, 0.67, 0.75, 0.91, 0.93, 0.24, 0.95, 0.85, 0.38, 0.66, 0.45, 0.2, 0.03, 0.7, 0.68, 0.06, 0.63, 0.83, 0.77, 0.22, 0.64, 0.14, 0.48, 0.12, 0.17, 0.41, 0.27, 0.88, 0.0]

def prueba_series(arr,x,y,i):
    while i != len(arr) - 1:
        if arr[i] >= 0.0 and arr[i] < 0.2:
            x = 0
        elif arr[i] >= 0.2 and arr[i] < 0.4:
            x = 1
        elif arr[i] >= 0.4 and arr[i] < 0.6:
            x = 2
        elif arr[i] >= 0.6 and arr[i] < 0.8:
            x = 3
        elif arr[i] >= 0.8 and arr[i] <= 1:
            x = 4

        if arr[i + 1] >= 0.0 and arr[i + 1] < 0.2:
            y = 0
        elif arr[i + 1] >= 0.2 and arr[i + 1] < 0.4:
            y = 1
        elif arr[i + 1] >= 0.4 and arr[i + 1] < 0.6:
            y = 2
        elif arr[i + 1] >= 0.6 and arr[i + 1] < 0.8:
            y = 3
        elif arr[i + 1] >= 0.8 and arr[i + 1] <= 1:
            y = 4
        i = i + 2
        matriz[x][y] += 1
    return matriz
recurrencia.pop()
print(prueba_series(recurrencia,0,0,0))


def prueba_series_chicuadrado(matriz,FE,arr):
    parejas = len(arr)/2
    FE = round(parejas/25)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_chicuadrado[i][j] = round(((FE- matriz[i][j])**2)/FE,3)
    for i in matriz_chicuadrado:
        print(i)
    suma=0
    for i in range(len(matriz_chicuadrado)):
        for j in range(len(matriz_chicuadrado)):
            suma = suma + matriz_chicuadrado[i][j]
    if suma <= chi_critico:
        return suma," <= ",chi_critico," se acepta la hipotesis de indenpendencia"
    else:
        return suma, " > ", chi_critico, " se acepta la hipotesis de indenpendencia"

print(prueba_series_chicuadrado(matriz,0,recurrencia))






