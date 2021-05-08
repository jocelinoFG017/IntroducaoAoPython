"""
.20. Ler um sequencia de números inteiros e determinar se eles são pares ou não. Deverá ser informado
o número de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.
"""

n = int(input('Informe quantos numeros deseja digitar : '))
while n != 1000:
    for i in range(0, n):
        vlr = int(input(f'valor {i}: '))
