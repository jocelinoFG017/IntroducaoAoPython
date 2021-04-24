"""
Leia uma velocidade em m/s(metros por segundo) e apresente-a convertida km/h(quilometros por hora).
 A fórmula de conversão é: K = M*3.6, sendo K a velocidade em km/h e M em m/s.
"""
vel = float(input("Informe a velocidade(m/s): "))
convert = vel*3.6
print("Convertida em m/s fica {:.2f}".format(convert))
