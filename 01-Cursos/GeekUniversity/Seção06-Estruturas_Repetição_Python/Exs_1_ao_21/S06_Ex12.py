"""
.12. Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente.
"""
n = int(input('Informe um numero: '))

for i in range(n, -1, -1):
    print(i)
