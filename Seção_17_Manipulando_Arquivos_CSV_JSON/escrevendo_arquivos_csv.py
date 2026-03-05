"""
→ Escrevendo em Arquivos CSV

# writer() -> gera um objeto para que possamos escrever em uma arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista
from csv import writer

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/filmes.csv','w', encoding='utf-8',newline='') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Druração'])
    while filme != 'sair':
        filme = input('Informe o Nome do Filme: ')
        if filme.lower() != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a Duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
        else:
            filme = 'sair'

#Escrevendo de outra maneira       
from csv import writer

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/filmes.csv','w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = writer(arquivo)
    escritor_csv.writerow(['Título', 'Gênero', 'Druração'])
    while True:
        filme = input('Informe o Nome do Filme: ')
        if filme.lower() == 'sair':
            break
        genero = input('Informe o Gênero: ')
        duracao = input('Informe a Duração (em minutos): ')
        escritor_csv.writerow([filme, genero, duracao])            
"""

# DictWriter
#OBS.: As chaves dos dicionários devem ser os mesmos do dicionário
from csv import DictWriter

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/filmes2.csv', 'w', encoding='utf-8', newline='') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o Nome do Filme (ou sair): ')
        if filme.lower() != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a Duração (em minutos): ')
            escritor_csv.writerow({"Título":filme, "Gênero": genero, "Duração":duracao})
        else:
            filme = 'sair'
