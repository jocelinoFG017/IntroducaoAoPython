"""
Escreva um programa que, dado dois números inteiros, mostre  na tela
o maior deles, assim como a diferença existente entre ambos.
"""
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
dif = 0
if n1 > n2:
    print(f"O maior: {n1}")
    dif = n1 - n2
    print(f"A diferença: : {dif}")
else:
    print(f"O maior: {n2}")
    dif = n2 - n1
    print(f"A diferença: {dif} ")