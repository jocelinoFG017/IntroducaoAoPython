"""
Levantando os próprios erros com o raise

raise -> Lança exceções

OBS: raise não é uma funcao, e sim uma palavra reservada
Pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens

A forma geral de utilização é:

raise TipoDoErro('mensagemdo de erro')

# exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser string')
    print(f'o texto {texto} será impresso na cor {cor}')


colore(1, 'azul')

# OBS: O raise, assim como o return, finaliza a funcao, ou seja, nada após o raise
é executado.
"""
# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')

    if type(texto) is not str:
        raise TypeError('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'o texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')


