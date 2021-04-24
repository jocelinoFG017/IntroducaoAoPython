"""
Receba a altura do degrau de uma escada e altura que o usuário deseja alcançar subindo a
escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

alturaDegrau = int(input("altura degrau da escada: "))
alturaDesejada = int(input("altura desejada para subir: "))
calculo = (alturaDesejada/alturaDegrau)

print("Você deverá subir {:.2f}"
      " degraus para atingir o seu objetivo.".format(calculo))
