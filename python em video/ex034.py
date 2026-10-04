salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    print(f'Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {salario + (salario*0.15):.2f}')
else:
    print(f'Um funcionário que ganhava R$ {salario:.2f}, com 10% de aumento, passa a receber R$ {salario + (salario*0.10):.2f}')