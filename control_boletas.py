from random import randint

def tiempo_llegada():
    return randint(0,120)
# #PROBAR EL CASO DE TIEMPO DE CONTROL DE ENTRADAS ENTRE 40 Y 100 SEGUNDOS
# def control_boleta():
#     return randint(40,100)

# DESCOMENTAR PARA PROBAR EL CASO DE TIEMPO DE CONTROL ENTRE 20 Y 80 SEGUNDOS
def control_boleta():
    return randint(20,80)

#Listas de Tiempos entre llegada y tiempo de llegada del sgte cliente
lista_tiempo=list()
lista_hora_llegada=list()

#Tiempo de control de boletas y Tiempo de salida
lista_control=list()
lista_hora_salida=list()

#Tiempo de espera en la cola
lista_tiempo_espera=list()
lista_cola=list()


#Variables Auxiliares
hora_llegada=0
hora_salida=0
indice=0
cola=0
j=0
print("***** Ingrese numero mayores a 0 *****")
 
numero_personas=int(input("Ingrese cantidad de Personas A Simular: "))
        

#Genera listas aleatorias de tiempos de llegada y de atencion
for i in range(numero_personas):
    lista_tiempo.append(tiempo_llegada())
    lista_control.append(control_boleta())

# MUESTRA EL TIEMPO ENTRE LLEGADAS DE LOS CLIENTES
for i in lista_tiempo:
    hora_llegada +=i
    lista_hora_llegada.append(hora_llegada)

#MUESTRA EL TIEMPO EN EL QUE UN CLIENTE SE DEMORO EN SER ATENDIDO
for i in lista_control:
    hora_salida+=i
    lista_hora_salida.append(hora_salida)

#MUESTRA EL TIEMPO DE ESPERA EN EL QUE UN CLIENTE DEBIO ESPERAR PARA SER ATENDIDO
while indice < len(lista_hora_llegada):
    tiempo_espera=abs(lista_hora_salida[indice]-(lista_hora_llegada[indice] + lista_control[indice] ))
    indice+=1
    lista_tiempo_espera.append(tiempo_espera)
suma_tiempo_espera=sum(lista_tiempo_espera)
promedio=suma_tiempo_espera / numero_personas

#DETERMINAR EL COMPORTAMIENTO Y EL TAMAÑO MAXIMO DE LA COLA DE LA COLA
for i in range(len(lista_hora_llegada)):
    if j ==  (len(lista_hora_llegada)):
        continue
    else:
        if (lista_hora_salida[i] - lista_hora_llegada[j]) >0:
            cola+=1
            
            lista_cola.append(cola)
        elif (lista_hora_salida[i] - lista_hora_llegada[j]) <0:
                    cola=cola
                    lista_cola.append(cola)
        j+=1





# suma_hora_llegada=sum(lista_hora_llegada)
# suma_hora_salida=sum(lista_hora_salida)
# sum_hora_control=sum(lista_control)


print(f"Lista Tiempo: {lista_tiempo}")
print(f"Lista Hora Llegada: {lista_hora_llegada}")

print("***------------------------***------------------------***")
print(f"Lista Control Boleta: {lista_control}")
print(f"Lista Hora Salida: {lista_hora_salida}")

print("***------------------------***------------------------***")
print(f"Lista tiempo espera: {lista_tiempo_espera}")
print("***------------------------***------------------------***")
print(f"Veces donde hubo Cola: {lista_cola[-1]}")
print("***------------------------***------------------------***")
print(f"Tiempo Promedio de espera en la cola fue de {promedio} segundos")