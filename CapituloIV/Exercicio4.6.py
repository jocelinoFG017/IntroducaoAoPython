"""
Escreva um programa que pergunte a distância que um passageiro deseja
percorrer em km. Calcule o preço  da passagem, cobrando R$ 0,50 por km
para viagens até 200km, e R$ 0,45 para viagens mais longas.
"""
distancia = float(input("Insira a distancia: "))

preco = 0
if distancia <= 200:
    preco = distancia * 0.50
    print("Preço a pagar R$ {} reais".format(preco))
else:
    preco = distancia * 0.45
    print("Preço a pagar R$ {} reais".format(preco))