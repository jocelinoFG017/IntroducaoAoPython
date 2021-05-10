"""
Entendendo o *args
 - O *args é um parametro, como outro qualquer
 utilizamos *args para defini-lo

 Mas oque é o parametro *args ?
 O parametro *args utilizado em uma função, coloca os valores extras informados
 como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis


# Exemplos

def soma_todos_numeros(n1, n2, n3):
    return n1+n2+n3

print(soma_todos_numeros(4, 5, 6))


# Entendendo o *args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'bem vindo geek'
    return 'nao o conheço'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'university', 3.145))

"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6] # lista de dados

# Desempacotador
print(soma_todos_numeros(*numeros))
# OBS: O * serve para que informemos ao python que estamos passando como argumento uma coleção de dados
# desta forma ele saberá que precisará antes desempacotar esses dados