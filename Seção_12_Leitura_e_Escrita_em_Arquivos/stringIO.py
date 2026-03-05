"""
→ StringIO


"""
#Import
from io import StringIO

mensagem = 'Este é uma string normal'

#Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos o texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos 
print(arquivo.read())

#Escrevendo outros textos
arquivo.write('\nOutro texto')

#Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())