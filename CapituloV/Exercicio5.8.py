"""
 Escreva  um programa que leia dois números. Imprima o resultado da multilicação do primeiro pelo segundo.
 Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que  podemos
 entender a multipicação como somas sucessivas de um deles. assim 4*5 =  5+5+5+5 = +4+4+4+4+4
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))
aux = 0
aux2 = 0
soma = 0

if n1 < n2:
    aux = n1
    aux2 = n2
else:
    aux = n2
    aux2 = n1
print("{} * {} = ".format(n1,n2))

x = 0
while x != aux:
    soma = soma + aux2
    print("+",aux2)
    x = x + 1
print("total = ", soma)



