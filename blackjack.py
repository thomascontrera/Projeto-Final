# Importa bibliotecas
import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

# Gera a tela principal
largura = 800
altura = 500
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Blackjack do Pericão')

# Inicia assets

# Imagens
tela_de_fundo = pygame.image.load('assets/img/mesa.jpg').convert()
tela_de_fundo_ajustada = pygame.transform.scale(tela_de_fundo, (largura, altura))

tampa_placar = pygame.image.load('assets/img/tampa placar.jpg').convert()
tampa_placar = pygame.transform.scale(tampa_placar, (150, 50))
tampa_placar_cima = pygame.image.load('assets/img/tampa_placar_cima.jpg').convert()
tampa_placar_cima = pygame.transform.scale(tampa_placar_cima, (150, 50))

carta_back = pygame.image.load('assets/img/cartas/cardback.png').convert()
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
oito_ouros = pygame.image.load('assets/img/cartas/8_of_diamonds.png').convert()
oito_espadas = pygame.image.load('assets/img/cartas/8_of_spades.png').convert()
oito_paus = pygame.image.load('assets/img/cartas/8_of_clubs.png').convert()
oito_copas = pygame.image.load('assets/img/cartas/8_of_hearts.png').convert()
nove_ouros = pygame.image.load('assets/img/cartas/9_of_diamonds.png').convert()
nove_espadas = pygame.image.load('assets/img/cartas/9_of_spades.png').convert()
nove_paus = pygame.image.load('assets/img/cartas/9_of_clubs.png').convert()
nove_copas = pygame.image.load('assets/img/cartas/9_of_hearts.png').convert()
dez_ouros = pygame.image.load('assets/img/cartas/10_of_diamonds.png').convert()
dez_espadas = pygame.image.load('assets/img/cartas/10_of_spades.png').convert()
dez_paus = pygame.image.load('assets/img/cartas/10_of_clubs.png').convert()
dez_copas = pygame.image.load('assets/img/cartas/10_of_hearts.png').convert()
j_ouros = pygame.image.load('assets/img/cartas/jack_of_diamonds.png').convert()
j_espadas = pygame.image.load('assets/img/cartas/jack_of_spades.png').convert()
j_paus = pygame.image.load('assets/img/cartas/jack_of_clubs.png').convert()
j_copas = pygame.image.load('assets/img/cartas/jack_of_hearts.png').convert()
q_ouros = pygame.image.load('assets/img/cartas/queen_of_diamonds.png').convert()
q_espadas = pygame.image.load('assets/img/cartas/queen_of_spades.png').convert()
q_paus = pygame.image.load('assets/img/cartas/queen_of_clubs.png').convert()
q_copas = pygame.image.load('assets/img/cartas/queen_of_hearts.png').convert()
k_ouros = pygame.image.load('assets/img/cartas/king_of_diamonds.png').convert()
k_espadas = pygame.image.load('assets/img/cartas/jack_of_spades.png').convert()
k_paus = pygame.image.load('assets/img/cartas/king_of_clubs.png').convert()
k_copas = pygame.image.load('assets/img/cartas/king_of_hearts.png').convert()

largura_botao = 100
altura_botao = 60
botao_comprar = pygame.image.load('assets/img/botao_comprar.jpg').convert()
botao_comprar = pygame.transform.scale(botao_comprar, (largura_botao, altura_botao))
botao_segurar = pygame.image.load('assets/img/botao_segurar.jpg').convert()
botao_segurar = pygame.transform.scale(botao_segurar, (largura_botao, altura_botao))


pericles_neutro = pygame.image.load('assets/img/pericles_empate.jpg').convert()
pericles_neutro = pygame.transform.scale(pericles_neutro, (largura, altura))

pericles_inicio = pygame.image.load('assets/img/pericles_inicio.jpg').convert()
pericles_inicio = pygame.transform.scale(pericles_inicio, (500,500))

pericles_triste = pygame.image.load('assets/img/pericles_triste.jpeg').convert()
pericles_triste = pygame.transform.scale(pericles_triste, (largura, altura))

