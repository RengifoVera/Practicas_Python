from random import randint,choices
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import count

""" 
PROBLEMA DE LOS DADOS

Asume que se juega con dos dados, uno de ellos es justo, el otro es cargado, es decir
la probabilidad de obtener un 6 es 0.5, los demás números tienen igual probabilidad.
decide cual es la suma que se obtiene con más alta frecuencia """

def Dado_Justo():
    dado= randint(1,6)
    return dado

def Dado_Cargado():
    numeros=[1,2,3,4,5,6]
    resultado=choices(numeros,weights=[1,1,1,1,1,5])
    r=int(resultado[0])
    return r

def resultado_sumas(a,b):
    
    # print("Primer DADO: " + str(a))
    # print("Segundo DADO: " + str(b))
    # print("Suma: " + str(a+b))
    # print("-------------------------")

    return(a+b)
            
# def resultado_dado_Cargado():
#     intentos=int(input("Ingrese cantidad de intentos: "))
#     #arreglo de porcentajes con aumento de 0.5% en probabilidad de que caiga el numero 6
#     simulacion= np.random.choice(list(range(1,7)),intentos,p=[0.1,0.1,0.1,0.1,0.1,0.5])
#     #grafica donde se muestra que el numero 6 cayo con mas frecuencia que los otros
#     count,bins,ignored = plt.hist(simulacion,25,density=False)
#     print(simulacion)
#     return(plt.show())

def suma_comun(a):
    #Recibe una lista, y devuelve un diccionario con todas las repeticiones de cada valor
    return {i:a.count(i) for i in a}


intentos=int(input("Ingrese Cantidad de Intentos: "))
lista_sumas=list()
#limitando intentos amenos de 100 mil lanzamientos
if intentos > 100000:
    print("INTENTALO CON UN VALOR MENOR A 100MIL INTENTOS")
else:
    for i in range(intentos):
        lista_sumas.append(resultado_sumas(Dado_Justo(),Dado_Cargado()))

    print(lista_sumas)

    resultado=suma_comun(lista_sumas) 
    maximo=max(resultado, key=resultado.get)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("  la suma que se obtiene con más alta frecuencia y tiene como resultado el numero ->",maximo," con ",resultado[maximo],f"apariciones en {intentos} intentos")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
