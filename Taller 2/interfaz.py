from tkinter import Entry, Label, LabelFrame, Tk,Button,N, font


root=Tk()

root.title("Interfaz Grafica")
root.geometry('1030x500')

#GUI GENERADORES PSEUDOALEATORIOS
frame_inicio=LabelFrame(root,text="Generadores Pseudoaleatorios",font=("Arial"),height=10,labelanchor=N)
frame_inicio.pack()
frame_inicio.place(x=30,y=30)

Label(frame_inicio,text="Nombre De Archivo Leer: ",font=("Arial")).grid(row=3,column=0)

entra_nombre=Entry(frame_inicio,width=30)
entra_nombre.grid(row=3,column=1)

btn_congruente=Button(frame_inicio,text="Generador\nCongruente",width=17,height=2,font=("Arial",12),command=lambda:congruente()).grid(row=3,column=4,padx=10,pady=20)
btn_minimo=Button(frame_inicio,text="Generador\n Minimo Estandar",width=17,height=2,font=("Arial",12),command=lambda:minimo()).grid(row=3,column=5,padx=10,pady=20)
btn_congruente=Button(frame_inicio,text="Generador\n Random.py",width=17,height=2,font=("Arial",12),command=lambda:minimo()).grid(row=3,column=6,padx=10,pady=20)


#funciones generadores

def congruente():
    root=Tk()
    root.title("Generador Congruente")
    root.geometry('500x300')
    btn_salir=Button(root,text="Salir",width=15,height=2,command=lambda:salir())
    btn_salir.pack(side='bottom')
    def salir():
        root.destroy()
    root.mainloop()


def minimo():
    root=Tk()
    root.title("Generador Minimo")
    root.geometry('500x300')
    btn_salir=Button(root,text="Salir",width=15,height=2,command=lambda:salir())
    btn_salir.pack(side='bottom')
    def salir():
        root.destroy()
    root.mainloop()

def random():
    root=Tk()
    root.title("Generador Random")
    root.geometry('500x300')
    btn_salir=Button(root,text="Salir",width=15,height=2,command=lambda:salir())
    btn_salir.pack(side='bottom')
    def salir():
        root.destroy()
    root.mainloop()


#GUI PRUEBAS DE UNIFORMIDAD E INDEPENDENCIA 

frame_pruebas=LabelFrame(root,text="Pruebas Uniformidad E Independencia",font=("Arial"),height=10,labelanchor=N)
frame_pruebas.pack()
frame_pruebas.place(x=30,y=150)


entra_nombre=Entry(frame_pruebas,width=30)
entra_nombre.grid(row=3,column=1)


Label(frame_pruebas,text="Nombre De Archivo A Leer: ",font=("Arial",12)).grid(row=3,column=0)

btn_x2=Button(frame_pruebas,text="Prueba χ²",font=('Arial',12),height=2)
btn_x2.grid(row=3,column=2,padx=10)

btn_kolmogorov=Button(frame_pruebas,text="Pruebas De \n Kolmogorov",height=2,font=('Arial',12))
btn_kolmogorov.grid(row=3,column=3,padx=10,pady=20)

btn_corridas=Button(frame_pruebas,text="Pruebas de\n Corridas",font=("Arial",12),height=2)
btn_corridas.grid(row=3,column=4,padx=10,pady=20)

btn_series=Button(frame_pruebas,text="Pruebas de \n Series",font=('Arial',12),height=2)
btn_series.grid(row=3,column=5,padx=10,pady=20)

btn_poker=Button(frame_pruebas,text='Pruebas de \n Poker',font=('Arial',12),height=2)
btn_poker.grid(row=3,column=6,padx=10,pady=20)































btn_salir=Button(root,text="SALIR",bd=3,width=15,height=2,bg="khaki",command=lambda:salir())
btn_salir.pack(side="bottom")

def salir():
    root.destroy()


root.mainloop()