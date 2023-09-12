from pathlib import Path
from shutil import rmtree
""" 
caminho_projeto = Path()

# Caminho relativo = resumido
print(caminho_projeto)

# caminho absoluto = completo projeto
print(caminho_projeto.absolute())

# caminho absoluto do arquivo
caminho_arquivo = Path(__file__)
print(caminho_arquivo)

# caminho absoluto da pasta mãe do arquivo
# print(caminho_arquivo.parent)

# caminho absoluto de duas pastas antes do arquivo (volta duas pastas do arquivo do projeto)
# print(caminho_arquivo.parent.parent)

# Determinado um novo caminho
ideias = caminho_arquivo.parent / 'ideias'
print(ideias)
print(ideias / 'arquivo.txt')

# Mostrar a Home do usuário (nenhuma pasta ou arquivo será criado, apenas exibido o caminha)
print(Path.home())
print(Path.home() / 'Desktop')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

# Criação de arquivo
arquivo.touch()

# Escrevendo no arquivo
arquivo.write_text('Olá Mundo')
# segundo write irá sobrescrever o anterior
arquivo.write_text('Olá de novo')

# Lendo o arquivo no terminal
print(arquivo.read_text())

# Apagando o arquivo
arquivo.unlink()

# Abre o arquivo e escreve dentro dele (toda vez que executar, serão escritas novas linhas abaixo)
caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch()

with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(caminho_arquivo.read_text())
"""

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá de novo')
caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
# Cria o diretório e se o mesmo já existir, não fará nada
caminho_pasta.mkdir(exist_ok=True)

# Criando subpastas
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

# Criando um arquivo dentro da subpasta
outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

# Criando outro arquivo dentro da pasta 'Python é legal'
mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey voçê')

# Apagando pastas contendo subpastas e arquivos recursivamente
# Esta é a melhor maneira de apagar, pois não consegue-se apagar pasta contendo arquivos ou subpastas
rmtree(caminho_pasta)
