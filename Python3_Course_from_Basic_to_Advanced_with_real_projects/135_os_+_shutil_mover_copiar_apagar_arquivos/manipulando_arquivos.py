# utilizamos o r minúsculo para evitar problemas com barras invertidas no caminho dos arquivos
# caminho_windows = r'C:\Program Files'

import os
import shutil

caminho_original = r'I:\Musicas'
caminho_novo = r'I:\Musicas2'

conta = 0
try:
    os.mkdir(caminho_novo)  # Criação da nova pasta
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        # conta += 1
        # Caminho completo dos arquivos na pasta original
        old_file_path = os.path.join(root, file)
        # Junção do novo caminho da pasta com o nome dos arquivos
        new_file_path = os.path.join(caminho_novo, file)
        # print(old_file_path)
        # print(new_file_path)

        # if '.m4a' in file:
        # conta += 1
        # Copia arquivos específicos
        # shutil.copy(old_file_path, new_file_path)
        # print(f'Arquivo {file} copiados com sucesso!')

        # Removendo arquivos
        if '.m4a' in file:
            conta += 1
            os.remove(new_file_path)

        # shutil.move(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso!')

print(f'Foram movidos {conta} arquivos com sucesso!')
