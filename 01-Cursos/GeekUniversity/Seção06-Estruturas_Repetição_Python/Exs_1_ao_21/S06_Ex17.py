"""
.17.Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naturais.
"""
n = int(input('Informe um numero: '))
soma = 0
for i in range(0, n+1):
    print(i)
    soma = soma + i
print(f'soma de todos os Nº pares = {soma}')
