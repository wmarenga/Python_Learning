# Funcoes

# Sintaxe Basica de uma funcao
def nome_da_funcao2(parametros):
    "corpo da funcao"


def minha_funcao():
    print('Minha primeira funcao personalizada!!!')


minha_funcao()

# Definindo uma funcao sem parametro


def exibe_mensagem():
    print('Seja bem-Vindo!!!')
    # Poderia ser, dependendo do contexto, return 'Seja Bem-Vindo!!!'


exibe_mensagem()
msg = exibe_mensagem()

# Chamando uma funcao


def mensagem7():
    print('Seja Bem Vindo!!!')


mensagem1 = mensagem7()
print(mensagem1)

# Criando uma funcao que inicialmente nao realiza nenhuma acao


def funcao99():
    pass


var1 = funcao99()  # Nao acontecera absolutamente nada

print(type(var1))  # Retornara NoneType

# Funcao interagindo com o usuario
usuario3 = input('Digite o seu nome: ')


def mensagem_digitada(nome):
    print(f'Bem vindo {nome}!!!')


# Qualquer valor que eu inserir em usuario3 sera inserido na funcao (nome = qualquer valor)
mensagem_digitada(usuario3)


def funcao10(msg='Ola', nome='usuario', msg2='Seja Bem Vindo!!!'):
    return f'{msg} {nome} {msg2}'


variavel3 = funcao10(nome=input('Digite o seu nome: '))

print(variavel3)


# Passando o parametro ao chamar a funcao


def funcao5(msg):
    print(msg)


mensagem4 = 'Boas Vindas!!!'
funcao5(mensagem4)


# Parametrizando uma funcao ao chamar a mesma
def mensagem3(nome):
    print(f'Bem vindo(a) {nome}!!!')


usuario2 = mensagem3('Fernando')
print(usuario2)


# Funcoes com 2 ou mais parametros


def mensagem(nome, idade):
    print(f'{nome} tem {idade} anos...')


# Temos que seguir a ordem (A, B)
usuario1 = mensagem('Fernando', 33)

print(usuario1)

# Definindo parametros padrao


def funcao2(msg, nome='usuario'):
    print(f'{msg} para {nome}')


funcao2('Bem Vindo!!!')
funcao2('Bem Vindo!!!', 'Fernando')

# Passando um parametro nomeado e recebendo o resto padrao


def funcao8(msg='Ola', nome='usuario', msg2='Seja Bem Vindo!!!'):
    print(msg, nome, msg2)


# Nesta situacao temos que especificar aonde queremos alterar o dado
funcao8(msg='Ui', nome='Fernando')

# Funcao input() como parametro de uma funcao personalizada


def funcao4(mensagem, nome):
    print(mensagem, nome)


funcao4('Ola', input('Digite o seu nome: '))

# Variaveis dentro de funcoes


def funcao6(msg='Ola', nome='usuario', msg2='Seja Bem Vindo!!!'):
    nome = input('Digite o seu nome: ')
    print(msg, nome, msg2)


variavel2 = funcao6()


# Operacao matematica ou logica por meio de funcao

def soma(n1, n2):
    return f'O resultado da soma e: {n1 + n2}'


n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))

print(soma(n1, n2))

# Operacoes compostas dentro de uma funcao


def aumento_percentual(valor, percentual):
    return (valor + (valor * percentual) / 100)


num1 = int(input('Digite o valor: '))
num2 = int(input('Voce deseja somar quantos % ? '))

calculo = aumento_percentual(num1, num2)

print(f'O valor final sera: {calculo:.2f} reais')

print(f'O valor final sera: {calculo:.2f} reais')

print(f'O valor final sera: R$ {calculo:.2f} reais')


# Estruturas condicionais dentro de funcoes 1


def repetidor(msg):
    contador = 0
    while contador < 5:
        print(msg)
        contador += 1


