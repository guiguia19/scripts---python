p = int(input('Digite o primeiro número: '))
s = int(input('Digite o segundo número: '))
t = int(input('Digite o terceiro número: '))
if p <s and t:
    menor = p
if s <p and t:
    menor = s
if t <p and s:
    menor = t
print(f'O menor número foi {menor}')
if p >s and t:
    maior = p
if s >p and t:
    maior = s
if t >p and s:
    maior = t
print(f'O maior número foi {maior}')