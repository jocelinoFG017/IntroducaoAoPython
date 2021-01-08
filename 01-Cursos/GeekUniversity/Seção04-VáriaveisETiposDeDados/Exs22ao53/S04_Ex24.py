"""
Leia um valor de área em metros quadrados m² e apresente-o em acres. A fórmula
de conversão é: A = M * 0.000247, sendo M a área em m² e A a área em acres.
"""
area = float(input("Valor da área (M²): "))
convert = area * 0.000247
print("Em Acres fica: {:.6f}".format(convert))

