"""
Any e all

all()  -> Retorna True se todos os elementos do iterável são verdadeiros
ou ainda se o iterável está vazio. Retorna True ou False


print(all([0, 1, 2, 3, 4]))  # sao verdadeiros ? False, 0 é False
print(all([1, 2, 3, 4]))  # sao verdadeiros ? True
print(all('geek'))  # True

nomes = ['Carlos', 'Camila', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all([num for num in [4, 2, 10] if num % 2 == 0]))

Any -> Retorna True se qualquer elemento do iterável for verdadeiro. Se
o iteravel estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

print(any([num for num in [4, 2, 10, 6, 9] if num % 2 == 0])) # True

