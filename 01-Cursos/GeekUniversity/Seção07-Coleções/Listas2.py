"""
# Continuação

# utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Acesso aos elementos de forma indexada
cores = ['verde','amarelo', 'azul','branco']
print(cores[1]) # amarelo
print(cores[2]) # azul

# elementos indexados de forma inversa
# Para entender melhor pense na lista como um circulo
print(cores[-1]) # branco
print(cores[-2]) # azul

cores = ['verde','amarelo', 'azul','branco']
# gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice,cor)

    # encontrar o indice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 10, 5]
#Em qual indice da lista esta o valor 6 ?
print(numeros.index(6))
# retornao indice do primeiro elemento encontrado
print(numeros.index(5))

# fazer busca dentro de um range, ou seja, em qual indice começar a buscar
print(numeros.index(5, 0)) # Buscando apartir do indice 1
print(numeros.index(5, 3)) # Buscando apartir do indice 1

# fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # busca o indice do valor 8, entre os indices 3 a 6

lista1 = [1, 5, 3, 4, 2, 6, 2]
lista2 = ['g', 'e', 'e', 'k']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek Universty')

print(lista1)


#Revisao slicing
#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Trabalhando com slicing de listas, com o parametro inicio
lista = [1, 2, 3, 4]

print(lista[::]) # imprime toda a lista
print(lista[1:]) # inicia no indice 1 e pega todos os outros valores seguintes


# Parametro FIM
print(lista[:2]) # começa no indice 0, e pega até o indice 2 - 1
print(lista[:4]) # começa no indice 0, e pega até o indice 4 - 1
print(lista[1:3])# começa no indice 1, e pega até o indice 3 - 1

# Parametro PASSO

print(lista[1::2]) # começa em 1 e vai ate o final de 2 em 2
print(lista[::2]) # começa em 0 e vai ate o final de 2 em 2


#Invertendo valores em uma lista

nomes = ['geek', 'university']

nomes[0], nomes[1] = nomes[1], nomes[0]
# ou simplesmente utilize o reverse
print(nomes)


# Soma, Valor maximo, valor minimo, tamanho

lista = [1, 2, 3, 4, 5, 6, 7]

print(sum(lista))  # soma
print(max(lista))  # valor maximo
print(min(lista))  # valor minimo
print(len(lista))  # tamanho da lista


#transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
print(type(lista))

tupla  = tuple(lista)
print(tupla)
print(type(tupla))


#  desempacotamento de lista
lista = [1, 2, 3]

num1,num2,num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (shallow copy e deep copy)

lista = [1,2,3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)
#  Ao utilizarmos o copy() copiamos os dados para uma nova lista, mas estes dados
#  são independentes, não afetando a outra lista, isso chama-se deep copy

"""


# forma 2 shallow copy

lista = [1,2,3]
print(lista)

nova = lista

print(nova)

nova.append(4)
#veja que utilizamos a cópia via atribuição, utilizando este metodo
# as mudanças feitas em uma lista tambem são modificadas na outra lista
print(lista)
print(nova)
