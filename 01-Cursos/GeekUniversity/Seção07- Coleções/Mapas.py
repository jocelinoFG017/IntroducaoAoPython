"""
Mapas(maps) -> conhecidos em python como dicionarios


#  Iterar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$  {receita[chave]}')

#  Acessando as chaves
for chave in receita.keys():
    print(receita[chave])

#  Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#  Desenpacotamento de dicionarios
for chave, valor in receita.items():
    print(f'chave={chave} e  valor={valor}')
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita.keys())

#  soma,valor maximo e minimo,tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
