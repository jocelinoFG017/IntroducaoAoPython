"""
Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5,
mas não simultaneamente pelos dois.
"""

n = int(input("Informe un número: "))

if (n % 3 == 0) and (n % 5 == 0):
    print("Divisível por 3 e 5")
else:
    if n % 3 == 0:
        print("Divisível por 3")
    if n % 5 == 0:
        print("Divisível por 5")
# print("Divisível por 3 e 5")
