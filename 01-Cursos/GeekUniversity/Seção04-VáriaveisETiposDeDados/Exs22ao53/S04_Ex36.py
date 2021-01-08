"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro é calulado por meio da seguinte fórmula:
V = pi * raio² * altura, onde pi = 3.141592.
"""
altura = float(input("Informa a altura: "))
raio = float(input("Informa o raio: "))
pi = 3.141592
volume = pi*(raio*raio)*altura

print("O volume do cilindro é = {:.3f}".format(volume))
