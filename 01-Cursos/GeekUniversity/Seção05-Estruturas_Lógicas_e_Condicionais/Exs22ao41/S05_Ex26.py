"""
.26. leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso,calcule o consumo de Km/l e escreva uma mensagem de acordo com a tabela abaixo:

  - CONSUMO   | (KM/L) | MENSAGEM
  - menor que | 8      | Venda o carro!
  - entre     | 8 e 14 | Econômico!
  - maior que | 12     | Super Econômico!
"""

distancia = float(input("Informe a distância em KM: "))
gasolina =  float(input("Informe a qtd de L de gasolina: "))

consumo = distancia/gasolina
if consumo < 8:
    print("Venda o carro")
elif 8 <= consumo < 14:
    print("Econômico")
else:
    print("Super Econômico")







