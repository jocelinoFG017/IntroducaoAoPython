"""
.40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
consumidor.

    - Custo de Fábrica                  |  % do Distribuidor    |  % dos Impostos
      Até R$ 12.000,00                  |       5               |  isento
      Entre R$ 12.000,00 e 25.000,00    |       10              |   15
      Acima de R$ 25.000,00             |       15              |  20



"""
custo_fabrica = float(input('Informe o custo de fábrica do carro: '))

if custo_fabrica <= 12000:
    comissao_distribuidor = ((custo_fabrica * 5) / 100)
    print('Custo do carro novo = R$ {:.2f}'.format(custo_fabrica + comissao_distribuidor))

elif (custo_fabrica > 12000) and (custo_fabrica < 25000):
    comissao_distribuidor = ((custo_fabrica * 10) / 100)
    imposto = ((custo_fabrica * 15) / 100)
    print('Custo do carro novo = R$ {:.2f}'.format(custo_fabrica + comissao_distribuidor + imposto))

elif custo_fabrica > 25000:
    comissao_distribuidor = ((custo_fabrica * 15) / 100)
    imposto = ((custo_fabrica * 20) / 100)
    print('Custo do carro novo = R$ {:.2f}'.format(custo_fabrica + comissao_distribuidor + imposto))


