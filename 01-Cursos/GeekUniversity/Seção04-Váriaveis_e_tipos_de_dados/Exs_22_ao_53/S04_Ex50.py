"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a
partir de sua idade e do ano atual.
"""

idade = int(input("Informe sua idade: "))
ano = int(input("Informe o ano atual: "))

dataNasc = ano - idade

print(f"Você nasceu em {dataNasc}")
print(f"e tem {idade} anos")
