"""
.28. Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor
    E, conforme mostra a fórmula a seguir:

    - E = 1 + 1/1! + 1/2! + 1/3! +.... 1/N!

"""
n = int(input('Digite um número: '))
E = 1

if n > 0:
    for i in range(1, n + 1):
        fatorial = 1
        for j in range(1, i + 1):
            fatorial *= j
        calculo = (1 / fatorial)
        E += calculo
    print("{:.2f}".format(E))
