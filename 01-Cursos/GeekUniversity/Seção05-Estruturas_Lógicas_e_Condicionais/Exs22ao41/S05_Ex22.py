"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não
se aposentar. As condições para a aposentadoria são:
 - Ter pelo menos 65 anos.
 - Ou ter trabalhado pelo menos 30 anos.
 - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = int(input("Idade: "))
tempoS = int(input("Tempo de Serviço: "))
if tempoS > idade :
    print("Dados Inválidos.")
else:
    if idade >= 65:
        print("Pode se Aposentar")
    elif tempoS >= 30:
        print("Pode se Aposentar")
    elif idade >= 60 and tempoS >= 25:
        print("Pode se Aposentar")
    else:
        print("Não Pode se Aposentar")

