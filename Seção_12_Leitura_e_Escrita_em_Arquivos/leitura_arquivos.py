"""
→ Leitura de Arquivos

"""
arquivo = open(r'Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8')


ret = arquivo.read()

print(ret)
print(type(ret)) #String
#Para ler o conteúdo de um arquivo após a sua abertura, devemos usar o read()
#print(arquivo.read())



