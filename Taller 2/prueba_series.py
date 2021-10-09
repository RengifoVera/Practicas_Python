



def prueba_series(arr):
    x=0
    y=0
    i=0
    matriz =  []

    for i in range(5):
        matriz.append([0]*5)

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
# arr,min=generador_minimo(5,106,6075,2)
# arr.pop()



def prueba_series_chicuadrado(matriz,arr):
    matriz_chicuadrado=[]
    for i in range(5):
        matriz_chicuadrado.append([0]*5)
    FE=0
    parejas = len(arr)/2
    FE = round(parejas/25)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz_chicuadrado[i][j] = round(((FE- matriz[i][j])**2)/FE,3)
    suma=0
    for i in range(len(matriz_chicuadrado)):
        for j in range(len(matriz_chicuadrado)):
            suma = suma + matriz_chicuadrado[i][j]

    for i in matriz_chicuadrado:
        # print(i)
        return matriz_chicuadrado,suma

    



#print(prueba_series_chicuadrado(matriz,arr))



