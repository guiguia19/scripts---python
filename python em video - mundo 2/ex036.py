casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
periodo = int(input('Em quantos anos você deseja pagar? '))
prestação = ((casa / periodo) / (salario * 12)) * 100
if prestação < 30:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')
print(prestação)