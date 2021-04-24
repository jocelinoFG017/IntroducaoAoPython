"""
Faça um programa que leia um número inteiro positivo de três digitos(de 100 a 999).
gere outro número formado pelos digitos invertidos do numero lido. Exemplo:
NumeroLido = 123
NumeroGerado = 321
"""

n = int(input("Informe um número de 100 a 999: "))
invert = int(str(n)[::-1])
print("Invertido fica: {}".format(invert))
