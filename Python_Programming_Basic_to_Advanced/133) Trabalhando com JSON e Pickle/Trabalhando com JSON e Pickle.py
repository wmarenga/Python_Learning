"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores).

import json

# Converte todas as strings para aspas duplas, pois o json não trabalha com aspas simples.
# ["produto", {"PlayStation 4": ["2TB", "Novo", "220V", 2340]}]
ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

# {'_Gato__nome': 'Felix', '_Gato__raca': 'Vira-Lata'} => formato dicionário normal
print(felix.__dict__)

# {"_Gato__nome": "Felix", "_Gato__raca": "Vira-Lata"} => formato para json
ret = json.dumps(felix.__dict__)
print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

ret = jsonpickle.encode(felix)

print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')

with open('133) Trabalhando com JSON e Pickle/felix.json', 'w', encoding='cp1252') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('133) Trabalhando com JSON e Pickle/felix.json', 'r', encoding='cp1252') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
"""
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('133) Trabalhando com JSON e Pickle/felix.json', 'r', encoding='cp1252') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
