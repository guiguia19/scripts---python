import random
p = str(input('Digite o primeiro nome: '))
s = str(input('Digite o segundo nome: '))
t = str(input('Digite o terceiro nome: '))
q = str(input('Digite o quarto nome: '))
list = [p, s, t, q]
random.shuffle(list)
print('A ordem de apresentação será ')
print(list)