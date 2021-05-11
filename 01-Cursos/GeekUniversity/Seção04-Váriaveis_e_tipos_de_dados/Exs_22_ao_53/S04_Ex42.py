"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salario-base. além
disso, ele paga 7% de imposto sobre o salário-base.
"""

salario = float(input("Informe o salário: "))
gratificacao = ((salario*5)/100)
imposto = ((salario*7)/100)
calculo = salario +(gratificacao - imposto)
print("Salário a receber = {:.2f}".format(calculo))
print(f"gratificação: {gratificacao}")
print(f"imposto {imposto}")
