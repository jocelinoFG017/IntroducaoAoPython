"""
Faça um programa que solicite o preço de uma mercadoria e
o percentual de desconto. Exiba o valor do desconto e o preço
a pagar.
"""

preco = float(input("pRECO: "))
desconto = float(input("DESCONTO %: "))

novoDesconto = (preco*(100/100 + desconto/100))-preco

print("desconto R$: {}".format(novoDesconto))
print("preço original: {}".format(preco))
print("preço com desconto: {}".format(preco-novoDesconto))