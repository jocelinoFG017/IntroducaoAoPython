"""
Leia um valor de área em acres e apresente-o em metros quadrados m². A fórmula
de conversão é: M = A * 4048.58, sendo M a área em m² e A a área em acres.
"""
area = float(input("Valor da área (Acres): "))
convert = area * 4048.58
print("Em M² fica: {:.2f}".format(convert))
