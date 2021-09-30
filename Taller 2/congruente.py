def generador_congruente(x,a,c,m):

    resultado=list()
    recurrencia=list()
    resultado.append(x)

    def se_repite(arr,x):
        if arr.count(x)>1:
            return True
        else:
            False

    for i in range(m):
        x=((a * x) + c) % m
        r = x/m
        r=round(r,3)
        resultado.append(x)
        recurrencia.append(r)
        if se_repite(recurrencia,recurrencia[0]):
            break

    return recurrencia,resultado

 

