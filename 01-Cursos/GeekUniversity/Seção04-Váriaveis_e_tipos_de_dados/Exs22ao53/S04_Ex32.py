"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o
antecessor de seu dobro.
"""
n = int(input("Informe um numero: "))
tri = n * 3
sucT = tri + 1

dob = n * 2
antD = dob - 1

soma = antD + sucT
print("soma = {}".format(soma))
