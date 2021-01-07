"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A formula de conversão é: K = C + 273.15 . sendo K a temperatura em Kelvin
e C a temperatura em Celsius.
"""
temp = float(input("Informe a temperatura(C): "))
k = temp + 273.15
print("Em Fahrenheit é {:.2f}".format(k))
