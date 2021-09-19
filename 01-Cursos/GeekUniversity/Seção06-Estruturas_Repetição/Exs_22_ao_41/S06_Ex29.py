"""
.29. Faça um programa para calcular o valor da série, para 5 termos.

    - S = 0 + 1/2! + 1/4! + 1/6 +...
"""
from math import factorial

soma = 0
termos = 5

for i in range(1, termos + 1):
    if i % 2 == 0:  # Condição para encontrar valores pares
        soma = soma + 1/factorial(i)

print(soma)
