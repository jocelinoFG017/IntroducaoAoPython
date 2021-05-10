"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o
intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadas anteriormente obedece
aos pesos: trabalho de laboratório: 2;  avaliação semestral:3; exame final:5. De acordo
com o resultado, mostre na tela se o aluno está reprovado(média entre 0 e 2.9), de recuperação
(entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""
print("A seguir informe notas de 0.0 a 10.0")
nota1 = float(input("Trabalho de Laboratório: "))
nota2 = float(input("Avaliação Semestral: "))
nota3 = float(input("nota3: "))

tLab = nota1 * 2
tSemestral = nota2 * 3
eFinal = nota3 * 5

media = (tLab + tSemestral + eFinal)/(2+3+5)
if (media >= 0.0) and (media <= 2.9):
    print("Media = {:.2f}".format(media))
    print("Reprovado")
elif (media >= 3) and (media <= 4.9):
    print("Media = {:.2f}".format(media))
    print("De Recuperação")
else:
    print("Media = {:.2f}".format(media))
    print("Aprovado")