# Nao e necessario especificar msg (pode ser omitido)
repetidor(msg=input('Digite algo para ser repetido 5 vezes: '))

# Estruturas condicionais dentro de funcoes 2


def divisao(n1, n2):
    if n2 == 0:
        return 'Operacao Invalida'
    else:
        return round((n1 / n2), 2)


num1 = int(input('Digite o Primeiro numero: '))
num2 = int(input('Digite o Segundo numero: '))

print(f'O resultado da divisao e: {divisao(num1, num2)}')

# Estruturas condicionais dentro de funcoes 3 (Exercicio Fizz Buzz)


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} e divisivel por 3 e por 5'
    if num % 5 == 0:
        return f'Buzz, {num} e divisivel por 5'
    if num % 3 == 0:
        return f'Fizz, {num} e divisivel por 3'
    return num


print(fizz_buzz(num=int(input('Digite um numero: '))))

# Funcao com argumentos externos
# Usando (*args), podemos informar quantos argumentos quisermos


def funcao97(*args):
    for parametro in args:
        print(parametro)


argumentos = ('nome', 'idade', 'sexo')

funcao97(argumentos)

# Desempacotando elementos de uma lista como parametros de uma funcao


lista1 = ['nome', 'idade', 'sexo', 'nacionalidade']


def funcao(*args):
    print('Informacoes necessarias: ')
    print(args)


funcao(lista1)

# Funcao com parametros baseados em *args e **kwargs

# Supondo que esta cadastrando senhas e usuarios em um sistema
# *args - permite que possamos informar variaveis externas
# **kwargs - parametros definidos manualmente dentro dos parametros do chamamento da funcao


def cadastro(*args, **kwargs):
    print(args)
    print(kwargs)


senhas_padrao = [12345, 11111, 54321]

resultado = cadastro(*senhas_padrao, usuario='user', administrador='admin')

resultado

# Parametros externos para Args e nomeados para Kwargs
# Por convencao se usa *args e **kwargs mas poderiamos usar qualquer sequencia de caracteres. O importante e manter 1* e 2** (*aaa = *args/ *bbb = **kwargs)


def cadastro1(*args, **kwargs):
    nome = kwargs['usuario']
    nome2 = kwargs['administrador']
    senha1 = args[0]
    senha2 = args[1]

    print(f'O usuario padrao e: {nome}')
    print(f'O administrador e: {nome2}')
    print(f'A senha padrao e: {senha1}')
    print(f'A senha alternativa e: {senha2}')


senhas_padrao = [12345, 11111]

cadastro1(*senhas_padrao, usuario='user', administrador='admin')

# Fiuncao que recebe outra funcao cokmo parametro

# Esta funcao recebe um parametro e executa ele mesmo


def mestre(funcao96):
    return funcao96()


def msg_boas_vindas():
    return 'Seja Muito Bem Vindo!!!'


executa = mestre(msg_boas_vindas)

print(executa)

# Expressoes Lambda/ Funcoes Vazias

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))


def variavel2(num1, num2): return num1 * num2


print(variavel2(num1, num2))

# Escopo Global e Escopo Local

variavel1 = 'Paulo'


def funcao50():
    print(f'Print da variavel do escopo global: {variavel1}')


funcao50()


def funcao51():
    variavel2 = 'Maria'
    print(f'Print da variavel do escopo local: {variavel2}')


funcao51()

# Modificando uma variavel global de dentro de uma funcao

num1 = 100

print(f'Variavel com seu valor inicial: {num1}')


def modificador():
    global num1
    num1 = 200
    print(f'Variavel alterada dentro da funcao: {num1}')


modificador()

print(f'Variavel atualizada pela funcao modificador: {num1}')


def repetidor(msg, vezes):
    contador = 0
    while contador < vezes:
        print(msg)
        contador += 1


print(repetidor(msg=input('Digite uma mensagem a ser repetida; '),
      vezes=int(input('Digite quantas vezes que repetir a mensagem: '))))
