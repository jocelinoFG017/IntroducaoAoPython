"""
# O programa anterior do livro

fim = int(input("Digite  o último número a imprimir: "))
x = 0
while x <= fim:
    print(x)
    x = x +2

#Altere o programa anterior para exibir os  resultados no mesmo formato de tabuada: 2x1 =2, 2x2= 4,...
"""
fim = int(input("Digite  o fim da tabuada: "))
x = 1
while x >= 1 and x <= 10:
    #print(x)
    print("{} * {} = {}".format(fim, x, fim*x))
    x = x +1