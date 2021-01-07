"""
Faça um programa que calcule o aumento de um salario. Ele deve solicitar o valor do salário
e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

salario = float(input("salario: "))
aumento = float(input("porcentagem aumento: "))
novoSalario = 0.0
aumento = (salario*aumento)/100
novoSalario = salario+(aumento)


print("Valor do aumento:",aumento)
print("novo salario: ",novoSalario)