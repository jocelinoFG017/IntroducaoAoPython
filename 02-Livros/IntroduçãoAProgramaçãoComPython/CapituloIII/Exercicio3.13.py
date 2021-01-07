"""
Escreva um programa que converta uma temperatura digitada em ºC em º F.
A formula para essa conversão é F = ((9*C)/5) + 32

"""

temperatura  = float(input("Celsius: "))
far =  ((9*temperatura)/5) + 32

print("{} em Fahrenheit é = {}".format(temperatura,far))