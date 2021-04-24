"""
Leia um ângulo em radianos  e apresente-o convertido em graus. A Fórmula de conversão
é : G = R *180/pi, sendo G o ângulo em graus e R em Radianos e pi = 3.14
"""
pi = 3.14 #pi = 3.1415 é mais exato o resultado
angulo = float(input("Informe um angulo(Radianos): "))
convert = angulo*180/pi
print("Convertido em Graus Fica: {:.3f}".format(convert))
