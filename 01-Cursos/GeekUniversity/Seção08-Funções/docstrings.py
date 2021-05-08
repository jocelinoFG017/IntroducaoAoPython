"""
Documentando Funções com Docstring em python

OBS: Podemos ter acesso a documentação de uma função utilizando a propriedade especial __doc__

podemos ainda acessar a documentação com a função help
"""


def diz_oi():
    """Uma função simples que retorna a string oi"""
    return 'oi'


def exponencial(n, p=2):
    """
    Função que retorna por padrao o quadrado de numero ou numero  à potencia informada
    :param n:
    :param p:
    :return:
    """
    return n ** p

