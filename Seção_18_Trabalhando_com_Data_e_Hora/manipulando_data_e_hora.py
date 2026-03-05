"""
→ Manipulando data e hora
import datetime
#print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

#Retorna a data e hora corrente
print(datetime.datetime.now())

#datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

#replace()
inicio = datetime.datetime.now()
print(inicio)

#Alterando o horário para 16h, 0min, 0s, 0micros
inicio = inicio.replace(hour=16,minute =0, second=0,microsecond=0)

print(inicio)



# Recebendo dados do usuário e convertendo em data

import datetime

evento = datetime.datetime(2026, 4, 1,0)

print(type(evento))

print(type('31/12/2025'))
print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/aaaa):  ')


nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento))
"""

import datetime

evento = datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))