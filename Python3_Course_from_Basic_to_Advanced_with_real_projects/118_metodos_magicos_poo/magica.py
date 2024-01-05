# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):
        print('Método new foi chamado')

        # SINGLETON
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    # Com este método podemos chamar como se fosse uma função a(1, 2, 3, 4, 5, nome='Luiz')
    def __call__(self, *args, **kwargs):
        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    def __del__(self):
        print('Objeto coletado.')

    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = A('luiz otávio')
print(a)  # Será exibido em def __str__(self):
print(len(a))  # Será exibido em def __len__(self):
