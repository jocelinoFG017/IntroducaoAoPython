"""
# O programa anterior do livro

fim = int(input("Digite  o último número a imprimir: "))
x = 0
while x <= fim:
    print(x)
    x = x +2

# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
"""
fim = int(input("Digite  o último número a imprimir: "))
x = 1
multiplo = 3
while x <= fim:
    #print(x)
    if x <= 10:
        print("{}º Multiplo de 3: {}".format(x,multiplo * x))
    x = x +1
