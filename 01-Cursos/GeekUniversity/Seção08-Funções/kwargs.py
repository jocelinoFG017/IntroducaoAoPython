"""
**Kwargs
É só mais um parametro, mas diferente do *args que coloca os valores extras em uma
tupla, o **kwargs exige que utilizemos parametros nomeados, e transforma esses
parametros extras em um dicionario.

# exemplo

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor de {pessoa.title()} é {cor}')


cores(marcos='verde', julia='amarelo')
#OBS: Nem os parametros *args e **kwargs são obrigatórios.

cores()

cores(geek='navy')


#exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'cumprimento pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek !"
    return 'nao o conheço'


print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossa funções podemos ter(NESTA ORDEM):
# - Parametros obrigatórios;
# - *args;
# - Parametros default(não obrigatório);
# - **kwargs;


def minha_funcao(idade, nome,*args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('nao solteiro')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'felipe', eu='não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)


# Entendendo porque é importante manter a ordem dos parametros na declaração

#função com a ordem correta de parametros
#def mostra(a, b, *args, instrutor='geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]


#Função com a ordem incorreta de parametros
def mostra(a, b, instrutor='geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


# a = 1
# b = 2
# args = (3,)
# instrutor = 'geek'
# kwargs = {'sobrenome': 'university', 'cargo' = 'instrutor'}

print(mostra(1, 2, 3, sobrenome='university', cargo='instrutor'))

# Desempacotar com kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'felicity', 'sobrenome': 'Smoke'}

print(mostra_nomes(**nomes))  # desempacotando o dicionario com o duplo asterisco


"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a+b+c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(1, 2, 3)
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS: os nomes das chaves em um dicionario devem ser os mesmos dos parametros da função
# dicionario = dict(d=1, e=2, f=3) Type Error
# soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='geek')
soma_multiplos_numeros(**dicionario, lang='python')

