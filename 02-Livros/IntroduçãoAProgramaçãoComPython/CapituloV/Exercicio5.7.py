"""
# O programa anterior do livro

fim = int(input("Digite  o último número a imprimir: "))
x = 0
while x <= fim:
    print(x)
    x = x +2
# modifique o programa anterior de forma que o usuário também digite o inicio
#e o fim da tabuada, em vez de começar com 1 e 10.
"""
inicio = int(input("Digite  o Inicio da tabuada: "))
fim = int(input("Digite  o fim da tabuada: "))
x = inicio
while x <= fim and x :
    print("{} * {} = {}".format(x, fim, fim * x))
    x = x + 1
