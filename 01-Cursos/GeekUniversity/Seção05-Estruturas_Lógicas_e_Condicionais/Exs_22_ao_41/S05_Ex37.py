"""
.37. As tarifas de certo parque de estacionamentos são as seguintes:

    * 1ª e 2ª hora - R$ 1,00 cada
    * 3ª e 4ª hora - R$ 1,40 cada
    * 5ª hora e seguintes- R$ 2,00 cada

    O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem
    estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse
    permanecido 120 minutos. Os momentos de chegada ao parque e partidas destes são apresentados
    na forma de pares de inteiros, representado horas e minutos.
    Por exemplo, o par 12 50 representara 'Dez para uma da tarde'. Pretende-se criar um programa
    que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo
    estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior
    a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma
    situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.
"""
#  Chegada
print('Informe o horario de CHEGADA ao estacionamento')

hora_chegada = int(input('Hora de chegada: '))
hora_min_chegada = 0
total_chegada = 0
result_chegada = 0
custo = 0
if (hora_chegada <= 24) and (hora_chegada >= 0):
    min_chegada = int(input('Min de chegada: '))

    if (min_chegada <= 60) and (min_chegada >= 0):
        hora_min_chegada = hora_chegada * 60
        total_chegada = hora_min_chegada + min_chegada
        print('total minutos = ', total_chegada)
        print('ok')

    else:
        print('Minuto inválido, informe o min entre 0 e 60.')
    # total_chegada = hora_chegada+min_chegada

else:
    print('Hora inválida, informe a hora entre 0 e 24. ')

#  Partida

print('Informe o horario de PARTIDA ao estacionamento')

hora_partida = int(input('Hora de partida: '))
hora_min_patida = 0
total_partida = 0

if (hora_partida <= 60) and (hora_partida >= 0):
    min_partida = int(input('Min de partida: '))

    if (min_partida <= 60) and (min_partida >= 0):
        hora_min_partida = hora_partida * 60
        total_partida = hora_min_partida + min_partida
        print('total minutos = ', total_partida)
        print('ok')
    else:
        print('Minuto inválido, informe o min entre 0 e 60.')
    # total_chegada = hora_chegada+min_chegada
else:
    print('Hora inválida, informe a hora entre 0 e 24. ')
total_hora = 0
if total_chegada < total_partida:  # Se a hora de chegada for menor que a hora da partida
    a = total_partida - total_chegada
    total_hora = a / 60
    print(a)
    print('Total em horas: ', total_hora)

    # Custo do estacionamento
    if (total_hora > 0) and (total_hora <= 2):
        custo = total_hora * 1.0
        print(f'Custo em R$ = {custo}')
    elif (total_hora > 2) and (total_hora <= 4):
        custo = total_hora * 1.40
        print(f'Custo em R$ = {custo}')
    elif total_hora > 4:
        custo = total_hora * 2.0
        print(f'Custo em R$ = {custo}')
else:  # Se a hora de partida for menor que a hora de chegada
    a = total_chegada - total_partida
    total_hora = (a + 1440) / 60  # 1 dia equivale a 1440 minutos
    print(a)
    print('Total em horas: ', total_hora)

    # Custo do estacionamento
    print(' Seu carro ficou mais de 24 horas no '
          '\n estacionamento, a cobrança por hora passou a ser R$ 2,00')
    if (total_hora > 0) and (total_hora <= 2):
        custo = total_hora * 1.0
        print(f'Custo em R$ = {custo}')
    elif (total_hora > 2) and (total_hora <= 4):
        custo = total_hora * 1.40
        print(f'Custo em R$ = {custo}')
    elif total_hora > 4:
        custo = total_hora * 2.0
        print(f'Custo em R$ = {custo}')
