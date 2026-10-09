n1 = int(input("Digite o primeiro númro: "))
n2 = int(input("Digite o segundo número: "))
if n1>n2:
    print(f'O primeiro número é o maior: {n1} e o segundo número é o menor: {n2}')
elif n1==n2:
    print(f'Ambos os números são iguais')
elif n1<n2:
    print(f'O segundo número é o maior: {n2} e o primeiro número é o menor: {n1}')