"""
Escreva um programa para  aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar  o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30 % do salário. Calcule o valor da prestação
como sendo o valor da  casa a comprar dividindo pelo numero de meses a pagar

"""
valorCasa = float(input("Valor da casa: "))
salario = float(input("Salario: "))
qtdAnos = float(input("Quantidade de anos pagando: "))

prestacaoMensal = valorCasa/ (qtdAnos * 12)
salario30 = ((salario*30)/100)

if prestacaoMensal > salario30:
    print("Empréstimo Não Aprovado")
else:
    print("Empréstimo Aprovado")
    print("Valor das parcelas R$ {:.2f} reais".format(prestacaoMensal))


