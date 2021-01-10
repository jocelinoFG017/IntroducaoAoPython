"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""
n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))

if n1 > n2:
    print("{} é maior que {}".format(n1,n2))
else:
    print("{} é maior que {}".format(n2,n1))