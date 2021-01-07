"""
Escreva  um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
exiba  os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período.
"""

depInicial = float(input("Deposito Inicial: "))
taxaJuros =  float(input("Taxa de Juros da Poupança: "))
x = 1
print("Deposito Inicial ",depInicial)
aux = depInicial
while x<= 24:
    print("------ Mes {} ------".format(x))
    aux = (aux + (aux*taxaJuros)/100)
    print("--- Total... {:.2f}".format(aux))
    print("-------------------")
    print("-------------------")
    x = x + 1


