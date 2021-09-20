def generador_congruente(x,a,c,m):

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

    print(f"Recurrencia: {recurrencia} \n Resultado: {resultado}")
    print(f"Periodo: {len(resultado)-1}")
    return (recurrencia)
    
recurrencia=generador_congruente(5,106,1283,6975)

