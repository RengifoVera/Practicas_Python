



def prueba_chicuadrado():
    from tkinter import Frame, Tk,ttk,CENTER
    from chi import xcuadrado
    ventana_chi=Tk()
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
    rango_i=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    FO,FE,CHI =xcuadrado()
    records=Tabla_Chi.get_children()
    for elementos in records:
            Tabla_Chi.delete(elementos)
    for i in range(10):
        Tabla_Chi.insert("",0,values=(f"{rango_i[i]}-{rango_i[i+1]} {FO[i]} {FE} {CHI[i]}"))


    ventana_chi.mainloop()

def prueba_kolmogorov():
    from tkinter import Frame, Tk,ttk,CENTER
    from kolmogorov import kolmogorov
    ventana_kolmo=Tk()
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
    rango_i=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    rangos,L_FOA,POA,PEA,PEA_POA=kolmogorov()

    records=Tabla_kolmo.get_children()
    for elementos in records:
            Tabla_kolmo.delete(elementos)
    for i in range(10):
            Tabla_kolmo.insert("",0,values=(f"{rango_i[i]}-{rango_i[i+1]} {rangos[i]} {L_FOA[i]} {POA[i]} {PEA[i]} {PEA_POA[i]}"))


    ventana_kolmo.mainloop()