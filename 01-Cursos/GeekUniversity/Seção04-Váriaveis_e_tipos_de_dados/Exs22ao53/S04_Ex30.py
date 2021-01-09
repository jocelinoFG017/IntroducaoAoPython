"""
Leia um valor em real e a cotação do dolar. Em seguida, imprima
o valor correspondente em dólares.
"""
real = float(input("Valor em R$: "))
cotacao = float(input("Cotação em $: "))
convert = real * cotacao
print("Em dólares($) fica = {:.2f}".format(convert))
