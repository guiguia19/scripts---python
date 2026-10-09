nome = str(input('Qual o seu nome? ')).title().strip()
if nome == 'Guilherme':
    print('Que nome bonito!')
elif nome == 'Gustavo' or nome == 'Joyce' or nome == 'Luciano':
    print('Provavelmente você é parente do Guilherme')
elif nome in 'Ana Hamira Laryssa Gabs':
    print('Provavelmente você é amiga do Guilherme')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')