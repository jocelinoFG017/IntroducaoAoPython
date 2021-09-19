"""
Map

 - Com o map, fazemos o mapeamento de valores para função

import math


def area(r):
    # Calcula a area de um circulo com um raio r
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum do calculo
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - usando map

# map é uma função que recebe dois parametros : O primeira é a função e o segundo um iterável
# Retorna um map object
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
# OBS: Após utilizar a função map, depois da primeira utilização do resultado ele zera.

# Para fixar  - map

# Temos dados Iteráveis

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

# O map Object: f(a1),f(a2), f(...), f(an)

"""
# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26),
           ('Tokyo', 27), ('Nova York', 28)]

print(cidades)
# f = 9/5 * c + 32

# lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
