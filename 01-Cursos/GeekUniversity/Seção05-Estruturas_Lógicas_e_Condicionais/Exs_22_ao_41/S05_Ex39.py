"""
.39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera
o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um
aumento proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de
serviço na empresa, cada funcionário irá receber um bonus adicional de salário. Faça um programa
que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do
salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

    -  Salário  Atual       | Reajuste(%)       |  Tempo de Serviço     |  Bônus
    Até 500,00              |  25%              |  Abaixo de 1 ano      |  Sem Bônus
    Até 1000,00             |  20%              |  De 1 a 3 anos        |  100,00
    Até 1500,00             |  15%              |  De 4 a 6 anos        |  200,00
    Até 2000,00             |  10%              |  De 7 a 10 anos       |  300,00
    Acima de 2000,00        |  Sem Reajuste     |  Mais de 10 anos      |  500,00

"""
salario_atual = float(input('Informe o salário atual: '))
tempo_servico = float(input('Informe o seu tempo de serviço(em ANOS): '))

reajuste = 0

if (salario_atual <= 500) and (tempo_servico < 1):
    reajuste = ((salario_atual * 25) / 100)
    salario_reajustado = salario_atual + reajuste
    print(f'Salario reajustado = {salario_reajustado} sem direito a bônus')

if (salario_atual <= 1000) and (tempo_servico > 1 and tempo_servico <= 3):
    reajuste = ((salario_atual * 20) / 100)
    salario_reajustado = salario_atual + reajuste + 100
    print(f'Salario reajustado = {salario_reajustado} ')

if (salario_atual <= 1500) and (tempo_servico > 4 and tempo_servico <= 6):
    reajuste = ((salario_atual * 15) / 100)
    salario_reajustado = salario_atual + reajuste + 200

    print(f'Salario reajustado = {salario_reajustado} ')

if (salario_atual <= 2000) and (tempo_servico > 7 and tempo_servico <= 10):
    reajuste = ((salario_atual * 10) / 100)
    salario_reajustado = salario_atual + reajuste + 300

    print(f'Salario reajustado = {salario_reajustado} ')

if salario_atual > 2000 and (tempo_servico > 10):
    salario_reajustado = salario_atual + reajuste + 500

    print(f'Salario reajustado = {salario_reajustado}, sem direito a reajuste ')
else:
    print('Sem direito a aumento')
