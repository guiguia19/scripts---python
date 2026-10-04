import random
from time import sleep
linha = '-=' * 28
print(linha)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(linha)
print('Pensando...')
sleep(1)
adivinhe = int(input('Em que número eu pensei? '))
lista = [0,1,2,3,4,5]
sorteado = random.choice(lista)
if adivinhe == sorteado:
    print('Parabéns você acertou!')
else:
    print(f'Que pena, eu tinha pensado no {sorteado}')
print('-----------Fim-----------')