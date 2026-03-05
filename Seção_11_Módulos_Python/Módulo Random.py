"""
→ Módulo Random



import random

print(random.random())

# Veja que para usar a função random colocamos o nome do pacote e o nome da função
#Separados por ponto (.)

from random import random
print(random())

for i in range(10):
    print(random())

from random import uniform

for i in range(10):
    print(uniform(3,7)) # 7 não é incluído

    
#Gerador de números da loteria - Números inteiros
from random import randint

for i in range(6):
    print(randint(1,61), end=', ') #Números de 1 a 60

#choice()
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(cartas[0])
"""





