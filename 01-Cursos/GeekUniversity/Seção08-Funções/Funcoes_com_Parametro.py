"""
Funções com Parametro(de entrada)

 - Funções que recebem dados para serem processados dentro da mesma

Um programa qualquer tem:
    entrada->processamento-> saida

Uma função qualquer :
    - Não possuem entrada;
    - Não possuem saida;
    - possuem entrada mas, não possuem saida;
    - possuem saida mas, não possuem entrada;
    - possuem entrada e saida;

#  Refatorando uma função


def quadrado(numero):
    # return numero*numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando a funcao


def cantar_parabens(aniversariante):
    print('parabens pra voce')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'Viva o {aniversariante}!')


cantar_parabens('marcos')

# Funções podem ter N parametros de entrada, ou seja, podemos receber
# como entrada em uma função quantos parametros forem necessários. Eles são
# separados por vírgula.
# Exemplos


def soma(a, b):
    return a + b


def multiplica(n1, n2):
    return n1 * n2


def outra(n1, b, msg):
    return (n1 + b)*msg


print(soma(2, 5))
print(multiplica(4, 5))
print(outra(3, 2, 'geek '))

# Nomeando parametros


def nome_completo(nome, sobrenome):
    return f'seu nome completo é {nome} {sobrenome}'


print(nome_completo('angelina', 'jolie'))

# Diferença entre parametros e argumentos
# Parametros sao variaveis declaradas na definição de uma função;
# Argumentos sao dados passados durante a execução de uma função;

# a ordem dos parametros importam

nome = 'felicity'
sobrenome = 'smoke'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados(KeyWord Arguments)
print(nome_completo(nome='angelina', sobrenome='jolie'))
print(nome_completo(sobrenome='marques', nome='garcia'))

"""
# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

