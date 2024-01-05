import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
# print(response.text) # exibe o html da página

html = BeautifulSoup(response.text, 'html.parser')
# print(html) # exibe o html, porém podemos selecionar coisasS

for pergunta in html.select('.s-post-summary.js-post-summary'):
    # print(pergunta)
    titulo = pergunta.select_one('.s-link')
    # print(titulo.text)
    data = pergunta.select_one('.relativetime')
    # print(data.text, titulo.text, sep='\t')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(f'{data.text} => {titulo.text} ({votos.text} votos).')
