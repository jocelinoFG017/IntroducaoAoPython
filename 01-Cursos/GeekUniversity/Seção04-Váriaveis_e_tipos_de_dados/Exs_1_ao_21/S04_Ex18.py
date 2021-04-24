"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A
formula de conversão é: L = 1000*M, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

volume = float(input("Valor Volume(m³): "))
convert = volume*1000
print("Em Litros fica: {:.2f}".format(convert))
