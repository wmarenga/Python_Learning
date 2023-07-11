import interface
#import sys
#sys.path.append(
#    '/Users/Marenga/Desktop/Programação/Python/Curso_em_Video/Mundo3_Python3/exercicio115/lib/interface')


def arquivoExiste(nome):
    try:
        a = open(nome, 'r+')  # "rt" => read and test.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'r+')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
