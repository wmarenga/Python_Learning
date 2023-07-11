from lib import interface
from lib import arquivo
from time import sleep

arq = '/Users/Marenga/Desktop/Programação/Python/Curso_em_Video/Mundo3_Python3/exercicio115/lib/arquivo/cursoemvideo.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(
        ['Ver Pessoa Cadastrada', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabeçalho('Opção 2')
    elif resposta == 3:
        interface.cabeçalho('Sair do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
