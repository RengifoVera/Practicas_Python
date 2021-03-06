from tkinter import Entry, Label, LabelFrame, StringVar, Tk,Button,N, Toplevel, font, ttk, CENTER, END ,messagebox as mb,Frame
from tkinter.constants import CHECKBUTTON, DISABLED, E, NORMAL
from congruente import *
from minimos import generador_minimo
from prueba_corridas import prueba_corrridas_congruente, prueba_corrridas_lenguaje
from randoom import generador_lenguaje

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
entra_m.grid(row=4,column=5,padx=10)

Label(frame_inicio,text="Decimales",font=("Arial",8)).grid(row=5,column=5)
#SELECCION DE DECIMALES
entra_d=ttk.Combobox(frame_inicio,width=20,state='readonly',font=("Arial",12))
entra_d.set("Cantidad Decimales")
decimales=["2","3","5"]
entra_d['values']=decimales
entra_d.grid(row=6,column=5,padx=10)


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
    entra_m.get(),
    entra_d.get()
)).grid(row=3,column=8,padx=15,rowspan=2)


btn_random=Button(frame_inicio,text="Generador\n Random.py",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:generador_len(
    int(entra_m.get())
))
btn_random.grid(row=6,column=8,rowspan=2)


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

entra_tipo=ttk.Combobox(root,width=15,state='readonly',font=("Arial",12))
entra_tipo.set("Ingrese Opcion")
opciones=["Congruente","Minimo","Random.py"]
entra_tipo['values']=opciones
entra_tipo.place(x=460,y=400)

