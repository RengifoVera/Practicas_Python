from minimos import generador_minimo
from congruente import generador_congruente
from randoom import generador_lenguaje

def chi_cuadrado(x,a,m,d):
    chi_critico = 16.92
    FE=0
    chi_calculado=0
    rangos=[0]*10
    recurrencias,min=generador_minimo(x,a,m,d)
    #recurrencias,min=generador_minimo(5,106,6075)
    recurrencias.pop() 
    FE=round((len(recurrencias))/10)
    for i in range(len(recurrencias)):
        if recurrencias[i]>=0 and recurrencias[i]<0.1:
            rangos[0]+=1
        elif recurrencias[i]>=0.1 and recurrencias[i]<0.2:
            rangos[1]+=1
        elif recurrencias[i]>=0.2 and recurrencias[i]<0.3:
            rangos[2]+=1
        elif recurrencias[i]>=0.3 and recurrencias[i]<0.4:
            rangos[3]+=1
        elif recurrencias[i]>=0.4 and recurrencias[i]<0.5:
            rangos[4]+=1
        elif recurrencias[i]>=0.5 and recurrencias[i]<0.6:
            rangos[5]+=1
        elif recurrencias[i]>=0.6 and recurrencias[i]<0.7:
            rangos[6]+=1
        elif recurrencias[i]>=0.7 and recurrencias[i]<0.8:
            rangos[7]+=1
        elif recurrencias[i]>=0.8 and recurrencias[i]<0.9:
            rangos[8]+=1
        elif recurrencias[i]>=0.9 and recurrencias[i]<=1:
            rangos[9]+=1
    a = 0
    for i in range(len(rangos)):
        a += 0.1
        return rangos,FE

    
def chi_cuadrado_congruente(x,a,c,m):
    chi_critico = 16.92
    FE=0
    chi_calculado=0
    rangos=[0]*10
    recurrencias,min=generador_congruente(x,a,c,m)
    #recurrencias,min=generador_minimo(5,106,6075)
    recurrencias.pop() 
    FE=round((len(recurrencias))/10)
    for i in range(len(recurrencias)):
        if recurrencias[i]>=0 and recurrencias[i]<0.1:
            rangos[0]+=1
        elif recurrencias[i]>=0.1 and recurrencias[i]<0.2:
            rangos[1]+=1
        elif recurrencias[i]>=0.2 and recurrencias[i]<0.3:
            rangos[2]+=1
        elif recurrencias[i]>=0.3 and recurrencias[i]<0.4:
            rangos[3]+=1
        elif recurrencias[i]>=0.4 and recurrencias[i]<0.5:
            rangos[4]+=1
        elif recurrencias[i]>=0.5 and recurrencias[i]<0.6:
            rangos[5]+=1
        elif recurrencias[i]>=0.6 and recurrencias[i]<0.7:
            rangos[6]+=1
        elif recurrencias[i]>=0.7 and recurrencias[i]<0.8:
            rangos[7]+=1
        elif recurrencias[i]>=0.8 and recurrencias[i]<0.9:
            rangos[8]+=1
        elif recurrencias[i]>=0.9 and recurrencias[i]<=1:
            rangos[9]+=1
    a = 0
    for i in range(len(rangos)):
        a += 0.1
        return rangos,FE



def chi_cuadrado_random(m):
    chi_critico = 16.92
    FE=0
    chi_calculado=0
    rangos=[0]*10
    recurrencias,min=generador_lenguaje(m)
    recurrencias.pop() 
    FE=round((len(recurrencias))/10)
    for i in range(len(recurrencias)):
        if recurrencias[i]>=0 and recurrencias[i]<0.1:
            rangos[0]+=1
        elif recurrencias[i]>=0.1 and recurrencias[i]<0.2:
            rangos[1]+=1
        elif recurrencias[i]>=0.2 and recurrencias[i]<0.3:
            rangos[2]+=1
        elif recurrencias[i]>=0.3 and recurrencias[i]<0.4:
            rangos[3]+=1
        elif recurrencias[i]>=0.4 and recurrencias[i]<0.5:
            rangos[4]+=1
        elif recurrencias[i]>=0.5 and recurrencias[i]<0.6:
            rangos[5]+=1
        elif recurrencias[i]>=0.6 and recurrencias[i]<0.7:
            rangos[6]+=1
        elif recurrencias[i]>=0.7 and recurrencias[i]<0.8:
            rangos[7]+=1
        elif recurrencias[i]>=0.8 and recurrencias[i]<0.9:
            rangos[8]+=1
        elif recurrencias[i]>=0.9 and recurrencias[i]<=1:
            rangos[9]+=1
    a = 0
    for i in range(len(rangos)):
        a += 0.1
        return rangos,FE



