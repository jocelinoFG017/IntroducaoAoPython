"""
.5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
soma = 0
for i in range(0, 10):
    valor = int(input(f'Informe o valor {i+1}: '))
    soma = soma + valor
print(f"A soma de todos os valores é = {soma}")
