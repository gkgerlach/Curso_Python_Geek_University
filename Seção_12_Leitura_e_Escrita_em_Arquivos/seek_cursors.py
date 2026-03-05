"""
→ Seek e Cursors

arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')

print(arquivo.read())

#Movimentando o Cursor pelo arquivo usando o seek()
arquivo.seek(300)
print(arquivo.read())

arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')
print(arquivo.read()) #1°Linha
print(arquivo.read()) #2°Linha
print(arquivo.read()) #3°Linha


arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')

ret = arquivo.readline()
print(type(ret))
print(ret)

lista = ret.split(' ') #Gera uma Lista!!
print(lista)

print(lista.count('Teste'))

#Qunatidade de Linhas
arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')
linhas = arquivo.readlines()

print(len(linhas))

#Fechando um arquivo
arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')

print(arquivo.read())

print(arquivo.closed) #False

arquivo.close()

print(arquivo.closed) #True
"""


arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')

print(arquivo.read())
arquivo.seek(40)
print(arquivo.read(10))