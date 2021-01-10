"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
 - O número digitado ao quadrado
 - A raiz quadrada do número digitado
"""
n = float(input("Informe um número: "))
rq = pow(n,1/2)
if n >= 0:
    print("{} ao quadrado é = {:.2f}: ".format(n, n ** 2))
    print("Raiz Quadrada de {} é = {:.2f}: ".format(n, rq))