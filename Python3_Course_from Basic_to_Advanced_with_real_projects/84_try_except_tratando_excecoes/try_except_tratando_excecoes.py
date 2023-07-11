# Exemplo básico (mostra qualquer erro - não aconselhavel)

from logging import exception
from re import A


try:
    print(a)
except:
    print('Erro!')

# Exemplo mais específico
try:
    # print(a)  # NameError
    # a = []
    # print(a[1])  # IndexError
    # a = {}
    # print(a[1])  # KeyError
    a = {}
except NameError as erro:  # Somente NameError
    print('Erro do desenvolvedor, fale com ele')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:  # captura qualquer outro erro no código
    print('Ocorreu um erro inesperado')
else:  # Será sempre executado quando o código não tiver erro.
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Será executado se tiver erro ou não.')


print('Bora continuar...')

# Método de tratar exceção atribuindo um valor padrão em caso de erro.

try:
    a = 1/0
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:  # Somente NameError
    print('Erro do desenvolvedor, fale com ele')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
except Exception as erro:  # captura qualquer outro erro no código
    print('Ocorreu um erro inesperado')
else:  # Será sempre executado quando o código não tiver erro.
    pass
finally:
    a = None


print(a)
