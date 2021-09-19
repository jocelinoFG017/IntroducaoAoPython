"""
Zip -> Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteráveis
passados como entrada em pares


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip))

# SEMPRE podemos gerar uma lista, tupla ou dicionario
print(list(zip1))
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

# o zip() utiliza como parametro o menor tamanho em iteravel. Isso significa que se estiver trabalhando
# com iteraveis de tamanhos diferentes, irá parar quando os elementos do menor iteravel acavar
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))



# Podemos utilizar diferentes iteraveis com zip

tupla = 1, 2, 3, 4, 5,
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas
dados = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(list(zip(*dados)))


"""
# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedra', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
