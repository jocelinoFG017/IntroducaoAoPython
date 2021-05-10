"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance

"""
#  Fazendo o import
from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final da lista
print(deq)
deq.appendleft('k')  # Adiciona no começo da lista
print(deq)

# Remover elementos
print(deq.pop())  # Remove o ultimo elemento
print(deq)

print(deq.popleft())  # remove e retorna o primeiro elemento
print(deq)
