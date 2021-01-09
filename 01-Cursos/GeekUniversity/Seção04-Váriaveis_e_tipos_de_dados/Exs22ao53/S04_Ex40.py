"""
Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que
deverá ser paga, sabendo-se que são descontados 8% para o imposto de renda.
"""

dias = int(input("Informe o Nº de dias: "))
valor = dias * 30.00
descontoIR = valor-(valor*12)/100
print("Valor a ser pago: {:.2f}".format(descontoIR))
