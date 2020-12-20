"""
Escreva um programa que leia dois números e que pergunte qual operação
voce deseja realizar. você deve  poder calcular soma(+), subtração(-)
, multipicação(*) e a divisao(/). Exiba o resultado da operação solicitada
"""
n1 = float(input("Numero n1: "))
n2 = float(input("Numero n2: "))
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op  = int(input("Qual operação deseja realizar?"))
while (op != 0):
    if op == 1:
        print("1 - Adição Selecionada")
        print("{} + {}  = {}".format(n1, n2, n1+n2))
        break
    if op == 2:
        print("2 - Subtração Selecionada")
        print("{} - {}  = {}".format(n1, n2, n1-n2))
        break
    if op == 3:
        print("3 - Multiplicação Selecionada")
        print("{} * {}  = {}".format(n1, n2, n1*n2))
        break
    if op == 4:
        print("4 - Divisão Selecionada")
        print("{} / {}  = {}".format(n1, n2, n1/n2))
        break
