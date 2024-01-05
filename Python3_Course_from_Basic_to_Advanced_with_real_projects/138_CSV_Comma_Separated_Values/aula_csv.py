"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('138_CSV_Comma_Separated_Values/clientes.csv', 'r') as arquivo:
    # convertendo para uma list comprehension para ler fora do with, pois o arquivo foi fechado.
    dados = [x for x in csv.DictReader(arquivo)]

print(dados)

with open('138_CSV_Comma_Separated_Values/clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL  # todos os arquivos ficam com aspas duplas.
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
