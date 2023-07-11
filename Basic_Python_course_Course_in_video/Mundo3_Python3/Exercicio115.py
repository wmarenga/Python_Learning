# Exercício Python 115a - Criando um menú:
# Vamos criar um menu em Python, usando modularização.
#
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
# seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar um nova pessoa e listar todas as
# pessoas cadastradas.

from exercicio115.lib import interface
from exercicio115.lib import arquivo
from time import sleep

arq = '/Users/Marenga/Desktop/Programação/Python/Curso_em_Video/Mundo3_Python3/exercicio115/lib/arquivo/cursoemvideo.txt'

arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(
        ['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        interface.cabeçalho('Opção 1')
    elif resposta == 2:
        interface.cabeçalho('Opção 2')
    elif resposta == 3:
        interface.cabeçalho('Sair do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
