from tkinter import Entry, Label, LabelFrame, Tk,Button,N, Toplevel, font, ttk, CENTER, END ,messagebox as mb,Frame
from congruente import *
from minimos import generador_minimo

root=Tk()

root.title("Interfaz Grafica NUMEROS PSEUDOALEATORIOS")
root.geometry('1100x700')

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

btn_limpiar=Button(frame_inicio,text="Limpiar Datos",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:limpiar())
btn_limpiar.grid(row=5,column=4,rowspan=2)

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
)).grid(row=3,column=8,padx=15,rowspan=2)


btn_random=Button(frame_inicio,text="Generador\n Random.py",width=17,height=2,font=("Arial",12),bg="MediumPurple1").grid(row=6,column=8,rowspan=2)


#TABLA DE RESULTADOS GENERADORES

Tabla_resultados=ttk.Treeview(root,columns=[f"{n}" for n in range(0,2)],height=25)
Tabla_resultados.place(x=650,y=60)

Tabla_resultados.column('#0',width=1,minwidth=0,stretch=False)

Label(root,text="El Periodo Es:",font=("Arial",12),fg="red").place(x=670,y=600)
entra_periodo=Entry(root)
entra_periodo.place(x=790,y=602)


Tabla_resultados.heading('#0',text='',anchor=CENTER)
Tabla_resultados.heading('#1',text='Recurencia',anchor=CENTER)
Tabla_resultados.heading('#2',text='Generador',anchor=CENTER)

#SCROLLBAR
vert=ttk.Scrollbar(root,orient="vertical",command=Tabla_resultados.yview)
vert.place(x=1036,y=62,height=520)


#GENERADORES
#INSERTA DATOS GENERADOR CONGRUENTE
def generar_con(x,a,c,m):
    records=Tabla_resultados.get_children()
    for elementos in records:
            Tabla_resultados.delete(elementos)
            entra_periodo.delete(0,END)
    if entra_x0.get() == ''or entra_a.get()== '' or entra_c.get()== '' or entra_m.get() == '':
        mb.showerror("ERROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")
    else:
        recurencia,resultado = generador_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
        for i in range(len(recurencia)-1,-1,-1):
            Tabla_resultados.insert("",0,values=(recurencia[i],resultado[i]))
        entra_periodo.insert(0,len(recurencia)-1)
        #limpiar() 

#INSERTA DATOS GENERADOR MINIMO
def generador_min(x,a,m):
    records=Tabla_resultados.get_children()
    for elementos in records:
            Tabla_resultados.delete(elementos)
            entra_periodo.delete(0,END)
    if entra_x0.get() == ''or entra_a.get()== '' or entra_m.get() == '':
        mb.showerror("ERROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")
    else:
        recurrencias,min=generador_minimo(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()))
        for i in range(len(recurrencias)-1,-1,-1):
            Tabla_resultados.insert("",0,values=(recurrencias[i],min[i]))
        entra_periodo.insert(0,len(recurrencias)-1)
    return recurrencias
    #limpiar()    




#PRUEBAS DE UNIFORMIDAD

#CHICUADRADO
from prueba_chicuadrado import chi_cuadrado
def prueba_chicuadrado():
    
    ventana_chi=Toplevel()
    ventana_chi.title("Prueba Chi Cuadrado (X2)")

    frame_chi=Frame(ventana_chi)
    frame_chi.pack()

    Tabla_Chi=ttk.Treeview(frame_chi,columns=[f"{n}" for n in range(0,4)],height=10)
    Tabla_Chi.grid(row=0,column=0)

    Tabla_Chi.column('#0',width=1,minwidth=0,stretch=False)
    Tabla_Chi.column('#1',width=70,minwidth=0,stretch=False)
    Tabla_Chi.column('#2',width=70,minwidth=0,stretch=False)
    Tabla_Chi.column('#3',width=70,minwidth=0,stretch=False)
    Tabla_Chi.column('#4',width=100,minwidth=0,stretch=False)

    Tabla_Chi.heading('#0',text='',anchor=CENTER)
    Tabla_Chi.heading('#1',text='Rango',anchor=CENTER)
    Tabla_Chi.heading('#2',text='FO',anchor=CENTER)
    Tabla_Chi.heading('#3',text='FE',anchor=CENTER)
    Tabla_Chi.heading('#4',text='(FE-FO)^2 / FE',anchor=CENTER)

    #RANGO
    rango_i=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    FO,FE=chi_cuadrado(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()))
    records=Tabla_Chi.get_children()
    for elementos in records:
            Tabla_Chi.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
        Tabla_Chi.insert("",0,values=(f"{rango_i[i]}-{round((rango_i[i]+0.1),1)} {FO[i]} {FE} {((FE - FO[i]) ** 2) / FE}"))

