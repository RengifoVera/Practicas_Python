from random import randint
#asignacion de valores
mat = [ [0 , 7.0, 5.1, 4.5, 7.3, 5.1, 8.5, 7.6],
        [7.0, 0, 2.2, 6.4, 11.4, 9.4, 3.2, 3.0],
        [5.1, 2.2, 0, 4.2, 9.2, 7.2, 3.6, 2.8],
        [4.5, 6.4, 4.2, 0, 5.0, 3.2, 6.1, 5.1],
        [7.3, 11.4, 9.2, 5.0, 0, 2.2, 10.8, 9.8],
        [5.1, 9.4, 7.2, 3.2, 2.2, 0, 9.2, 8.2],
        [8.5, 3.2, 3.6, 6.1, 10.8, 9.2, 0, 1.0],
        [7.6, 3.0, 2.8, 5.1, 9.8, 8.2, 1.0, 0]
        ]

#para saber la longitud de la matriz
m=len(mat)
n=len(mat[0])

#for para definir la cantidad de interacciones a tratar
iteracion = int(input("Cantidad de iteracciones:"))

#definimos la secuencia inicial y su varianza y la variable distancia
ruta = [1, 2, 3, 4, 5, 6, 7, 8]
lruta = len(ruta)
distancia = 0
distanciaMinima = 0
recorridoGanador = list()

for y in range(0, iteracion):

    #2 PUNTOS if para pasar la ruta inicial tal cual al ser la primera iteracion
    if y == 0:
        ruta = ruta
        print("La ruta es:", ruta)
    else:
        random1 = randint(1,8)
        print("Random #1:", random1)
        random2 = randint(1,8)
        print("Random #2:", random2)

        #for para intercambiar los 2 puntos entre ellos 
        for z in range(0, lruta):
            if random1 == ruta[z]:
                ruta[z] = random2
            elif random2 == ruta[z]:
                ruta[z] = random1
        print("La ruta nueva es:", ruta)
    
    '''#2 PARES if para pasar la ruta inicial tal cual al ser la primera iteracion
    if y == 0:
        ruta = ruta
        print("La ruta es:", ruta)
    else:
        random1 = randint(1,8)
        print("Random #1:", random1)
        random2 = randint(1,8)
        print("Random #2:", random2)
        random3 = randint(1,8)
        print("Random #3:", random3)
        random4 = randint(1,8)
        print("Random #4:", random4)
    
        #for para intercambiar los 2 pares entre ellos 
        for z in range(0, lruta):
            if random1 == ruta[z]:
                ruta[z] = random3
            elif random3 == ruta[z]:
                ruta[z] = random1
        print("Primer intercambio:", ruta)

        for z in range(0, lruta):
            if random2 == ruta[z]:
                ruta[z] = random4
            elif random4 == ruta[z]:
                ruta[z] = random2
        print("Segundo intercambio:", ruta)'''


    #for para recorrer el array ruta sumando las distancias en la matriz
    for x in range(0, lruta):
        
        if x == lruta-1:
            j = ruta[0]
        else:
            j = ruta[x+1]
            #print("escoger j inicial: ")
            #print(j)

        i = ruta[x]
        #print("escoger i: ")
        #print(i) 

        print(mat[i-1][j-1], end = ", ")
        distancia = distancia + mat[i-1][j-1]
        distanciaActual=distancia

    #deja la ditancia en 0 para en la nueva iteracion sumar la distancia de la nueva ruta
    distancia = 0

    #validacion para saber si la distancia de cada iteracion es menor que la anterior
    if distanciaMinima == 0:
        distanciaMinima = distanciaActual
        #recorridoGanador = ruta
        #print("entro al if")
    elif distanciaMinima>distanciaActual:
        distanciaMinima = distanciaActual
        #recorridoGanador = ruta
        #print("entro al elif")
    else:
        distanciaMinima = distanciaMinima

    print()
    print("La distancia es:", distanciaActual)
    print()

#print("El recorrido ganador es:", recorridoGanador)
print("La distancia minima es:", distanciaMinima)

    
