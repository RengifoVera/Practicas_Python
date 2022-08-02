from tkinter import ANCHOR, W, Button, Frame, Label, Text, Tk, LabelFrame, CENTER, END, Entry, messagebox as mb ,Canvas,E,NE
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
root = Tk()

root.title("Minizic")
# root.resizable(0, 0)

Label(root, text="MI ACADEMIA IMPERIAL", font=('impact', 30)).pack(side="top")

frame_all = Frame(root,highlightbackground="blue")
frame_all.pack(anchor=W)



Label(frame_all, text="Datos Entrada", font=(
    'Segoe UI Black', 15), anchor=W).grid(row=2, column=2)
Label(frame_all, text="Datos Salida", font=(
    'Segoe UI Black', 15)).grid(row=2, column=3)

datos_entrada = Text(frame_all, width=30, height=20)
datos_entrada.grid(row=3, column=2, pady=20, padx=20)

datos_salida = Text(frame_all, width=40, height=20)
datos_salida.grid(row=3, column=3, pady=20, padx=20)


btn_solucionar = Button(frame_all, text="SOLUCIONAR", font=(
    'Impact', 15), width=20, command=lambda: getData())
btn_solucionar.grid(row=4, column=2, pady=20, padx=20)

btn_salir = Button(frame_all, text="SALIR", font=(
    'Impact', 15), width=20, command=lambda:salir())
btn_salir.grid(row=4, column=3, pady=20, padx=20)

def getData():
    datos_salida.delete(1.0,END)
    entrada = datos_entrada.get(1.0, END).split()
    size_square=int(entrada[0])
    num_ciuidades=int(entrada[1])

    lista=entrada[2:]
    
    if int(size_square) <=50:
        #graficando 
        distancias = [lista[i:i + 3] for i in range(0, len(lista), 3)]
        print(distancias)
        df = pd.DataFrame(distancias, columns=["Ciudades", "X", "Y"])
        plt.axis([0,size_square,0,size_square])
        plt.scatter(df["X"], df["Y"])
        plt.title("DONDE PONER MI ACADEMIA IMPERIAL")
        plt.show()

        #mostrando codigo minizic
        #Variable
        variables=(f"var int: x;\nvar int: y;\n")
        #restricciones no negatividad
        restricciones = "constraint x>=0;\nconstraint y >=0;\n"
        #Tamano del cuadrado
        tamanio=(f"constraint x<={size_square};\nconstraint y<={size_square};\n")
        #Funcion Objetivo Minimizar
        funcion= (f"function var int: manhattan(var int:x1,var int:y1,var int:x2,var int: y2)\n=abs(x1 - x2) + abs(y1-y2);\nsolve minimize ")
        #Mostar DATOS
        show= 'output["x=",show(x),"y=",show(y)];'

        datos_salida.insert(1.0,variables)
        datos_salida.insert(END,restricciones)
        datos_salida.insert(END,tamanio)
        datos_salida.insert(END,funcion)
        
        #Datos para operar
        coord=zip(df["X"],df["Y"])
        for i,j in coord:
            ciudades=(f"manhattan({i},{j},x,y) + \n")
            datos_salida.insert(END,ciudades)

        lista=list()

        for i in df["X"]:
            lista.append(i)

            plt.boxplot(i)
            



        print(lista)

        datos_salida.insert(END,show)
    else:
        mb.showwarning("ERROR","El tamaño del cuadrado no puede ser mayor a 50")

    
    
        
def salir ():
    root.destroy()
root.mainloop()

