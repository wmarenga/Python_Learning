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

    def falar(self):
        print('Estou em Cliente.')


"""
class ClienteVip(Cliente):
    # A classe ClienteVip herda tudo de Cliente (subclasse)
    def falar(self):
        # Estamos chamando o método da classe pai Pessoa()
        # ou a classe superior/ acima Cliente()
        super().falar()
        Pessoa.falar(self)  # Ou tb especificando a classe
        # Este método está sobrepondo o falar() de Pessoa.
        print('Outra coisa qualquer.')
        # As subclasses não herdam métodos entre sí.
"""
# Adicionando o sobrenome


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        # Pessoa.__init__(self, nome, idade)  # Outra maneira
        self.sobrenome = sobrenome  # Adicionando um novo atributo

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
