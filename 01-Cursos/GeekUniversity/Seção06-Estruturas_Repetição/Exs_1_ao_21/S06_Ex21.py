"""
.21. Faça um programa que receba dois números. Calcule e mostre:

    - A soma dos números pares desse intervalo de números, incluindo os números digitados;
    - A multiplicação dos números ímpares desse intervalo, incluindo os digitados;
"""
n = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))

soma = 0
multi = 1
for i in range(n, n2+1):
    print(i)
    if i % 2 == 0:  # par
        soma = soma + i
    elif i % 2 == 1:  # impar
        multi = multi * i

print(f'Soma dos numeros Pares = {soma}')
print(f'Multiplicação dos numeros impares = {multi}')
