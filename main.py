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
        self.direccion=0
        self.disparar=random.randrange(100)
    def update(self):
        if(self.rect.x >= (ANCHO-self.rect[2])):
            self.direccion=1
        if(self.rect.x <= (self.rect[2])):
            self.direccion=0
        if (self.direccion == 0):
            self.rect.x+=5
        else:
            self.rect.x-=5
        self.disparar-=1
        if(self.disparar < 0):
            self.disparar=random.randrange(100)

class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.velocidad=5
        self.jugador=1
    def update(self):
        if(self.jugador==1):
            self.rect.x+=self.velocidad
        else:
            self.rect.x-=self.velocidad


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
posinif=[0,0]


ls_todos=pygame.sprite.Group()
ls_bala=pygame.sprite.Group()
ls_enemigos=pygame.sprite.Group()
ls_balase=pygame.sprite.Group()
ls_jugadores=pygame.sprite.Group()

mouse_pos=pygame.mouse.get_pos()

jugador=Jugador('bird.png')
jugador.rect.x=mouse_pos[0]
jugador.rect.y=mouse_pos[1]
ls_todos.add(jugador)
ls_jugadores.add(jugador)

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
puntos=0

while(not terminar):
    events = pygame.event.get()
    mouse_pos=pygame.mouse.get_pos()
    posinip=[mouse_pos[0],mouse_pos[1]]
    tipo = pygame.font.SysFont("monospace", 15)
    blood = tipo.render(("Vida actual: " + str(jugador.vida)),1, blanco)
    point = tipo.render(("Puntos: " + str(puntos)),1, blanco)
    for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            terminar=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print "pulsado"
            bala = Bala('bala.png')
            bala.rect.x=mouse_pos[0]+90
            bala.rect.y=mouse_pos[1]+50
            ls_bala.add(bala)
            ls_todos.add(bala)
            disparo=True


    pantalla.blit(fondo,posinif)
    jugador.rect.x=mouse_pos[0]
    jugador.rect.y=mouse_pos[1]

    for b in ls_bala:
        ls_impactos=pygame.sprite.spritecollide(b,ls_enemigos, True)
        for impacto in ls_impactos:
            ls_bala.remove(b)
            ls_todos.remove(b)
            puntos+=10
            

    ls_choque = pygame.sprite.spritecollide(jugador,ls_enemigos, False)
    for elemento in ls_choque:
        print 'choque'
        jugador.chocar()

    for be in ls_balase:
        impactos=pygame.sprite.spritecollide(be,ls_jugadores, False)
        for imp in impactos:
            jugador.chocar()
            ls_balase.remove(be)
            ls_todos.remove(be)

    pantalla.blit(blood, (0, 0))
    pantalla.blit(point, (0,20))
    ls_todos.draw(pantalla)
    ls_enemigos.draw(pantalla)

    for e in ls_enemigos:
        if(e.disparar == 0):
            balae=Bala('balae.png')
            balae.jugador=0
            balae.rect.x=e.rect.x
            balae.rect.y=e.rect.y
            ls_todos.add(balae)
            ls_balase.add(balae)

    ls_todos.update()
    pygame.display.flip()
    reloj.tick(60)
