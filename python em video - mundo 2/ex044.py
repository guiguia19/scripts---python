compra = float(input('Digite o preço da compra: '))
print('''Escolha uma das formas de pagamento:
[1] à vista dinheiro/pix
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'Sua compra foi de R${compra:.2f}, vai custar R${compra*0.90:.2f}')
elif opçao == 2:
    print(f'Sua compra foi de R${compra:.2f}, vai custar R${compra*0.95:.2f}')
elif opçao == 3:
    print(f'Sua compra foi de R${compra:.2f}, vai custar duas parcelas de R${compra/2:.2f}')
elif opçao == 4:
    total = compra*1.20
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela}X de {total/parcela:.2f}')