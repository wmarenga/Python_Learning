"""
Atributos de Classe - POO:

class A:
    vc = 123


a1 = A()
a2 = A()

A.vc = 321  # Altera a variavel de classe para todas as instâncias

# Não estamos alterando a variável da classe e somente criando um atributo
# direto na instância (a1 ou a2)
a1.vc = 444  # Aleramos somente a instância a1
print(a1.vc)  # Instânciando como a1
print(a2.vc)  # Instânciando como a2
print(A.vc)  # direto da classe

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

"""


class A:
    vc = 123

    def __init__(self):
        #self.vc = 321
        pass


a1 = A()
a2 = A()
A.vc = 'Alterado'

print(a1.vc)  # Instânciando como a1  (Output: 321)
print(a2.vc)  # Instânciando como a2  (Output: 321)
print(A.vc)  # direto da classe  (Output: 123)
