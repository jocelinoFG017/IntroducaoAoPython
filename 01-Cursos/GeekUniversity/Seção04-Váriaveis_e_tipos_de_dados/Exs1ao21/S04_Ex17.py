"""
Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
a formula de conversão é: P = C/2.54, sendo C o comprimento de centimetros e P o
comprimento em polegadas.
"""
comprimento = float(input("Valor Comprimento(pol): "))
convert = comprimento/2.54
print("Em centimetros fica: {:.2f}".format(convert))