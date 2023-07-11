# Sintaxe Basica usual

# POO (Identificado por class e o Nome da classe iniciado em maiuscula)
# No POO criamos moldes para elaborar novos objetos mais elaborados
'''
class Nome:
    objetos de classe
    metodos de classe


class Nome:
    metodo construtor
    objetos de classe
    metodos de classe
'''
# Criando uma classe vazia


from random import randint


class Pessoa:
    pass

# Criando atributos de classe de fora da classe


pessoa1 = Pessoa()

pessoa1.nome = 'Fernando'  # type: ignore
pessoa1.idade = 32  # type: ignore

print(pessoa1.nome)  # type: ignore
print(pessoa1.idade)  # type: ignore

# Criando funcoes (metodos de classe) dentro de uma classe
# Sempre que uma funcao esta dentro de uma classe, temos que incluir dentro de parenteses (self)


class Pessoa1:
    def acao1(self):
        print('ACAO 1 sendo executada...')


pessoa2 = Pessoa1()

pessoa2.acao1()


# Criando uma classe com metodo construtor (__init__) e objetos internos


class Pessoa2:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura


pessoa3 = Pessoa2('Fernando', 32, 'M', 1.90)


print(pessoa3.nome, pessoa3.idade)
print(f'Bem Vindo {pessoa3.nome}, parabens pelos seus {pessoa3.idade} anos!!!')


# Mais de um metodo de classe dentro de uma classe
# Precisamos seguir esta ordem (1-variavel global da classe, 2-metodo construtor, 3-metodo de classe)

class Pessoa3:
    # Seria o scopo global da classe
    ano_atual = 2020

    def __init__(self, nome, idade):
        # Criacao dos objetos do metodo construtor
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f'Seu ano de nascimento e {ano_nasc}')


pessoa4 = Pessoa3('Fernando', 32)

pessoa4.ano_nascimento()

# Usando metodos de classe de fora da classe


class Pessoa4:
    # Seria o scopo global da classe
    ano_atual = 2020

    def __init__(self, nome, idade):
        # Criacao dos objetos do metodo construtor
        self.nome = nome
        self.idade = idade

    ''' Torma o nosso metodo (funcao) acessivel ao escopo global. Este marcador
    e opcional (apenas para ficar mais direcionado para o metodo correto)'''
    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


pessoa5 = Pessoa4.ano_nasc('Fernando', 1987)

print(pessoa5.idade)

# Metodos estaticos

# Sao os metodos que nao possuem instancias como atributos.
# Funcionam como uma funcao normal dentro da classe


class Pessoa99:
    @staticmethod
    # Nao precisamos inserir nenhum metodo de classe (self), pois a funcao se tornou uma funcao comum
    def gerador_id():
        gerador = randint(100, 999)
        return gerador


print(Pessoa99.gerador_id())


# Atributos de classe

class Classe1:
    var1 = 101001


variavel1 = Classe1()

print(Classe1.var1)

print(variavel1.var1)

# Mudando um atributo de classe


class Classe2:
    var2 = str(101001)


variavel2 = Classe2()

Classe2.var2 = 'Maria'

print(Classe2.var2)


# Encapisulamento

class BaseDeDados:
    def __init__(self):
        self.dados = {}
        # self.dados = {} => Acessivel e desprotegido
        # self._dados = {}
        # self._dados = {} => declarado como protegido (ainda acessivel de fora da classe)
        # self.__dados = {}
        # self.dados = {} => declarado como privado - inacessivel e imutavel de fora da classe


base = BaseDeDados()

print(base.dados)

# Setando parametros como False em um metodo, afim de que sejam ignorados
''' Estes parametros se tornam opcionais. Se nao forem atribuidos valores,
os mesmos serao desconsiderados'''


class Pessoa2:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

# Usuario compartilhado entre metodos


class Pessoa:

    def __init__(self, nome, login=False, logoff=False):
        # Criacao dos objetos do metodo construtor
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        self.login = True
        return f'Bem Vindo {self.nome}, voce esta logado no sistema'


usuario = Pessoa('Fernando')

print(usuario.logar())
print(usuario.login)

# Excluir o valor de uma atributo

del usuario.nome
print(usuario.nome)
