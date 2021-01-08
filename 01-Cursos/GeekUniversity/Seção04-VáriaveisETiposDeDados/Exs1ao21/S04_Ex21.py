"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas. A
fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a
massa em libras
"""
massa = float(input("Valor Massa(Libras): "))
convert = massa *0.45
print("Em Quilogramas fica: {:.2f}".format(convert))
