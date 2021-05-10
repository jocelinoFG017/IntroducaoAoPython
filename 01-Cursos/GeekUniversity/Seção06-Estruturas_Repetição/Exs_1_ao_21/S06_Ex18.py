"""
.18.Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas
vezes o maior números foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""
qtd = int(input('Informe a quantidade de Nº a serem digitados: '))

maior = 0
count = 0

for i in range(1, qtd+1):

    numeros = int(input(f'numero {i}: '))

    if numeros > maior:
        maior = numeros
        count = 1
    elif maior == numeros:
        count = count + 1

print(f'maior = {maior}')
print(f'ocorrencias do maior numero = {count}')
