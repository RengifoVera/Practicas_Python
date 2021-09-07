lista_hora_llegada=[39,49,66,155,189,300,386,412,451,502,509,13]
lista_hora_salida=[83,151,220,319,364,417,469,568,611,703,773,827]
lista_control=[83,68,69,99,45,53,52,99,43,92,70,54,14]
lista_cola=list()
cola=0
j=0

for i in range(len(lista_hora_llegada)):
    if j ==  (len(lista_hora_llegada)):
        continue
    else:
        if (lista_control[i] - lista_hora_llegada[j]) >0:
            cola+=1
            
            lista_cola.append(cola)
        elif (lista_control[i] - lista_hora_llegada[j]) <0:
                    cola=cola
                    lista_cola.append(cola)
        j+=1

print(lista_cola[-1])