"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é:  M = 0.91 * J, sendo J o comprimento em Jardas e M o comprimento em
metros.
"""
comprimento = float(input("Valor Comprimento(Jardas): "))
convert = comprimento * 0.91
print("Em Metros fica: {:.2f}".format(convert))
