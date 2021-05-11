"""
Faça um programa que leia o valor da hora de trabalho(em reais) e o número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""
valorHora = float(input("Valor Hora Trabalhada R$: "))
horaTrab = float(input("Horas Trabalhada : "))
valor = valorHora * horaTrab
calc = valor+((valor*10)/100)
print("Valor a ser pago = {}".format(calc))
