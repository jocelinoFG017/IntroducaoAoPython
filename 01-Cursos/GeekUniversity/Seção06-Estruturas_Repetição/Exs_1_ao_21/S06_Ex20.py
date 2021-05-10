"""
.20. Ler um sequencia de números inteiros e determinar se eles são pares ou não. Deverá ser informado
o número de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.
"""
n = int(input('Informe quantos numeros deseja digitar : '))
print('Digite 1000 para sair')

count_pares = 0
aux = 0
count_n_lidos = 0
while aux != 1000:
    for i in range(0, n):
        vlr = int(input(f'Informe o valor {i+1}: '))
        if vlr % 2 == 0 and vlr != 1000:
            count_pares = count_pares + 1
        count_n_lidos = count_n_lidos + 1
        if vlr == 1000:
            aux = 1000
            break

    print(f'Foi(foram) lido(s) {count_n_lidos} numero(s)')
    print(f'Total de numeros pares lido = {count_pares}')
