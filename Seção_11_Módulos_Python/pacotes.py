"""
→ Pacotes

from testes_pacotes import geek1, geek2

#importando geek3 e geek4
from testes_pacotes.teste_2 import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4,6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

print(geek3.funcao3() + ' ' + geek4.funcao4())
"""

#Importando apenas a função 
from testes_pacotes.geek1 import funcao1
from testes_pacotes.teste_2.geek4 import funcao4

print(funcao1(1,4))
print(funcao4())
