"""
.13.Faça um programa que leia um número inteiro positivo par N e imprima todos os números
pares de 0 até N em ordem crescente.
"""
n = int(input('Informe um numero: '))
for i in range(0, n, 2):
    print(i)
