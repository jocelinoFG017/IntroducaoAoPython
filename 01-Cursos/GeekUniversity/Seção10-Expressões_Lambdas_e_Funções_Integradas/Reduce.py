"""
Reduce

 - A partir do python versão 3.+ a função reduce() não é mais uma função integrada(built-in),
 agora temos que importar e utilizar esta função a partir do módulo 'functools'

 Guido Von Rossum : Utilize a função reduce() se você realmente precisa dela. Em todo caso,
 99% das vezes um loop for é mais legível.

 Para entender o reduce():
    # Imagine qe você tem um coleção de dados:
        dados = [a1, a2, a3,..., an]
    # E você tem uma função que recebe dois parametros:
        def funcao(x, y):
            return x * y

Assim como a função map() e filter(), a função reduce() recebe dois parametros: a função e o iterável.

    reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    - passo 1: res = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    - passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o terceiro elemento
    e guarda o resultado.

    Isso é repetido até a final.
     - passo3: res3 = f(res2, a4)
     .
     .
     .
     passo n: res n = f(resm, an)

ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No
final o reduce() irá retornar o valor final.

Alternativamente, poderíamos ver a função reduce() como:
    funcao(funcao(funcao(a1, a2), a3), a4), ....), an)
"""
# Como funciona na prática
# Vamos utilizar a função reduce() para multiplicar todos os numeros em uma lista

from functools import reduce
dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# para aplicar o reduce() nós precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# utilizando um loop normal

res = 1

for n in dados:
    res = res * n

print(res)

