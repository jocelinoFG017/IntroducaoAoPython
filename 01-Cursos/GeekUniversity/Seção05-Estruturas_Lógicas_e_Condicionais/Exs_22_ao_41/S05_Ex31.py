"""
.31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a
seguir, verifique e mostre qual a classificação dessa pessoa.

 - ALTURA          |   PESO              PESO                PESO
 - ALTURA          | ATÉ 60 | ENTRE 60 E 90 (INCLUSIVE) | ACIMA DE 90
 - Menor que 1,20  | A      |            D              | G
 - de 1,20 a 1,70  | B      |            E              | H
 - Maior que 1,70  | C      |            F              | I
"""

altura = float(input("Altura: "))
peso = float(input("Peso: "))

if altura <= 1.20 :
    if peso <= 60:
        print("A")
    elif (peso > 60 )and peso <= 90:
        print("D")
    elif peso > 90:
        print("G")
elif altura > 1.20 and (altura <= 1.70):
    if peso <= 60:
        print("B")
    elif (peso > 60) and peso <= 90:
        print("E")
    elif peso > 90:
        print("H")
elif altura > 1.70:
    if peso <= 60:
        print("C")
    elif (peso > 60) and peso <= 90:
        print("F")
    elif peso > 90:
        print("I")
