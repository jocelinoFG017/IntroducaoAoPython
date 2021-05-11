"""
List Comprehensions Parte 1 e 2
 -Utilizando List Comprehensions nós podemos gerar novas listas com dados processados
 a partir de outro iterável.
 # Sintaxe de List comprehensions
    - [dado for dados in iterável]

# Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

# OBS: Para entender melhor oque está acontecendo devemos dividir a expressão em duas partes
#  - A primeira parte: for numero in numeros
#  - A segunda parte: numero * 10
def funcion(valor):
    return valor * valor


res = [funcion(numero) for numero in numeros]
print(res)

# List comprehensions VS Loop

# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)

# List Comprehensions
print([numero * 2 for numero in numeros])


# Outros Exemplos
# 1

nome = 'geek university'
print([letra.upper() for letra in nome])

# 2


def upp(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']
print([upp(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

#################################################################
##################### PARTE 2 A PARTIR DE DAQUI #################
#################################################################
List Comprehensions
 -  Nós podemos adicionar estruturas condicionais lógicas às nossas list Comprehension

"""

# Exemplos
# 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par módulo de 2 é 0. 0 é False em python. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero impar módulo de 2 é 1. 1 é True em Python
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
