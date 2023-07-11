"""
https://docs.python.org/3/library/functions.html#open
"""
import os

caminho_procura = input('Digite o caminho da pasta que deseja procurar: ')
termo_procura = input('Digite os termo que deseja procurar: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = tamanho
        texto = 'b'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kb'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Gb'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'Tb'
    else:
        tamanho /= peta
        texto = 'Pb'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                # print(arquivo) # exibe o nome e a extensão dos arquivos
                # print(caminho_completo)  # exibe o caminho do arquivo em suas pastas
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                # print(nome_arquivo)  # exibe o nome do arquivo
                # print(ext_arquivo)  # exibe a extensão do arquivo
                tamanho = os.path.getsize(caminho_completo)
                # print(tamanho)  # tamanho do arquivo em bytes
                print(
                    f"""\n Encontrei o arquivo: {arquivo}
                    Caminho: {caminho_completo}
                    Nome: {nome_arquivo}
                    Extensão: {ext_arquivo}
                    Tamanho formatado: {formata_tamanho(tamanho)}""")
            except PermissionError:
                print('Sem permissões.')
            except FileNotFoundError:
                print('Arquivo não encontrado.')
            except Exception as e:
                print(f'Erro desconhecido: {e}')

print()
print(f'Foram encontrados {conta} arquivos.\n')
