"""
Faça um programa para converter uma letra maiúscula em letra minúscula.
Use a tabela ASCII para resolver o problema.
"""
letra = input("Informe uma LETRA maiúscula: ")
codigo = ord(letra)
aux = codigo + 32
convert = chr(aux)
#print(codigo)
print(convert)
#print(letra.lower())