"""
.19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada
um dos algarismos que compõem o número.
"""
n = int(input('Informe um numero: '))

if (n > 100) and n < 999:
    trsn = str(n)
    for i, v in enumerate(trsn):
        print(v)
else:
    print('Numero inválido')
