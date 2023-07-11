"""
Aula 23 - Tratamento de Erros e Exceções:
Exemplo:
primt(x) - Erro de sintaxe

print(x) - É um erro de semântica, pois a variável "x" não foi definida (NameError). Erro de excessão.

n = int(input('Num: '))
print(n)

(Excessão - ValueError), Se for digitado "oito" será apresentado erro, pois a variável é inteira.

a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

(Excessão - ZeroDivisionError), Se for digitado o valor "0" para o denominador teremos o erro de divisão por zero.
(Excessão - TypeError), (r = 2 / '2'), será apresentado erro pois estamos dividindo um número inteiro por uma string. 
(Excessão - IndexError), lst = [3, 6, 4], print(lst[3]), será apresentado um erro pois o índice 3 não existe na lista.
(Excessão - ModuloNotFoundError), import uteis, se o módulo não estiver definido será apresentado este erro.

Comando para identificar um erro:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
except TypeError:
    # falhau
except ValueError:
    # falhou
except OSError:
    # falhou
else:  # DEU CERTO. Esta cláusula é opcional.
    print(f'O resultado é {r:.1f}')
finally:  # Será executado sempre, independente de dar erro, esta cláusula é opcional.
    print('Volte sempre! Muito Obrigado!')    

"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    # DEU CERTO. Esta cláusula é opcional.
    print(f'O resultado é {r:.1f}')
finally:  # Será executado sempre, independente de dar erro, esta cláusula é opcional.
    print('Volte sempre! Muito Obrigado!')
