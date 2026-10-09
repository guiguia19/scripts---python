n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
if media>7.0:
    print(f'Sua média foi {media}, com isso você está APROVADO!')
elif media<=4.9:
    print(f'Sua média foi {media}, com isso você está REPROVADO!')
elif media>=5.0 and media<=6.9:
    print(f'Sua média foi {media}, com isso você está de RECUPERAÇÃO!')