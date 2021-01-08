"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%¨.
"""
salario = float(input("Valor do salário: "))
aumento = salario+((salario*25)/100)

print(f"salario original = {salario}")
print("salario com aumento = {:.2f}".format(aumento))
