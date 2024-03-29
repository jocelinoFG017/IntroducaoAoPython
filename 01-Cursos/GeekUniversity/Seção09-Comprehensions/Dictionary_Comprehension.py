"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:
lista  = [1, 2, 3, 4]

Se quisermos criar uma tupla:
tupla = (1, 2, 3, 4)

Se quisermos criar um conjunto(set):
conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionario:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#   Sintaxe
{chave:valor for valor in iterável} -> Dictionary comprehension
{valor for valor in iterável} -> List comprehension


# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# exemplo 2
numero = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numero}

print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

"""
# exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
