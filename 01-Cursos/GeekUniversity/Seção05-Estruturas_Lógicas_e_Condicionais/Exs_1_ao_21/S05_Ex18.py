"""
Faça um programa  que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básico, por exemplo). O usuário escolha uma das opções e o
seu programa então pede dois valores numéricos e realiza a operação, mos-
trando o resultado e saindo.
"""
print(" ---- Informe sua escolha de opção abaixo (somente um por vez) ---- ")
print("1 - Adição ")
print("2 - Subtração ")
print("3 - Divisão ")
print("4 - Multiplicação ")
op = int(input("Escolha de opção: "))

if (op > 0) and (op < 5):
    n1 = int(input("1º Número: "))
    n2 = int(input("2º Número: "))
    if op == 1:
        print("{} + {} = {}".format(n1,n2,n1+n2))
    elif op == 2:
        print("{} - {} = {}".format(n1, n2, n1 - n2))
    elif op == 3:
        if n2 == 0:
            print("n2 não pode ser zero")
        else:
            print("{} / {} = {}".format(n1, n2, n1 / n2))
    else:
        print("{} * {} = {}".format(n1, n2, n1 * n2))
else:
    print("Opção inválida.")
