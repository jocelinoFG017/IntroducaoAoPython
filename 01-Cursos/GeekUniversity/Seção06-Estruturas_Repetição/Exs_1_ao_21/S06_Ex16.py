"""
.16.Faça um programa que leia um número inteiro positivo impar N e imprima todos os números
impares de 0 até N em ordem decrescente.
"""
n = int(input('Informe um numero: '))
for i in range(n, 0, -1):
    if i % 2 == 1:
        print(i)
