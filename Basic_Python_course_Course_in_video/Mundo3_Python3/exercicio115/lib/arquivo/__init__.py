
def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
        """
        for linha in a:
            dado = linha.splt(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        """
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        # 'at' => append arquivo de texto.
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome:<30} => {idade:>3} anos\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo Registro de {nome} adicionado.')
            a.close()
