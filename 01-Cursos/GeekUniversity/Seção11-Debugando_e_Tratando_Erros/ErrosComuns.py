"""
Erros mais comuns em python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

1- SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo
que o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError:

# exA
def funcao:
    print("geek")

#exB
def = 1

#exC
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida

#Exemplos NameError
ExA:
print(geek)

#B

a = 18
if a < 10:
    msg = "maior q 10"

print(msg)


3 - TypeError -> Ocorre quando uma funcao/operação é aplicada a um tipo errado

# exemplos
#A
print(len(5))

#B
print('geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo
de dado utilizando um indice inválido.
# exemplos

# A
lista = ['geek']
print(lista[2])

# B
lista = ['geek']
print(lista[0][10])

5 - ValueError -> Ocorre quando uma funcao/operação built-in(integrada) recebe um argumento
com tipo correto mas valor inapropriado.
#Exemplos

#A
print(int('geek'))

# B
print(float('geek'))

6 - > KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave inexistente
# exemplos

#A
dic = {}
print(dic['geek'])


7 -> AttributeError -> Ocorre quando uma variavel nao tem um atributo/funcao.

# exemplos

# A
tupla = (11, 2, 31, 4, 5)
print(tupla.sort())

8 IndentationError -> Ocorre quando nao respeitamos a indentação do python(4 espaços)

# Exemplos

#A
def nova():
print("String")
nova()

#B
for i in range(10):
i + 1
print(i)

OBS: Exceptions e Erros são sinônimos na programação

"""