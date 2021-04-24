"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um
concurso. Sendo que da quantia total.
O primeiro(1º) ganhador receberá 46%.
O segundo(2º) receberá 32%.
O terceiro(3º) receberá o restante.
"""

quantia = 780_000.00
primeiro = (quantia*46)/100
segundo =  (quantia*32)/100
terceiro = (quantia*(100-(46+32)))/100
print("O 1º receberá R$ {:.2f}".format(primeiro))
print("O 2º receberá R$ {:.2f}".format(segundo))
print("O 3º receberá R$ {:.2f}".format(terceiro))
#print(primeiro+segundo+terceiro)
