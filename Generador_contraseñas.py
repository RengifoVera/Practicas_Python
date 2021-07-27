import random
import string

def Generador_contrasenas():
    letra_mayuscula1= random.choice(string.ascii_uppercase)
    letra_mayuscula2= random.choice(string.ascii_uppercase)
    letra_minuscula=random.choice(string.ascii_lowercase)
    letra_minuscula2=random.choice(string.ascii_lowercase)
    digito=random.randrange(0,9)
    digito2=random.randrange(0,9)
    puntuacion = random.choice(string.punctuation)
    puntuacion2 = random.choice(string.punctuation)

    resultado = letra_mayuscula1 + letra_mayuscula2 + letra_minuscula + letra_minuscula2 + str(digito) + str(digito2) +puntuacion2 + puntuacion
    return  resultado


print( " Tu constraseña segura es : " + Generador_contrasenas())