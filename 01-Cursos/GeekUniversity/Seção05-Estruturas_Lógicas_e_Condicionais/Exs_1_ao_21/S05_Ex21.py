"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números. (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).
opção =
"""
print(" ---- Informe sua escolha abaixo ---- ")
print("1 - Soma ")
print("2 - Diferença (M-m)")
print("3 - Produto ")
print("4 - Divisão ")
op = int(input("Escolha de opção: "))

if (op > 0) and (op < 5):
    n1 = int(input("1º Número: "))
    n2 = int(input("2º Número: "))
    if op == 1:
        print("{} + {} = {}".format(n1, n2, n1+n2))
    elif op == 2:
        if n1 > n2:
            print("{} - {} = {}".format(n1, n2, n1 - n2))
        else:
            print("{} - {} = {}".format(n1, n2, n2 - n1))
    elif op == 3:
        print("{} * {} = {}".format(n1, n2, n1 * n2))
    else:
        # numerador = n1
        denominador = n2
        if denominador == 0:
            print("O denominador(n2) não pode ser zero")
        else:
            print("{} / {} = {:.2f}".format(n1, n2, n1 / n2))
else:
    print("Opção inválida.")
