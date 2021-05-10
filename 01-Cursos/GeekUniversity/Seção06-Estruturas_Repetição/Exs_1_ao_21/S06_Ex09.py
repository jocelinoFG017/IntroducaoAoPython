"""
.9. Faça um programa que leia um número inteiro N e depois imprima os N
primeiros números naturais ímpares.
"""
n = int(input('Informe um numero: '))
for i in range(1, n):
    if n > 0:
        if i % 2 == 1:
            print(i)
