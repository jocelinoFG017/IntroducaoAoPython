"""
Utilizando Lambdas

-   Conhecidas por Expressões lambdas, ou simplismente Lambdas, são funções sem nome, ou seja,
    Funções anônimas

# Função em python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Exemplo de expressão lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina ', 'JOLIE'))
print(nome_completo(' Felicity     ', 'Smoke'))

# Em funções python podemos ter nenhuma ou várias entradas.Em lambdas também
am = lambda: 'Como não amar python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: x * y ** 0.5

tres = lambda x, y ,z: 3/(1/x + 1/y + 1/z)

#n = lambda x1,x2,...., xn: <expressão>

print(am())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))
# OBS: Se passarmos mais parametros ou mais argumentos do que parametros esperados teremos um TypeError

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Ariel Manzur', 'Chris Bradfield', 'Clarice Lispector',
           'Douglas Adams', 'Arthur Conan Doyle', 'H. G. Wells']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

"""
# Função Quadrática

# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def gera_func_quadratica(a, b, c):
    """
    Retorna a função f(x) = a * x ** 2 + b * x + c
    """
    return lambda x: a * x ** 2 + b * x + c


teste = gera_func_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(gera_func_quadratica(3, 0, 1)(2))
