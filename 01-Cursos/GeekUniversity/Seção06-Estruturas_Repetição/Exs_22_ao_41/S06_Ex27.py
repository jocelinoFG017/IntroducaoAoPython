"""
.27. Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série
harmônica:
    - H(n) = 1 + 1/2 + 1/3 + 1/4 + ... 1/n

    Faça um programa que leia um valor n inteiro e apresente o valor de H(n).

"""

vlr = int(input("Informe um valor inteiro: "))

#  variavel que soma os valores obtidos pelo loop
h = 0

i = 1
for i in range(i, vlr + 1):
    h = h + 1/i

print(vlr/h)
