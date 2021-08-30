from random import randint 

def tiempo_llegada():
    return randint(0,120)

def control_boleta():
    return randint(40,100)

lista_tiempo=list()
lista_control=list()
cola=0
for i in range(100):
    lista_tiempo.append(tiempo_llegada())
    lista_control.append(control_boleta())

for i in lista_tiempo:
    
    if  i+1 == len(lista_tiempo):
        break
    
    elif (lista_control[i] - (lista_tiempo[i+1])) < 0:

        Resultado=lista_control[i] - lista_tiempo[i+1]

        lista_tiempo[i+1]=lista_tiempo[i+1]+ Resultado

        cola+=1    

        print(f"Hay cola {cola} Esperando {Resultado} segundos mas")




print(f"TIEMPO DE LLEGADA: \n{lista_tiempo}")
print("-----------")
print(f"CONTROL BOLETA:\n {lista_control}")