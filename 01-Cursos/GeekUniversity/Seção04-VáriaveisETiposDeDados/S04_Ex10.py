"""
Leia uma velocidade em km/h(quilometros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M m/s.
"""
vel = float(input("Informe a velocidade(km/h): "))
convert = vel/3.6
print("Convertida em m/s fica {:.2f}".format(convert))
