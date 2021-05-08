"""
.15.Faça um programa que leia um número inteiro positivo impar N e imprima todos os números
impares de 0 até N em ordem crescente.
"""
n = int(input('Informe um numero: '))
for i in range(0, n):
    if i % 2 == 1:
        print(i)
