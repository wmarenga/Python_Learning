# Desafio 73:
# Crie uma Tupla preenchida com os 20 primeiros colocados da tabela
# do campeonato Brasileiro de futebol, na ordem de colocação. Depois
# mostre:
# A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o time da Chapecoense.

tabela = ('Internacional', 'Atlético Mineiro', 'São Paulo', 'Vasco da Gama',
          'Flamengo', 'Palmeiras', 'Santos', 'Fluminense', 'Ceará', 'Chapecoense', 'Fortaleza',
          'Atlético Goiano', 'Grémio', 'Atlético Paranaense', 'Sport Recife', 'Corinthians',
          'Bahia', 'Botafogo', 'Goiás', 'Coritiba')
print('-='*30)
print(f'Lista dos times do Brasileirão: {tabela}')
print('-='*30)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-='*30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabética: {sorted(tabela)}')
print('-='*30)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')
print('-='*30)