Label(root,text="Elige con cual Generador\nhacer las pruebas" ,font=("Arial",10)).place(x=475,y=350)


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
def generador_min(x,a,m,d):
    
    records=Tabla_resultados.get_children()
    for elementos in records:
            Tabla_resultados.delete(elementos)
            entra_periodo.delete(0,END)
    if entra_x0.get() == ''or entra_a.get()== '' or entra_m.get() == '':
        mb.showerror("ERROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")
    else:
        recurrencias,min=generador_minimo(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
        for i in range(len(recurrencias)-1,-1,-1):
            Tabla_resultados.insert("",0,values=(recurrencias[i],min[i]))
        entra_periodo.insert(0,len(min)-1)
    

#INSERTA DATOS GENERADOR DEL LENGUAJE
def generador_len(m):
    records=Tabla_resultados.get_children()
    for elementos in records:
            Tabla_resultados.delete(elementos)
            entra_periodo.delete(0,END)
    if entra_m.get()=='':
        mb.showerror("ERROR","CAMPOS VACIO O FALTA INGRESAR ALGUN CAMPO")
    else:
        recurrencias,min=generador_lenguaje(entra_m.get())
        for i in range(len(recurrencias)-1,-1,-1):
            Tabla_resultados.insert("",0,values=(recurrencias[i],min[i]))
        entra_periodo.insert(0,len(recurrencias)-1)

#PRUEBAS DE UNIFORMIDAD

#CHICUADRADO
from prueba_chicuadrado import chi_cuadrado,chi_cuadrado_congruente,chi_cuadrado_random
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
    CHI_CRI=19.62

    #ELGIENDO GENERADOR
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
        FO,FE=chi_cuadrado(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
        FO,FE=chi_cuadrado_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
    elif entra_tipo.get()=="Random.py":
        FO,FE=chi_cuadrado_random(int(entra_m.get()))

    #_---------------------_#
    records=Tabla_Chi.get_children()
    for elementos in records:
            Tabla_Chi.delete(elementos)

    #_---------------------_#
    CHI_CAL=0
    for i in range(len(rango_i)-1,-1,-1):
        Tabla_Chi.insert("",0,values=(f"{rango_i[i]}-{round((rango_i[i]+0.1),1)} {FO[i]} {FE} {((FE - FO[i]) ** 2) / FE}"))
        CHI_CAL = CHI_CAL + ((FE - FO[i]) ** 2) / FE

    
    #RESULTADO
   

    if CHI_CAL <= CHI_CRI:
        Label(ventana_chi,text=f"{CHI_CAL} <= {CHI_CRI} se acepta la distribucion U(0,1)").pack(side="bottom")
    else:
        Label(ventana_chi,text="No se acepta la distribucion U(0,1)").pack(side="bottom")

#KOLMOGOROV
from prueba_kolmogorov import kolmogorov, kolmogorov_congruente,kolmogorov_lenguaje
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

    #ELIGIENDO GENERADOR PARA REALIZAR PRUEBAS
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
            rangos,L_FOA,POA,PEA,PEA_POA=kolmogorov(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
            rangos,L_FOA,POA,PEA,PEA_POA=kolmogorov_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
    elif entra_tipo.get()=="Random.py":
            rangos,L_FOA,POA,PEA,PEA_POA=kolmogorov_lenguaje(int(entra_m.get()))

    #RANGO KOLMOGOROV
    rango_i=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    DM_critico = 0.043

    records=Tabla_kolmo.get_children()
    for elementos in records:
            Tabla_kolmo.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
            Tabla_kolmo.insert("",0,values=(f"{rango_i[i]}-{round((rango_i[i]+0.1),1)} {rangos[i]} {L_FOA[i]} {POA[i]} {PEA[i]} {PEA_POA[i]}"))
    


    #CONCLUSIONES RESULTADOS
    if max(PEA_POA) <= DM_critico:
        Label(ventana_kolmo,text=f"{max(PEA_POA)} <= {DM_critico} se acepta la distribucion U(0,1)").pack(side="bottom")
    else:
        Label(ventana_kolmo,text="No se acepta la distribucion U(0,1)").pack(side="bottom")



frame_uniformidad=LabelFrame(root,text="PRUEBAS DE UNIFORMIDAD",font=("Arial",12),labelanchor=N)
frame_uniformidad.pack()
frame_uniformidad.place(x=50,y=320)


btn_chi=Button(frame_uniformidad,text="CHI CUADRADO(X2)",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_chicuadrado())
btn_chi.grid(row=0,column=0,padx=15,pady=15)
btn_kolmo=Button(frame_uniformidad,text="KOLMOGOROV",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_kolmogorov())
btn_kolmo.grid(row=0,column=1,padx=15,pady=15)


#PRUEBAS DE INDEPENDENCIA

#PRUEBA CORRIDAS
from prueba_corridas import prueba_corrridas
def prueba_corrida():
    ventana_corrida=Toplevel()
    ventana_corrida.title("Prueba CORRIDA")
    frame_corrida=Frame(ventana_corrida)
    frame_corrida.pack()
     #ELIGIENDO GENERADOR PARA REALIZAR PRUEBAS
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
        corrida,Z_OBSERVADO=prueba_corrridas(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
        corrida,Z_OBSERVADO=prueba_corrridas_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
    elif entra_tipo.get()=="Random.py":
        corrida,Z_OBSERVADO=prueba_corrridas_lenguaje(int(entra_m.get()))

    Z1 = 1.96
    Z2 = -1.96

    Label(frame_corrida,text="PRUEBA CORRIDA :",font=("Arial",12)).grid(row=0,column=0,padx=15,pady=20)
    Label(frame_corrida,text=corrida,font=("Arial",20),fg="red").grid(row=0,column=1,padx=15,pady=20)

   

    if Z_OBSERVADO >= Z2 and Z_OBSERVADO<= Z1:
        Label(ventana_corrida,text=f"{Z_OBSERVADO} se encuentra en el intervalo [{Z1},{Z2}]").pack(side="bottom")
    else:
        Label(ventana_corrida,text=f"{Z_OBSERVADO} NO se encuentra en el intervalo [{Z1},{Z2}]").pack(side="bottom")


from prueba_series import prueba_series, prueba_series_chicuadrado
#PRUEBA SERIES
def prueba_series_interfaz():
    ventana_series=Toplevel()
    ventana_series.title("Prueba SERIES")
    frame_serie=Frame(ventana_series)
    frame_serie.pack()

    Tabla_serie=ttk.Treeview(frame_serie,columns=[f"{n}" for n in range(0,6)],height=6)
    Tabla_serie.grid(row=0,column=0)

    Tabla_serie.column('#0',width=0,minwidth=0,stretch=False)
    Tabla_serie.column('#1',width=70,minwidth=0,stretch=False)
    Tabla_serie.column('#2',width=70,minwidth=0,stretch=False)
    Tabla_serie.column('#3',width=70,minwidth=0,stretch=False)
    Tabla_serie.column('#4',width=70,minwidth=0,stretch=False)
    Tabla_serie.column('#5',width=70,minwidth=0,stretch=False)
    Tabla_serie.column('#6',width=70,minwidth=0,stretch=False)


    Tabla_serie.heading('#0',text='',anchor=CENTER)
    Tabla_serie.heading('#1',text='',anchor=CENTER)
    Tabla_serie.heading('#2',text='0.2-0.4',anchor=CENTER)
    Tabla_serie.heading('#3',text='0.4-0.6',anchor=CENTER)
    Tabla_serie.heading('#4',text='0.6-0.8',anchor=CENTER)
    Tabla_serie.heading('#5',text='0.8-1',anchor=CENTER)
    Tabla_serie.heading('#6',text='0.8-1',anchor=CENTER)

    
         #ELIGIENDO GENERADOR PARA REALIZAR PRUEBAS
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
        recurrencias,min=generador_minimo(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
        recurrencias,min=generador_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_c.get()),int(entra_m.get()))
    elif entra_tipo.get()=="Random.py":
        recurrencias,min=generador_lenguaje(int(entra_m.get()))


    recurrencias,min=generador_minimo(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))

    rango_i=[0,0.2,0.4,0.6,0.8]
    recurrencias.pop()
    matriz=prueba_series(recurrencias)
    matriz_chicuadrado,suma=prueba_series_chicuadrado(matriz,recurrencias)

    chi_critico=36.42
    records=Tabla_serie.get_children()
    for elementos in records:
            Tabla_serie.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
            Tabla_serie.insert("",0,values=(f"{rango_i[i]}-{round(rango_i[i]+0.2,2)} {matriz_chicuadrado[i]}"))

   
    Label(ventana_series,text=(f"SERIES = {matriz}")).pack(side="bottom")

    if suma <= chi_critico:
        Label(ventana_series,text=(F"{suma} <= {chi_critico} se ACEPTA la hipotesis de indenpendencia")).pack(side="bottom")
    else:
        Label(ventana_series,text=(F"{suma} > {chi_critico} se NO ACEPTA la hipotesis de indenpendencia")).pack(side="bottom")

from prueba_poker3 import prueba_poker, prueba_poker_congruente, prueba_poker_lenguaje
#PRUEBA POKER 3 DECIMALES
def prueba_poker_interfaz():
    ventana_poker=Toplevel()
    ventana_poker.title("Prueba POKER 3 DECIMALES")
    frame_poker=Frame(ventana_poker)
    frame_poker.pack()

    Tabla_poker=ttk.Treeview(frame_poker,columns=[f"{n}" for n in range(0,4)],height=3)
    Tabla_poker.grid(row=0,column=0)

    Tabla_poker.column('#0',width=0,minwidth=0,stretch=False)
    Tabla_poker.column('#1',width=70,minwidth=0,stretch=False)
    Tabla_poker.column('#2',width=70,minwidth=0,stretch=False)
    Tabla_poker.column('#3',width=70,minwidth=0,stretch=False)
    Tabla_poker.column('#4',width=120,minwidth=0,stretch=False)



    Tabla_poker.heading('#0',text='',anchor=CENTER)
    Tabla_poker.heading('#1',text='CLASE',anchor=CENTER)
    Tabla_poker.heading('#2',text='FO',anchor=CENTER)
    Tabla_poker.heading('#3',text='FE',anchor=CENTER)
    Tabla_poker.heading('#4',text='(FE-FO)^2/FE',anchor=CENTER)

    #ELGIENDO GENERADOR
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
        CLASES,FE,FO_FE,CHI_CAL=prueba_poker(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
       CLASES,FE,FO_FE,CHI_CAL=prueba_poker_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_c.get()))
    elif entra_tipo.get()=="Random.py":
        CLASES,FE,FO_FE,CHI_CAL=prueba_poker_lenguaje(int(entra_m.get()))


    rango_i=[1,2,3]
    chi_critico = 5.9915
    records=Tabla_poker.get_children()
    for elementos in records:
            Tabla_poker.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
            Tabla_poker.insert("",0,values=(f"{rango_i[i]} {CLASES[i]} {FE[i]} {FO_FE[i]}"))
    if CHI_CAL <= chi_critico:
        Label(ventana_poker,text=(f"{CHI_CAL} <= {chi_critico} Se ACEPTA LA HIPOTESIS" ),font=('Arial',10)).pack(side="bottom")
    elif CHI_CAL > chi_critico:
        Label(ventana_poker,text=(f"{CHI_CAL} > {chi_critico} NO SE ACEPTA LA HIPOTESIS" ),font=('Arial',10)).pack(side="bottom")

from prueba_poker5 import prueba_poker5, prueba_poker5_congruente,prueba_poker5_lenguaje
#PRUEBA POKER 5 DECIMALES
def prueba_poker_interfaz5():
    ventana_poker5=Toplevel()
    ventana_poker5.title("Prueba POKER 5 DECIMALES")
    frame_poker5=Frame(ventana_poker5)
    frame_poker5.pack()

    Tabla_poker5=ttk.Treeview(frame_poker5,columns=[f"{n}" for n in range(0,5)],height=7)
    Tabla_poker5.grid(row=0,column=0)

    Tabla_poker5.column('#0',width=0,minwidth=0,stretch=False)
    Tabla_poker5.column('#1',width=120,minwidth=0,stretch=False)
    Tabla_poker5.column('#2',width=120,minwidth=0,stretch=False)
    Tabla_poker5.column('#3',width=120,minwidth=0,stretch=False)
    Tabla_poker5.column('#4',width=120,minwidth=0,stretch=False)
    Tabla_poker5.column('#5',width=120,minwidth=0,stretch=False)
    Tabla_poker5.heading('#0',text='',anchor=CENTER)
    Tabla_poker5.heading('#1',text='CLASE',anchor=CENTER)
    Tabla_poker5.heading('#2',text='O(i)',anchor=CENTER)
    Tabla_poker5.heading('#3',text='PROBABILIDAD',anchor=CENTER)
    Tabla_poker5.heading('#4',text='EI',anchor=CENTER)
    Tabla_poker5.heading('#5',text='(FE-FO)^2/FE',anchor=CENTER)

        #ELGIENDO GENERADOR
    if entra_tipo.get()=="Ingrese Opcion":
        mb.showerror("ERROR","INGRESE UN TIPO DE PRUEBA")
    if entra_tipo.get()=="Minimo":
        Oi,PRO,EI,FE_FO,suma=prueba_poker5(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Congruente":
        Oi,PRO,EI,FE_FO,suma=prueba_poker5_congruente(int(entra_x0.get()),int(entra_a.get()),int(entra_m.get()),int(entra_d.get()))
    elif entra_tipo.get()=="Random.py":
        Oi,PRO,EI,FE_FO,suma=prueba_poker5_lenguaje(int(entra_m.get()))

    rango_i=["TD","PAR","2PAR","TP","TERCIA","POKER","QUINTILLA"]
    chi_critico=12.592

    records=Tabla_poker5.get_children()
    for elementos in records:
        Tabla_poker5.delete(elementos)
    for i in range(len(rango_i)-1,-1,-1):
            Tabla_poker5.insert("",0,values=(f"{rango_i[i]} {Oi[i]}  {PRO[i]} {EI[i]} {FE_FO[i]}"))

    if suma<=chi_critico:
        Label(ventana_poker5,text=(f"{suma} <= {chi_critico} se ACEPTA la hipotesis de indenpencia"),font=('Arial',10)).pack(side="bottom")
    else:
        Label(ventana_poker5,text=(f"{suma} > {chi_critico} se RECHAZA la hipotesis de indenpencia"),font=('Arial',10)).pack(side="bottom")

    
    




frame_independencia=LabelFrame(root,text="PRUEBAS DE INDEPENDENCIA",font=("Arial",12),labelanchor=N)
frame_independencia.pack()
frame_independencia.place(x=50,y=450)


btn_corrida=Button(frame_independencia,text="CORRIDA",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_corrida())
btn_corrida.grid(row=0,column=0,padx=15,pady=15)
btn_serie=Button(frame_independencia,text="SERIE",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:prueba_series_interfaz()).grid(row=0,column=1,padx=15,pady=15)
btn_poker=Button(frame_independencia,text="POKER",width=17,height=2,font=("Arial",12),bg="MediumPurple1",command=lambda:seleccion(entra_d.get())).grid(row=1,column=0,padx=15,pady=15)

def seleccion(d):
    if d == "3":
        prueba_poker_interfaz()
    elif d == "5":
        prueba_poker_interfaz5()



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