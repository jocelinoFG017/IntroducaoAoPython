"""
.24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse
numero, com exceção dele próprio. EX: a soma dos divisores do número 66 é
 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""
n = int(input('Informe um numero: '))
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma = soma + i

print(soma)
