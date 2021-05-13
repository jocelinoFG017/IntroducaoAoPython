"""
.23.Faça um programa que leia um número inteiro positivo e imprima seus divisores.
"""
n = int(input('Informe um numero: '))

for i in range(1, n):
    if n % i == 0:
        print(i)
