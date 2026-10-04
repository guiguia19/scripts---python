import math
from math import sqrt as rq
co = float(input('Digite o cateto oposto: '))
ca =  float(input('Digite o cateto adjacente: '))
s = rq(co**2 + ca**2)
print(f'A hipotenusa vai medir {s:.2f}!')