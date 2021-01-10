"""
Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""
n = float(input("Informe um número: "))
rq = pow(n,1/2)
if n >= 0:
    print("Raiz Quadrada de {} é = {:.2f}: ".format(n,rq))
else:
    print("{} ao quadrado é = - {:.2f}: ".format(n,n**2))