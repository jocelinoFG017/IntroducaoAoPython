"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira  tem peso 2. Ao
final, mostrar a média do aluno e indicar se o aluno foi aprovado ou
reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))

divisor = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2))
dividendo = 1 + 1 + 2
media = divisor/dividendo

if media >= 6.0:
    print("Aprovado")
    print("Media = {:.2f}".format(media))
else:
    print("Reprovado")
    print("Media = {:.2f}".format(media))
