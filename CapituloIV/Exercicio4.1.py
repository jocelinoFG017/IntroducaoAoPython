"""
# programa 4.1 - lê dois valores e imprime qual é o maior


Analise o programa 4.1. Responda o que acontece seo primeiro e o segundo valor
forem iguais? Explique.

r: Nenhum  valor será mostrado na tela, pois nenhuma das
condições de ambos os ifs não foram atendidas

"""

a = int(input("1º valor: "))
b = int(input("2º valor: "))


if a>b:
    print("a > b")
if b>a :
    print("b>a")
