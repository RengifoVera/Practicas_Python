
def ahorcado(palabra_buscada):

    palabra_buscada=input("Ingrese Palabra A Buscar: ")

    g_palabra=list()

    g_palabra.append(palabra_buscada)

    intentos=0

    while intentos >= 0:
        palabra_ingresada=input("Ingrese Palabra: ")

        if palabra_ingresada != "".join(g_palabra):
            print("Tu Palabra fue: " + palabra_ingresada)
            intentos+=1
            print("Palabra Inconrrecta llevas " + str(intentos) + " intentos") 
            
        elif palabra_ingresada == "".join(g_palabra):
            print("Tu Palabra fue: " + palabra_ingresada)
            print("Palabra Correcta " + "".join(g_palabra)  )
            break
    

print(ahorcado("hola"))



    
        

