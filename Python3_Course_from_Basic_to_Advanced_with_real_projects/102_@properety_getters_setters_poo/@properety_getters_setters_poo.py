"""
Getters e Setters:

O getter obtem um valor e o setter configura um valor.
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter (coleta o preço)
    @property
    def nome(self):
        return self.nome2

    # Setter
    @nome.setter
    def nome(self, valor_n):
        self.nome2 = valor_n.lower()

    # Getter (coleta o preço)
    @property
    def preco(self):
        return self.preco2

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self.preco2 = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)
