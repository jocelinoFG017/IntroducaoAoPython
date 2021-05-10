"""
Dicionários (Dictionaries)
OBS: Em algumas linguagens de programação os dicionários python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.
Dicionários são representados por {}.
print(type({}))

# Criação de Dicionários

#  Forma1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}

print(paises)

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos')

print(paises)

#  Acessando elementos

# Forma 1 = Acessando via chave

print(paises['br'])
print(paises['eua'])
#  OBS: caso a chave de acesso esteja incorreta, teremos um KeyError

# Forma 2= Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# pode-se definir um valor default, caso nao seja
# encontrado o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')
print(pais)

#  Pode-se verificar se determinada chave se encontra em um dicionario
print('br' in paises) #  chave
print('ru' in paises)
print('Estados Unidos' in paises) #  valor

#  Podemos utilizar qualquer tipo de dado (int, boolean, float, string)

# tuplas sao bastante interessante de serem utilizadas como chaves de dicionario
localidades = {
    (34.1812, 89.1527): 'Escritório em Tókyo',
    (14.1316, 19.1319): 'Escritório em Ipanema',
    (24.1517, 29.13298): 'Escritório em Terezina',
}
print(localidades)
print(type(localidades))


#  Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)

#  Forma 1 - mais comum
receita['abr'] = 350
print(receita)

#  Forma 2
novo_dado = {'mai': 500}

receita.update(novo_dado)
print(receita)

#  Atualizando dados em um dicionario

#  Forma 1
receita['mai'] = 550
print(receita)

#  Forma 2
receita.update({'mai': 600})
print(receita)

#  a forma de adicionar e atualizar dados em dicionarios é a mesma
#  Em dicionários NÃO podemos ter chaves repetidas.

#  Remover dados de um dicionario
receita = {'jan': 100, 'fev': 200, 'mar': 300}
print(receita)
#  Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)
#  OBS: precisamos sempre informar a chave, caso o elemento nao seja encontrado , um KeyError é retornado
#  OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado

#  Forma 2
del receita['fev']
print(receita)
# Neste caso o valor do objeto removido não é retornado


# exemplo carrinho de compras
carrinho = []
produto1 = {'nome': 'playstation4', 'quantidade': '1', 'preco': 2300}
produto2 = {'nome': 'god of war', 'quantidade': '1', 'preco': 150}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)


# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionario (Zerar os dados)
d.clear()
print(d)


# Copiando um dicionário para outro

# Forma 1 - Deep copy
novo = d.copy()

print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow copy

novo = d
novo['d'] = 4
print(d)
print(novo)
"""
# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
#  OBS: O método fromkeys recebe dois parametros um iteravel e um valor.
#  Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave um valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)