import math
g = float(input('Digite o ângulo: '))
rad = math.radians(g)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print(f"O ângulo de {g} tem o Seno de {s:.2f}\nO ângulo de {g} tem o Cosseno de {c:.2f}\nO ângulo de {g} tem a Tangente de {t:.2f}")