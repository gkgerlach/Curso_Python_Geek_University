"""
→ Trabalhando com Delta de Data e Hora

import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2028,3,3,0)
nascimento = datetime.datetime(1998,4,20,4)

tempo_para_evento = aniversario - data_hoje


print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
"""

import datetime

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento = data_compra + regra_boleto
print(vencimento)