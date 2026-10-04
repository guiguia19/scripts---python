v = float(input("Digite o valor total da conta: "))
p = int(input("Digite quantas pessoas pagarão: "))
vt = v + (v * 0.12)
vf = vt/p
print(f'\n O valor total da conta é: {vt:.2f}')
print(f'O valor individual é: {vf:.2f}')