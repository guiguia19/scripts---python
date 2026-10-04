preço = float(input('Qual o preço do produto? R$ '))
valor = preço - (preço * 0.05)
print (f'O produto que custava R$ {preço:.2f}, na promo com desconto de 5% vai custar R$ {valor:.2f}')