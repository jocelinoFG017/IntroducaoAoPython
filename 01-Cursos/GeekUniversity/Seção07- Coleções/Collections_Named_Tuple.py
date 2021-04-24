"""
Módulo Collections -> Named Tupple

# Recap tupla
tupla = (1, 2, 3,)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parametros.

"""

# Fazendo o import
from collections import namedtuple
#  Precisamos definir o nome e os parametros

#  Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

#  Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

#  Acessando os dados

#  Forma 1
print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome

#  Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('chow-chow'))

print(ray.count('chow-chow'))
