"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A formula de conversão é: C = K - 273.15 . sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""
temp = float(input("Informe a temperatura(K): "))
c = temp - 273.15
print("Em Fahrenheit é {:.2f}".format(c))
