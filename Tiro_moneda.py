from random import choice

"""
***ENUNCIADO DEL EJERCICIO***

Un juego: (tomado de Bernardo Calderon, Introducción a la simulación, 1975) Usted
lanza una moneda y cuenta el número de caras y sellos que se va obteniendo.El juego
termina cuando la diferencia entre caras y sellos sea 3, no interesa cual sea mayor. En
este instante usted recibe $8 por el juego, pero tiene que pagar $1 por cada lanzamiento
que usted haya hecho.`? le conviene a Usted participar en el juego.

Considere también la situación, donde el juego es adicionalmente limitado a un máximo
de 15 lanzamientos.

        *** CONCLUSION ***

        EN GENERAL EL JUEGO TERMINA SIENDO DESFAVORABLE

"""

#me indica que salio en el lanzamiento si cara o sello de la moneda de manera aleatoria
def lanzamiento_moneda():
    lados=["CARA","SELLO"]
    eleccion = (choice(lados))
    return (eleccion)

# #dejando que el usuario elija la cantidad de lanzamientos
lista=list()
pago=8
cantidad_lanzamientos=int(input("Ingrese Cantidad de Lanzamientos: "))
for i in range(cantidad_lanzamientos):
        lista.append(lanzamiento_moneda())
        x=lista.count("SELLO")
        y=lista.count("CARA")
        if x-y == 3:
            break

print(lista)
print(f"CANTIDAD QUE SALIO SELLO: {x}")
print(f"CANTIDAD QUE SALIO CARA: {y}")
print(f"Recibiste {pago} pero te descontamos {1} por cada lanzamiento ,  en total recibiste {pago-cantidad_lanzamientos}\n")
print("--------------------------LIMITANDOLO A SOLO 15 LANZAMIENTOS -----------------------------------\n")
#limitando la cantidad de lanzamientos a 15
lista_limite=list()
lanzamientos=1
while lanzamientos <= 15:
    lista_limite.append(lanzamiento_moneda())
    x_l=lista_limite.count("SELLO")
    y_l=lista_limite.count("CARA")
    if x_l-y_l == 3:
        break
    lanzamientos+=1
print(f"CANTIDAD QUE SALIO SELLO: {x_l}")
print(f"CANTIDAD QUE SALIO CARA: {y_l}")
print(lista_limite)
print(f"Recibiste {pago} pero te descontamos {1} por cada lanzamiento ,  en total recibiste {pago-lanzamientos}")



