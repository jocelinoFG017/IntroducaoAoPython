"""
Generators Expression

Aulas anteriores fora vistos;
 - List Comprehension;
 - Dictionary Comprehension;
 - Set Comprehension;
 Não vimos:
    - Tuple Comprehension.... porque elas se chamam generators



nomes = ['Carlos', 'Camila', 'Carla', 'Vanessa']

#  List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#  Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


# Utilidade de getsizeof() -> Retorna a quantidade em bytes da memória do elemento passado
# como parametro

from sys import getsizeof

#  Mostra quantos bytes a string está ocupando.

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))


from sys import getsizeof

#  Gerando uma lista de Numeros com list Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

#  Gerando uma lista de Numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#  Gerando uma lista de Numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

#  Gerando uma lista de numeros com o generator
gen = getsizeof((x * 10 for x in range(1000)))

print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension: {set_comp}')
print(f'Dict Comprehension: {dic_comp}')
print(f'Generator Expression: {gen}')

"""
#  Posso iterar ? Sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