pericles_feliz = pygame.image.load('assets/img/pericles_vitoria.jpg').convert()
pericles_feliz = pygame.transform.scale(pericles_feliz, (largura,altura))


# Cor
branco = (250,250,250)
vermelho = (250, 0, 0)
verde = (0,250,0)
preto = (0,0,0)

# Fontes
fonte_mini = pygame.font.Font('assets/font/radiant-beauty-regular.ttf',60)
fonte_pequena = pygame.font.Font('assets/font/radiant-beauty-regular.ttf',60)
fonte_placar = pygame.font.Font('assets/font/BOBCAT.TTF',40)
fonte = pygame.font.Font('assets/font/Raphtalia Personal Use.ttf',50)

# Textos
bem_vindo = fonte.render('Bem Vindo ao', True, preto)

blackjack = fonte.render('BLACKJACK', True, vermelho)
perao = fonte.render('DO PERÃO', True, vermelho)

jogar = fonte_pequena.render('para jogar', True, preto)
clique = fonte_pequena.render('clique no', True, preto)
pericao = fonte_pequena.render('pericão', True, preto)

# Sons
largarofreio = pygame.mixer.Sound('assets/áudio/Se_eu_largar_o_freio (online-audio-converter.com).mp3')
uhul = pygame.mixer.Sound('assets/áudio/Uhul _Zé_Roberto (online-audio-converter.com).mp3')
mary = pygame.mixer.Sound('assets/áudio/Água_coca_latao (online-audio-converter.com).mp3')
rapaiz = pygame.mixer.Sound('assets/áudio/Rapaz _Xaropinho (online-audio-converter.com).mp3')



# Lista de cartas e dicionário de pontuação
lista_cartas = [a_ouros, a_espadas, a_paus, a_copas, dois_ouros, dois_espadas, dois_paus, dois_copas, tres_ouros, tres_espadas, tres_paus, tres_copas, quatro_ouros, quatro_espadas, quatro_paus, quatro_copas, cinco_ouros, cinco_espadas, cinco_paus, cinco_copas, seis_ouros, seis_espadas, seis_paus, seis_copas, sete_ouros, sete_espadas, sete_paus, sete_copas, oito_ouros, oito_espadas, oito_paus, oito_copas, nove_ouros, nove_espadas, nove_paus, nove_copas, dez_ouros, dez_espadas, dez_paus, dez_copas, j_ouros, j_espadas, j_paus, j_copas, q_ouros, q_espadas, q_paus, q_copas, k_ouros, k_espadas, k_paus, k_copas]
dicionario = {dois_ouros: 2, dois_espadas:2, dois_paus:2, dois_copas:2, tres_ouros:3, tres_espadas:3, tres_paus:3, tres_copas:3, quatro_ouros:4, quatro_espadas:4, quatro_paus:4, quatro_copas:4, cinco_ouros:5, cinco_espadas:5, cinco_paus:5, cinco_copas:5, seis_ouros:6, seis_espadas:6, seis_paus:6, seis_copas:6, sete_ouros:7, sete_espadas:7, sete_paus:7, sete_copas:7, oito_ouros:8, oito_espadas:8, oito_paus:8, oito_copas:8, nove_ouros:9, nove_espadas:9, nove_paus:9, nove_copas:9, dez_ouros:10, dez_espadas:10, dez_paus:10, dez_copas:10, j_ouros:10, j_espadas:10, j_paus:10, j_copas:10, q_ouros:10, q_espadas:10, q_paus:10, q_copas:10, k_ouros:10, k_espadas:10, k_paus:10, k_copas:10}

