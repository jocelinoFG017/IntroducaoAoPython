"""
.6. Faça um programa que leia 10 inteiros e imprima sua média.
"""
soma = 0
media = 0
for i in range(0, 10):
    valor = int(input(f'Informe o valor {i+1}: '))
    soma = soma + valor
media = soma/10
print(f"A media de todos os valores é = {media}")
