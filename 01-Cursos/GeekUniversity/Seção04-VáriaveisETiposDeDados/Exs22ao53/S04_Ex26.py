"""
Leia um valor de área em metros quadrados m² e apresente-o em hectares. A fórmula
de conversão é: H = M * 0.0001, sendo M a área em m² e H a área em hectares.
"""
area = float(input("Valor da área (M²): "))
convert = area * 0.0001
print("Em Hectares fica: {:.4f}".format(convert))

