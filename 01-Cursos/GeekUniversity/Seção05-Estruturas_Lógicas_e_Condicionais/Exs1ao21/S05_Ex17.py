"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

 - A = ((baseMaior + baseMenor)*altura)/2

 Lembre-se a base MAIOR e a base menor devem ser números maiores que zero.
"""
baseMaior = float(input("BaseMaior: "))
baseMenor = float(input("BaseMenor: "))
altura = float(input("Altura: "))


if baseMaior > 0:
    if baseMenor > 0:
        area = ((baseMaior + baseMenor) * altura) / 2
        print("A área do trapézio é = {:.2f}".format(area))
    else:
        print("A baseMenor deve ser maior que zero(0)")
else:
    print("A baseMaior deve ser maior que zero(0)")
