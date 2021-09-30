
def generador_minimo(x,a,m):
    recurrencias=list()
    min=list()

    def se_repite(arr,x):
        if arr.count(x)>1:
            return True
        else:
            return False

    for i in range(m):
        xn=(a*x)%m
        R=round(xn/m,2)
        recurrencias.append(R)
        min.append(xn)
        x=xn
        if se_repite(min,min[0]):
            break       
   

    return recurrencias,min

