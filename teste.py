import random

lista_cartas = ['A','A','A','A','J','J','J','J','K','K','K','K','Q','Q','Q','Q','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
cartas = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
fichas = 20
jogar = input('Você deseja jogar BlackJack? [s/n]')

while jogar == 's':
    blackjack_mesa = False
    blackjack_player = False
    
    print('Você tem {} fichas'.format(fichas))

    if fichas == 0:
        print('Compre mais fichas!')
        mais_fichas = input('Você quer comprar mais fichas? [s/n] ')
        if mais_fichas == 's':
            quantas = int(input('Quantas fichas deseja comprar? '))
            fichas += quantas
            print('Você tem {} fichas'.format(fichas))
            aposta = aposta = int(input('Quantas fichas você quer apostar? '))
    else:
        aposta = int(input('Quantas fichas você quer apostar? '))

    while aposta > fichas:
        if fichas == 0:
            print('Compre mais fichas!')
            mais_fichas = input('Você quer comprar mais fichas? [s/n] ')
            if mais_fichas == 's':
                quantas = int(input('Quantas fichas deseja comprar? '))
                fichas += quantas
                print('Você tem {} fichas'.format(fichas))
        else:
            print('Você não tem fichas suficientes para esta aposta!')
            print('Compre mais fichas ou diminua a aposta!')
            mais_fichas = input('Você quer comprar mais fichas? [s/n] ')
            if mais_fichas == 's':
                quantas = int(input('Quantas fichas deseja comprar? '))
                fichas += quantas
                print('Você tem {} fichas'.format(fichas))
                aposta = int(input('Quantas fichas você quer apostar?'))
            else:
                aposta = int(input('Quantas fichas você quer apostar?'))

    fichas -= aposta

    certeza = input('Você tem certeza? [s/n]')

    pontuacao_player1 = 0
    pontuacao_player2 = 0
    pontuacao_mesa1 = 0
    pontuacao_mesa2 = 0

    if certeza == 's':
        c1_player = random.choice(lista_cartas)
        print('Carta 1 jogador: {}'.format(c1_player))
        #lista_cartas.remove(c1_player)
        if c1_player in cartas.keys():
            c1_player = cartas[c1_player]

        if c1_player == 'A':
            print('Você tem 1 ou 11')
        else:
            print('Você tem {}'.format(c1_player))

        c1_mesa = random.choice(lista_cartas)
        print('Carta 1 mesa: {}'.format(c1_mesa))
        lista_cartas.remove(c1_mesa)
        if c1_mesa in cartas.keys():
            c1_mesa = cartas[c1_mesa]

        if c1_mesa != 'A':
            print('A mesa tem {}'.format(c1_mesa))
        else:
            print('A mesa tem 1 ou 11')
        
        c2_player = random.choice(lista_cartas)
        print('Carta 2 jogador: {}'.format(c2_player))
        #lista_cartas.remove(c2_player)
        if c2_player in cartas.keys():
            c2_player = cartas[c2_player]
        
        c2_mesa = random.choice(lista_cartas)
        #lista_cartas.remove(c2_mesa)
        if c2_mesa in cartas.keys():
            c2_mesa = cartas[c2_mesa]

        if c1_player != 'A' and c2_player != 'A':
            pontuacao_player1 = c1_player + c2_player
            pontuacao_player2 = pontuacao_player1
            print('Você tem {} '.format(c1_player + c2_player))

        if c1_player != 'A' and c2_player == 'A':
            pontuacao_player1 = c1_player + 1
            pontuacao_player2 = c1_player + 11
            if c1_player == 10:
                print('Blackjack!')
                print('Você tem 21!')
                blackjack_player = True
            else:
                print('Você tem {} ou {} '.format(pontuacao_player1, pontuacao_player2))

        if c1_player == 'A' and c2_player != 'A':
            pontuacao_player1 = c2_player+1
            pontuacao_player2 = c2_player+11
            if c2_player == 10:
                print('Blackjack!')
                print('Você tem 21!')
                blackjack_player = True
            else:
                print('Você tem {} ou {} pontos'.format(pontuacao_player1, pontuacao_player2))

        if c1_player == 'A' and c2_player == 'A':
            pontuacao_player1 = 2
            pontuacao_player2 = 12
            print('Você tem 2 ou 12 ')

        if pontuacao_player2 != 21:
            buy_hold = input('Você deseja comprar ou segurar? [comprar/segurar]')
        if pontuacao_player2 == 21:
            buy_hold = 'segurar'

        while buy_hold == 'comprar':
            extra_player = random.choice(lista_cartas)
            print('Carta extra jogador: {}'.format(extra_player))
            #lista_cartas.remove(extra_player)
            if extra_player in cartas.keys():
                extra_player = cartas[extra_player]

            if extra_player == 'A':
                if pontuacao_player1 <= 10 and pontuacao_player2 <= 10:
                    pontuacao_player1 += 1
                    pontuacao_player2 += 11
                elif pontuacao_player1 > 10 and pontuacao_player2 > 10:
                    pontuacao_player1 += 1
                    pontuacao_player2 += 1
                elif pontuacao_player1 <= 10 and pontuacao_player2 > 10:
                    pontuacao_player1 += 1
                    pontuacao_player2 += 1

            if extra_player != 'A':
                pontuacao_player1 += extra_player
                pontuacao_player2 += extra_player
        
            if pontuacao_player1 <= 21 and pontuacao_player2 <= 21:
                if pontuacao_player1 == pontuacao_player2:
                    print('Você tem {}'.format(pontuacao_player1))
                else:
                    print('Você tem {} ou {}'.format(pontuacao_player1,pontuacao_player2))

            if pontuacao_player1 <= 21 and pontuacao_player2 > 21:
                print('Você tem {}'.format(pontuacao_player1))

            if pontuacao_player1 > 21:
                print('{}! Estourou!'.format(pontuacao_player1))
                print('Você perdeu {} fichas'.format(aposta))
                break
            
            buy_hold = input('Você deseja comprar ou segurar? [comprar/segurar]')
        

        if buy_hold == 'segurar':
            if pontuacao_player1 <= 21 and pontuacao_player2 <= 21:
                pontuacao_player = pontuacao_player2
                print('Você tem {}'.format(pontuacao_player))
            if pontuacao_player1 <= 21 and pontuacao_player2 > 21:
                pontuacao_player = pontuacao_player1
                print('Você tem {}'.format(pontuacao_player))

            print('Carta 2 mesa: {}'.format(c2_mesa))

            if c1_mesa != 'A' and c2_mesa != 'A':
                pontuacao_mesa1 = c1_mesa + c2_mesa
                pontuacao_mesa2 = pontuacao_mesa1
                print('A mesa tem {} pontos'.format(pontuacao_mesa1))

            elif c1_mesa != 'A' and c2_mesa == 'A':
                pontuacao_mesa1 = c1_mesa + 1
                pontuacao_mesa2 = c1_mesa + 11
                if c1_mesa == 10:
                    print('Blackjack!')
                    print('A mesa tem 21!')
                    blackjack_mesa = True
                else:
                    print('A mesa tem {} ou {} pontos'.format(pontuacao_mesa1,pontuacao_mesa2))
            
            elif c1_mesa == 'A' and c2_mesa != 'A':
                pontuacao_mesa1 = c2_mesa + 1
                pontuacao_mesa2 = c2_mesa + 11
                if c2_mesa == 10:
                    print('Blackjack!')
                    print('A mesa tem 21!')
                    blackjack_mesa = True
                else:
                    print('A mesa tem {} ou {} pontos'.format(pontuacao_mesa1,pontuacao_mesa2))
            
            elif c1_mesa == 'A' and c2_mesa == 'A':
                pontuacao_mesa1 = 2
                pontuacao_mesa2 = 12
                print('A mesa tem 2 ou 12 pontos')
            
            if pontuacao_player < pontuacao_mesa2:
                print('Você perdeu {} fichas'.format(aposta))

            if pontuacao_player == pontuacao_mesa2:
                if pontuacao_player == 21:
                    if blackjack_mesa == True and blackjack_player == True:
                        print('Empate!')
                        print('Você ganhou {} fichas'.format(aposta))
                        fichas += aposta
                        
                    elif blackjack_mesa == False and blackjack_player == False:
                        print('Empate!')
                        print('Você ganhou {} fichas'.format(aposta))
                        fichas += aposta
                        
                    elif blackjack_mesa == True and blackjack_player == False:
                        print('Você perdeu {} fichas'.format(aposta))
                        
                    elif blackjack_mesa == False and blackjack_player == True:
                        print('Você ganhou {} fichas'.format(2*aposta))
                        fichas += aposta*2

                elif pontuacao_player >= 17:
                    print('Empate!')
                    print('Você ganhou {} fichas'.format(aposta))
                    fichas += aposta
                    
                else:
                    extra_mesa = random.choice(lista_cartas)
                    print('Carta extra mesa: {}'.format(extra_mesa))
                    #lista_cartas.remove(extra_mesa)
                    if extra_mesa in cartas.keys():
                        extra_mesa = cartas[extra_mesa]

                    if extra_mesa == 'A':
                        if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 11
                        elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 1
                        elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 1

                    if extra_mesa != 'A':
                        pontuacao_mesa1 += extra_mesa
                        pontuacao_mesa2 += extra_mesa

                    if pontuacao_mesa1 <= 21 and pontuacao_mesa2 <= 21:
                        if pontuacao_mesa2 > pontuacao_player:
                            pontuacao_mesa = pontuacao_mesa2
                            print('A mesa fez {}'.format(pontuacao_mesa))
                            print('Você perdeu {} fichas'.format(aposta))
                            
                        elif pontuacao_mesa1 > pontuacao_player:
                            pontuacao_mesa = pontuacao_mesa1
                            print('A mesa fez {}'.format(pontuacao_mesa))
                            print('Você perdeu {} fichas'.format(aposta))
                            
                        elif pontuacao_mesa1 != pontuacao_mesa2:
                            print('A mesa tem {} ou {}'.format(pontuacao_mesa1,pontuacao_mesa2))
                        elif pontuacao_mesa1 == pontuacao_mesa2:
                            print('A mesa tem {}'.format(pontuacao_mesa1))
  
                    if pontuacao_mesa1 <= 21 and pontuacao_mesa2 > 21:
                        if pontuacao_mesa1 > pontuacao_player:
                            pontuacao_mesa = pontuacao_mesa1
                            print('A mesa fez {}'.format(pontuacao_mesa))
                            print('Você perdeu {} fichas'.format(aposta))
                    
                        elif pontuacao_mesa1 != pontuacao_mesa2:
                            print('A mesa tem {} ou {}'.format(pontuacao_mesa1,pontuacao_mesa2))
                        elif pontuacao_mesa1 == pontuacao_mesa2:
                            print('A mesa tem {}'.format(pontuacao_mesa1))
                      
                    if pontuacao_mesa1 > 21 and pontuacao_mesa2 > 21:
                        print('{}! Estorou!'.format(pontuacao_mesa1))
                        print('Você ganhou {} fichas'.format(aposta*2))
                        fichas += 2*aposta

            while pontuacao_player > pontuacao_mesa2:

                extra_mesa = random.choice(lista_cartas)
                print('Carta extra mesa: {}'.format(extra_mesa))
                #lista_cartas.remove(extra_mesa)
                if extra_mesa in cartas.keys():
                    extra_mesa = cartas[extra_mesa]
                
                if extra_mesa == 'A':
                    if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                        pontuacao_mesa1 += 1
                        pontuacao_mesa2 += 11
                    elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                        pontuacao_mesa1 += 1
                        pontuacao_mesa2 += 1
                    elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                        pontuacao_mesa1 += 1
                        pontuacao_mesa2 += 1

                if extra_mesa != 'A':
                    pontuacao_mesa1 += extra_mesa
                    pontuacao_mesa2 += extra_mesa
                

                if pontuacao_mesa1 <= 21 and pontuacao_mesa2 <= 21:
                    if pontuacao_mesa2 > pontuacao_player:
                        pontuacao_mesa = pontuacao_mesa2
                        print('A mesa fez {}'.format(pontuacao_mesa))
                        print('Você perdeu {} fichas'.format(aposta))
                        
                    elif pontuacao_mesa1 > pontuacao_player:
                        pontuacao_mesa = pontuacao_mesa1
                        print('A mesa fez {}'.format(pontuacao_mesa))
                        print('Você perdeu {} fichas'.format(aposta))
                        
                    elif pontuacao_mesa2 == pontuacao_player:
                        if pontuacao_mesa1 >= 17:
                            print('A mesa fez {}'.format(pontuacao_mesa2))
                            print('Empate!')
                            print('Você ganhou {} fichas'.format(aposta))
                            fichas += aposta
                            
                    elif pontuacao_mesa1 != pontuacao_mesa2:
                        print('A mesa tem {} ou {}'.format(pontuacao_mesa1,pontuacao_mesa2))
                    elif pontuacao_mesa1 == pontuacao_mesa2:
                        print('A mesa tem {}'.format(pontuacao_mesa1))
  
                if pontuacao_mesa1 <= 21 and pontuacao_mesa2 > 21:
                    if pontuacao_mesa1 > pontuacao_player:
                        pontuacao_mesa = pontuacao_mesa1
                        print('A mesa fez {}'.format(pontuacao_mesa))
                        print('Você perdeu {} fichas'.format(aposta))
                        
                    elif pontuacao_mesa1 == pontuacao_player:
                        if pontuacao_mesa1 >= 17:
                            print('A mesa fez {}'.format(pontuacao_mesa1))
                            print('Empate!')
                            print('Você ganhou {} fichas'.format(aposta))
                            fichas += aposta
                    else:
                        print('A mesa tem {}'.format(pontuacao_mesa1))
                      
                if pontuacao_mesa1 > 21 and pontuacao_mesa2 > 21:
                    print('{}! Estorou!'.format(pontuacao_mesa1))
                    print('Você ganhou {} fichas'.format(aposta*2))
                    fichas += 2*aposta

            while pontuacao_player > pontuacao_mesa1 and pontuacao_mesa2 > pontuacao_player:
                if pontuacao_mesa2 > 21:
                    extra_mesa = random.choice(lista_cartas)
                    print('Carta extra mesa: {}'.format(extra_mesa))

                    if extra_mesa in cartas.keys():
                        extra_mesa = cartas[extra_mesa]
                
                    if extra_mesa == 'A':
                        if pontuacao_mesa1 <= 10 and pontuacao_mesa2 <= 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 11
                        elif pontuacao_mesa1 > 10 and pontuacao_mesa2 > 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 1
                        elif pontuacao_mesa1 <= 10 and pontuacao_mesa2 > 10:
                            pontuacao_mesa1 += 1
                            pontuacao_mesa2 += 1

                    if extra_mesa != 'A':
                        pontuacao_mesa1 += extra_mesa
                        pontuacao_mesa2 += extra_mesa

                    if pontuacao_mesa1 <= 21:
                        if pontuacao_mesa1 > pontuacao_player:
                            print('A mesa fez')
                            print('Você perdeu {} fichas'.format(aposta))
                
                        if pontuacao_mesa1 == pontuacao_player:
                            if pontuacao_player >= 17:
                                print('A mesa fez')
                                print('Empate!')
                                print('Você ganhou {} fichas'.format(aposta))
                    
                    elif pontuacao_mesa1 > 21:
                        print('{}! Estourou!'.format(pontuacao_mesa1))
                        print('Você ganhou {} fichas'.format(2*aposta))
                        fichas += 2*aposta
                    
                    if pontuacao_mesa1 < pontuacao_player:
                        print('A mesa tem {}'.format(pontuacao_mesa1))
                        

    jogar = input('Deseja jogar novamente? [s/n]')
    lista_cartas = ['A','A','A','A','J','J','J','J','K','K','K','K','Q','Q','Q','Q','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']