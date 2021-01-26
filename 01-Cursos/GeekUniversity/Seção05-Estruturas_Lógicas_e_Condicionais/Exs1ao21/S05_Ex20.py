"""
Dados três valores, A,B,C, verificar se eles podem ser valores dos lados de um triângulo e,
se forem, se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos

 - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.

 - Chama-se equilátero o triângulo que tem três lados iguais.

 - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.

 - Recebe o nome de escaleno o triângulo que tem três lados diferentes.
"""

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

if a == c and a == b and b == c:
    print("Triângulo Equilátero.")
elif (a != b) and (a != c) and (b != c):
    print("Triângulo Escaleno.")
else:# (a == b) or (a == c) or (b == c):
    print("Triângulo Isósceles.")

