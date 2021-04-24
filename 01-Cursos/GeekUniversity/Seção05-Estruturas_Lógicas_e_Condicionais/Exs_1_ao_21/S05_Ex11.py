"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela
a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8(2+5+1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem "Número inválido".
"""
n = int(input("Informe um número: "))
soma = 0
if n > 0:
    print(f"n = {n}")
    while n > 0:
        soma += n % 10
        n = n // 10
    print("Soma dos algarismo: {:.0f}".format(soma))
else:
    print("Número Inválido")
