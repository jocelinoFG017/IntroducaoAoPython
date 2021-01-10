"""
Usando switch, escreva um programa que leia um  inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda se,
2 e assim por diante.
"""
dia = int(input("Informe um número de 1 a 7: "))
if (dia > 0) and (dia < 8):
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    elif dia == 7:
        print("Sábado")
else:
    print("Número Inválido")