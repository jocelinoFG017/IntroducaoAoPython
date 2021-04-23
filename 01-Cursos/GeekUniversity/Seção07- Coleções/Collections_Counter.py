"""
Módulo Collections - Counter(Contador)

Collections -> high-performance Container Datatypes

Counter - Recebe um iteravel como parametro e cria um objeto do tipo collections Counter,
que é parecido com um dicionario, contendo como chave o elemento da lista passada como parametro e
como valor a quantidade de ocorrências desse elemento

#  Realizando o import
from collections import Counter

#  Exemplo 1

#  Podemo utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 2, 5, 53, 12, 4, 5, 1, 1, 2, 2]
#  Utilizando Counter
res = Counter(lista)
# Para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrências
print(type(res))
print(res)

# Exemplo 2
print(Counter('geek University'))
"""
from collections import Counter

texto = """ 
É creditada como uma das responsáveis por reavivar o teen pop no final da década de 1990 
e somar sua habilidade vocal para discursar sobre temas como a sexualidade e o feminismo. 
Ao passo em que continuamente reinventava sua imagem, tornou-se conhecida por seus visuais
 extravagantes e não convencionais. Além de provocar polêmica, seus trabalhos foram 
 elogiados pela crítica especializada, pelos quais tem sido citada
como influência para diversos artistas. 
"""

palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)
#  Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
