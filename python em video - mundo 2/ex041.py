ano = int(input('Digite o ano de nascimento:'))
idade = 2026-ano
if idade<=9:
    print(f'O atleta tem {idade} anos\nSua classificação é: MIRIM')
elif idade>=10 and idade<=14:
    print(f'O atleta tem {idade} anos\nSua classificação é: INFANTIL')
elif idade>=15 and idade<=19:
    print(f'O atleta tem {idade} anos\nSua classificação é: JUNIOR')
elif idade>=20 and idade<=24:
    print(f'O atleta tem {idade} anos\nSua classificação é: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos\nSua classificação é: MASTER')