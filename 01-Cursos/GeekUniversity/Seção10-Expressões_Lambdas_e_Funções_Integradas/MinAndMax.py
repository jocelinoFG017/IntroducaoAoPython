"""
Min() e Max()

max() -> retorna o maior valor  ou o maior de dois ou mais elementos

#  Exemplos
lista = [1, 2, 8, 4, 23, 123]
print(max(lista))

tupla = (1, 2, 8, 4, 23, 123)
print(max(tupla))

conjunto = {1, 2, 8, 4, 23, 123}
print(max(conjunto))

dicionario = {'a': 1, 'b': 2, 'c': 8, 'd': 4, 'e': 23, 'f': 123}
print(max(dicionario.values()))


# Faça um programa que receba dois valores e retorna o maior valor
vlr1 = int(input("VALOR 1: "))
vlr2 = int(input("VALOR 2: "))

print(max(vlr1, vlr2))

print(max(1, 34, 15, 65, 12))
print(max('a', 'abc', 'ab'))
print(max('a', 'b','c', 'g'))

min() -> Contrário do max()

# outros exemplos

nomes = ['Arya', 'Joel', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))
"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

#  DESAFIO! imprimir o titulo da musica mais e menos tocada
print('desafio')
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! imprimir o titulo da musica mais e menos tocada sem usar o min(), max() e lambda
print('desafio 2')

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']


for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

