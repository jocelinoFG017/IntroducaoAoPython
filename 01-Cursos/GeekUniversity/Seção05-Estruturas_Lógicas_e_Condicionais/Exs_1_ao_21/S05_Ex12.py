"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem
"Número inválido". Se o número for positivo, calcular o logaritmo deste
numero.
"""
import math
n = int(input("n: "))
log = 0
if n > 0:
    log = math.log(n)
    print("{:.2f}".format(log))
else:
    print("Número Inválido.")
