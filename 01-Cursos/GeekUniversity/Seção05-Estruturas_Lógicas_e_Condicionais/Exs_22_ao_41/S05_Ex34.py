"""
.34. Leia a nota e o número de faltas de um aluno, e escreve seu conceito. De acordo com a
tabela abaixo, quando  o aluno  tem mais de 20 faltas ocorre a redução do conceito.

 - NOTA        | CONCEITO(ATÉ 20 FALTAS) | CONCEITO(MAIS DE 20 FALTAS)
 - 9.0 a 10.0  |            A            |            B            |
 - 7.5 a 8.9   |            B            |            C            |
 - 5.0 a 7.4   |            C            |            D            |
 - 4.0 a 4.9   |            D            |            E            |
 - 0.0 a 3.9   |            E            |            E            |
"""
nota = float(input('Nota do aluno: '))
num_faltas = int(input('Numeros de faltas do aluno: '))

if (nota >= 0.0) and (nota <= 3.9):
    if num_faltas > 20:
        print('E')
    else:
        print('E')
elif (nota >= 4.0) and (nota <= 4.9):
    if num_faltas > 20:
        print('E')
    else:
        print('D')
elif (nota >= 5.0) and (nota <= 7.4):
    if num_faltas > 20:
        print('C')
    else:
        print('D')
elif (nota >= 7.5) and (nota <= 8.9):
    if num_faltas > 20:
        print('C')
    else:
        print('B')
elif (nota >= 9.0) and (nota <= 10.0):
    if num_faltas > 20:
        print('B')
    else:
        print('A')
