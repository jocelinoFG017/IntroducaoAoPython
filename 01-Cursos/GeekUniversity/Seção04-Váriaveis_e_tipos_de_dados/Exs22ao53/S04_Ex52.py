"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada um deu para realização da aposta. Faça um
programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia do prêmio com base no valor investido.
"""
valor = float(input("Valor do Prêmio: "))

aposta1 = float(input("Valor da Aposta 01: "))
aposta2 = float(input("Valor da Aposta 02: "))
aposta3 = float(input("Valor da Aposta 03: "))

total = aposta1 + aposta2 + aposta3

aux1 = (aposta1 / total) * valor
aux2 = (aposta2 / total) * valor
aux3 = (aposta3 / total) * valor


print("Aposta 01 ganhou R$: {:.2f} reais".format(aux1))
print("Aposta 02 ganhou R$: {:.2f} reais".format(aux2))
print("Aposta 03 ganhou R$: {:.2f} reais".format(aux3))