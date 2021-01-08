"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A
fórmula de conversão é: L = K/ 0.45, sendo K a massa em quilogramas e L a
massa em libras
"""
massa = float(input("Valor Massa(Quilogramas): "))
convert = massa / 0.45
print("Em Libras fica: {:.2f}".format(convert))
