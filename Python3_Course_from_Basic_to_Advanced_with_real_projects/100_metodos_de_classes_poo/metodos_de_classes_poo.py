"""
Quando usar um método de instância ou de classe?

- Este método é relacionado à classe (molde em geral) ou a instância,
ou seja, específico de cada objeto. Cada objeto terá um valor diferente.
"""


class Pessoa:
    # atributo de classe (ano_atual)
    ano_atual = 2019

    # Métodos de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Criando um método de classe
    # Teremos acesso a varável que é um atributo da classe (ano_atual)
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


#p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()
