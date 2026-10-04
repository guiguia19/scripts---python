nome = str(input("Qual seu nome completo? "))
nome_limpo = nome.title()
print(f'Seu nome tem Silva? {"Silva" in nome_limpo}')