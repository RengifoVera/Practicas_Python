import math
def generador_minimo(a,x,m):
    recurrencias=list()
    min=list()
    min.append(x)
    for i in range(m):
        if x > 0:
            x = (a * x) % m
            r=x/m
            r=round(r,2)
            recurrencias.append(r)
            min.append(x)
            if x == min[0]:
                break
        else:
            break
    print(f"Recurrencias: {recurrencias}")
    print(f"Generador: {min}")
    print(f"Periodo: {len(min)-1}")
    return recurrencias
recurrencias=generador_minimo(106,5,6075)