velocidade = float(input('Qual a velocidade do veiculo? '))
if velocidade < 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido de 80Km/h\nVocê deve pagar uma multa de R${(velocidade-80)*7 :.2f}')