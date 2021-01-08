"""
Sejam A e B os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √(a²+b²). Faça um programa que receba os valores de A e B e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""
import math
a = float(input("Valor A: "))
b = float(input("Valor B: "))

result = ((a*a)+(b*b))
hip = math.sqrt(result)
#hip = result ** 0.5

print("O valor da hipotenusa é {:.2f}".format(hip))
