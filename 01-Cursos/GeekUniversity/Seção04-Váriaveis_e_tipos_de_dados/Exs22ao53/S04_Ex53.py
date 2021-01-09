"""
Faça um programa para ler as dimensões de um terreno(comprimento C e largura L),
bem como o preço do metro de tela P. Imprima o custo para cercar este mesmo
terreno com tela.
"""
comprimento = float(input("Comprimento(C): "))
largura = float(input("Largura: (L)"))
preco = float(input("Preço do metro de tela (P): "))

valor = comprimento * largura * preco
print("Valor a pagar para cercar o terreno(R$): {:.2f}".format(valor))

