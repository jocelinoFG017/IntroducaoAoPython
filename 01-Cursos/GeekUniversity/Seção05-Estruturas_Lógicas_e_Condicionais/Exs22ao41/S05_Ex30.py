"""
.30. Faça um programa que receba três números e mostre-os em ordem crescente.
"""
n1 = int(input("Informe o n1: "))
n2 = int(input("Informe o n2: "))
n3 = int(input("Informe o n3: "))

print(" n1 = {} \n n2 = {} \n n3 = {}".format(n1,n2,n3))
print("Ordem Crescente")

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("{} {} {}".format(n3, n2, n1))
    else:
        print("{} {} {}".format(n2, n3, n1))
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print("{} {} {}".format(n3, n1, n2))
    else:
        print("{} {} {}".format(n1, n3, n2))
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print("{} {} {}".format(n2, n1, n3))
    else:
        print("{} {} {}".format(n1, n2, n3))
else:
    print("Números iguais")


