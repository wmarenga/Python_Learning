"""
Sistema de Arquivos - Manipulação:

Documentação:
https://docs.python.org/3/library/os.html?highlight=os#module-os

# Descobrindo se um arquivo ou diretório existe
# Podemos usar condições if, while, etc para várias situações
# (criar, excluir, etc) arquivos/ diretórios.

import os

# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('teste.py'))  # True

# Diretório

# Paths relativos
print(os.path.exists('src'))  # True
print(os.path.exists('geek'))  # False
print(os.path.exists('Exercicios/Exercicio2_Media.py'))  # True

# Paths absolutos
print(os.path.exists(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\tests\\testsoma.py'))  # True
print(os.path.exists(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\geek.py'))  # False
print(os.path.exists(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\env'))  # True

# Criando arquivos

# Forma 1:
open('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\arquivo-teste.txt', 'w').close()

# Forma 2:
open('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\arquivo-teste2.txt', 'a').close()

# Forma 3:
with open('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\arquivo-teste3.txt', 'w') as arquivo:
    pass

# Somente funciona em sistemas Unix:
os.mknod('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\arquivo-teste4.txt')
os.mknod('95) Sistema de Arquivos_Manipulacao/geek')

# Obs: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError
# Obs: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

# Caminho relativo
os.mkdir('templates')
# Obs: A função mkdir() cria um diretório se este não existir. Caso contrário, teremos FileExistsError

# Caminho absoluto
os.mkdir('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\templates')

Obs: Se não tivermos permissão para criar o diretório teremos um PermissionError

os.mkdir('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\templates\\geek\\university')
Obs: Se o sistema não encontrar o diretório/ caminho para criar o diretório, apresentará o
erro FileNotFoundError.

# Podemos criar uma cadeia de diretórios (multi-diretórios)

# absoluto
# os.makedirs('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\templates\\geek\\university')

# relativo
os.makedirs('95) Sistema de Arquivos_Manipulacao\\templates\\geek\\university')

# Obs: Se já existir o diretório, teremos um FileExistsError

# Se o diretório já existir, não apresentar erro (ignorar)

# relativo
os.makedirs(
    '95) Sistema de Arquivos_Manipulacao\\templates\\novo2\\outro2', exist_ok=True)
# Obs: Não exclui nada, somente ignora.

# Renomeando arquivos e diretórios

os.rename('95) Sistema de Arquivos_Manipulacao\\templates',
         '95) Sistema de Arquivos_Manipulacao\\geek2')

# Internamente
os.rename('95) Sistema de Arquivos_Manipulacao\\geek2\\bosta',
          '95) Sistema de Arquivos_Manipulacao\\geek2\\university')
# Obs: Se o diretório não existir, teremos um FileNotFoundError
# Obs: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomeando arquivos
os.rename(
    '95) Sistema de Arquivos_Manipulacao\\geek2\\university\\university\\teste.txt', '95) Sistema de Arquivos_Manipulacao\\geek2\\university\\university\\prova.txt')

# Removendo arquivos
# Obs: ATENÇÃO! Tomem cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório,
# eles não vão para a lixeira. Eles somem.

os.remove(
    '95) Sistema de Arquivos_Manipulacao\\geek2\\university\\university\\prova.txt')

# Obs: Se você estiver no Windows e o arquivo que você for deletar estiver em uso,
# será gerado um erro (Não observei este erro)

# Obs: Caso o arquivo não exista teremos o FileNotFoundError

# Obs: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError
# Como remover diretórios (Varios)
os.rmdir('95) Sistema de Arquivos_Manipulacao\\geek2\\novo2\\outro2')

# Obs: Se o diretório tiver qualquer conteúdo, teremos um OSError
# Obs: Se o diretório não existir, teremos um FileNotFoundError

*** Criando vários arquivos no sistema Posix (Linux e Mac Os)
touch arquivo{1..1000}.txt

# Removendo uma árvore de diretórios

# Somente arquivos
for arquivo in os.scandir('95) Sistema de Arquivos_Manipulacao\\geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Removendo uma árvore de diretórios vazios
os.removedirs(
    '95) Sistema de Arquivos_Manipulacao\\geek2\\university\\university')
# Temos que informar o caminho completo, até o último diretório.
# Se algum dos diretórios contiver arquivos ou outros diretórios/ arquivos,
# o processo é interrompido.

# Instalando uma biblioteca para mover para o lixo (arquivos e diretórios)
>> pip install send2trash
>> python -m pip install -U send2trash

Se não for possível instalar temos que antes, instalar (Linux e Mac OS):
>> sudo apt-get install lsb-core

# Importando a biblioteca send2trash (Diretórios e Arquivos)

import os
from send2trash import send2trash

# Não vai para a lixeira. É deletado imediatamente
# os.remove(
#    '95) Sistema de Arquivos_Manipulacao\\geek2\\novo2\\conteudo.txt')

# vai para a lixeira, podendo ser restaurado (arquivo).
send2trash(
    '95) Sistema de Arquivos_Manipulacao\\geek2\\novo2\\conteudo.txt')

# Obs: Se o arquivo não existir, teremos OSError

# vai para a lixeira, podendo ser restaurado (Diretório).
send2trash(
    '95) Sistema de Arquivos_Manipulacao\\geek2\\novo2')

# Trabalhando com arquivos e diretórios temporários

# Criando um diretório temporário
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\95) Sistema de Arquivos_Manipulacao\\geek2\\arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# Obs: Possivelmente, o código acima não irá funcionar se você estiver utilizando o
# Windows. Por conta deste sistema trabalhar de forma diferente com arquivos temporários.

# Criando um arquivo temporário

import os
import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')  # o b é para converter para binário
    tmp.seek(0)
    print(tmp.read())

# Obs: Em arquivos temporários só conseguimos escrever bits. Por este motivo
# utilizamos b'com uma string'.

# Podemos criar sem o with também

import os
import tempfile

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
# Outra maneira de criar

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()
"""
