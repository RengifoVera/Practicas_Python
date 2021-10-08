

import math
def se_repite(arr,x):
    if arr.count(x)>1:
        return True
    else:
        False


def generadorEstandarMinimoNormal(x,a,m,d):
    numeros_generados=[]
    recurrencia=[]
    while True:
        xn=(a*x)%m
        R=round(xn/m,d)
        recurrencia.append(R)
        numeros_generados.append(xn)
        x=xn
        if se_repite(numeros_generados,numeros_generados[0]):
            break
    return numeros_generados,len(numeros_generados)-1


def  generador_minimo(x,a,m,d):
    q=math.floor(m/a)
    r=m%a
    resultados=[]
    recurrencia=[]
    while True:
        xn= (a*(x%q)) - r*(math.floor(x/q))
        if xn<0:
            xn=xn+m
        if xn<0:
            return generadorEstandarMinimoNormal(x,a,m)
        R=round(xn/m,d)
        resultados.append(xn)
        recurrencia.append(R)
        x=xn
        if se_repite(resultados,resultados[0]):
            return recurrencia,resultados


#print(generador_minimo(5,12,21))
# def generador_minimo(x,a,m):
#     recurrencias=list()
#     min=list()

#     def se_repite(arr,x):
#         if arr.count(x)>1:
#             return True
#         else:
#             return False

#     for i in range(m):
#         xn=(a*x)%m
#         R=round(xn/m,2)
#         recurrencias.append(R)
#         min.append(xn)
#         x=xn
#         if se_repite(min,min[0]):
#             break       
   

#     return recurrencias,min

