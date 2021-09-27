from math import floor
def generador_minimo(a,x,m):
    recurrencias=list()
    min=list()
    min.append(x)
    q=floor(m/a)
    r=m%a
    for i in range(m):
        x=(a * (x % q) - r * (floor(x/q)))
        if x < 0:    
            x=x+m
        recurrencias.append(round(x/m,2))
        min.append(x)
        if x < 0:
            print("\nCON LOS DATOS INGRESADOS NO SE PUEDE EVITAR EL OVERFLOW","\nPROBABLEMENTE LOS DATOS SEAN MUY PEQUEÑOS",x)
            break
        elif x == min[0]:
            break
       
#    print(f"Recurrencias: {recurrencias}")
#    print(f"Generador: {min}")
#    print(f"Periodo: {len(min)-1}")
    return recurrencias,min
#recurrencias,min=generador_minimo(106,5,6075)

#print(recurrencias,min)
