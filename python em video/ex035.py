p = float(input('Digite o primeiro número: '))
s = float(input('Digite o segundo número: '))
t = float(input('Digite o terceiro número: '))
maior = p
if s>p and s>t:
    maior = s
if t>s and t>p:
    maior = t
soma = (p+s+t) - maior
if soma>maior:
    print('As restas formam um triangulo!')
else:
    print('As retas não formam um triangulo!')