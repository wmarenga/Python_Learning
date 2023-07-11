"""
POO - Propriedades - Properties


Em linguagens de programação como o Java, ao declararmos atributos privados
nas classes, costumamos criar métodos públicos para  a manipulação desses
atributos. Esses métodos são conhecidos por getters e setters, onde os
getters retornam o valor do atributo e os setters alteram o valor do mesmo.

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self): # Acessa ou retorna o valor de um atributo
        return self.__numero

    def get_titular(self): # Acessa ou retorna o valor de um atributo
        return self.__titular

    def set_titular(self, titular): # Altera o valor de um atributo
        self.__titular = titular

    def get_saldo(self): # Acessa ou retorna o valor de um atributo
        return self.__saldo

    def get_limite(self): # Acessa ou retorna o valor de um atributo
        return self.__limite

    def set_limite(self, limite): # Altera o valor de um atributo
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')


print(conta1.__dict__)
conta1.set_limite(999999) # Altera o valor de um atributo
print(conta1.__dict__)

"""
# Em Python, utilizamos propriedade em vez de getters e setters


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property  # Decorator para getters
    def numero(self):
        return self.__numero

    @property  # Decorator para getters
    def titular(self):
        return self.__titular

    @property  # Decorator para getters
    def saldo(self):
        return self.__saldo

    @property  # Decorator para getters
    def limite(self):
        return self.__limite

    @limite.setter  # Decorator para setters
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

print(conta1.valor_total)
print(conta2.valor_total)
