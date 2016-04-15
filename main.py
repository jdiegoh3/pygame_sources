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

class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()

class Jugador(pygame.sprite.Sprite):

    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.vida = 100
    def chocar(self):
        self.vida-=10

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
ls_bala=pygame.sprite.Group()
ls_enemigos=pygame.sprite.Group()

mouse_pos=pygame.mouse.get_pos()

jugador=Jugador('bird.png')
jugador.rect.x=mouse_pos[0]
jugador.rect.y=mouse_pos[1]
ls_todos.add(jugador)

fondo=pygame.image.load('fondo.jpg').convert()

for i in range(5):
    enemigo = Enemigo('alienizq.png')
    enemigo.rect.x=random.randrange(ANCHO-enemigo.rect[2])
    enemigo.rect.y=random.randrange(ALTO-enemigo.rect[3])
    ls_enemigos.add(enemigo)
    ls_todos.add(enemigo)

s_bala=pygame.mixer.Sound('laser.wav')
pantalla.blit(fondo,posinif)
ls_todos.draw(pantalla)
ls_enemigos.draw(pantalla)

pygame.mouse.set_visible(False) #Oculta el puntero del mouse

pygame.display.flip()
reloj=pygame.time.Clock()
terminar=False
disparo=False

while(not terminar):
    events = pygame.event.get()
    mouse_pos=pygame.mouse.get_pos()
    posinip=[mouse_pos[0],mouse_pos[1]]

    for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            terminar=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print "pulsado"
            bala = Bala('bala.png')
            bala.rect.x=mouse_pos[0]
            bala.rect.y=mouse_pos[1]+90
            ls_bala.add(bala)
            ls_todos.add(bala)
            disparo=True
            posinib[0]=mouse_pos[0]+90
            posinib[1]=mouse_pos[1]+50

    pantalla.blit(fondo,posinif)
    jugador.rect.x=mouse_pos[0]
    jugador.rect.y=mouse_pos[1]
    ls_choque = pygame.sprite.spritecollide(jugador,ls_enemigos, False)
    for elemento in ls_choque:
        print 'choque'
        jugador.chocar()
        print jugador.vida

    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)
    if disparo:
        if(posinib[0] < ANCHO):
            posinib[0]+=5
            
            s_bala.play()
        else:
            disparo=False


    pygame.display.flip()
    reloj.tick(60)
