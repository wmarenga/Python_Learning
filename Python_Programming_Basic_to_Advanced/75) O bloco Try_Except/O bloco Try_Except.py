""" 
O bloco Try/ Except:

Utilizamos o bloco try/ except para tratar erros que podem ocorrer no nosso codigo. Prevenindo
assim que o programa para de funcionar e o usuario receba mensagens de erro insperadas.

A forma geral mais simples e:

try:
    /execucao problematica
except:
    /o que deve ser feito em caso de problema

# Exemplo 1:- Tratando um erro generico

#geek() # NameError: name 'geek' is not defined

try:
    geek() # NameError: name 'geek' is not defined
except:
    print('Deu algum problema')

# Tente executar a funcao Geek(), caso voce encontre erros, imprima a mensagem de erro.

# Exemplo 2:- Tratando um erro generico

try:
    len(5)
except:
    print('Deu algum problema')

Obs: Tratar erro de forma generica nao e a melhor forma de tratamento de erros. O ideal
e sempre tratar de forma especifica.

# Exemplo 3 - Tratando um erro especifico

try:
    geek()
except NameError:
    print('Voce esta utilizando uma funcao inexistente')

# Exemplo 4 - Tratando um erro especifico

try:
    len(5) # TypeError: len() takes exactly one argument (0 given)
except NameError:
    print('Voce esta utilizando uma funcao inexistente')

# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5) # TypeError: len() takes exactly one argument (0 given)
except TypeError as err:
    print(f'A aplicacao gerou o seguinte erro: {err}')

# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5) # TypeError: len() takes exactly one argument (0 given)
except TypeError as err:
    print(f'A aplicacao gerou o seguinte erro: {err}')
    
# Exemplo 6 - Tratando um erro especifico com mais um generico

try:
    geek()
except NameError as erra:
    print(f'Deu NamedError: {erra}')
except NameError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
    
# Exemplo 7 - Tratando um erro especifico com funcoes

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

print(pega_valor(dic, 'game')) # KeyError
print(pega_valor(7, 'nome')) # TypeError

"""
