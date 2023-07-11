""" 
Try, Except, Else e Finally:

Dica de quando e onde tratar codigo:

Atencao! Toda entrada de dados deve ser tratada!

Obs: A funcao do usuario e Destruir seu sistema.

Else => E executado somente se nao ocorrer o erro.

# Exemplo (try/ except):

num = 0

try:
    num = int(input('Informe um numero:  '))
except ValueError:
    print('Valor incorreto, digite novamente: ')

print(f'Voce digitou {num} ')

# Exemplo (try/ except/ else):

num = 0

try:
    num = int(input('Informe um numero:  '))
except ValueError:
    print('Valor incorreto, digite novamente: ')
else:
    print(f'Voce digitou {num} ')

# O programa so entra no else se o valor estiver correto.

# Finally:

try:
    num = int(input('Informe um numero:  '))
except ValueError:
    print('Voce nao digitou um valor valido.')
else:
    print(f'Voce digitou o numero {num}')
finally:
    print('Executando o finally')

# Obs: O bloco finally e SEMPRE executado. Independente se houver excecao ou nao.

# O finally, geralmente e utilizado para fechar ou desalocar recursos.
# Ex.: Finalizacao com um acesso a banco de dados, fechar um arquivo para escrita, etc.

# Exemplo mais Complexo ERRADO:

def dividir(a, b):
    return a/ b


num1 = int(input('Informe o primeiro numero: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico.')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto.')

# Exemplo mais Complexo CERTO:
# Obs: Voce e responsavel pelas entradas das suas funcoes. Entao, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Nao e possivel realizar uma divisao por zero'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais Complexo - Tratamento generico:
# Obs: Bem mais simples, porem nao trata os erros individulamente.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais Complexo - Tratamento semi-generico:
# Obs: Bem mais simples, porem nao trata os erros individulamente.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err: # Podemos passar uma tupla com varios erros possiveis 
                                                    # e criar uma apelido para ver a descricao do erro.
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

"""
