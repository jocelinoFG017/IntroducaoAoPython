"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversão é: F = C*(9.0/5.0)+32.0. sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
temp = float(input("Informe a temperatura(C): "))
f = temp*(9.0/5.0)+32
print(f"Em Fahrenheit é {f}")
