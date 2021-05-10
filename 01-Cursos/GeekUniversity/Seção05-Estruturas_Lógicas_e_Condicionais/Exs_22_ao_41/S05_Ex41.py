"""
.41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo
com a tabela abaixo.
    IMC          | Classificação
    -------------|-------------
    < 18,5       | Abaixo do peso
    18.6 - 24.9  | Saudável
    25.0 - 29.9  | Peso em excesso
    30.0 - 34.9  | Obesidade grau I
    35.0 - 39.9  | Obesidade grau II (severa)
    >= 40.0      | Obesidade grau III (mórbida)
"""
print(" -------  Sistema de Calculo do IMC - Indide de Massa Corpórea")
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura*altura)

print('IMC = {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif (imc >= 18.6) and (imc <= 24.9):
    print('Saúdavel')
elif (imc >= 25.0) and (imc <= 29.9):
    print('Peso em excesso')
elif (imc >= 30.0) and (imc <= 34.9):
    print('Obesidade grau I')
elif (imc >= 35.0) and (imc <= 39.9):
    print('Obesidade grau II (Severa)')
elif imc >= 40.0:
    print('Obesidade grau III (Mórbida)')
