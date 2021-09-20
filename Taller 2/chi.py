from minimos import recurrencias
import math

def xcuadrado():
    xcrit=16.92
    lista_resultados=list()
    rango=[0,0,0,0,0,0,0,0,0,0]
    cont=0
    FE=(len(recurrencias)-1)/10
    for u in recurrencias:
        if u >=0 and u < 0.1:
            rango[0]+=1   
        elif u >=0.1 and u < 0.2:
            rango[1]+=1
        elif u >=0.2 and u < 0.3:
            rango[2]+=1
        elif u >=0.3 and u < 0.4:
            rango[3]+=1
        elif u >=0.4 and u < 0.5:
            rango[4]+=1
        elif u >=0.5 and u < 0.6:
            rango[5]+=1
        elif u >=0.6 and u < 0.7:
            rango[6]+=1
        elif u >=0.7 and u < 0.8:
            rango[7]+=1
        elif u >=0.8 and u < 0.9:
            rango[8]+=1
        elif u >=0.9 and u < 1:
            rango[9]+=1
        

    #FORMULA
    lista_xcalculado=list()
    for i in range(len(rango)):
        xcalculado=round(((FE - rango[cont])**2)/FE,3)
        lista_xcalculado.append(xcalculado)
        cont+=1


    return(f"FE: {FE}\nFO : {rango} \n(FE - FO)^2 / FE: {lista_xcalculado}\nXCalculado: {sum(lista_xcalculado)}")






xcuadrado()







        



print(xcuadrado())