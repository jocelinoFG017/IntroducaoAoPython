"""
Módulo Collections - Ordered Dict

#  Em um dicionario, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for chave, valor in dicionario.items():
    print(f'chave= {chave}:valor= {valor}')

# Ordered Dict é um dicionario que nos garante a ordem de inserção dos elementos.

#  Fazendo o import
from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave,valor in dicionario.items():
    print(f'chave= {chave}: valor= {valor}')
"""
# Entendendo a diferença entre Dict e Ordered Dict
from collections import OrderedDict
# Dicionarios comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True, já que a ordem dos elementos não importa para os dicionarios comuns
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False, já que as ordens dos elementos importa para o Ordered Dict