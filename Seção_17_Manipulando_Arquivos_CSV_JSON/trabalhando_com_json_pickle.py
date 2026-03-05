"""
→ Trabalhando com JSON e Pickle


import json

ret = json.dumps(['produto', {'Playstation 5': ('2TB', 'Novo', '120V', 3499)}])
print(type(ret))
print(ret)

import json

class Gato:

    def __init__(self,nome, raca):
        self.__nome = nome
        self.__raca=raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
    

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

#Integrando o JSON com Pickle
import jsonpickle

class Gato:

    def __init__(self,nome, raca):
        self.__nome = nome
        self.__raca=raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
    

felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)

print(ret)


#Escrevendo o arquivo json/pickle
import jsonpickle

class Gato:

    def __init__(self,nome, raca):
        self.__nome = nome
        self.__raca=raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
    

felix = Gato('Felix', 'Vira-Lata')

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix) #encode modela para o formato jsonpickle
    arquivo.write(ret)
"""

import jsonpickle

class Gato:

    def __init__(self,nome, raca):
        self.__nome = nome
        self.__raca=raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca
    


with open('Seção_17_Manipulando_Arquivos_CSV_JSON/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)