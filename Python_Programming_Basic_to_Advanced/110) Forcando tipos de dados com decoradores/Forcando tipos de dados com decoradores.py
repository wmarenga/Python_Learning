"""
Forcando tipos de dados com decoradores:

# Em Python, não precisamos declarar um variável como inteira, string, etc.,
basta atribuírmos o dado à variável e automaticamente o seu tipo será definido.

numero = 10
nome = 'Felicity'

Em Java:

int numero = 10;
string nome = 'Felicity';

Em algumas situações, nós precisaremos forçar a predefinição do tipo prévia de
uma varível.

zip

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)

(1, 2), (3, 4), (5, 6)
"""
# Exemplo


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # str('Geek'), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir('1', 5)
