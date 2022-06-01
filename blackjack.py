# Importa bibliotecas
import pygame
import random

pygame.init()

# Gera a tela principal
largura = 800
altura = 500
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Blackjack')

# Inicia assets
tela_de_fundo = pygame.image.load('assets/img/penup_1654060177597432-1.jpg').convert()
tela_de_fundo_ajustada = pygame.transform.scale(tela_de_fundo, (largura, altura))


largura_ficha = 
altura_ficha = 
ficha = pygame.image.load('').convert()
ficha_ajustada = pygame.transform.scale(ficha, (, ))

largura_carta = pygame.image.load('').convert()
altura_carta = pygame.image.load('').convert()
a_ouros = pygame.image.load('assets/img/cartas/ace_of_diamonds.png').convert()
a_espadas = pygame.image.load('assets/img/cartas/ace_of_spades.png').convert() 
a_paus = pygame.image.load('assets/img/cartas/ace_of_clubs.png').convert()
a_copas = pygame.image.load('assets/img/cartas/ace_of_hearts.png').convert()
dois_ouros = pygame.image.load('assets/img/cartas/2_of_diamonds.png').convert()
dois_espadas = pygame.image.load('assets/img/cartas/2_of_spades.png').convert()
dois_paus = pygame.image.load('assets/img/cartas/2_of_clubs.png').convert()
dois_copas = pygame.image.load('assets/img/cartas/2_of_hearts.png').convert()
tres_ouros = pygame.image.load('assets/img/cartas/3_of_diamonds.png').convert()
tres_espadas = pygame.image.load('assets/img/cartas/3_of_spades.png').convert()
tres_paus = pygame.image.load('assets/img/cartas/3_of_clubs.png').convert()
tres_copas = pygame.image.load('assets/img/cartas/3_of_hearts.png').convert()
quatro_ouros = pygame.image.load('assets/img/cartas/4_of_diamonds.png').convert()
quatro_espadas = pygame.image.load('assets/img/cartas/4_of_spades.png').convert()
quatro_paus = pygame.image.load('assets/img/cartas/4_of_clubs.png').convert()
quatro_copas = pygame.image.load('assets/img/cartas/4_of_hearts.png').convert()
cinco_ouros = pygame.image.load('assets/img/cartas/5_of_diamonds.png').convert()
cinco_espadas = pygame.image.load('assets/img/cartas/5_of_spades.png').convert()
cinco_paus = pygame.image.load('assets/img/cartas/5_of_clubs.png').convert()
cinco_copas = pygame.image.load('assets/img/cartas/5_of_hearts.png').convert()
seis_ouros = pygame.image.load('assets/img/cartas/6_of_diamonds.png').convert()
seis_espadas = pygame.image.load('assets/img/cartas/6_of_spades.png').convert()
seis_paus = pygame.image.load('assets/img/cartas/6_of_clubs.png').convert()
seis_copas = pygame.image.load('assets/img/cartas/6_of_hearts.png').convert()
sete_ouros = pygame.image.load('assets/img/cartas/7_of_diamonds.png').convert()
sete_espadas = pygame.image.load('assets/img/cartas/7_of_spades.png').convert()
sete_paus = pygame.image.load('assets/img/cartas/7_of_clubs.png').convert()
sete_copas = pygame.image.load('assets/img/cartas/7_of_hearts.png').convert()
oito_ouros = pygame.image.load('assets/img/cartas/').convert()
oito_espadas = pygame.image.load('assets/img/cartas/').convert()
oito_paus = pygame.image.load('assets/img/cartas/').convert()
oito_copas = pygame.image.load('assets/img/cartas/').convert()
nove_ouros = pygame.image.load('assets/img/cartas/').convert()
nove_espadas = pygame.image.load('assets/img/cartas/').convert()
nove_paus = pygame.image.load('assets/img/cartas/').convert()
nove_copas = pygame.image.load('assets/img/cartas/').convert()
dez_ouros = pygame.image.load('assets/img/cartas/').convert()
dez_espadas = pygame.image.load('assets/img/cartas/').convert()
dez_paus = pygame.image.load('assets/img/cartas/').convert()
dez_copas = pygame.image.load('assets/img/cartas/').convert()
j_ouros = pygame.image.load('assets/img/cartas/').convert()
j_espadas = pygame.image.load('assets/img/cartas/').convert()
j_paus = pygame.image.load('assets/img/cartas/').convert()
j_copas = pygame.image.load('assets/img/cartas/').convert()
q_ouros = pygame.image.load('assets/img/cartas/').convert()
q_espadas = pygame.image.load('assets/img/cartas/').convert()
q_paus = pygame.image.load('assets/img/cartas/').convert()
q_copas = pygame.image.load('assets/img/cartas/').convert()
k_ouros = pygame.image.load('assets/img/cartas/').convert()
k_espadas = pygame.image.load('assets/img/cartas/').convert()
k_paus = pygame.image.load('assets/img/cartas/').convert()
k_copas = pygame.image.load('assets/img/cartas/').convert()


# Inicia estruturas de dados
lista_cartas = [a_ouros, a_espadas, a_paus, a_copas, dois_ouros, dois_espadas, dois_paus, dois_copas, tres_ouros, tres_espadas, tres_paus, tres_copas, quatro_ouros, quatro_espadas, quatro_paus, quatro_copas, cinco_ouros, cinco_espadas, cinco_paus, cinco_copas, seis_ouros, seis_espadas, seis_paus, seis_copas, sete_ouros, sete_espadas, sete_paus, sete_copas, oito_ouros, oito_espadas, oito_paus, oito_copas, nove_ouros, nove_espadas, nove_paus, nove_copas, dez_ouros, dez_espadas, dez_paus, dez_copas, j_ouros, j_espadas, j_paus, j_copas, q_ouros, q_espadas, q_paus, q_copas, k_ouros, k_espadas, k_paus, k_copas]
dicionario = {dois_ouros: 2, dois_espadas:2, dois_paus:2, dois_copas:2, tres_ouros:3, tres_espadas:3, tres_paus:3, tres_copas:3, quatro_ouros:4, quatro_espadas:4, quatro_paus:4, quatro_copas:4, cinco_ouros:5, cinco_espadas:5, cinco_paus:5, cinco_copas:5, seis_ouros:6, seis_espadas:6, seis_paus:6, seis_copas:6, sete_ouros:7, sete_espadas:7, sete_paus:7, sete_copas:7, oito_ouros:8, oito_espadas:8, oito_paus:8, oito_copas:8, nove_ouros:9, nove_espadas:9, nove_paus:9, nove_copas:9, dez_ouros:10, dez_espadas:10, dez_paus:10, dez_copas:10, j_ouros:10, j_espadas:10, j_paus:10, j_copas:10, q_ouros:10, q_espadas:10, q_paus:10, q_copas:10, k_ouros:10, k_espadas:10, k_paus:10, k_copas:10}


class Carta(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

    def uptade(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x == 400 and self.rect.y == 400:
            self.speedx = 0
            self.speedy = 0




cartas_player = []
carta1 = Carta(a_ouros,400,400)
cartas_player.append(carta1)

game = True
# Loop principal do jogo
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    janela.fill((255,255,255))
    janela.blit(tela_de_fundo_ajustada, (0,0))

    for carta in cartas_player:
        janela.blit(carta.image,carta.rect)
    
    pygame.display.update()


pygame.quit()


