"""
Decoradores com Diferentes Assinaturas:

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanha de {acompanhamento},
    por favor.'


# Testando

# print(saudacao(input('Digite o seu nome: ')))

# TypeError: ordenar() missing 1 required positional argument: 'acompanhamento'
# print(ordenar('Picanha', 'Batata Frita'))

# Para resolver o TypeError, utilizamos um padrão de projeto chamado Decorator
# Pattern (*args, **kwargs)

# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros
# de entrada.

# Refatorando com o Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanha de {acompanhamento}, por favor.'


print(ordenar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())

# Obs: Vale lembrar que podemos utilizar parâmetros nomeados.

print(ordenar(acompanhamento='Batata Frita', principal='Picanha'))

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando

print(soma_dez(10, 12))  # 22

# Deveria ser 22, porem o primeiro valor tem que ser 10.
# Valor incorreto! Primeiro argumento precisa ser 10
print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))

# Valor incorreto! Primeiro argumento precisa ser pizza
print(comida_favorita('sanduiche', 'pizza'))

"""
