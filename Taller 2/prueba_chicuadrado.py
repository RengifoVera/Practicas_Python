from minimos import generador_minimo
def chi_cuadrado(x,a,m):
    chi_critico = 16.92
    FE=0
    chi_calculado=0
    rangos=[0]*10
    recurrencias,min=generador_minimo(x,a,m)
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
    for i in range(len(rangos)):
        chi_calculado = chi_calculado + ((FE - rangos[i]) ** 2) / FE

    #print("\n\n{:^20}  {:^20} {:^20} {:^20}".format("RANGO", "FO", "FE", "(FE-FO)^2/FE"))
    a = 0

    for i in range(len(rangos)):
        a += 0.1
        #print("{:^10} {:^0} {:^34} {:^8} {:^30}  ".format(round(a - 0.1, 1), round(a, 1), rangos[i], FE,((FE - rangos[i]) ** 2) / FE))
    
        return rangos,FE


    if chi_calculado <= chi_critico:
        print("\n", " " * 30, chi_calculado, "<=", chi_critico)
        print ("se acepta la distribucion U(0,1)")
    else:
        print ("no se acepta la distribucion U(0,1)")
    



