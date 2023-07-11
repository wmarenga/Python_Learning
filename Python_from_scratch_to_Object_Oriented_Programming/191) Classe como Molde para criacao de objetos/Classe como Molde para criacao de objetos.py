# Clasee como Molde para criacao de objetos
# Usaremos a classe como molde para varias entradas de dados distintos

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa1 = Pessoa('Mariana', 32, 'F', 1.90)
print(pessoa1.nome)
print(pessoa1.altura)

pessoa2 = Pessoa('Gilberto', 33, 'M', 1.90)
print(pessoa1.nome)
print(pessoa2.idade)
