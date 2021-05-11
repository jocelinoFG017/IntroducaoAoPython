"""
.35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em
anos não bissextos.
"""
print("A seguir digite uma data")

ano = int(input("Ano: "))
if ano > 0:
    mes = int(input("Mes: "))
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if (mes > 0) and (mes < 13):
            dia = int(input("Dia: "))
            if mes == 2:
                if dia > 29:
                    print("Dia inválido.")
        else:
            print('mes inválido tente novamente')
    else:
        if (mes > 0) and (mes < 13):
            dia = int(input("Dia: "))
            if mes == 2:
                if dia > 28:
                    print("Dia inválido. Neste ano fevereiro tem 28 dias")
        else:
            print('mes inválido tente novamente')
else:
    print("Ano inválido")
print(f"A data informada foi {dia}/{mes}/{ano}")
