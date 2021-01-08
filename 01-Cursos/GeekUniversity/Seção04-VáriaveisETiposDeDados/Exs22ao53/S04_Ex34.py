"""
Leia o valor de um raio de um círculo e calcule. Imprima a área do círculo
correspondente. A área do círculo é x * raio², considere x = 3.141592.
"""
raio = float(input("raio: "))
x = 3.141592
area = x * (raio*raio)

print("area do círculo: {:.2f}".format(area))
