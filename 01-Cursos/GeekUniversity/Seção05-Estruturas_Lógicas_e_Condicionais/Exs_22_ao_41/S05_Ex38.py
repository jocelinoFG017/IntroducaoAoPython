"""
.38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, mês e ano. Teste a validade desta data para saber se está é uma data válida. Teste se
o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro (29 se o ano for
bissexto), dia <= 30 em abril, junho,setembro e novembro, dia <= 31 nos outros meses. Teste
a validade do mês: mês > 0 e mês < 13. Teste a validade a validade do ano: ano <=  ano atual
(use uma constante definida com o valor igual a 2008). imprimir: 'Data válida' ou 'data inválida'
no final da execução do programa.
"""
print("A seguir informe uma data de nascimento: ")
data_atual = 2008

d = 'Dia inválido'

dia = int(input("Dia: "))
if dia > 0:
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    if ano >= 2008:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if (mes > 0) and mes < 13:
                if mes == 2 and dia > 29:
                    print(d)

                if dia <= 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                    print('Data Válida')
                    print(f'{dia}/{mes}/{ano}')
                else:
                    print(d)
        else:
            if (mes > 0) and mes < 13:
                if mes == 2 and dia > 28:
                    print(d)

                if dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
                    print('Data válida')
                    print(f'{dia}/{mes}/{ano}')
                else:
                    print(d)
    else:
        print('Data inválida')
else:
    print(d)
