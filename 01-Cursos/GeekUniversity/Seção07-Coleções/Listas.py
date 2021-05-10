"""
Listas em python:
 - São dinamicas: Ou seja não possuem tamanho fixo.
 - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja podemos colocar qualquer tipo de dado

em python as listas são representadas por []

lista1 = [1,5,3,4,2,2,2]
lista2 = ["1","g",'e']
lista3 = []
lista4 = list(range(11)) # LIST --> TRANSFORMA EM LISTA
print(lista4)
# encontrar valor em uma lista
if 8 in lista4:
    print("encontrado")
else:
    print("nao encontrado")

# ordenar lista
print(lista1)
lista1.sort()
print(lista1)


#Adicionar valores em uma lista
print(lista1)
lista1.append(43)
print(lista1)

#coloca a lista como elemento único(uma sublista)
lista1.append([8,12,13])
print(lista1)

#coloca cada elemento da lista como um valor adicional
lista1.extend([8,12,13])
print(lista1)


# juntar duas listas
lista6 = lista1 + lista2
print(lista6)

#inverter uma lista forma 1
lista1.reverse()
print(lista1)

#inverter uma lista forma 2
print(lista1[::-1])

# inserir valores na lista
lista1.insert(2, "novo valor")
print(lista1)

# copiar uma lista
lista6 = lista2.copy()
print(lista6)

#contar quantos elementos existem dentro de uma lista
print(len(lista2))

#remover o ultimo elemento de uma lista
# o pop não somente remove o ultimo elemento, como tambem o retorna

print(lista1)
lista1.pop()
print(lista1)

# podemos remover um elemento pelo indice
lista1.pop(2)
print(lista1)

# remover todos os elementos da lista
lista1.clear()
print(lista1)

#Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)


# converter uma string para uma lista
#xemplo 1
curso = "Programação em Python"
curso = curso.split()
print(curso)
# OBS : por default o split() separa os elementos da lista pelo espaço entre elas

#exemplo 2
curso = "programação, em , python, essencial"
curso = curso.split(",")
print(curso)

# Convertendo uma lista em String
lista6 = ["Programação","em","Python"]
print(lista6)
# Pega a lista6, coloca espaço entre cada elemento e transforma em uma String
curso = ' '.join(lista6)
print(curso)
# coloca $ entre cada elemento e transforma em uma String
curso = '$'.join(lista6)
print(curso)

# pode-se colocar qualquer tipo de dado em uma lista
lista6 = [1,2.1,True, 'geek',[21,12,42],'2']

# Iterando sobre listas

#Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma =soma + elemento
print(soma)


# Exemplo 2 - Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione a lista ou digite sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

"""
lista1 = [1,5,3,4,2,6,2]
lista2 = ['g','e','e','k']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek Universty')

print(lista1)
