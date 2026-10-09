num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[1] converter para BINÁRIO
[2] converte para OCTAL
[3]converte para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'A converção de {num} para BINÁRIO é {bin(num)[2:]}')
elif opçao == 2:
    print(f'A converção de {num} para OCTAL é {oct(num)[2:]}')
elif opçao == 3:
    print(f'A converção de {num} para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Digite uma das opções')