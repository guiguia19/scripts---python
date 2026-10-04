dia = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos kms você rodou com o carro? '))
sd = dia * 60
skm = km * 0.15
s = sd + skm
print(f'O total a pagar é de R${s:.2f}!')