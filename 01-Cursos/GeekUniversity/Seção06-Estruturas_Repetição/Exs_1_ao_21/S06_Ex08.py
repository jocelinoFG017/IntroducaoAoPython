"""
.8. Escreva um programa que leia 10 números e escreva o menor valor lido e o
maior valor lido.
"""
maior = 0
menor = 999999
for i in range(0, 5):
    num = int(input(f'Informe o valor {i+1}: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'maior = {maior}')
print(f'menor = {menor}')
