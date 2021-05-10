"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou ser for divisível por 4 e não for possível por 100.
por exemplo: 1988, 1992,1996.
"""
ano = int(input("Informe uma data(ano): "))
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não é Bissexto")
