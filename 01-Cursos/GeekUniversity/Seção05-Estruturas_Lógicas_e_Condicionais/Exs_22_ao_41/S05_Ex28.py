"""
.28. Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor númerico digitado pelo usuário.

 - (a) Geométrica : raiz³(x * y * z)
 - (b) Ponderada : (x + (2 * y) + (3 * z)) / 6
 - (c) Harmônica : 1 / (( 1 / x) + (1 / y) + (1 / z))
 - (d) Aritmética: (x + y + z)/3
"""
x = int(input("Informe o valor de X: "))
y = int(input("Informe o valor de Y: "))
z = int(input("Informe o valor de Z: "))

print("A - Geométrica")
print("B - Ponderada")
print("C - Harmônica")
print("D - Aritmética")
op = input("Escolha uma média acima: ")

geometrica = (x * y * z) ** (1/3)
ponderada = (x + (2 * y) + (3 * z)) / 6
harmonica = 1 / (( 1 / x) + (1 / y) + (1 / z))
aritmetica = (x + y + z)/3

if op == "A" or op == "a":
    print("A - Geométrica escolhida \n")
    print("Média = {:.2f}".format(geometrica))
elif op == "B" or op == "b":
    print("B - Ponderada escolhida \n")
    print("Média = {:.2f}".format(ponderada))
elif op == "C" or op == "c":
    print("C - Harmônica escolhida \n")
    print("Média = {:.2f}".format(harmonica))
elif op == "D" or op == "d":
    print("D - Aritmética escolhida \n")
    print("Média = {:.2f}".format(aritmetica))
