# Importa bibliotecas
import pygame
import random

pygame.init()

# Gera a tela principal
largura = 500
altura = 400
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Blackjack')

# Inicia estruturas de dados
game = True


# Loop principal do jogo
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    janela.fill((255,255,255))

    pygame.display.update()


pygame.quit()


