n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
print('A divisão inteira é {} e o resto é {}'.format(di, re))