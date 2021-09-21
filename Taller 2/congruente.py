def generador_congruente(x,a,c,m):

    resultado=[]
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
   
    return recurrencia,resultado

    


