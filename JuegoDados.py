from random import randint,choices
import numpy as np
#import matplotlib.pyplot as plt

#PARA VER GRAFICAS DEBE TENER EL MODULO MATPLOTLIB , INSTALANDOLO CON PIP INSTALL MATPLOTLIB

def Dado_Justo():
    dado= randint(1,6)
    return dado

def Dado_Cargado():
    #lista de numeros del dado cargado
    numeros=[1,2,3,4,5,6]
    #aunmenta la probabilidad en un 0.5% mas que el numero 6 caiga
    resultado=choices(numeros,weights=[1,1,1,1,1,5])
    r=int(resultado[0])
    return r

def resultado_sumas(a,b):
    return(a+b)

#MUESTRA UNA GRAFICA DONDE SE REFLEJA QUE HAY UN 
# #DADO CARGADO CON MAYOR PROBABILIDAD DE SALIR UN NUMERO SEIS      
  
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
#limitando intentos a menos de 1millon de lanzamientos 
# en caso de querer hacer mas lanzamientos,comentar o eliminar las lineas 49 y 51, y tabular correctamente
if intentos > 1000000:
    print("INTENTALO CON UN VALOR MENOR A 1 MILLON LANZAMIENTOS")
else:
    for i in range(intentos):
        lista_sumas.append(resultado_sumas(Dado_Justo(),Dado_Cargado()))

    print(lista_sumas)

    resultado=suma_comun(lista_sumas) 
    maximo=max(resultado, key=resultado.get)
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("  la suma que se obtiene con más alta frecuencia y tiene como resultado el numero ->",maximo," con ",resultado[maximo],f"apariciones en {intentos} intentos")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")

#grafica que muestra el numero que con mas frecuencia salio en la lista de sumas del justo y el cargado
# counts,bins,ignored=plt.hist(lista_sumas,25,density=False)
# plt.show()