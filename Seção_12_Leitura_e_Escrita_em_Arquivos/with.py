"""
→ With
"""

# Bloco With - Abre e fecha

with open(r'Seção_12_Leitura_e_Escrita_em_Arquivos/texto.txt', encoding='utf=8') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)

print(arquivo.closed)