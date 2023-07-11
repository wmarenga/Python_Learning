"""
Leitura de Arquivos:

Para ler conteúdo de um arquivo em Python, utilizamos a função integrada
open(), que literalmente significa 'abrir'.

open() => Na forma mais simples de utilização nós passamos apenas um
parâmetro de entrada, que neste caso é o caminho para o arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

Documentação:
https://docs.python.org/3/library/functions.html?highlight=open#open

# Obs: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro (FileNotFoundError).

# Exemplo:

arquivo = open(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura
    de arquivos\\texto.txt')
# print(arquivo)
# print(type(arquivo))

# <_io.TextIOWrapper name='C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\
Curso_Atual\\88) Leitura de arquivos\\texto.txt' mode='r' encoding='cp1252'>
# mode='r'=> abrindo somente como leitura
# <class '_io.TextIOWrapper'>

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a
função read().

# print(arquivo.read())

# não irá ler nada, pois chegou ao fim do arquivo e não terá nada a ser lido.
# print(arquivo.read())

# Obs: O Python, utiliza um recurso para trabalhar com arquivos chamado cursos.
Esse cursor, funciona como o cursor quando estamos escrevendo.

# Obs: A função read() lê todo o conteúdo do arquivo.

retorno = arquivo.read()

print(type(retorno)) # Retorna uma string
print(retorno)

# Como o retorno do arquivo é uma string, podemos utilizar os
# critérios e comandos de strings no retorno gerado do arquivo.

# Exemplo:
arquivo = open(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura de arquivos\\texto.txt')
retorno = arquivo.read()
# print(retorno)

ret_dividido = retorno.split()
print(len(ret_dividido))  # Gera uma lista de string, separadas pelos espaços.
"""
