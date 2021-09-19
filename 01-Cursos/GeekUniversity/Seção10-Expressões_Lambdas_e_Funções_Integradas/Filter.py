"""
Filter

filter() -> serve para filtrar dados de uma determindada coleção.

# Biblioteca utilizada para trabalhar com dados estatisticos
import statistics

# dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean()
# mean() -> realiza a media dos valores

media = statistics.mean(dados)

print('media = {:.2f}'.format(media))

# assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))
# OBS: Assim como na função map(), após serem utilizados os dados de filter()
# eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um iterável  e retorna um objeto
# mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável  e retorna um objeto
# filtrando apenas os elementos de acordo com a função.


"""
# Exemplo mais complexo
usuarios = [
    {"username": "Samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": 'Carla', 'tweets': ['eu amo gatos']},
    {"username": 'Bob123', 'tweets': []},
    {"username": 'Doggo', 'tweets': []},
    {"username": 'Joshua', 'tweets': ['eu amo cachorros', 'Vou sair hoje']}
]
print(usuarios)
# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

# combinar filte() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# DEVEMOS criar uma lista contendo 'sua instrutora é ' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
