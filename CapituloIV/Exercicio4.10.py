"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
elétrica. Pergunte a quantidade  de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o preço  a pagar de
acordo com a tabela a seguir.

#Tabela
            Preço pro tipo e faixa de consumo
    Tipo        | Faixa (kWh)   |       Preço
    --------------------------------------------
    Residencial | Até 500       |   R$ 0.40
    Residencial | Acima de 500  |   R$ 0.65
    Comercial   | Até 1000      |   R$ 0.55
    Comercial   | Acima de 1000 |   R$ 0.60
    Industrial  | Até 5000      |   R$ 0.55
    Industrial  | Acima de 5000 |   R$ 0.60
"""

quantidade = float(input("Quantidade Consumida (kWh): "))
print("Tipos \n R - Residêncial \n C - Comercial \n I - Industrial")
Tipo = input("Tipo de Instalação: ")
preco = 0
if Tipo == "R" or Tipo == "r":
    print("Tipo = ", Tipo)
    if quantidade <= 500:
        preco = quantidade * 0.40
        print("Preço a pagar R$ {:.2f} reais".format(preco))
    else:
        preco = quantidade * 0.65
        print("Preço a pagar:  R$ {:.2f} reais".format(preco))
#COMERCIAL
if Tipo == "C" or Tipo == "c":
    print("Tipo = ", Tipo)
    if quantidade <= 1000:
        preco = quantidade * 0.55
        print("Preço a pagar R$ {:.2f} reais".format(preco))
    else:
        preco = quantidade * 0.60
        print("Preço a pagar:  R$ {:.2f} reais".format(preco))
#INDUSTRIAL
if Tipo == "I" or Tipo == "i":
    print("Tipo = ", Tipo)
    if quantidade <= 5000:
        preco = quantidade * 0.55
        print("Preço a pagar R$ {:.2f} reais".format(preco))
    else:
        preco = quantidade * 0.60
        print("Preço a pagar:  R$ {:.2f} reais".format(preco))