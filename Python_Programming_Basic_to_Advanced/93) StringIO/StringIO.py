"""
StringIO:

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o
software precisa ter permissão:
    - Permissão de Leitura => Para ler o arquivo;
    - Permissão de escrita => para escrever o arquivo.

StringIO => Utilizado para ler e criar arquivos em memória.

# Para utilizarmos o "StringIO", primeiro fazemos o import
from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio
# para inserirmos texto depois.
arquivo = StringIO(mensagem)
# Equivalente a: arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos.
print(arquivo.read())
# Obs: Não será gerado nenhum arquivo de fato (apenas em memória).

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
"""
