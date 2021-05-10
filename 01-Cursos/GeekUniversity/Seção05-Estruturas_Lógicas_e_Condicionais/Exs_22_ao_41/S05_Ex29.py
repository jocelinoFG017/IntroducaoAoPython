"""
.29. Faça uma prova de matemática para crianças que estão aprendendo a somar múmeros inteiros
menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
"Qual é a soma de a + b, onde a e b são números aleatórios" Peça a resposta. Faça cinco perguntas
ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
"""
from random import randrange

pontos = 0

k = 0
for k in range(1, 6):
    a = randrange(0, 101)
    b = randrange(0, 101)

    soma = a + b
    print(f"Qual é a soma de {a} + {b} ? ")
    resposta = int(input("Resposta: "))

    if resposta == soma:
        print("Correto")
        pontos += 1
    else:
        print("Errado")

print("Total de acertos = ", pontos)
