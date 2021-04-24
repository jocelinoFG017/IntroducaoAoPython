"""
Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
nota1 = int(input("Nota 01: "))
nota2 = int(input("Nota 02: "))
nota3 = int(input("Nota 03: "))
nota4 = int(input("Nota 04: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print("A média é = {:.2f}".format(media))
