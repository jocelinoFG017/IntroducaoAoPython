"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as seguintes fórmulas (onde H corresponde à altura):
 - Homens: (72.7 * H) - 58
 - Mulheres: (62.1 * H) - 44.7
"""
altura = float(input("altura: "))
sexo = input("sexo: ")
calcula = 0

if sexo == "H" or sexo == "h":
    print("homem")
    calcula = (72.7 * altura) - 58
    print("Seu peso ideal é: {}".format(calcula))
elif sexo == "M" or sexo == "m":
    print("mulher")
    calcula = (61.2 * altura) - 44.7
    print("Seu peso ideal é: {}".format(calcula))
else:
    print("Dados Inválidos.")
