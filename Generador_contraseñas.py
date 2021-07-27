import random
import string

def Generador_contrasenas():
    #SELECCIONAMOS ALEATORIAMENTE LETRAS MAYUSCULAS DESDE LA A - Z
    letra_mayuscula1= random.choice(string.ascii_uppercase)
    letra_mayuscula2= random.choice(string.ascii_uppercase)
    
    #SELECCIONAMOS ALEATORIAMENTE LETRAS MINUSCULAS DESDE LA A - Z
    letra_minuscula=random.choice(string.ascii_lowercase)
    letra_minuscula2=random.choice(string.ascii_lowercase)

    
    #SELECCIONAMOS ALEATORIAMENTE DIGITOS ENTRE 0 - 9
    digito=random.randrange(0,9)
    digito2=random.randrange(0,9)
    
    #SELECCIONAMOS ALEATORIAMENTE SIGNOS DE PUNTUACION
    puntuacion = random.choice(string.punctuation)
    puntuacion2 = random.choice(string.punctuation)


    # CONCATENAMOS CADA UNO DE LOS CARACTERES Y NUMEROS GENERADOS 
    resultado = letra_mayuscula1 + letra_mayuscula2 + letra_minuscula + letra_minuscula2 + str(digito) + str(digito2) +puntuacion2 + puntuacion
    
    # RETORNAMOS LA CONTRASEÑA CON LOS DATOS GENERADOS
    return  resultado


print( " Tu constraseña segura es : " + Generador_contrasenas())