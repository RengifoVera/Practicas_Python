def estandar_minimo(a,x,m):
    min=list()
    recurrencia=list()
    min.append(x)

    for i in range(m):
        if x > 0:
            x= (a * x) % m
            r=x/m
            r=round(r,3)
            recurrencia.append(r)
            min.append(x)
            if x== min[0]:
                break
        else:
            print("No Puede usarse una semilla menor o igual a cero ")
            break

    
    print(f"Secuencia de numeros: {min}")
    print(f"Resultados Recurrencia {recurrencia}")
    print(f"Periodo: {len(min)-1}")

def minimo_factorizado(a,x,m):
    pass

print(estandar_minimo(12,5,10000))