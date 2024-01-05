from zipfile import ZipFile
import os

# Para caminhos com barra invertida (\), utilize r
caminho = r'teste/'

# ESCREVE
with ZipFile('142_zip_compactando_descompactando_arquivos/arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# LISTA
with ZipFile('142_zip_compactando_descompactando_arquivos/arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAI
with ZipFile('142_zip_compactando_descompactando_arquivos/arquivo.zip', 'r') as zip:
    zip.extractall('142_zip_compactando_descompactando_arquivos/descompactado')