game = False
jogo_rolando = True
while jogo_rolando:
    largarofreio.play()
    # Completa a janela com branco
    janela.fill((250,250,250))

    # Desenha a imagem do Péricles
    janela.blit(pericles_inicio, (150,0))

    # Escreve os textos da tela inicial
    janela.blit(bem_vindo, (25,80))

    janela.blit(blackjack, (30,140))
    janela.blit(perao, (40,190))

    janela.blit(jogar, (600,180))
    janela.blit(clique, (600,220))
    janela.blit(pericao, (600,260))

    # Inicializa mouse
    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_rolando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 250 <= mouse[0] <= 550 and 30 <= mouse[1] <= 500:
                game = True
                largarofreio.stop()

    # Classe de carta
    class Carta(pygame.sprite.Sprite):
        def __init__(self,img,x,y,delay=0.6):
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = 0
            self.speedy = 0
            self.delay = delay
            self.tempocriacao = time.time()
            self.exibir = False

        def update(self):
            
            t = time.time()
            if t - self.tempocriacao > self.delay:
                self.exibir = True
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            if self.rect.x == 400 and self.rect.y == 400:
                self.speedx = 0
                self.speedy = 0

    # Classe de placar
    class Placar(pygame.sprite.Sprite):
        def __init__(self,txt,x,y,delay=0.6):
            pygame.sprite.Sprite.__init__(self)

            self.text = txt
            self.rect = self.text.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = 0
            self.speedy = 0
            self.delay = delay
            self.tempocriacao = time.time()
            self.exibir = False

        def update(self):
            
            t = time.time()
            if t - self.tempocriacao > self.delay:
                self.exibir = True
            self.rect.x += self.speedx
            self.rect.y += self.speedy


    # Variáveis iniciais
    cartas = []  # Lista que armazena todas as cartas que saem do baralho
    pp = []  # Lista que armazena a pontuação do jogador a cada carta que sai do baralho
    pm = []  # Lista que armazena a pontuação da mesa a cada carta que sai do baralho

    posicao_player = 370
    posicao_mesa = 370

    pontuacao_player1 = 0
    pontuacao_player2 = 0
    pontuacao_mesa1 = 0
    pontuacao_mesa2 = 0

    delay = 0

    jogo_inicial = True
    jogada_player = True
    jogo_fim = False
    estouro = False
    vitoria = False
    derrota = False
    empate = False

    i=0
    
    # Loop principal do jogo
    while game:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game = False
                jogo_rolando= False

            if jogo_inicial == True:  # Enquanto os primeiros sorteios ocorrem
                
                # Sorteia a carta 1 do jogador e adiciona na lista 'cartas'
                c1_player = random.choice(lista_cartas)
                if c1_player in dicionario.keys():
                    pontuacao_player1 += dicionario[c1_player]  
                    pontuacao_player2 += dicionario[c1_player]
                else:  
                    pontuacao_player1 += 1
                    pontuacao_player2 += 11

                if pontuacao_player1 == pontuacao_player2:
                    pontuacaojogador = fonte_placar.render(str(pontuacao_player1), True, branco)
                    pontuacaojogador = Placar(pontuacaojogador,525,325,0.3)
                else:
                    pontuacaojogador = fonte_placar.render('{} ou {}'.format(pontuacao_player1, pontuacao_player2), True, branco)
                    pontuacaojogador = Placar(pontuacaojogador,525,325,0.3)

                pp.append(pontuacaojogador)
                
                c1_player = Carta(c1_player,350,300,0.3) 
                cartas.append(c1_player)
                
                # Sorteia a carta 1 da mesa e adiciona na lista 'cartas'
                c1_mesa = random.choice(lista_cartas)
                if c1_mesa in dicionario.keys():
                    pontuacao_mesa1 += dicionario[c1_mesa]
                    pontuacao_mesa2 += dicionario[c1_mesa]
                else:
                    pontuacao_mesa1 += 1
                    pontuacao_mesa2 += 11
                
                if pontuacao_mesa1 == pontuacao_mesa2:
                    pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                    pontuacaomesa = Placar(pontuacaomesa,525,100,0.6)
                else:
                    pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                    pontuacaomesa = Placar(pontuacaomesa,525,100,0.6)

                pm.append(pontuacaomesa)
                
                c1_mesa = Carta(c1_mesa,350,100,0.6)    
                cartas.append(c1_mesa)

                # Sorteia a carta 2 do jogador e adiciona na lista 'cartas'
                c2_player = random.choice(lista_cartas)
                if c2_player in dicionario.keys():
                    pontuacao_player1 += dicionario[c2_player]  
                    pontuacao_player2 += dicionario[c2_player]
                else:  
                    pontuacao_player1 += 1
                    pontuacao_player2 += 11
                
                if pontuacao_player1 == pontuacao_player2:
                    pontuacaojogador = fonte_placar.render(str(pontuacao_player1), True, branco)
                    pontuacaojogador = Placar(pontuacaojogador,525,325,0.9)
                else:
                    pontuacaojogador = fonte_placar.render('{} ou {}'.format(pontuacao_player1, pontuacao_player2), True, branco)
                    pontuacaojogador = Placar(pontuacaojogador,525,325,0.9)

                pp.append(pontuacaojogador)
                
                c2_player = Carta(c2_player,370,300,0.9) 
                cartas.append(c2_player)
            
                # Adiciona uma carta virada na lista 'cartas'
                c2_mesa_escuro = Carta(carta_back,370,100,1.2)  
                cartas.append(c2_mesa_escuro)

                jogo_inicial = False  # Aconteceram os primeiros sorteios

            if event.type == pygame.MOUSEBUTTONDOWN:
                if i < 1:  # Uma vez que clicou o segurar, não é possível comprar e segurar mais
                    if 100 <= mouse[0] <= 100+largura_botao and 250 <= mouse[1] <= 250+altura_botao:  # Clique no botão de comprar
                        posicao_player += 20
                        delay = 0.4
                        extra_player = random.choice(lista_cartas)
                        if extra_player in dicionario.keys():
                            pontuacao_player1 += dicionario[extra_player]  
                            pontuacao_player2 += dicionario[extra_player]
                        else:
                            if pontuacao_player1 <= 10 and pontuacao_player2 <= 10:
                                pontuacao_player1 += 1
                                pontuacao_player2 += 11
                            elif pontuacao_player1 > 10 and pontuacao_player2 > 10:
                                pontuacao_player1 += 1
                                pontuacao_player2 += 1
                            elif pontuacao_player1 <= 10 and pontuacao_player2 > 10:
                                pontuacao_player1 += 1
                                pontuacao_player2 += 1  

                        if pontuacao_player1 == pontuacao_player2:
                            pontuacaojogador = fonte_placar.render(str(pontuacao_player1), True, branco)
                            pontuacaojogador = Placar(pontuacaojogador,525,325,delay)
                        else:
                            if pontuacao_player2 <= 21 and pontuacao_player1 <= 21:
                                pontuacaojogador = fonte_placar.render('{} ou {}'.format(pontuacao_player1, pontuacao_player2), True, branco)
                                pontuacaojogador = Placar(pontuacaojogador,525,325,delay)
                            elif pontuacao_player1 <= 21 and pontuacao_player2 > 21:
                                pontuacaojogador = fonte_placar.render('{}'.format(pontuacao_player1), True, branco)
                                pontuacaojogador = Placar(pontuacaojogador,525,325,delay)

                        pp.append(pontuacaojogador)

                        extra_player = Carta(extra_player,posicao_player,300,delay)
                        cartas.append(extra_player)
                        
                        if pontuacao_player1 > 21:  # Se as cartas do jogador estourarem
                            jogada_player = False
                            jogo_fim = True
                            i=1
                            
                    # Define a pontuação do jogador após terminar de comprar
                    if pontuacao_player1 <= 21 and pontuacao_player2 <= 21:
                        pontuacao_player = pontuacao_player2
                    if pontuacao_player1 <= 21 and pontuacao_player2 > 21:
                        pontuacao_player = pontuacao_player1
                    if pontuacao_player1 > 21:
                        pontuacao_player = 0 

                    if 100 <= mouse[0] <= 100+largura_botao and 175 <= mouse[1] <= 175+altura_botao and jogo_fim == False: # Clique no botão de segurar

                        # Impossibilita o comprar/segurar até que jogue novamente
                        i=1
                        jogada_player = False
                        
                        # Sorteia a carta 2 da mesa e adiciona na lista 'cartas'
                        delay = 0.3
                        c2_mesa = random.choice(lista_cartas)
                        if c2_mesa in dicionario.keys():
                            pontuacao_mesa1 += dicionario[c2_mesa]
                            pontuacao_mesa2 += dicionario[c2_mesa]
                        else:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 11

                        if pontuacao_mesa1 == pontuacao_mesa2:
                            pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                            pontuacaomesa = Placar(pontuacaomesa,525,100,delay)
                        else:
                            pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                            pontuacaomesa = Placar(pontuacaomesa,525,100,delay)

                        pm.append(pontuacaomesa)

                        c2_mesa = Carta(c2_mesa,370,100,delay)    
                        cartas.append(c2_mesa)
                                              
                        
                        while jogo_fim == False:

                            # Quando a pontuação maior da mesa está empatada com a pontuação do jogador
                            if pontuacao_player == pontuacao_mesa2:  
                                if pontuacao_player < 17:
                                    delay += 0.6
                                    posicao_mesa += 20
                                    extra_mesa = random.choice(lista_cartas)  # Sorteia carta extra da mesa se a pontuação for menor que 17 
                                    if extra_mesa in dicionario.keys():
                                        pontuacao_mesa1 += dicionario[extra_mesa]  
                                        pontuacao_mesa2 += dicionario[extra_mesa]
                                    else:
                                        if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 11
                                        elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1
                                        elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1

                                    if pontuacao_mesa1 == pontuacao_mesa2:
                                        pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)
                                    else:
                                        pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)

                                    pm.append(pontuacaomesa)

                                    extra_mesa = Carta(extra_mesa,posicao_mesa,100,delay)
                                    cartas.append(extra_mesa)
                                else:
                                    jogo_fim = True

                            #Quando a pontuação menor da mesa está empatada com a pontuação do jogador e a maior já passou de 21
                            elif pontuacao_mesa1 == pontuacao_player and pontuacao_mesa2 > 21:
                                if pontuacao_player < 17:
                                    delay += 0.6
                                    posicao_mesa += 20
                                    extra_mesa = random.choice(lista_cartas)  # Sorteia carta extra da mesa se a pontuação for menor que 17 
                                    if extra_mesa in dicionario.keys():
                                        pontuacao_mesa1 += dicionario[extra_mesa]  
                                        pontuacao_mesa2 += dicionario[extra_mesa]
                                    else:
                                        if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 11
                                        elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1
                                        elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1

                                    if pontuacao_mesa1 == pontuacao_mesa2:
                                        pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)
                                    else:
                                        pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)

                                    pm.append(pontuacaomesa)

                                    extra_mesa = Carta(extra_mesa,posicao_mesa,100,delay)
                                    cartas.append(extra_mesa)
                                
                                else:
                                    jogo_fim = True


                            # Quando o jogador tem mais pontos que a maior pontuação da mesa
                            elif pontuacao_player > pontuacao_mesa2:
                                posicao_mesa += 20
                                delay += 0.6
                                extra_mesa = random.choice(lista_cartas)
                                if extra_mesa in dicionario.keys():
                                    pontuacao_mesa1 += dicionario[extra_mesa]  
                                    pontuacao_mesa2 += dicionario[extra_mesa]
                                else:
                                    if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                                        pontuacao_mesa1 += 1
                                        pontuacao_mesa2 += 11
                                    elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                                        pontuacao_mesa1 += 1
                                        pontuacao_mesa2 += 1
                                    elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                                        pontuacao_mesa1 += 1
                                        pontuacao_mesa2 += 1  

                                if pontuacao_mesa1 == pontuacao_mesa2:
                                        pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)
                                else:
                                    pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                                    pontuacaomesa = Placar(pontuacaomesa,525,100,delay)

                                pm.append(pontuacaomesa)
                                
                                extra_mesa = Carta(extra_mesa,posicao_mesa,100,delay)
                                cartas.append(extra_mesa)
                
                            # Quando o jogador tem mais pontos que a menor pontuação da mesa e a maior já passou de 21
                            elif pontuacao_player > pontuacao_mesa1 and pontuacao_mesa2 > pontuacao_player:
                                if pontuacao_mesa2 > 21:
                                    delay += 0.6
                                    posicao_mesa += 20
                                    extra_mesa = random.choice(lista_cartas)
                                    if extra_mesa in dicionario.keys():
                                        pontuacao_mesa1 += dicionario[extra_mesa]  
                                        pontuacao_mesa2 += dicionario[extra_mesa]
                                    else:
                                        if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 11
                                        elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1
                                        elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                                            pontuacao_mesa1 += 1
                                            pontuacao_mesa2 += 1  
                                    
                                    if pontuacao_mesa1 == pontuacao_mesa2:
                                        pontuacaomesa = fonte_placar.render(str(pontuacao_mesa1), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)
                                    else:
                                        pontuacaomesa = fonte_placar.render('{} ou {}'.format(pontuacao_mesa1, pontuacao_mesa2), True, branco)
                                        pontuacaomesa = Placar(pontuacaomesa,525,100,delay)

                                    pm.append(pontuacaomesa)
                                    
                                    extra_mesa = Carta(extra_mesa,posicao_mesa,100,delay)
                                    cartas.append(extra_mesa)
                            
                            # A partida chega ao fim
                            if pontuacao_mesa2 > pontuacao_player and pontuacao_mesa2 <= 21:
                                jogo_fim = True
                            if pontuacao_player1 > pontuacao_mesa1 and pontuacao_mesa1 <= 21:
                                jogo_fim = True
                            if pontuacao_mesa1 > 21:
                                jogo_fim = True


                    # Define a pontuação final da mesa
                    if pontuacao_mesa1 <= 21 and pontuacao_mesa2 <= 21:
                        pontuacao_mesa = pontuacao_mesa2
                    elif pontuacao_mesa1 <= 21 and pontuacao_mesa2 > 21:
                        pontuacao_mesa = pontuacao_mesa1
                    elif pontuacao_mesa1 > 21:
                        pontuacao_mesa = 0

                    # Verifica e define texto para estouros
                
                    if pontuacao_player1 > 21 or pontuacao_mesa1 > 21:
                        estouro = True
                        #delay = 1
                        estourou = fonte_placar.render('Estourou!', True, vermelho)
                        estourou = Placar(estourou, 350, 225, delay)

                    # Define delay para aparecer resultado
                    delay = delay + 1.7
                    
                    # Verifica e define texto para os resultados 

                    if pontuacao_mesa > pontuacao_player:  # Derrota
                        resultado = fonte_pequena.render('Perdeu!', True, vermelho)
                        resultado = Placar(resultado, 0, 0, delay)
                        pericles = Carta(pericles_triste, 0, 0, delay)
                        derrota = True

                        # Define texto de jogar novamente
                        jogar = fonte_pequena.render('pressione qualquer', True, branco)
                        tecla = fonte_pequena.render('tecla para', True, branco)
                        novamente = fonte_pequena.render('jogar novamente', True, branco)
                        jogar = Placar(jogar, 10, 90, delay)
                        tecla = Placar(tecla, 30, 130, delay)
                        novamente = Placar(novamente, 10, 170, delay)
                        
                    elif pontuacao_mesa == pontuacao_player:  # Empate
                        resultado = fonte_pequena.render('Empate!', True, preto)
                        resultado = Placar(resultado, 0, 0, delay)
                        pericles = Carta(pericles_neutro, 0, 0, delay)
                        empate = True

                        # Define texto de jogar novamente
                        jogar = fonte_pequena.render('pressione qualquer', True, preto)
                        tecla = fonte_pequena.render('tecla para', True, preto)
                        novamente = fonte_pequena.render('jogar novamente', True, preto)
                        jogar = Placar(jogar, 550, 50, delay)
                        tecla = Placar(tecla, 560, 90, delay)
                        novamente = Placar(novamente, 540, 130, delay)

                        
                    else:  # Vitória
                        resultado = fonte_pequena.render('Ganhou!', True, verde)
                        resultado = Placar(resultado, 0, 0, delay)
                        pericles = Carta(pericles_feliz, 0, 0, delay)
                        vitoria = True

                        # Define texto de jogar novamente
                        jogar = fonte_pequena.render('pressione qualquer', True, branco)
                        tecla = fonte_pequena.render('tecla para', True, branco)
                        novamente = fonte_pequena.render('jogar novamente', True, branco)
                        jogar = Placar(jogar, 550, 50, delay)
                        tecla = Placar(tecla, 560, 90, delay)
                        novamente = Placar(novamente, 540, 130, delay)



                        
                    
                    # Define texto de 'jogar novamente'
                    
                    
                    

            if event.type == pygame.KEYUP and jogo_fim == True:  # Clique para jogar novamente

                cartas = []  # Lista que armazena todas as cartas que saem do baralho
                pp = []  # Lista que armazena a pontuação do jogador a cada carta que sai do baralho
                pm = []  # Lista que armazena a pontuação da mesa a cada carta que sai do baralho

                posicao_player = 370
                posicao_mesa = 370

                pontuacao_player1 = 0
                pontuacao_player2 = 0
                pontuacao_mesa1 = 0
                pontuacao_mesa2 = 0

                delay = 0

                jogo_inicial = True
                jogada_player = True
                jogo_fim = False
                estouro = False
                
                i=0

        mouse = pygame.mouse.get_pos()

        janela.blit(tela_de_fundo_ajustada, (0,0))
        # Desenha a pontuação do jogador para cada virada de carta
        for pontuacao in pp:
            if pontuacao.exibir:
                janela.blit(tampa_placar, (500,325))  
                janela.blit(pontuacao.text,pontuacao.rect)
            else:
                pontuacao.update()
        for pontuacao in pm:
            if pontuacao.exibir:
                janela.blit(tampa_placar_cima, (500,100))
                janela.blit(pontuacao.text,pontuacao.rect)
            else:
                pontuacao.update()

        # Desenha todas as cartas adicionadas na lista 'cartas' com um delay de   
        for carta in cartas:
            if carta.exibir:
                janela.blit(carta.image,carta.rect)
            else:
                carta.update()

        # Desenha os botões 'comprar' e 'segurar' enquanto o player puder escolher alguma dessas opções
        if jogada_player == True:
            janela.blit(botao_comprar, (100,250))
            janela.blit(botao_segurar, (100,175))

        # Quando as possíveis interações do usuário terminam
        if jogo_fim == True:

            # Exibe 'estourou!' quando estoura
            if estouro == True:
                if estourou.exibir:
                    janela.blit(estourou.text, estourou.rect)
                else:
                    estourou.update()
            
            # Exibe nova tela de fundo
            if pericles.exibir:
                janela.blit(pericles.image, pericles.rect)
            else:
                pericles.update()

            # Exibe o resultado
            if resultado.exibir:
                janela.blit(resultado.text, resultado.rect)
                if vitoria == True:
                    uhul.play()
                    vitoria = False
                if derrota == True:
                    rapaiz.play()
                    derrota = False
                if empate == True:
                    mary.play()
                    empate = False
            else:
                resultado.update()
            

            # Exibe texto de jogar novamente
            if jogar.exibir:
                janela.blit(jogar.text, jogar.rect)
            else:
                jogar.update()

            if tecla.exibir:
                janela.blit(tecla.text, tecla.rect)
            else:
                tecla.update()

            if novamente.exibir:
                janela.blit(novamente.text, novamente.rect)
            else:
                novamente.update()

        pygame.display.update()
    
    pygame.display.update()

pygame.quit()


