"""
Sorted
OBS-> NÃO confundir com o sort()
podemos utilizar o sorted() com qualquer iteravel.

Sorted() -> serve para ordenar
OBS: O sorted(), sempre retorna uma lista com os elementos do iteravel ordenados


# exemplo
numeros = [5, 1, 7, 6]
print(numeros)

print(sorted(numeros)) # ordena do menor para o maior
print(numeros)


numeros = [5, 1, 7, 6]
print(numeros)
print(sorted(numeros))
#  Adicionando parametros ao sorted()

print(sorted(numeros, reverse=True)) # ordena do maior para o menor


# PODEMOS utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "Samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": 'Carla', 'tweets': ['eu amo gatos']},
    {"username": 'jeff', 'tweets': []},
    {"username": 'Bob123', 'tweets': [], "cor": "amarelo"},
    {"username": 'Doggo', 'tweets': [], "cor": "amarelo", "musica": "rock"},
    {"username": 'Joshua', 'tweets': ['eu amo cachorros', 'Vou sair hoje']}
]
print(usuarios)
# ordenando pelo username - ordem AZ
print(sorted(usuarios, key=lambda usuario: usuario['username']))

#  Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))


"""
#  Ultimo exemplo
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
]
#  ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
