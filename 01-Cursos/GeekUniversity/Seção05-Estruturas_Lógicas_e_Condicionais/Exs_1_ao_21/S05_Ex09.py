"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima. Empréstimo não concedido, caso
contrário imprima: Empréstimo concedido.
"""
salario = float(input("salario R$: "))
prestacaoE = float(input("Prestação Empréstimo R$: "))

calcula = (salario*20)/100
# print(f"20% do salario = {calcula}")
if prestacaoE > calcula:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
