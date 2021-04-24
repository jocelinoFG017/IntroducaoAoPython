"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = M/0.91 , sendo J o comprimento em Jardas e M o comprimento em
metros.
"""
comprimento = float(input("Valor Comprimento(Metros): "))
convert = comprimento/0.91
print("Em Jardas fica: {:.2f}".format(convert))
