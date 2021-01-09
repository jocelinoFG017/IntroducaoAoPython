"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão é: C = 5.0*(F-32)/9.0. sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
temp = float(input("Informe a temperatura(F): "))
c = 5.0*(temp-32)/9.0
print(f"Em Fahrenheit é {c}")
