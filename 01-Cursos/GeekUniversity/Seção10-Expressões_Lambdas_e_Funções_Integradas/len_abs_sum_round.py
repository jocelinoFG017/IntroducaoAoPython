"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho, ou seja, o numero de itens de um iteravel

print(len("Geek University"))
print(len([1, 2, 3, 4, 5, 6, 7]))
print(len((1, 2, 3, 4, 5, 6,)))
print(len({1, 2, 3, 4, 5, 6}))
print(len({'a': 1, 'b': 2}))
print(len(range(0, 10)))

# por debaixo dos panos esta sendo executado a funcao abaixo.
# Dunder len
print('Geek University'.__len__())


# Abs -> Retorna o valor absoluto de um numero inteiro ou real

# Exemplos abs
print(abs(-5))
print(abs(3.14))
print(abs(-3.14))
print(abs(5))

# Sum -> Recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial


# Exemplos sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.14, 4.52, 12.231]))

print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))

# Round -> Retorna um numero arredondado para n digito de precisao após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada.
"""
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121212, 2))
print(round(1.219999999, 2))

