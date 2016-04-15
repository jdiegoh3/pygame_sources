import pygame
import random
import sys


ALTO=400
ANCHO=700

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()

class Usuario(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()

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

pajaro=pygame.image.load('bird.png').convert_alpha()
fondo=pygame.image.load('fondo.jpg').convert()
bala=pygame.image.load('bala.png').convert_alpha()

#enemigo=pygame.image.load('alienizq.png').convert_alpha()
ls_enemigos=pygame.sprite.Group()
for i in range(5):
    enemigo = Enemigo('alienizq.png')
    print enemigo.rect
    enemigo.rect.x=random.randrange(ANCHO-enemigo.rect[2])
    enemigo.rect.y=random.randrange(ALTO-enemigo.rect[3])
    ls_enemigos.add(enemigo)

s_bala=pygame.mixer.Sound('laser.wav')
pantalla.blit(fondo,posinif)
pantalla.blit(pajaro,posinip)
ls_enemigos.draw(pantalla)
#pantalla.blit(enemigo,posinie) Como ya enemigo es una clase se debe blitear asi


#pantalla.blit(bala,posinib)
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
    ls_enemigos.draw(pantalla)
    #pantalla.blit(enemigo,posinie)
    if disparo:
        if(posinib[0] < ANCHO):
            posinib[0]+=5
            pantalla.blit(bala,posinib)
            s_bala.play()
        else:
            disparo=False


    pygame.display.flip()
    reloj.tick(60)
