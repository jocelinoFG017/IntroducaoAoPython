"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
 - o total a pagar com desconto de 10 %.
 - o valor de cada parcela, no parcelamento de 3X sem juros.
 - a comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto).
 - a comissão do vendedor, no caso da venda ser parcelada(5% sobre o valor total).
"""

valor = float(input("Informe o valor: "))
desconto = valor-((valor*10)/100)
comissao = (desconto*5)/100
comissao2 = (valor*5)/100
print("Valor com 10% de desconto: {:.2f}".format(desconto))
print("Valor de cada parcela(3x sem juros sem desconto): {:.2f}".format(valor/3))
#print("Valor de cada parcela(3x sem juros com desconto): {:.2f}".format(desconto/3))
print("Comissão do Vendedor venda a vista: {:.2f}".format(comissao))
print("Comissão do Vendedor venda a parcelada: {:.2f}".format(comissao2))
