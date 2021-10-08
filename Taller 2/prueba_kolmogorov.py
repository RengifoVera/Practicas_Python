from minimos import generador_minimo
from congruente import generador_congruente
from randoom import generador_lenguaje

def kolmogorov(x,a,m,d):      
    rangos = [0] * 10
    DM_critico = 0.043
    PEA_POA = [0] * 10
    recurrencias,min=generador_minimo(x,a,m,d)
    recurrencias.pop()
    for i in range(len(recurrencias)):
        if recurrencias[i] >= 0 and recurrencias[i] < 0.1:
            rangos[0] += 1
        elif recurrencias[i] >= 0.1 and recurrencias[i] < 0.2:
            rangos[1] += 1
        elif recurrencias[i] >= 0.2 and recurrencias[i] < 0.3:
            rangos[2] += 1
        elif recurrencias[i] >= 0.3 and recurrencias[i] < 0.4:
            rangos[3] += 1
        elif recurrencias[i] >= 0.4 and recurrencias[i] < 0.5:
            rangos[4] += 1
        elif recurrencias[i] >= 0.5 and recurrencias[i] < 0.6:
            rangos[5] += 1
        elif recurrencias[i] >= 0.6 and recurrencias[i] < 0.7:
            rangos[6] += 1
        elif recurrencias[i] >= 0.7 and recurrencias[i] < 0.8:
            rangos[7] += 1
        elif recurrencias[i] >= 0.8 and recurrencias[i] < 0.9:
            rangos[8] += 1
        elif recurrencias[i] >= 0.9 and recurrencias[i] <= 1:
            rangos[9] += 1
    PEA = 0.0
    L_FOA=list()
    L_POA=list()
    L_PEA=list()
    FOA = 0
    a = 0.0
    for i in range(10):
        a += 0.1
        PEA = PEA + 0.1
        FOA = FOA + rangos[i]
        POA = FOA / (sum(rangos))
        L_POA.append(POA)
        L_FOA.append(FOA)
        L_PEA.append(round(PEA,1))
        PEA_POA[i] = abs(round(PEA - POA, 2))
    return rangos,L_FOA,L_POA,L_PEA,PEA_POA

def kolmogorov_congruente(x,a,c,m):
    rangos = [0] * 10
    DM_critico = 0.043
    PEA_POA = [0] * 10
    recurrencias,min=generador_congruente(x,a,c,m)
    recurrencias.pop()
    for i in range(len(recurrencias)):
        if recurrencias[i] >= 0 and recurrencias[i] < 0.1:
            rangos[0] += 1
        elif recurrencias[i] >= 0.1 and recurrencias[i] < 0.2:
            rangos[1] += 1
        elif recurrencias[i] >= 0.2 and recurrencias[i] < 0.3:
            rangos[2] += 1
        elif recurrencias[i] >= 0.3 and recurrencias[i] < 0.4:
            rangos[3] += 1
        elif recurrencias[i] >= 0.4 and recurrencias[i] < 0.5:
            rangos[4] += 1
        elif recurrencias[i] >= 0.5 and recurrencias[i] < 0.6:
            rangos[5] += 1
        elif recurrencias[i] >= 0.6 and recurrencias[i] < 0.7:
            rangos[6] += 1
        elif recurrencias[i] >= 0.7 and recurrencias[i] < 0.8:
            rangos[7] += 1
        elif recurrencias[i] >= 0.8 and recurrencias[i] < 0.9:
            rangos[8] += 1
        elif recurrencias[i] >= 0.9 and recurrencias[i] <= 1:
            rangos[9] += 1
    PEA = 0.0
    L_FOA=list()
    L_POA=list()
    L_PEA=list()
    FOA = 0
    a = 0.0
    for i in range(10):
        a += 0.1
        PEA = PEA + 0.1
        FOA = FOA + rangos[i]
        POA = FOA / (sum(rangos))
        L_POA.append(POA)
        L_FOA.append(FOA)
        L_PEA.append(round(PEA,1))
        PEA_POA[i] = abs(round(PEA - POA, 2))
    return rangos,L_FOA,L_POA,L_PEA,PEA_POA

def kolmogorov_lenguaje(m):      
    rangos = [0] * 10
    DM_critico = 0.043
    PEA_POA = [0] * 10
    recurrencias,min=generador_lenguaje(m)
    recurrencias.pop()
    for i in range(len(recurrencias)):
        if recurrencias[i] >= 0 and recurrencias[i] < 0.1:
            rangos[0] += 1
        elif recurrencias[i] >= 0.1 and recurrencias[i] < 0.2:
            rangos[1] += 1
        elif recurrencias[i] >= 0.2 and recurrencias[i] < 0.3:
            rangos[2] += 1
        elif recurrencias[i] >= 0.3 and recurrencias[i] < 0.4:
            rangos[3] += 1
        elif recurrencias[i] >= 0.4 and recurrencias[i] < 0.5:
            rangos[4] += 1
        elif recurrencias[i] >= 0.5 and recurrencias[i] < 0.6:
            rangos[5] += 1
        elif recurrencias[i] >= 0.6 and recurrencias[i] < 0.7:
            rangos[6] += 1
        elif recurrencias[i] >= 0.7 and recurrencias[i] < 0.8:
            rangos[7] += 1
        elif recurrencias[i] >= 0.8 and recurrencias[i] < 0.9:
            rangos[8] += 1
        elif recurrencias[i] >= 0.9 and recurrencias[i] <= 1:
            rangos[9] += 1
    PEA = 0.0
    L_FOA=list()
    L_POA=list()
    L_PEA=list()
    FOA = 0
    a = 0.0
    for i in range(10):
        a += 0.1
        PEA = PEA + 0.1
        FOA = FOA + rangos[i]
        POA = FOA / (sum(rangos))
        L_POA.append(POA)
        L_FOA.append(FOA)
        L_PEA.append(round(PEA,1))
        PEA_POA[i] = abs(round(PEA - POA, 2))
    return rangos,L_FOA,L_POA,L_PEA,PEA_POA