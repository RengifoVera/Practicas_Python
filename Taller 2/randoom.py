import random as r
def generador_lenguaje(m):
    numeros_generados=list()
    recurrencia=list()
    for i in range(m):
        x= r.randint(0,m)
        numeros_generados.append(x)
        recurrencia.append(x/m)
    return recurrencia,numeros_generados

#print(generador_lenguaje(1000))