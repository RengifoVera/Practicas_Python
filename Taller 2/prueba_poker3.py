from minimos import generador_minimo
from congruente import generador_congruente
from randoom import generador_lenguaje


def prueba_poker(x,a,m,d):
    recurrencias,min=generador_minimo(x,a,m,d)
    recurrencias.pop()
    clases=[0]*3
    probabilidades=[0.01,0.24,0.72]
    for i in range(len(recurrencias)):
        x=str(recurrencias[i])
        if len(x)==3:
            x+="00"
        elif len(x)==4:
            x+="0"
        if x[2] == x[3] and x[3] == x[4]:
            clases[0] += 1
        elif x[2] == x[3] and x[4] != x[3] or x[2] != x[3] and x[3] == x[4] or x[2] != x[3] and x[2] == x[4]:
            clases[1] = clases[1] + 1
        else:
            clases[2] += 1
    clase=1
    chi_calculado=0
    list_FE=list()
    list_FE_FO=list()
    #print("{:^20}  {:^20} {:^20} {:^20}".format("clase", "FO", "FE", "(FE-FO)^2/FE"))
    for i in range(3):
        FE = round(probabilidades[i]*len(recurrencias),3)
        list_FE.append(FE)
        chi_calculado= chi_calculado+round((FE - clases[i]) ** 2 / FE, 3)
        FO_FE=round((FE - clases[i]) ** 2 / FE, 3)
        list_FE_FO.append(FO_FE)
        #print("{:^20} {:^20} {:^20} {:^20} ".format(clase, clases[i], FE,FO_FE ))
        clase =clase+ 1
    return clases,list_FE,list_FE_FO,chi_calculado

def prueba_poker_congruente(x,a,c,m):
    recurrencias,min=generador_congruente(x,a,c,m)
    recurrencias.pop()
    clases=[0]*3
    probabilidades=[0.01,0.24,0.72]
    for i in range(len(recurrencias)):
        x=str(recurrencias[i])
        if len(x)==3:
            x+="00"
        elif len(x)==4:
            x+="0"
        if x[2] == x[3] and x[3] == x[4]:
            clases[0] += 1
        elif x[2] == x[3] and x[4] != x[3] or x[2] != x[3] and x[3] == x[4] or x[2] != x[3] and x[2] == x[4]:
            clases[1] = clases[1] + 1
        else:
            clases[2] += 1
    clase=1
    chi_calculado=0
    list_FE=list()
    list_FE_FO=list()
    #print("{:^20}  {:^20} {:^20} {:^20}".format("clase", "FO", "FE", "(FE-FO)^2/FE"))
    for i in range(3):
        FE = round(probabilidades[i]*len(recurrencias),3)
        list_FE.append(FE)
        chi_calculado= chi_calculado+round((FE - clases[i]) ** 2 / FE, 3)
        FO_FE=round((FE - clases[i]) ** 2 / FE, 3)
        list_FE_FO.append(FO_FE)
        #print("{:^20} {:^20} {:^20} {:^20} ".format(clase, clases[i], FE,FO_FE ))
        clase =clase+ 1
    return clases,list_FE,list_FE_FO,chi_calculado

def prueba_poker_lenguaje(m):
    recurrencias,min=generador_lenguaje(m)
    recurrencias.pop()
    clases=[0]*3
    probabilidades=[0.01,0.24,0.72]
    for i in range(len(recurrencias)):
        x=str(recurrencias[i])
        if len(x)==3:
            x+="00"
        elif len(x)==4:
            x+="0"
        if x[2] == x[3] and x[3] == x[4]:
            clases[0] += 1
        elif x[2] == x[3] and x[4] != x[3] or x[2] != x[3] and x[3] == x[4] or x[2] != x[3] and x[2] == x[4]:
            clases[1] = clases[1] + 1
        else:
            clases[2] += 1
    clase=1
    chi_calculado=0
    list_FE=list()
    list_FE_FO=list()
    #print("{:^20}  {:^20} {:^20} {:^20}".format("clase", "FO", "FE", "(FE-FO)^2/FE"))
    for i in range(3):
        FE = round(probabilidades[i]*len(recurrencias),3)
        list_FE.append(FE)
        chi_calculado= chi_calculado+round((FE - clases[i]) ** 2 / FE, 3)
        FO_FE=round((FE - clases[i]) ** 2 / FE, 3)
        list_FE_FO.append(FO_FE)
        #print("{:^20} {:^20} {:^20} {:^20} ".format(clase, clases[i], FE,FO_FE ))
        clase =clase+ 1
    return clases,list_FE,list_FE_FO,chi_calculado



