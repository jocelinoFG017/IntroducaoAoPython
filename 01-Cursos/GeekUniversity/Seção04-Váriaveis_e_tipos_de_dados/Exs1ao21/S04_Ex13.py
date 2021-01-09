"""
Leia um Distância em quilômetros e apresente-a convertida em milhas. A fórmula de
conversão é : M = k/1.61, sendo K distância em quilômetros e M em milhas
"""
dist = float(input("Informe a Distância(quilômetros): "))
convert = dist/1.61
print("Convertido em Milhas fica: {:.2f}".format(convert))
