"""
Escreva um programa que leia um  valor em metros e
o exiba convertido em milimetros.
"""


metros = float(input())

def conversao(valor):
    milimetros = valor * 1000
    return milimetros

print(conversao(metros))
