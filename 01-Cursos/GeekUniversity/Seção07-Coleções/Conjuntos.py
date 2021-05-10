"""
Conjuntos
 - Conjuntos em qualquer linguagem de programação, estamos fazendo referencia à teoria
   dos conjuntos da matemática.

 - Aqui no python os conjuntos são chamados de Sets.

 Da mesma forma que na matemática:
 - Sets(conjuntos) não possuem valores duplicados
 - Sets(conjuntos) não possuem valore ordenados
 - Elementos não são acessados via indice, ou seja, conjuntos não são indexados

 Conjuntos são bons para se utilizar quando precisamos armazenar elementos
 mas não nos importamos com a sua ordenação, quando não precisamos nos preocupar com
 chaves, valores e itens duplicados.
 Os conjuntos (Sets) são referenciados em python com {}

 Diferenças entre Conjuntos(Sets) e Mapas(Dicionarios):
  - Um dicionario tem chave/valor
  - Um conjunto tem apenas valor


#  Definindo um conjunto

#  Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(s)
print(type(s))
# OBS: ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# Sem gerar erro e não fará parte do conjunto

#  Forma 2 - Mais Comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print("tem o 3")
else:
    print("Não tem o 3")


#  Importante lembra que conjuntos, além de não terem valores duplicados não tem ordem

# Listas aceitam valores duplicados , entao temos 10 elementos
lista = [99, 2, 32, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista}')

# Tuplas aceitam valores duplicados , entao temos 10 elementos
tupla = (99, 2, 32, 23, 2, 12, 1, 44, 5, 34)
print(f'tupla: {tupla}')

# Dicionarios não aceitam chaves duplicadas, entao temos 8 elementos
dicionario = {}.fromkeys([99, 2, 32, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionario: {dicionario}')

# Conjuntos não aceitam valores duplicados, entao temos 8 elementos
conjunto = {99, 2, 32, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto: {conjunto}')


# Podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 23.12, 45}
print(s)
print(type(s))

# Podemos iterar em sets normalmente
for valor in s:
    print(valor)


# Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu.
# E os visitantes informam manualmente a cidade de onde vieram.
# Nos adicionamos cada cidade em uma lista python, já que uma lista aceita elementos repetidos

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos quantas cidades distintas temos(únicas).
# oque voce faria? um loop na lista?
# Podemos utilizar set para isso:

print(len(set(cidades)))


#  Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
print(s)


#  Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

#  Forma 1 -
s.remove(3)  # Não é indice, informamos o valor a ser removido, por que conjuntos não sao indexados
print(s)

#  Forma 2
s.discard(2)  # nessa forma, se o valor Ñ for encontrado nenhum erro é gerado
print(s)

#  Copiando um conjunto para outro...

# Forma 1 - deep copy

novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow copy
novo = s
novo.add(4)
print(novo)
print(s)

#  Remover todos os itens de um conjunto
s.clear()
print(s)

#  Métodos matemáticos de conjuntos

#  Imagine que temos dois conjuntos, um contendo estudantes do curso de python e outro do curso de java
estudante_python = {'Marcos', 'Patricia', 'Ellen', 'Julia', 'Pedro', 'Guilherme'}
estudante_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
#  Veja que alguns alunos que estudam python também estudam java
#  Precisamos gerar um conjunto com nomes de estudantes unicos

#  Forma 1 - Utilizando Union
unicos1 = estudante_python.union(estudante_java)
print(unicos1)

#  Forma 2 - Utilizando o caractere pipe |
unicos2 = estudante_python | estudante_java
print(unicos2)

# gerar um conjunto de estudantes  que estao em ambos os cursos

#  Forma 1 - Utilizando intersection
ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)

#  Forma 2 - Utilizando o &
ambos2 = estudante_python & estudante_java
print(ambos2)

# gerar um conjunto de estudantes que nao estao no outro
so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)
"""
#  soma, valor maximo e minimo, e tamanho

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))


