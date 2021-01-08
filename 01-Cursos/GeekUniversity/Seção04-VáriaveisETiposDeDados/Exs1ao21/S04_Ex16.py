"""
Leia um valor de comprimento em polegados e apresente-o convertido em centimetros.
a formula de conversão é: C = P*2.54, sendo C o comprimento de centimetros e P o
comprimento em polegadas.
"""
comprimento = float(input("Valor Comprimento(pol): "))
convert = comprimento * 2.54
print("Em centimetros fica: {:.2f}".format(convert))