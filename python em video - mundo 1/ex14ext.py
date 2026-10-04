import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=-23.5475&longitude=-46.6361&current=temperature_2m&timezone=America/Sao_Paulo"
resposta = requests.get(url)
dados = resposta.json()
temperatura = dados['current']['temperature_2m']
unidade = dados['current_units']['temperature_2m']
f = temperatura * 1.8 + 32
print (f' A temperatura atual é de {temperatura}{unidade} e em fahrenheit {f:.1f}ºF')