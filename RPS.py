# inicio do programa

from random import randint

points1 = 0
points2 = 0

loop = True
choice = int(input('===== Bem vindo ao jokenô game ===== \n \n  Escolha qual modalidade você deseja jogar: \n 1 - Jogador vs Jogador \n 2 - Jogador vs Computador \n 3 - Computador vs Computador \n R:  '))
while loop:

    if choice == 1:
        player1 = int(input('===== VEZ DO JOGADOR 1 ===== \n  Escolha uma das opcoes: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n R: '))
        player2 = int(input('===== VEZ DO JOGADOR 2 ===== \n  Escolha uma das opcoes: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n R: '))
        winner = player1 - player2

        if winner == 0:
            print('Empate!!!')
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        elif winner == -2:
            print('O jogador 1 venceu esta rodada!!!')
            points1 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        elif winner == 1:
            print('O jogador 1 venceu esta rodada!!!')
            points1 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        else:
            print('O jogador 2 venceu esta rodada!!!')
            points2 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

    elif choice == 2:
        player1 = int(input(
            '===== VEZ DO JOGADOR 1 ===== \n  Escolha uma das opcoes: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n R: '))
        player2 = randint(1, 3)
        winner = player1 - player2

        if winner == 0:
            print('Empate!!!')
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        elif winner == -2:
            print('O jogador 1 venceu esta rodada!!!')
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')
            points1 += 1

        elif winner == 1:
            print('O jogador 1 venceu esta rodada!!!')
            points1 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        else:
            print('O jogador 2 venceu esta rodada!!!')
            points2 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        loop = input('Deseja continuar?(S/N): ')
        if loop == 'N' or loop == 'n':
            if points1 > points2:
                print(f'O VENCEDOR É O JOGADOR 1 COM {points1} PONTOS CONTRA {points2} PONTOS DO JOGADOR 2 ')

            elif points2 > points1:
                print(f'O VENCEDOR É O JOGADOR 2 COM {points2} PONTOS CONTRA {points1} PONTOS DO JOGADOR 1 ')

            else:
                print(f'EMPATE ENTRE O JOGADOR 1 COM {points1} PONTOS E O JOGADOR 2 COM {points2} PONTOS ')

            loop = False

    elif choice == 3:
        player1 = randint(1,3)
        player2 = randint(1, 3)
        winner = player1 - player2

        if winner == 0:
            print('Empate!!!')
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        elif winner == -2:
            print('O jogador 1 venceu esta rodada!!!')
            points1 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        elif winner == 1:
            print('O jogador 1 venceu esta rodada!!!')
            points1 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

        else:
            print('O jogador 2 venceu esta rodada!!!')
            points2 += 1
            print(f'Jogador 1 - {points1} pontos | Jogador 2 - {points2} pontos')

    loop = input('Deseja continuar?(S/N): ')
    if loop == 'N' or loop == 'n':
        if points1 > points2:
            print(f'O VENCEDOR É O JOGADOR 1 COM {points1} PONTOS CONTRA {points2} PONTOS DO JOGADOR 2 ')

        elif points2 > points1:
            print(f'O VENCEDOR É O JOGADOR 2 COM {points2} PONTOS CONTRA {points1} PONTOS DO JOGADOR 1 ')

        else:
            print(f'EMPATE ENTRE O JOGADOR 1 COM {points1} PONTOS E O JOGADOR 2 COM {points2} PONTOS ')

        print(
            '===== OBRIGADO POR JOGAR ===== \n projeto feito por: Pedro Magno e Patrick Davidsonn')
        loop = False