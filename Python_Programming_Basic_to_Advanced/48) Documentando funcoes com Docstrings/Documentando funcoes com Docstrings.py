""" 
Documentando funcoes com Docstrings:

# Imprimir a ajuda mo metodo (print)
print(help(print))

# Exemplos

def diz_oi():
    Uma funcao simples que retorna a string 'Oi! '
    return 'Oi! '

print(diz_oi())
print(help(diz_oi))

# Obs: Podemos ter acesso a documentacao de uma funcao em Python utilizando a propriedade 
# especial __doc__
help.__doc__
print.__doc__

"""
def exponencial(numero, potencia=2):
    """ 
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' infromada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potemcia: Potencai que queremos gerar o exponencial. Por padrao e 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

exponencial.__doc__

#Output:
"""
\n    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' infromada.
\n    :param numero: Numero que desejamos gerar o exponencial.
\n    :param potemcia: Potencai que queremos gerar o exponencial. Por padrao e 2.
\n    :return: Retorna o exponencial de 'numero' por 'potencia'.
\n    
"""

# Utilizando o help(exponencial), fica tudo mais organizado

# >>> help(exponencial)
"""
Help on function exponencial in module __main__:

exponencial(numero, potencia=2)
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' infromada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potemcia: Potencai que queremos gerar o exponencial. Por padrao e 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
"""