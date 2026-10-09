ano = int(input('Digite seu ano de nascimento: '))
idade = 2026-ano
if idade<18:
    print(f'Quem nasceu em {ano} tem {idade} em 2026\nAinda faltam {18-idade} anos para o alistamento\nSeu alistamento será em {2026+(18-idade)}')
elif idade>18:
    print(f'Quem nasceu em {ano} tem {idade} em 2026\nVocê já deveria ter se alistado há {idade-18} anos\nSeu alistamento foi em {2026-(idade-18)}')
else:
    print(f'Quem nasceu em {ano} tem {idade} em 2026\nVocê tem que se alistar IMEDIATAMENTE!')