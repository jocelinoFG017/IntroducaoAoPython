"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}


"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# outros EXEMPLOS

numeros = {x ** 2 for x in range(10)}
print(numeros)
# Desafio: Faça um alteração na estrutura acima para gerar um dicionario ao invés de um set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar
letras = {letra for letra in 'geek university'}
print(letras)
