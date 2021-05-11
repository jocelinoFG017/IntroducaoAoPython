"""
Leia um valor de área em hectares e apresente-o em metros quadrados m². A fórmula
de conversão é: M = H * 10.000, sendo M a área em m² e H a área em hectares.
"""
area = float(input("Valor da hectares: "))
convert = area * 10.000
print("Em m² fica: {:.4f}".format(convert))
