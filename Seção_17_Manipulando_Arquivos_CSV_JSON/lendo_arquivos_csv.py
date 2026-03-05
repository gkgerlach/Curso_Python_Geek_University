"""
→ Lendo Arquivos CSV

with open(r'Seção_17_Manipulando_Arquivos_CSV_JSON\lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    #print(type(dados))
    print(dados)

#Reader
from csv import reader

with open(r'Seção_17_Manipulando_Arquivos_CSV_JSON\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #Pular o cabeçalho
    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cm')

        
#DictReader
from csv import DictReader

with open(r'Seção_17_Manipulando_Arquivos_CSV_JSON\lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #Cada linha é uma OrderedDict
        print(f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}')
"""


#DictReader com outro separador
import os
from csv import DictReader

caminho = os.path.join('Seção_17_Manipulando_Arquivos_CSV_JSON', 'lutadores.csv')
with open(caminho, encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        #Cada linha é uma OrderedDict
        print(f'{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}')