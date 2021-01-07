"""
Escreva  um programa que leia dois números.Imprima a divisão inteira do primeiro pelo segundo,
assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular
o resultado. Lembre-se de que podemos entender quociente da divisão  de dois números como a
quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 /4 = 5, uma vez que
podemos subtrair 4 cinco vezes de 20.
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))
aux = 0
x = n1
while x >= n2:
    x = x - n2
    aux = aux + 1
resto = x
print("{} / {} = {} Quociente {}resto".format(n1,n2,aux,resto))