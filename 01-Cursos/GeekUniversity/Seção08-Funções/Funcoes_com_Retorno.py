"""
Funções com retorno


numeros = [1, 2, 3]
ret = numeros.pop() # Retorno de pop
print(ret)
print(numeros)

OBS  : Em python, quando uma função não retorna nenhum valor, o retorno é None
OBS2 : Funções python que retornam valores, devem retornar esses valores com
a palavra reservada return

# Exemplo função com retorno


def quadrado_de_sete():
    return 7*7


ret = quadrado_de_sete()
print(f'Retorno = {ret}')
#  ou
print(f'Retorno = {quadrado_de_sete()}')

OBS: palavra reservada return
1 - Finaliza a função, ou seja, sai da execução da função.
2 - Podemos ter, em uma função diferentes returns.
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;


# Exemplo 1 -  Finaliza a função, ou seja, sai da execução da função.


def diz_oi():
    print('Estou sendo executado')
    return 'oi'
    print('nao Estou sendo executado')


print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função diferentes returns.

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;


def outra_funcao():
    return 2, 3, 4, 5


#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())

# Vamos criar uma funcao para jogar uma moeda
from random import random

def joga_moeda():
    # Gera um numero pseudorandomico entre 0 e 1

    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""
# Erros comuns na utilização do return de uma função, que na vdd nem é erro e sim codificação desnecessária


def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
