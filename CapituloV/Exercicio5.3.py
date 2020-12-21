"""
Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10,9,8...1,0 e Fogo! na tela.

"""

x = 10
while x <= 10 and x >= 0:
    print(x)
    if x == 0:
        print("Fogo!")
    x = x -1
