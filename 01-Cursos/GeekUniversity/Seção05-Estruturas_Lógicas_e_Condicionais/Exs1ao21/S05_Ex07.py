"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem Números Iguais.
"""
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))


if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Números Iguais")