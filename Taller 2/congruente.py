def generador_congruente(x,a,c,m):
    
    x=int(input("Ingrese X0: "))
    a=int(input("Ingrese A: "))
    c=int(input("Ingrese C: "))
    m=int(input("Ingrese M: "))

    resultado=list()
    recurrencia=list()
    resultado.append(x)

    for i in range(m):
        x=((a * x) + c) % m
        r = x/m
        r=round(r,3)
        resultado.append(x)
        recurrencia.append(r)
        if x == resultado[0]:
            break

    print(recurrencia,resultado)
    print(f"Periodo: {len(resultado)-1}")
        

print(generador_congruente(27,17,43,100))
