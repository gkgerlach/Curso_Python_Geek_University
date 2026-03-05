"""
→ Métodos de datas e horas



#Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine(
    (datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time()
)

print(manutencao)


#Econtrar o dia da semana, weekday()
#Os dias da semana no weekday() começa em 0, sendo esta a segunda-feira

manutencao = datetime.datetime.combine(
    (datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time()
)

print(manutencao.weekday())
"""

