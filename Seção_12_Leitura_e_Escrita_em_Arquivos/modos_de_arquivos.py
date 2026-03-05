"""
→ Modos de Arquivos

try:
    with open('Seção_12_Leitura_e_Escrita_em_Arquivos/frutas.txt', 'x', encoding='utf=8') as arquivo:
        arquivo.write('Teste de conteúdo')
except FileExistsError:
    print('Arquivo já existente!')

#Exemplo 'a'
with open('Seção_12_Leitura_e_Escrita_em_Arquivos/frutas.txt', 'a', encoding='utf=8') as arquivo:
    while True:
        fruta = input('Informa a fruta ou digite sair: ')
        if fruta.lower() != 'sair':
            arquivo.write(fruta.capitalize() + '\n')
            #ou arquivo arquivo.write('\n')
        else:
            break


#Exemplo 'r+'
with open('Seção_12_Leitura_e_Escrita_em_Arquivos/frutas.txt', 'r+', encoding='utf=8') as arquivo:
    print(arquivo.read())
"""

with open('Seção_12_Leitura_e_Escrita_em_Arquivos/frutas.txt', 'r+', encoding='utf=8') as arquivo:
    print(arquivo.read())