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
    if (v1<=79) and (v2<=25):
        x=v1
        y=v2
######FUNÇÃO 3
def nvprint():
    screen.blit(background, (0,0))
    screen.blit(ast_surface,(x,y))
    pygame.display.flip()

######Teste da função 1
def testecoord(ntestes):
    import random
    erro=0
    acerto=0
    global x, y
    for cont in range (ntestes):
        nx = random.randint(-100,100)
        ny = random.randint(-100,100)
        nvcoord(nx,ny)
        #depois tentar usar "|"/"(condição) or (condição)"
        if (x>79) or (x<0) or (y<0) or (y>25):
            print ("x=%i y = %i"%(x, y))
            erro = erro+1
        else:
            acerto = acerto+1
    print ("Certos: %i \nErrados:%i"%(acerto,erro))
            
           
        

    
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
