import requests
resposta = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
dados = resposta.json()
v = float(dados['USDBRL']['bid'])
c = float(input("Quantos reais você tem na carteira? R$"))
d = c / v
print('Com R${:.2f} você pode comprar US${:.2f}'.format(c, d))
