"""
→ Pickle


#Escrita em arquivo Pickle
felix = Gato('Felix')
pluto = Cachorro('Pluto')

#Arquivo Binarizado

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)

#Teste
#Escrita em arquivo Pickle
dexter = Gato('Dexter')
pandora = Cachorro('Pandora')

#Arquivo Binarizado

with open('Seção_17_Manipulando_Arquivos_CSV_JSON/animais2.pickle', 'wb') as arquivo:
    pickle.dump((dexter, pandora), arquivo)

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome=nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')


# Fazer a leitura de dados em arquivos pickle
with open('Seção_17_Manipulando_Arquivos_CSV_JSON/animais2.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print('\n')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
"""

import pickle

class Animal:

    def __init__(self, nome):
        self.__nome=nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')


# Fazer a leitura de dados em arquivos pickle
with open('Seção_17_Manipulando_Arquivos_CSV_JSON/animais2.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')
    print('\n')
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
