"""
Leia um número fornecido pelo usuário. Se esse número for positivo,
calcule a raiz quadrada do número. Se o número for negativo, mostre
uma mensagem dizendo que o número é inválido.
"""
n = int(input("Informe um número: "))
rq = pow(n,1/2)
if n >= 0:
    print("Raiz Quadrada de {} é = {:.2f}: ".format(n,rq))
else:
    print("Número Inválido, Digite um número positivo.")