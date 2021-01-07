"""
Escreva um programa que pergunte a quantidade de KM percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias
pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
"""

QuantKM = float(input("KM: "))
QuantDias = float(input("Dias: "))

preco = (QuantKM * 0.15) + (QuantDias*60)
print("Preco a pagar: {}".format(preco))


