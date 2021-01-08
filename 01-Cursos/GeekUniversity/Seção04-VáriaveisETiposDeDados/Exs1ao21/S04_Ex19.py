"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
formula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

volume = float(input("Valor Volume(litros): "))
convert = volume/1000
print("Em m³ fica: {:.2f}".format(convert))
