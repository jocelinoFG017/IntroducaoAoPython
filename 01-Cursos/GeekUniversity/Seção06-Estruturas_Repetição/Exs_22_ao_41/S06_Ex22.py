"""
.22. Escreva um programa completo que permita qualquer aluno introduzir, pelo teclado, uma sequencia
arbitraria de notas(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspon-
dente média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido
ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.

"""

qtd_notas = 0
soma = 0
media = 0

while True:
    n = int(input('Digite notas entre 10 e 20: '))
    if n < 10 or n > 20:
        print('Nota inválida')
        break
    else:
        soma = soma + n
        qtd_notas = qtd_notas + 1
    media = soma / qtd_notas
print(f'Soma das notas = {soma}')
print(f'notas informadas = {qtd_notas}')
print(f'media = {media:.2f}')
