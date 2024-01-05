"""
Em Python tudo é um objeto: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)

*** Uma classe é um molde para ensinar a criar outros objetos.

# mcs-> metaclasse; name-> nome da classe que será criada;
# bases-> classes pai das classes que serão criadas; namespace-> contém todos os atributos e métodos criados na classe.


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala na class {name}.')
        else:
            if not callable(namespace['b_fala']):
                print(
                    f'b_fala precisa ser um método, não atributo na class {name}.')

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    def b_fala(self):  # método de classe
        print('Oi')
    teste = 'Wow'  # atributo de classe


b = B()
# b.fala()  # Instanciamos um método (fala) da classe pai (A) que chama um
# método (b_fala) da classe filha (B).
"""

# Impedindo que o atributo da classe filha (B) sobrescreva o atributo da classe pai (A).


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            # não conseguimos sobrescrever o valor da classe A.
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor C'


b = B()
c = C()
print(b.attr_classe)
print(c.attr_classe)
