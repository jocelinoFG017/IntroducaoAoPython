"""
Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e
quantos anos ele já fumou. Considere que um fumante perde 10 minutos
de vida a cada cigarro, e calcule quantos dias de vida um fumante
perderá. Exiba o total em dias.
"""

qtdCigarros = int(input("Cigarros/dia: ")) # 2 cigarros/dia
qtdAnos = int(input("anos: ")) # 2 anos

anos =(qtdAnos * 365 * qtdCigarros*10)
dias =  anos/(24*60)

print("Voce perdeu {:.1f} dias da sua vida".format(dias))

