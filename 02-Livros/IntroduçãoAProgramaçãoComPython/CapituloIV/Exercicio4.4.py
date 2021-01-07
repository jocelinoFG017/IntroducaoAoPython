"""
Escreva um programa que pergunte o salário do funcionario e calcule o
valor do aumento. Para salários superiores a R$1250.00, calcule um aumento de 10%.
para os inferiores ou iguais, de 15%.
"""

salario = float(input("salario: "))
aumento = 0

if salario> 1250.00:
    aumento = salario+((salario* 10)/100)
    print("salario+aumento: {}".format(aumento))
if salario <= 1250.00:
    aumento = salario + ((salario * 15) / 100)
    print("salario+aumento: {}".format(aumento))