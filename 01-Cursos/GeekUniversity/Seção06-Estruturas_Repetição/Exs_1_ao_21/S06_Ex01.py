"""
.1. Faça um programa que determine e mostre os cinco primeiro multiplos de 3,
considerando números maiores que 0.
"""
n = 1
for n in range(18):
    if n > 0:
        if n % 3 == 0:
            print(n)
