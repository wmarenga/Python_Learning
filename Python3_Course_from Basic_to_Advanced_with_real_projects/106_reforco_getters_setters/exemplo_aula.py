# Ambos são funções:
# GETTER (@property) = (get) OBTER/ LER UM VALOR (.)  => podemos configurar sem o setter.
# SETTER (@setter) = (set) CONFIGURANDO UM VALOR (=)  => não podemos ter sem o getter.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.nome2

    @nome.setter
    def nome(self, nome):
        print('SETTER FOI EXECUTADO')
        self.nome2 = nome.title()

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'


p1 = Pessoa('otávio')
print(p1.nome)
print(p1.sobrenome)
