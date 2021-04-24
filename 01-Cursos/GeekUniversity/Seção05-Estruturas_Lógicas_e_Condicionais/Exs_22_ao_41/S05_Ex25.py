"""
Calcule as raízes da equação de 2º grau:
Lembrando que:

 - x =  (- b +- raiz(delta))

 - delta = b²* (-4ac)
E ax²+bx+c = 0 representa uma equação de 2º grau.

A variável a tem que ser diferente de zero. Caso seja igual imprima a
mensagem "Não é equação de segundo grau."

 - Se delta < 0, não existe real. Imprima a mensagem "Não existe raiz"
 - Se delta = 0, existe raiz real, Imprima a raiz e a mensagem "Raiz única"
 - Se delta >= 0, Imprima duas raízes reais
"""
import math

a = int(input("Valor de A: "))

if a == 0:
    print("Não é equação de 2º grau")
else:
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))

    valorX = 0
    delta = 0

    delta = ((b*b) - (4*a*c))

    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        print("Raíz Única")
        valorX= -b / (2 * a)
        print("delta = 0, Raiz: {:.2f}".format(valorX))
    elif delta > 0:
        valorX = (-b + math.sqrt(delta)) / (2 * a)
        ValorX2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Raiz 1: {:.2f}".format(valorX))
        print("Raiz 2: {:.2f}".format(ValorX2))
