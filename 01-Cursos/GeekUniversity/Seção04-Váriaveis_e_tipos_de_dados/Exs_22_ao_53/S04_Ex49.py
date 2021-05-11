"""
Faça um programa que leia o horário(hora,minuto e segundo) de inicio e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora,minutos e segundos) do término da mesma.
"""
horario = int(input("Horario de inicio: "))
duracao = int(input("Duração experiência: "))

hora = horario // 3600
horaT = (horario + duracao) // 3600
horaD = horaT-hora

resto = horario % 3600
restoT = (horario+duracao) % 3600

minutos = resto // 60
minutosT = restoT // 60
minutosD = minutosT-minutos

resto= resto % 60
restoT = restoT % 60

seg = resto // 1
segT = restoT // 1
segD = segT-seg

print(f"Começou as : {hora} horas:  {minutos} min: {seg} seg")
print(f"Terminou as: {horaT} horas: {minutosT} min: {segT} seg")
print(f"duração : {horaD} horas:{minutosD} min:{segD} seg")
