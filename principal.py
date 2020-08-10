#!/usr/bin/env python3


import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)  # frequency, size, channels, buffersize

    pygame.mixer.init()
    pygame.mixer.music.load('Musica/ChipNDaleMusic.mp3')
    pygame.mixer.music.play(3)

    fondoJuego=pygame.image.load('fondoFrutas.jpg')

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    puntos = 0
    candidata = ""

    abc= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    items=["Nombres","Colores","Frutas y Verduras","Paises","Capitales","Animales"]
    nombres= lectura("nombres")
    colores= lectura("colores")
    frutasYverduras= lectura("frutasYverduras")
    paises= lectura("paises")
    capitales= lectura("capitales")
    animales= lectura("animales")

    listaDeTodo=[nombres,colores,frutasYverduras,paises,capitales,animales]
    #print(colores)
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]
    i=0
    while i < len(items):
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        fps = 3

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)
                        puntos+=sumar
                        palabraUsuario=""
                        i=i+1

        segundos = pygame.time.get_ticks() / 1000

        # limpiar pantalla anterior
        screen.blit(fondoJuego,[0,0])
        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
        else:
            eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundos)
        pygame.display.flip()



    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
