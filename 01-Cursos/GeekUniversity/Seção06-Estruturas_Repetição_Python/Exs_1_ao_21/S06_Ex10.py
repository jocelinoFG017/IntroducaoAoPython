"""
.10. Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
"""
soma = 0
for i in range(0, 50):
    if i % 2 == 0:
        soma = soma + i
        print(i)
print(f'soma de todos os Nº pares = {soma}')
