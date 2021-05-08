"""
Funcoes com parametro Default(padrão)
-  Funções onde a passagem de parametros é opcional

# Exemplo de funcao onde a passagem de parametro seja opcional
print('geek')
print()

# exemplo de funcao onde a passagem de parametro seja obrigatoria

def quadrado(numero):
    return numero ** 2
print(quadrado(2))


def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial(3))

# OBS: se o usuario passar somente um parametro este será atribuido ao parametro numero, e será
# calculado o quadrado deste numero.
# Se o usuario passar 2 argumentos, o primeiro será atribuido ao parametro numero e o segundo ao parametro potencia
# e entao será calculada esta potencia.

print(exponencial())

# em funções python os parametros DEVEM estar sempre ao final da declaração

def t(p, n=2):
    return n ** p
print(t(6))

# outros exemplos

def soma(n1, n2):
    return n1 + n2

print(soma(4,3))
print(soma(4) # typeError)
print(soma()) # TypeError

# Exemplo mais complexo


def mostra_info(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return 'bem vindo instrutor'
    elif nome == 'geek':
        return 'vc nao é um instrutor'
    return f'olá {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('ozzy'))

# por que utilizar parametros com valor default?

# - Nos permite ser maix flixiveis nas funções
# - Evita erros de parametros incorretos
# - Nos permite trabalhar com exemplos mais legíveis no código.

Quais tipos de dados podemos utilizar como valores default para parametros?
    - Qualquer tipo de dado.


# Exemplos


def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, f=soma):
    return f(n1, n2)


def sub(n1, n2):
    return n1-n2


print(mat(2, 3))
print(mat(2, 2, sub))


# Escopo - Evitar problemas e confusões...

#Variaveis globais
#Variaveis locais

ins = 'geek'  # global


def oi():
    ins = 'python' # local
    return f'oi {ins}'


# se a var global e local forem iguais a local tem preferencia
print(oi())

def oi():
    prof = 'geek'
    return f'ola {prof}'

print(oi())
print(prof) # nameError


# Atenção com var globais(se puder evitar, evite)
total = 0

def increment():
    total = total + 1  # UnboundLocalError (a variavel não foi inicializada)
    return total
print(increment())

# Atenção com var globais(se puder evitar, evite)
total = 0


def increment():
    global total # pega a variavel global

    total = total + 1
    return total


print(increment())

"""
# Podemos ter funções que são declaradas dentro funções
# e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())