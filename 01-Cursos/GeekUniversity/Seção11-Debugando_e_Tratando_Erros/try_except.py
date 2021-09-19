"""
O bloco Try/Except
Uitlizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Prevenindo que o programa para de funcionar e o usuario receba mensagens de erros
inesperadas.

A forma geral mais simples é :

try:
    //execução problematica
except:
    / oque deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print("algo está errado")


# Exemplo 2 - Tratando um erro genérico
try:
    len(5)
except:
    print('ALGO está errado')

## OBS: Tratar erros de forma generica não é a melhor forma de tratamento de erros. O ideal é sempre
tratar erros de forma especifica.


# Exemplo 3 - Tratando um erro especifico
try:
    geek()
except NameError:
    print('Voce está utilizando uma funcao inexistente')


# Exemplo 4 - Tratando um erro especifico
try:
    len(5)
except TypeError:
    print('Voce está utilizando uma funcao inexistente')


# Exemplo 5 - Tratando um erro especifico com detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicaçã gerou o seguinte erro: {err}')


# PODEMOS EFETUAR DIVERSOS TRATAMENTOS DE ERRO DE UMA VEZ
try:
    len(5)
    # geek()
    # print('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print("Deu um erro diferente")

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "geek"}

print(pega_valor(dic, "nome"))

