class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):  # A classe B está herdando tudo que está em A.
    def falar(self):
        def falar(self):  # A classe B está sobrescrevendo o método em A.
            print('Falando... Estou em B.')


class C(A):  # A classe C está herdando de A também.
    def falar(self):
        print('Falando... Estou em C.')


class D(B, C):  # Herança múltipla (busca da esquerda para direita.)
    def falar(self):
        print('Falando... Estou em C.')


d = D()
d.falar()
