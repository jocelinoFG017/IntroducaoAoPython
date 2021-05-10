"""
Tuplas Imutáveis e são representadas por ()

#cuidado 1: As tuplas são representadas por (), mas veja

tupla1 = (1 , 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1 , 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4) # isso não é uma tupla
print(tupla3)

print(type(tupla3))
tupla4 = (4, ) # isso é uma tupla
print(tupla4)
print(type(tupla4))

# Tuplas são definidas pelo uso da virgula, e não dos parenteses()

# Gerar tupla dinamica com range (inicio,fim, passo)
tupla = tuple(range(11))
print(tupla)

# desenpacotamento de tupla
tupla = ('geek university', 'python')
escola, curso = tupla

print(escola)
print(curso)

#  soma, valor maximo, valor minimo e tamanho
tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#  concatenação de tuplas
tupla1 = (1, 2, 3, )
print(tupla1)

tupla2 = (4, 5, 6, )
print(tupla2)

print(tupla1 + tupla2)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3, )
print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3, )
for n in tupla:
    print(n)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('geek university')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas

#Deve-se utilizar sempre que não seja necessário modificar os dados cntidos em uma coleção

# Exemplo 1
meses= ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')
print(meses)

#  Acesso aos elementos das tuplas é semelhante ao de uma lista
print(meses[5])

#  Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

 # verificamos em qual indice um elemento está na tupla
print(meses.index('Junho'))

# slicing

# tupla[inicio:fim:passo]

print(meses[0:])


"""

#  Por que utilizar tuplas ?
#  - tuplas são mais rápidas do que listas
#  - tuplas deixam seu código mais seguro*
#  *(isso pq trabalhar com elementos imutáveis traz segurança para o código)

# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de shallow copy
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)