"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa
diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o
usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do
produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado não for
válido, mostrar uma mensagem de erro.
"""
valor = float(input("Valor do Produto R$: "))
uf = input("Estado(sigla): ")
valorF = 0

if uf == "MG" or uf == "mg":
    valorF = valor + (valor*7)/100
    print("Preço Final = {:.2f}".format(valorF))
elif uf == "SP" or uf == "sp":
    valorF = valor + (valor*12)/100
    print("Preço Final = {:.2f}".format(valorF))
elif uf == "RJ" or uf == "rj":
    valorF = valor + (valor*15)/100
    print("Preço Final = {:.2f}".format(valorF))
elif uf == "MS" or uf == "ms":
    valorF = valor + (valor*8)/100
    print("Preço Final = {:.2f}".format(valorF))
else:
    print("Estado inválido...")