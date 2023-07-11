# @Property_Getters_Setters

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

# Getter


@ property
def preco(self):
    return self._preco

# Setter


@ preco.setter
def preco(self, valor):
    if isinstance(valor, str):
        valor = float(valor.replace('R$', ''))
    self._preco = valor


produto1 = Produto('Camiseta', 99)
produto1.desconto(5)
print(f'Valor de Produto1 com desconto: {produto1.preco}')

# Simulacao de eroo
# produto2 = Produto('Calca', 'R$59')
# Correto
produto2 = Produto('Calca', 59)
produto2.desconto(15)
print(f'Valor de Produto2 com desconto: {produto2.preco}')