#KOLMOGOROV
from prueba_kolmogorov import kolmogorov
def prueba_kolmogorov():
    ventana_kolmo=Toplevel()
    ventana_kolmo.title("Prueba KOLMOGOROV")

    frame_kolmo=Frame(ventana_kolmo)
    frame_kolmo.pack()

    Tabla_kolmo=ttk.Treeview(frame_kolmo,columns=[f"{n}" for n in range(0,6)],height=10)
    Tabla_kolmo.grid(row=0,column=0)

    Tabla_kolmo.column('#0',width=1,minwidth=0,stretch=False)
    Tabla_kolmo.column('#1',width=70,minwidth=0,stretch=False)
    Tabla_kolmo.column('#2',width=70,minwidth=0,stretch=False)
    Tabla_kolmo.column('#3',width=70,minwidth=0,stretch=False)
    Tabla_kolmo.column('#4',width=130,minwidth=0,stretch=False)
    Tabla_kolmo.column('#5',width=70,minwidth=0,stretch=False)
    Tabla_kolmo.column('#6',width=100,minwidth=0,stretch=False)

    Tabla_kolmo.heading('#0',text='',anchor=CENTER)
    Tabla_kolmo.heading('#1',text='Rango',anchor=CENTER)
    Tabla_kolmo.heading('#2',text='FO',anchor=CENTER)
    Tabla_kolmo.heading('#3',text='FOA',anchor=CENTER)
    Tabla_kolmo.heading('#4',text='POA',anchor=CENTER)
    Tabla_kolmo.heading('#5',text='PEA',anchor=CENTER)
    Tabla_kolmo.heading('#6',text='|PEA - POA|',anchor=CENTER)


    #RANGO KOLMOGOROV
    rango_i=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    rangos,L_FOA,POA,PEA,PEA_POA=kolmogorov(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()))


    records=Tabla_kolmo.get_children()
    for elementos in records:
            Tabla_kolmo.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
            Tabla_kolmo.insert("",0,values=(f"{rango_i[i]}-{round((rango_i[i]+0.1),1)} {rangos[i]} {L_FOA[i]} {POA[i]} {PEA[i]} {PEA_POA[i]}"))

frame_uniformidad=LabelFrame(root,text="PRUEBAS DE UNIFORMIDAD",font=("Arial",12),labelanchor=N)
frame_uniformidad.pack()
frame_uniformidad.place(x=50,y=300)

#SE ELIGE CON QUE GENERADOR SE DESEA HACER LAS PRUEBAS DE BONDAD

entra_tipo=ttk.Combobox(frame_uniformidad,width=20,state='readonly')
entra_tipo.set("Ingrese Opcion")
opciones=["Congruente","Minimo"]
entra_tipo['values']=opciones
entra_tipo.grid(row=0,column=3,pady=15,padx=15)

btn_chi=Button(frame_uniformidad,text="CHI CUADRADO(X2)",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_chicuadrado())
btn_chi.grid(row=0,column=0,padx=15,pady=15)
btn_kolmo=Button(frame_uniformidad,text="KOLMOGOROV",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_kolmogorov())
btn_kolmo.grid(row=0,column=1,padx=15,pady=15)


#PRUEBAS DE INDEPENDENCIA


def prueba_corrida():
    from prueba_corridas import prueba_corrridas
    ventana_corrida=Toplevel()

    ventana_corrida.title("Prueba CORRIDA")
    frame_corrida=Frame(ventana_corrida)
    frame_corrida.pack()

    corrida=prueba_corrridas(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()))

    Label(frame_corrida,text="PRUEBA CORRIDA :",font=("Arial",12)).grid(row=0,column=0,padx=15,pady=20)
    entra_corrida=Entry(frame_corrida,font=("Arial"),width=100,fg="red")
    entra_corrida.grid(row=0,column=1,padx=15,pady=20)
    print(corrida)
   

    entra_corrida.insert(END,corrida)

    

frame_independencia=LabelFrame(root,text="PRUEBAS DE INDEPENDENCIA",font=("Arial",12),labelanchor=N)
frame_independencia.pack()
frame_independencia.place(x=50,y=420)


btn_corrida=Button(frame_independencia,text="CORRIDA",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_corrida())
btn_corrida.grid(row=0,column=0,padx=15,pady=15)
btn_serie=Button(frame_independencia,text="SERIE",width=17,height=2,font=("Arial",12),bg="MediumPurple1").grid(row=0,column=1,padx=15,pady=15)
btn_poker=Button(frame_independencia,text="POKER",width=17,height=2,font=("Arial",12),bg="MediumPurple1").grid(row=1,column=0,padx=15,pady=15)























btn_salir=Button(root,text="SALIR",bd=3,width=15,height=2,bg="khaki",command=lambda:salir())
btn_salir.pack(side="bottom")
#LIMPIA DATOS DE ENTRADA Y TABLAS DE GENERADORES
def limpiar():
    entra_x0.delete(0,END)
    entra_a.delete(0,END)
    entra_c.delete(0,END)
    entra_m.delete(0,END)
    records=Tabla_resultados.get_children()
    for elementos in records:
            Tabla_resultados.delete(elementos)
            entra_periodo.delete(0,END)

def salir():
    root.destroy()


root.mainloop()