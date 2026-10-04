import random
p = str(input('Digite o nome do primeiro aluno: '))
s = str(input('Digite o nome do segundo aluno: '))
t = str(input('Digite o nome do terceiro aluno: '))
q = str(input('Digite o nome do quarto aluno: '))
print(f'O aluno sorteado foi: {random.choice([p, s, t, q])}')