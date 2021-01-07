"""
Faça um programa que leia a quantidade de dias,horas,minutos e segundos do usuario.
Calcule o total em segundos.
"""
converteDia = 0
converteMinuto = 0
converteHora = 0
total = 0

dia = int(input("Dia: "))
if dia > 0 and dia < 32:
    converteDia = dia * 86400
    hora = int(input("Hora: "))
    converteHora = hora * 3600
    if hora >= 1 and hora <= 24:
        min = int(input("Minuto: "))
        converteMinuto = min * 60
        if min >= 0 and min < 61:
            seg = int(input("Segundo: "))
            if seg >= 0 and seg < 61:
                total = converteMinuto + converteHora + converteDia + seg
                print("total em segundos: {}".format(total)+"s")