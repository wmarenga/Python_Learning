"""
Sistema de Arquivos e Navegação:

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos
importar e fazer uso do módulo "os".

os => Operating System (Sistema Operacional).

# Fazer o import
import os

# getcwd() => pega o current work directory (diretório de trabalho corrente)
# Retorna o caminho absoluto
print(os.getcwd())

# Podemos utilizar o chdir() para mudar o diretório:

# Adiantando um diretório
import os
os.chdir('94) Sistema de Arquivos e Navegacao')
print(os.getcwd())

# Voltando 1 diretórios
os.chdir('..')
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

import os
print(os.path.isabs('C:\\Users\\wmare\\OneDrive\\Área de Trabalho
\\Curso_Atual'))  # True

# Obs: para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios. Usando duas barras invertidas.
print(os.path.isabs('c:\\Users\\wmare'))

windows => c:\
Posix (Linux, Mac) => / (Melhor organização e segurança)

Linux:
sudo apt install tree
Exibe em forma de árvore de diretórios

Paths:

Absolute => C://caminho completo até o arquivo (windows)
            /home/wmare/arquivo.py (Linux)

Relative => "/home/workspaces/backups/../ (Linux)"
# ../ volta um diretório acima
# ./ diretório local

Verifica informações da máquina em Windowsr e Linux

import sys
import os
import platform

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes do sistema operacional
# print(os.uname()) # No Linux

print(platform.uname())  # No windows

print(sys.platform)

import os

# C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual
print(os.getcwd())

# Junta o path e cria diretórios
res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros,
# sendo o primeiro o diretório atual e o segundo o diretório
# que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()
import os
# print(os.listdir())  # Gera uma lista
# print(len(os.listdir()))  # Quantos diretórios temos

# print(os.listdir('c:\\'))  # Especificando um caminho
# print(len(os.listdir('c:\\')))

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
# É gerado um iterator (convertemos para uma lista)

scanner = os.scandir()

# print(list(os.scandir('c:\\')))

arquivos = list(scanner)

print(arquivos[0].inode())  # Numeracao do objeto na árvore de diretórios
print(arquivos[0].is_dir())  # É um diretório? True
print(arquivos[0].is_file())  # É um arquivo? False
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo ($Recycle.Bin)
print(arquivos[0].path)  # Caminho até o arquivo (c:\\$Recycle.Bin)
# os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0,
# st_uid=0, st_gid=0, st_size=0, st_atime=1650389203, st_mtime=1647904493,
# st_ctime=1622895048)
print(arquivos[0].stat())  # Estatísticas sobre o arquivo
# st_size=0 => tamanho do arquivo em bites.

# print(dir(arquivos[0]))

# Obs: Quando utilizamos a função scandir(), nós precisamos fechá-la, assim
# como quando abrimos um arquivo.

scanner.close()
"""
