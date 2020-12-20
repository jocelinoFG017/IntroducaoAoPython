""" Tabela 4.2
Categoria   | Linhas executadas
    1       |1,2,3,19
    2       |1,2,4,5,6,19
    3       |1,2,4,5,7,8,9,19
    4       |1,2,4,5,7,8,10,11,12,19
    5       |1,2,4,5,7,8,10,11,13,14,15,19
    Outras  |1,2,4,5,7,8,10,11,13,14,16,17,18,19

R: Comparação de resultados feita, as linhas executadas são as mesmas da tabela 4.2
confere.

"""
#Programa 4.6 - categoria X preco
categoria = int(input("Digite a  categoria do produto: "))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria Inválida, digite um valor entre 1 e 5!")
                    preco = 0
print("O preço do produto é : {:.2f}".format(preco))
