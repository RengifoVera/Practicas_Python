from tkinter import Entry, Label, Frame, LabelFrame, StringVar, Tk,Button,N, ttk ,messagebox as mb
from tkinter.constants import ANCHOR, CENTER, END, VERTICAL
from congruente import *
from minimos import *
root=Tk()

root.title("Interfaz Grafica")
root.geometry('1030x1000')

#GUI GENERADORES PSEUDOALEATORIOS
frame_inicio=LabelFrame(root,text="GENERADORES" ,font=("Arial",12),labelanchor=N)
frame_inicio.pack()
frame_inicio.place(x=50,y=50)

Label(frame_inicio,text="Xo",font=("Arial")).grid(row=1,column=4)
entra_x0=Entry(frame_inicio,width=25)
entra_x0.grid(row=2,column=4,padx=10,pady=20)

Label(frame_inicio,text="A",font=("Arial")).grid(row=1,column=5)
entra_a=Entry(frame_inicio,width=25)
entra_a.grid(row=2,column=5,padx=10,pady=20)

Label(frame_inicio,text="C",font=("Arial")).grid(row=3,column=4)
entra_c=Entry(frame_inicio,width=25)
entra_c.grid(row=4,column=4,padx=10,pady=20)

Label(frame_inicio,text="M",font=("Arial")).grid(row=3,column=5)
entra_m=Entry(frame_inicio,width=25)
entra_m.grid(row=4,column=5,padx=10,pady=20)


btn_congruente=Button(frame_inicio,text="Generador\nCongruente",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:generar_con(
    entra_x0.get(),
    entra_a.get(),
    entra_c.get(),
    entra_m.get()
))
btn_congruente.grid(row=1,column=8,padx=15,rowspan=2)

btn_minimo=Button(frame_inicio,text="Generador\n Minimo Estandar",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:generador_min(
    entra_x0.get(),
    entra_a.get(),
    entra_m.get()
)).grid(row=6,column=8)


btn_random=Button(frame_inicio,text="Generador\n Random.py",width=17,height=2,font=("Arial",12),bg="MediumPurple1").grid(row=3,column=8,padx=15,rowspan=2)


#TABLA DE RESULTADOS

Tabla_resultados=ttk.Treeview(root,columns=[f"{n}" for n in range(0,2)],height=25)
Tabla_resultados.place(x=650,y=60)

Tabla_resultados.column('#0',width=1,minwidth=0,stretch=False)

Label(root,text="El Periodo Es:",font=("Arial",12),fg="red").place(x=670,y=600)
entra_periodo=Entry(root)
entra_periodo.place(x=790,y=602)


Tabla_resultados.heading('#0',text='',anchor=CENTER)
Tabla_resultados.heading('#1',text='Recurencia',anchor=CENTER)
Tabla_resultados.heading('#2',text='Resultados',anchor=CENTER)

#SCROLLBAR
vert=ttk.Scrollbar(root,orient="vertical",command=Tabla_resultados.yview)
vert.place(x=1036,y=62,height=520)


#INSERTA DATOS GENERADOR CONGRUENTE
def generar_con(x,a,c,m):
    if entra_x0.get() == ''or entra_a.get()== '' or entra_c.get()== '' or entra_m.get() == '':
        mb.showerror("EROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")
    else:
        recurencia,resultado = generador_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
        for i in range(len(recurencia)):
            Tabla_resultados.insert("",0,values=(recurencia[i],resultado[i]))
        entra_periodo.insert(0,len(recurencia))
        limpiar()


def generador_min(x,a,m):
    if entra_x0.get() == ''or entra_a.get()== '' or entra_m.get() == '':
        mb.showerror("EROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")

    else:
        recurrencias,min=generador_minimo(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()))

        for i in range(len(recurrencias)):
            Tabla_resultados.insert("",0,values=(recurrencias[i],min[i]))
        entra_periodo.insert(0,len(recurrencias))










def limpiar():
    entra_x0.delete(0,END)
    entra_a.delete(0,END)
    entra_c.delete(0,END)
    entra_m.delete(0,END)

































btn_salir=Button(root,text="SALIR",bd=3,width=15,height=2,bg="khaki",command=lambda:salir())
btn_salir.pack(side="bottom")

def salir():
    root.destroy()


root.mainloop()