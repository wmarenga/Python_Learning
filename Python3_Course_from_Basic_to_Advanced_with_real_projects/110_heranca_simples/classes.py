# É chamada de super classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando!')


class Cliente(Pessoa):
    # A classe Cliente herda tudo de Pessoa (subclasse)
    def comprar(self):
        print(f'{self.nomeclasse} está comprando!')


class Aluno(Pessoa):
    # A classe Aluno herda tudo de Pessoa (subclasse)
    def estudar(self):
        print(f'{self.nomeclasse} está estudando!')

# As subclasses não herdam métodos entre sí.
