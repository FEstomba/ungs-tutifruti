from configuracion import *
from principal import *
import math
import random


#Funcion de lectura de archivos
def lectura(nombreArchivo):
    f = open(nombreArchivo + '.txt','r')
    contenido = f.read()
    f.close()
    return limpiarPalabra(contenido).splitlines()

#Esta funcion devuelve una letra al azar de la lista de items.
def unaAlAzar(lista):


 return (random.choice(lista))

# Esta funcion devuelve un puntaje positivo si la palabra que el usuario puso se encuentra
# en la lista del pp, de lo contrario no sumara puntaje.
def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
  palabraLimpia=limpiarPalabra(palabraUsuario)
  if(palabraLimpia!="" and palabraLimpia[0]==letra):
    contador=0
    for itemActual in items:
        if itemActual==item:
            lista=listaDeTodo[contador]
            for palabraActual in lista:
                if palabraActual==palabraLimpia:
                    sonido=pygame.mixer.Sound("Sonidos/correct-ding.wav")
                    sonido.play()

                    return 10

        contador=contador+1
  sonido = pygame.mixer.Sound("Sonidos/chicharra-error-incorrecto.wav")
  sonido.play()
  return 0
#Esta funcion reemplaza los caracteres que poseen mayuscula a minuscula y las vocales que
# tienen tildes o diereis por uno sin nada.
def limpiarPalabra(palabra):
    palabraLimpia=palabra.lower()
    remplazos=(
        ("á","a"),
        ("é","e"),
        ("í","i"),
        ("ó","o"),
        ("ú","u"),
        ("ü","u"),
        ("ï","i"),
    )
    for caracCon,caracSin in remplazos:
        palabraLimpia=palabraLimpia.replace(caracCon,caracSin)
    return palabraLimpia


#Esta funcion devuelve una nueva lista con los items que se encuentran en el pp(programa principal) para poder comparar con los que el usuario puso.
#En caso de no tener palabra para esa letra dentro del pp, devolvera ""(vacio).
def juegaCompu(letraAzar, listaDeTodo):
    palabrasValidas=[]
    for categoria in listaDeTodo:
        palabraEncontrada=""
        for palabra in categoria:
         if letraAzar == palabra[0]:
           palabraEncontrada=palabra
           break
        palabrasValidas.append(palabraEncontrada)
    return palabrasValidas




