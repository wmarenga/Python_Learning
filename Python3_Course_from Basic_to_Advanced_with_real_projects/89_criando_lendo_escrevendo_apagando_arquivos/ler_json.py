import json

with open('89_criando_lendo_escrevendo_apagando_arquivos/abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Voltar a ser dicionário

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
