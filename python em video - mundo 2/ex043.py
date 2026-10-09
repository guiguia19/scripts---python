peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso/(altura*altura)
if imc<=18.5:
    print(f'O IMC dessa pessoa é de {imc:.2f}\nVocê está ABAIXO DO PESO normal, cuidado!')
elif imc>=18.6 and imc<=25:
    print(f'O IMC dessa pessoa é de {imc:.2f}\nVocê está no PESO IDEAL, parabens!')
elif imc>=25.1 and imc<=30:
    print(f'O IMC dessa pessoa é de {imc:.2f}\nVocê está no SOBREPESO, está bem, mas pode melhorar!')
elif imc>=30.1 and imc<=40:
    print(f'O IMC dessa pessoa é de {imc:.2f}\nVocê está na OBESIDADE, atenção!')
else:
    print(f'O IMC dessa pessoa é de {imc:.2f}\nVocê está na OBESIDADE MÓRBIDA, cuidado!')