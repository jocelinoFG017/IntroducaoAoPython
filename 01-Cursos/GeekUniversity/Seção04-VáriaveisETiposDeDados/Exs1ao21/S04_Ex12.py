"""
Leia um Distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é : K = 1.61 * M, sendo K distância em quilômetros e M em milhas
"""
dist = float(input("Informe a Distância(Milhas): "))
convert = dist*1.61
print("Convertido em Quilômetros fica: {:.2f}".format(convert))
