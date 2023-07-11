import urllib3
import pandas as pd

# Primeira etapa
http = urllib3.PoolManager()

response = http.request(
    'GET', 'https://ec.europa.eu/agrifood/api/beef/prices?memberStateCodes=PT&years=2019,2020&months=1,3,9&weeks=5,6,7,8,40,41,42&beginDate=01/09/2019&endDate=02/02/2020&carcassCategories=heifers,cows')

# Altera caracteres
cut = '[{' + str(response.data[2:-2])[2:-1][5:-3] + '}]'
cut = cut.replace(' ', '')
cut = cut.replace(r'\n', '')
cut = cut.replace(r"\x", "/x")

# # Gera o Arquivo json
with (open(r"C:\Users\wmare\Desktop\gis.json", "w")) as arquivo:
    arquivo.write(cut)

# Segunda etapa (omitir a primeira etapa antes)

# Conversao json para csv
df = pd.read_json(r'C:\Users\wmare\Desktop\gis.json')
df.to_csv(r'C:\Users\wmare\Desktop\gis.csv', index=None)
