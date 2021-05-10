"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são
válidas e exiba na tela a média destas notas. Uma nota válida deve ser,
obrigatoriamente, um  valor entre 0.0 e 10.0, onde caso a nota possua um
valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota1 = float(input("Informe a nota1: "))
nota2 = float(input("Informe a nota2: "))
media = (nota1+nota2)/2

if (nota1 >= 0.0) and (nota1 <= 10.0) and (nota2 >= 0.0) and (nota2 <= 10.0):
    print(f"Nota1 válida = {nota1}")
    print(f"Nota2 válida = {nota2}")
    print("Média = {:.2f}".format(media))
else:
    print("Uma das notas é inválida")
    print("Tente outra vez com valores válidos de 0.0 a 10.0")
