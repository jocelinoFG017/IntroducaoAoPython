"""
.26. Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.

OBS: No loop for colocamos +17, pq queremos saber qual é o primeiro multiplo após o numero digitado
exemplo(    entrada = 44
            saida   = 55 -> pq 55 é o primeiro multiplo de 11 depois após o 44.
            )
"""

numero = int(input("Informe um numero: "))
j = numero
#  Listas para guardar os valores dos multiplos encontrados
mult11 = []
mult13 = []
mult17 = []

#  Operadores de controle ( Utilizados para evitar o print de numeros repetidos)
count11 = 0
count13 = 0
count17 = 0

#  Loop para encontrar e armazenar os valores em listas
for numero in range(numero, numero + 17):
    if numero % 11 == 0:
        mult11.append(numero)
    elif numero % 13 == 0:
        mult13.append(numero)
    elif numero % 17 == 0:
        mult17.append(numero)

#  Loop para mostrar os primeiros valores das listas
for i in range(numero, numero + 17):
    if i % 11 == 0:
        count11 = count11 + 1
        if count11 == 1:
            print(f' O primeiro multiplo de 11  depois de {j} é: {mult11[0]}')
    elif i % 13 == 0:
        count13 = count13 + 1
        if count13 == 1:
            print(f' O primeiro multiplo de 13  depois de {j} é: {mult13[0]}')
    elif i % 17 == 0:
        count17 = count17 + 1
        if count17 == 1:
            print(f' O primeiro multiplo de 17  depois de {j} é: {mult17[0]}')
