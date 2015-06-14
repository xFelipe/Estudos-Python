import pygame, sys, time, os
from pygame.locals import *

x=250
y=250

#####FUNÇÃO 1
def resetar():
    global x,y
    
    y=40
    x=40
######FUNÇÃO 2
def nvcoord(v1,v2):
    global x, y
    if x<=79 | y<=25:
        x=v1
        y=v2
######FUNÇÃO 3
def nvprint():
    screen.blit(background, (0,0))
    screen.blit(ast_surface,(x,y))
    pygame.display.flip()

######Teste

    
def teste():
    erro=0
    acerto=0
    for cont in range (10000)
        nx = random.randint(-100,100)
        ny = random.randint(-100,100)
        

    
######Esa função fez respectivamente: Printou o fundo, 
######printou o * na posição, atualizou tela.

#inicia os modulos
pygame.init()

#janela principal
window = pygame.display.set_mode((800,600))


screen = pygame.display.get_surface()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
pygame.display.set_caption("Teste")

#arquivo: Reconhecendo arquivo, reconhecendo imagem
ast = os.path.join("asterisco.jpg")
ast_surface = pygame.image.load(ast)

######Usando função para imprimir X E Y
nvprint()



time.sleep(3)
resetar()
nvprint()


time.sleep(5)
pygame.display.quit()
