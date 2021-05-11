"""
Leia um número inteiro de 4 dígitos(de 1000 a 9999) e imprima um dígito por linha
"""

n = int(input("Informe um número de 1000 a 9999: "))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print(m)
print(c)
print(u)
print(d)
