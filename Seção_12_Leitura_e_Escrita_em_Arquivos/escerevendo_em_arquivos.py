"""
→ Escrevendo em Arquivos


#Pythonica
with open('Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', 'w', encoding='utf=8') as arquivo:
    arquivo.write('Escrevendo qualquer coisa para testar a função open() \n')
    arquivo.write('Este curso está me ajudando a ficar bom em Python\n')
    arquivo.write('Estou aprendendo a ler arquivos\n')
    arquivo.write('Linguagem de alto nível (nível de abstração relativamente elevado)')

#Não Pythonica
arquivo = open('Seção_12_Leitura_e_Escrita_em_Arquivos/mais_um.txt', 'w', encoding='utf=8')

arquivo.write('Olá, texto para o arquivo "mais_um"\n')
arquivo.write('Fechando\n')

arquivo.close

with open('Seção_12_Leitura_e_Escrita_em_Arquivos/geek.txt', 'w', encoding='utf=8') as arquivo:
    arquivo.write('Geek\n'*100)
"""

with open('Seção_12_Leitura_e_Escrita_em_Arquivos/frutas.txt', 'w', encoding='utf=8') as arquivo:
    while True:
        fruta = input('Informa a fruta ou digite sair: ')
        if fruta.lower() != 'sair':
            arquivo.write(fruta + '\n')
            #ou arquivo arquivo.write('\n')
        else:
            break
