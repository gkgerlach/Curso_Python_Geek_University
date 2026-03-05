"""
→ Sistema de Arquivo de Navegação

#Fazer import
import os

#getcwd()
print('Diretório -> '+ os.getcwd())

os.chdir('..')
print('Diretório 1 -> '+ os.getcwd())

os.chdir('..')
print('Diretório 2-> '+ os.getcwd())

os.chdir('..')
print('Diretório 3-> '+ os.getcwd())

os.chdir('..')
print('Diretório 4-> '+ os.getcwd())

import sys
print(sys.platform)


import os

print(os.getcwd()) # caminho do diretório

res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)

print(os.getcwd())


import os

print(os.listdir())
print(len(os.listdir()))
"""

import os

scanner = os.scandir()

arquivos = list(scanner)
#print(dir(arquivos[1]))
print(arquivos[1].inode()) #identificador de inode, numeração
print(arquivos[1].is_dir()) #É um diretório
print(arquivos[1].is_file()) #É um arquivo?
print(arquivos[1].is_symlink()) #É um link simbólico
print(arquivos[1].name) #Nome do arquivo
print(arquivos[1].path) #Nome do caminho
print(arquivos[1].stat()) #Estatísticas

scanner.close()
