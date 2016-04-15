import pygame
import random
import sys


ALTO=400
ANCHO=700

blanco=(255,255,255)
#Inicializacion de pantalla
pygame.init()
pantalla=pygame.display.set_mode([ANCHO,ALTO])
pygame.display.set_caption("Nave game v0.1 - [JDH]", 'Spine Runtime')
pantalla.fill(blanco)

 #Cargando imagenes
posinip=[20,20]
posinif=[0,0]
posinib=[100,100]
posinie=[ANCHO-200,100]

ls_todos=pygame.sprite.Group()
mouse_pos=pygame.mouse.get_pos()
pajaro=pygame.image.load('bird.png').convert_alpha()
fondo=pygame.image.load('fondo.jpg').convert()
bala=pygame.image.load('bala.png').convert_alpha()
enemigo=pygame.image.load('alienizq.png').convert_alpha()

s_bala=pygame.mixer.Sound('laser.wav')
pantalla.blit(fondo,posinif)
pantalla.blit(pajaro,posinip)
pantalla.blit(enemigo,posinie)


pantalla.blit(bala,posinib)
pygame.mouse.set_visible(False) #Oculta el puntero del mouse
#Obtengo x,y del objeto
marco=pajaro.get_rect()

pygame.display.flip()
reloj=pygame.time.Clock()
terminar=False
disparo=False

while(not terminar):
    events = pygame.event.get()
    mouse_pos=pygame.mouse.get_pos()
    posinip=[mouse_pos[0],mouse_pos[1]]
    #print pygame.mouse.get_pressed()
    for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            terminar=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print "pulsado"
            disparo=True
            posinib[0]=mouse_pos[0]+90
            posinib[1]=mouse_pos[1]+50

    pantalla.blit(fondo,posinif)
    pantalla.blit(pajaro,posinip)
    pantalla.blit(enemigo,posinie)
    if disparo:
        if(posinib[0] < ANCHO):
            posinib[0]+=5
            pantalla.blit(bala,posinib)
            s_bala.play()
        else:
            disparo=False


    pygame.display.flip()
    reloj.tick(60)
