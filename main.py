import pygame
import sys

ALTO=400
ANCHO=500
blanco=(255,255,255)
#Inicializacion de pantalla
pygame.init()
pantalla=pygame.display.set_mode([ANCHO,ALTO])
pantalla.fill(blanco)

 #Cargando imagenes
posinip=[20,20]
posinif=[0,0]
pajaro=pygame.image.load('bird.png')
#fondo=pygame.image.load('fondo.jpg')
pantalla.blit(pajaro,posinip)
#pantalla.blit(fondo,posinif)
#Obtengo x,y del objeto
marco=pajaro.get_rect()

pygame.display.flip()

terminar=False
while(not terminar):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            terminar=True
