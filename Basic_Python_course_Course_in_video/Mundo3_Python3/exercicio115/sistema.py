from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = '/Users/Marenga/Desktop/Programação/Python/Curso_em_Video/Mundo3_Python3/exercicio115/lib/arquivo/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Sair do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
