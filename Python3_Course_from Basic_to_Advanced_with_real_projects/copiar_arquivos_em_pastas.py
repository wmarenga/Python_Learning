import os
import shutil

# Definindo a pasta principal
caminho_origem = "E://18a_Musica_ CD_Doaçao"
caminho_destino = "G://1aaa"

try:
    os.mkdir(caminho_destino)
except FileExistsError as e:
    print(f'Pasta {caminho_destino} já existe!')

for root, dirs, files in os.walk(caminho_origem):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_destino, file)
        print(new_file_path)

        try:
            shutil.copy(old_file_path, new_file_path)
        except:
            continue
