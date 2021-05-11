"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%.
"""
valor = float(input("Valor do Produto: "))
desconto = valor-((valor*12)/100)

print(f"Valor original = {valor}")
print("Valor com desconto {}".format(desconto))
