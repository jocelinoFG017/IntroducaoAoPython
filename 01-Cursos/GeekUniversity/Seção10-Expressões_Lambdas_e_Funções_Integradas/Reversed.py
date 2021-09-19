"""
Reversed

OBS: NÃO confundir com a funcao reverse() estudada em lista
A funcao reverse() só funciona em listas, já a reversed() funciona em qualquer
iteravel.

A função reversed() retorna um iteravel chamado
ListReversedIterator
"""

#  Exemplos

lista = [1, 2, 3, 4, 5, 6]
res = reversed(lista)

print(res)
print(type(res))
# podemos reverted o elemento retornado para um lista, tupla ou conjunto

# lista
print(list(reversed(lista)))

#  tupla
print(tuple(reversed(lista)))

# OBS: em conjuntos não definimos a ordem dos elementos
# Conjunto(set)
print(set(reversed(lista)))


# podemos iteravel sobre o reversed

for letra in reversed("Geek University"):
    print(letra, end='')

#  Mesmo uso sem o for
print('\n')
print(''.join(list(reversed('Geek University'))))

# Slice de String
print('Geek University'[::-1])

# Podemos utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print('n')

# podemos fazer isso utilizando o range()
for n in range(9, -1, -1):
    print(n)
