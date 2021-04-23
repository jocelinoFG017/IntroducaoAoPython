""".33. Um novo produto vai sofrer aumento de acordo com a tabela abaixo. Leia  o preço antigo,
calcule  e escreva  o preço novo, e escreva  uma mensagem  em função do preço novo (de acordo com
a segunda tabela)

 --- TABELA 01
 - PREÇO ANTIGO        | PERCENTUAL DE AUMENTO
 - Até R$50            |            5%
 - Entre R$50 e R$100  |            10%
 - Acima de R$100      |            15%

 --- TABELA 02
 - PREÇO NOVO                      |         MENSAGEM
 - Até R$80                        |            barato
 - Entre R$80 e R$120(inclusive)   |            Normal
 - Entre R$120 e R$200(inclusive)  |            Caro
 - Acima de R$200                  |            Muito Caro
"""
preco = float(input('Informe o preço do produto R$: '))
novo_preco = 0

if preco <= 50:  # Aumento de 5%
    novo_preco = preco+((preco*5)/100)
    if novo_preco <= 80:
        print('Barato')
        print(novo_preco)

elif (preco > 50) and (preco <= 100):  # Aumento de 10%
    novo_preco = preco + ((preco * 10) / 100)
    if(novo_preco >= 80) and (novo_preco <= 120):
        print('Normal')
        print(novo_preco)
    else:
        print('Barato')
        print(novo_preco)

elif preco > 100:  # Aumento de 15%
    novo_preco = preco + ((preco * 15) / 100)
    if (novo_preco > 120) and (novo_preco <= 200):
        print('Caro')
        print(novo_preco)
    elif novo_preco > 200:
        print('Muito Caro')
        print(novo_preco)
    else:
        print('Normal')
        print(novo_preco)
