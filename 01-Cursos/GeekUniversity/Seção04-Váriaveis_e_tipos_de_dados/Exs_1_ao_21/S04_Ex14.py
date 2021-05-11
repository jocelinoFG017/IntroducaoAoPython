"""
Leia um ângulo em graus  e apresente-o convertido em radianos. A Fórmula de conversão
é : R = G * pi / 180, sendo G o ângulo em graus e R em Radianos e pi = 3.14
"""
angulo = float(input("Informe um angulo(Graus): "))
convert = angulo*3.14/180
print("Convertido em Radianos Fica: {:.2f}".format(convert))
