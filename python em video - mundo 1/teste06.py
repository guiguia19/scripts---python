'''nome = str(input('Qual seu nome? ')).strip().title()
if nome == 'Guilherme':
    print('Seja bem vindo Guilherme!')
else:
    print('Digite o nome correto!')
print('---FIM---')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')