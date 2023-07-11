"""
Atributos (POO):

Atributos representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:

- Atributos de instância;
- Atributos de classe;
- Atributos DInâmicos.

Atributo de instância:

Atributos de instância: São atributos declarados dentro do método construtor.

OBS: Método construtor: É um método especial utilizado para a construção do
objeto.


# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python:

def funcao(): # Como a função (funcao) está fora da classe, ela se
                chama função. Dentro da classe ela se chamará Método.
    print('Algo')

class Lampada:

    def __init__(self, voltagem, cor): # __init__ => Método construtor
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# O self é apenas uma convenção, podemos utilizar qualquer nome no lugar
de self, contudo o mais correto é utilizar self mesmo.

class Teste:
    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade


Em Python, por convenção, ficou estabelecido que, todo atributo de uma
classe é público. Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como
privado, ou seja, que deve ser acessado/utilizado somente dentro da
própria classe onde está declarado, utiliza-se __ duplo underscore no
início de seu nome.

Isso é conhecido também como Name Mangling.

# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email    # Público
        self.__senha = senha  # Privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem
Python não vai impedrir que façamos acesso aos atributos sinalizados
como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email) # >> user@gmail.com

print(user.__senha)  # AttributeError

print(dir(user)) # '_Acesso__senha' => _Nome da classe__Nome do
                    atributo restrito

print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer
                            este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

O que significa atributos de instância?

Significa, que ao criarmos instâncias/objetos de uma classe, todas as
instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

# Atributos de Classe

# Atributos de classe, são atributos, que são declarados diretamente
na classe, ou seja, fora do contrutor. Geralmente já inicializamos um valor,
e este valor é compartilhado entre todas as instâncias da classe. Ou seja,
ao invés de cada instância da classe ter seus próprios valores como é o caso
dos atributos de instância, com os atributos de classe todas as instâncias
terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributo de classe (estáticos)
    imposto = 1.05  # 0.05% de imposto
    contador = 0                    # Atributo de classe

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome            # Atributo de instância
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso
a um atributo de classe.

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos
de classe aqui em Python são chamados de atributos estáticos;

# Atributos Dinâmicos -> Um atributos de instância que pode ser criado
em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor},
Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor},
Peso: {p1.peso}') # AttributeError

# Deletando atributos

print(p1.__dict__) # Mostra/ Acessa o dicionário de atributos de instância
print(p2.__dict__)

# print(Produto.__dict__) # Mostra/ Acessa o dicionário de atributos de classe

del p2.peso # Funciona para atributo dinâmico
del p2.valor # Também funciona para atributo de instância
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)

# Classes com Atributo de Instância Público

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email    # Público
        self.__senha = senha  # Privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

"""
