"""
 - Definindo Funções

 Funções são pequenas partes de código que realizam tarefas especificas;
 Uma função pode ou não receber entrada de dados e retornar uma saida de dados;
 Muito uteis para executar procedimentos similares por repetidas vezes;

 OBS: Se vocês escrever uma função que realiza várias tarefas dentro dela, é bom
 fazer uma verificação para que a função seja simplificada.

 já utilizamos várias funções desde que iniciamos o curso
  - print()
  - len()
  - max()
  - min()
  - count()
  - e muitas outras;
#  Exemplo  de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']
#  Utilizando a função integrada(Built-in) do python -> print()
# print(cores)
cores.append('roxo')
# print(cores)
cores.clear()
# print(cores)


# Como definir funções

Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for composto, separados por underline(Snake case)

parametros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não.

bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento dafunção acontece.

Obs: Veja que para definirmos uma função utilizamos a palavra reservada 'def'.

# definindo a primeira funcao


def diga_oi():
    print('oi')


# chamada de execução
diga_oi()

#  nunca esqueça do () quando for executar uma função

"""
# Exemplo2


def cantar_parabens():
    print('parabens pra voce')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')


#cantar_parabens()

# for n in range(5):
#    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de
# um função e executar esta função atráves da variável

canta = cantar_parabens

canta()
