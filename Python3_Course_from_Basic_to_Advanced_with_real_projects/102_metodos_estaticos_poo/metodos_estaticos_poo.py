from random import randint


class Pessoa:
    # atributo de classe (ano_atual)
    ano_atual = 2019

    # Métodos de instância
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Métodos de instância = self (precisamos de uma instância para
    # utilizar o método)
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Criando um método de classe
    # Teremos acesso a varável que é um atributo da classe (ano_atual)
    # No método de classe não precisamos de instâncias mas sim da
    # classe em si.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # O método não necessita nem da instância e nem da classe (função normal)
    # Não utilizamos self e cls dentro de métodos estáticos
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


# p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
# Poderíamos chamar o método pela instância também (Pessoa())
print(p1.gera_id())
