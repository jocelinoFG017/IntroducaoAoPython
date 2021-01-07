"""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi
multado. nesse caso, exiba o valor da multa, cobrando R$ 5 por km
acima de 80km/h
"""

velocidade = int(input("velocidade: "))
multa = 0
if velocidade > 80:
    multa = (velocidade-80) * 5
    print("multado em {} reais".format(multa))
else:
    print("tudo certo")