"""
.32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
cada execução somente será calculado um pedido. O cardápio de lanchonete segue o padrão abaixo.

 - ESPECIFICAÇÃO    | CÓDIGO | PREÇO
 - Cachorro Quente  | 100    | 1.20
 - Bauru Simples    | 101    | 1.30
 - Bauru com Ovo    | 102    | 1.50
 - Hamburguer       | 103    | 1.20
 - Cheeseburguer    | 104    | 1.70
 - Suco             | 105    | 2.20
 - Refrigerante     | 106    | 1.00
"""
cod = int(input("Insira o código do produto: "))
qtd = int(input("Insira a quantidade: "))
total = 0.0

print("Seu pedido foi: ")
if cod == 100:
    print(f"{qtd} cachorro Quente")
    total = qtd * 1.20
    print(f" total {total}")
elif cod == 101:
    print(f"{qtd} Bauru Simples")
    total = qtd * 1.30
    print(f" total {total}")
elif cod == 102:
    print(f"{qtd} Bauru com Ovo")
    total = qtd * 1.50
    print(f" total {total}")
elif cod == 103:
    print(f"{qtd} Hamburguer")
    total = qtd * 1.20
    print(f" total {total}")
elif cod == 104:
    print(f"{qtd} CheeseBurguer")
    total = qtd * 1.70
    print(f" total {total}")
elif cod == 105:
    print(f"{qtd} Suco")
    total = qtd * 2.20
    print(f" total {total}")
elif cod == 106:
    print(f"{qtd} Refrigerante")
    total = qtd * 1.00
    print(f" total {total}")
