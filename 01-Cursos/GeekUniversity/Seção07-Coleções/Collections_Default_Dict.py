"""
Módulo Collections - Default Dict

Default Dict -> Ao criar um dicionario o default dict, nós informamos um valor
default, podendo utilizar um labda para isso. Este valor será utilizado sempre
que não houver um valor definido. Caso tentemos acessar a chave que não existe,
essa chave será criada e o valor default será atribuido.

#  Relembrando dicionarios

dicionario = {'curso': 'Programação em python'}
print(dicionario)
print(dicionario['curso'])

# OBS: Lambdas são funcões sem nome, que podem ou não receber parametros de entrada e retornar valores.
"""
#  Fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em python'
print(dicionario)

print(dicionario['outro'])  # KeyError no dicionario comum, mas aqui não
print(dicionario)



