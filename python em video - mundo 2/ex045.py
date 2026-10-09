import random
import time
linha = '-='*15
print('''Escolha uma das formas jogada:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
lista = ('Pedra', 'Papel', 'Tesoura')
sorteado = random.randint(0,2)
print(linha)
print(f'O computador escolheu {lista[sorteado]}')
print(f'O jogador escolheu {lista[jogada]}')
print(linha)
if sorteado == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
            print('COMPUTADOR VENCE')
if sorteado == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
            print('JOGADOR VENCE')
if sorteado == 2:
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
            print('COMPUTADOR VENCE')