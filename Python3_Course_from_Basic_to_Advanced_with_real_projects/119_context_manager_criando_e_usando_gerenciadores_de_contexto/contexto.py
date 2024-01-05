"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # Tratei a exceção
        return True

# Sem gerenciador de contexto
arquivo = open('abc.txt', 'w')
arquivo.write('Alguma coisa')
arquivo.close()

# com gerenciador de contexto
with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

"""
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir(Path.home() / 'Desktop/Curso_Atual/119_context_manager_criando_e_usando_gerenciadores_de_contexto/abc2.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
