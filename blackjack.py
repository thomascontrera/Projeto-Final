# Importa bibliotecas
import pygame
import random

pygame.init()

# Gera a tela principal
largura = 500
altura = 400
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Blackjack')

# Inicia assets
tela_de_fundo = pygame.image.load('').convert()
tela_de_fundo_ajustada = pygame.transform.scale(tela_de_fundo, (largura, altura))

largura_ficha = 
altura_ficha = 
ficha = pygame.image.load('').convert()
ficha_ajustada = pygame.transform.scale(ficha, (, ))

largura_carta = 
altura_carta = 
a_ouros =
a_espadas =  
a_paus = 
a_copas = 
dois_ouros = 
dois_espadas = 
dois_paus = 
dois_copas = 
tres_ouros = 
tres_espadas = 
tres_paus = 
tres_copas = 
quatro_ouros = 
quatro_espadas = 
quatro_paus = 
quatro_copas = 
cinco_ouros = 
cinco_espadas = 
cinco_paus = 
cinco_copas = 
seis_ouros = 
seis_espadas = 
seis_paus = 
seis_copas = 
sete_ouros = 
sete_espadas = 
sete_paus = 
sete_copas = 
oito_ouros = 
oito_espadas = 
oito_paus = 
oito_copas = 
nove_ouros = 
nove_espadas = 
nove_paus = 
nove_copas = 
dez_ouros = 
dez_espadas = 
dez_paus = 
dez_copas = 
j_ouros = 
j_espadas = 
j_paus = 
j_copas = 
q_ouros = 
q_espadas = 
q_paus = 
q_copas = 
k_ouros = 
k_espadas = 
k_paus = 
k_copas = 

# Inicia estruturas de dados
lista_cartas = []
dicionario = {}
game = True

# Loop principal do jogo
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    janela.fill((255,255,255))

    pygame.display.update()


pygame.quit()


