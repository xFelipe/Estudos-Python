import pygame, sys, time, os
from pygame.locals import *

x=50
y=50
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

#Impressao do fundo branco e do arquivo carregado
screen.blit(background, (0,0))
screen.blit(ast_surface,(x,y))
#atualizando tela
pygame.display.flip()







time.sleep(5)
pygame.display.quit()
