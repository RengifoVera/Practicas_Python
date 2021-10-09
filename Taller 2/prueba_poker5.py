from minimos import generador_minimo
from congruente import generador_congruente
from randoom import generador_lenguaje

def prueba_poker5(x,a,m,d):
    recurrencias,min=generador_minimo(x,a,m,d)
    clases=["TD","PAR","2PAR","TP","TERCIA","POKER","QUINTILLA"]
    categorias = [0]*7
    probabilidades=[0.3024,0.504,0.108,0.009,0.072,0.0045,0.0001]
    aux=0
    z=0
    while z!= len(recurrencias):
        r = str(recurrencias[z])
        if len(r) == 3:
            r += "0000"
        elif len(r) == 4:
            r += "000"
        elif len(r) == 5:
            r += "00"
        elif len(r) == 6:
            r += "0"

        x = r[2:7]
        for i in range(len(x)):
            if x.count(x[i]) == 1:
                aux += 1
            elif x.count(x[i]) == 4:
                categorias[5] += 1
                aux = -1
                break
            elif x.count(x[i]) == 5:
                categorias[6] += 1
                aux = -1
                break

        if aux == 5:
            categorias[0] += 1
        elif aux == 3:
            categorias[1] += 1
        elif aux == 1:
            categorias[2] += 1
        elif aux == 0:
            categorias[3] += 1
        elif aux == 2:
            categorias[4] += 1
        aux = 0
        z += 1

    suma=0
    list_ei=list()
    list_fefo=list()
    # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format("clase", "O(i)", "PROBABILIDAD","EI", "(FE-FO)^2/FE"))
    for i in range(len(categorias)):
        Ei=len(recurrencias)*probabilidades[i]
        list_ei.append(Ei)
        suma+=((Ei-categorias[i])**2)/Ei
        FE_FO=((Ei-categorias[i])**2)/Ei
        list_fefo.append(FE_FO)
        # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format(clases[i],categorias[i],probabilidades[i],Ei,FE_FO))
 #   print(f"suma {suma}")
    return categorias,probabilidades,list_ei,list_fefo,suma

#print(prueba_poker5())

def prueba_poker5_congruente(x,a,c,m):
    recurrencias,min=generador_congruente(x,a,c,m)
    clases=["TD","PAR","2PAR","TP","TERCIA","POKER","QUINTILLA"]
    categorias = [0]*7
    probabilidades=[0.3024,0.504,0.108,0.009,0.072,0.0045,0.0001]
    aux=0
    z=0
    while z!= len(recurrencias):
        r = str(recurrencias[z])
        if len(r) == 3:
            r += "0000"
        elif len(r) == 4:
            r += "000"
        elif len(r) == 5:
            r += "00"
        elif len(r) == 6:
            r += "0"

        x = r[2:7]
        for i in range(len(x)):
            if x.count(x[i]) == 1:
                aux += 1
            elif x.count(x[i]) == 4:
                categorias[5] += 1
                aux = -1
                break
            elif x.count(x[i]) == 5:
                categorias[6] += 1
                aux = -1
                break

        if aux == 5:
            categorias[0] += 1
        elif aux == 3:
            categorias[1] += 1
        elif aux == 1:
            categorias[2] += 1
        elif aux == 0:
            categorias[3] += 1
        elif aux == 2:
            categorias[4] += 1
        aux = 0
        z += 1

    suma=0
    list_ei=list()
    list_fefo=list()
    # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format("clase", "O(i)", "PROBABILIDAD","EI", "(FE-FO)^2/FE"))
    for i in range(len(categorias)):
        Ei=len(recurrencias)*probabilidades[i]
        list_ei.append(Ei)
        suma+=((Ei-categorias[i])**2)/Ei
        FE_FO=((Ei-categorias[i])**2)/Ei
        list_fefo.append(FE_FO)
        # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format(clases[i],categorias[i],probabilidades[i],Ei,FE_FO))

    return categorias,probabilidades,list_ei,list_fefo,suma



def prueba_poker5_lenguaje(m):
    recurrencias,min=generador_lenguaje(m)
    clases=["TD","PAR","2PAR","TP","TERCIA","POKER","QUINTILLA"]
    categorias = [0]*7
    probabilidades=[0.3024,0.504,0.108,0.009,0.072,0.0045,0.0001]
    aux=0
    z=0
    while z!= len(recurrencias):
        r = str(recurrencias[z])
        if len(r) == 3:
            r += "0000"
        elif len(r) == 4:
            r += "000"
        elif len(r) == 5:
            r += "00"
        elif len(r) == 6:
            r += "0"

        x = r[2:7]
        for i in range(len(x)):
            if x.count(x[i]) == 1:
                aux += 1
            elif x.count(x[i]) == 4:
                categorias[5] += 1
                aux = -1
                break
            elif x.count(x[i]) == 5:
                categorias[6] += 1
                aux = -1
                break

        if aux == 5:
            categorias[0] += 1
        elif aux == 3:
            categorias[1] += 1
        elif aux == 1:
            categorias[2] += 1
        elif aux == 0:
            categorias[3] += 1
        elif aux == 2:
            categorias[4] += 1
        aux = 0
        z += 1

    suma=0
    list_ei=list()
    list_fefo=list()
    # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format("clase", "O(i)", "PROBABILIDAD","EI", "(FE-FO)^2/FE"))
    for i in range(len(categorias)):
        Ei=len(recurrencias)*probabilidades[i]
        list_ei.append(Ei)
        suma+=((Ei-categorias[i])**2)/Ei
        FE_FO=((Ei-categorias[i])**2)/Ei
        list_fefo.append(FE_FO)
        # print("{:^20}  {:^20} {:^20} {:^20} {:^20}".format(clases[i],categorias[i],probabilidades[i],Ei,FE_FO))

    return categorias,probabilidades,list_ei,list_fefo,suma



    