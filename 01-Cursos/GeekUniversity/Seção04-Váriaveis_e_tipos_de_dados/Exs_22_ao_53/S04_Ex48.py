"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
x = int(input())

hora = x // 3600
resto = x % 3600

minutos = resto // 60
resto= resto % 60
seg = resto // 1
print("{}h:{}m:{}s".format(hora, minutos, seg))
# print("{} horas : {} min: {} seg".format())
