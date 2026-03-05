"""
→ Sistema de Arquivos - Manipulação

#Forma 1
open(r'Seção_12_Leitura_e_Escrita_em_Arquivos\arquivo_teste.txt', 'w').close()

#Forma 2 
open(r'Seção_12_Leitura_e_Escrita_em_Arquivos\arquivo_teste2.txt', 'a').close()

#Forma 3
with open(r'Seção_12_Leitura_e_Escrita_em_Arquivos\arquivo_teste3.txt', 'a') as arquivo:
    pass #Abrindo o bloco e sem fazer nada



#Criando Diretórios
os.makedirs('templates/python/texto.txt')
os.makedirs('templates/python/texto.txt', exist_ok=True)


#Renomeando arquivos
os.rename('templete/novo2', 'geek')

os.rename(r'Seção_12_Leitura_e_Escrita_em_Arquivos\frutas.txt', r'Seção_12_Leitura_e_Escrita_em_Arquivos\frutas1.txt')

#Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

#Criando um diretório temporário        
with tempfile.TemporaryDirectory() as tmp: #Criando um diretório
    print(f'Criei o diretório temporário {tmp}')
    with open(os.path.join(tmp,'arquivo_temporario.txt'),'w') as arquivo: #Criando um arquivo dentro do diretório
        arquivo.write('Geek University\n')
    input()

#Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n') #b-> em dados binários
    tmp.seek(0)
    print(tmp.read())

#Sem with
arquivo = tempfile.TemporaryFile() as tmp:
tmp.write(b'Geek University\n') #b-> em dados binários
tmp.seek(0)
print(tmp.read())
arquivo.close()
"""
import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)
input()

arquivo.close()
