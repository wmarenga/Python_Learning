""" 
Otimizacao de rota:

Qual a melhor rota entre os pontos 1 e 7 ?

Devemos definir como binaria as decisoes das rotas (1 - rota escolhida e 0 - para rota nao escolhida)
"""
" primeiro no"
x12= 220
x13 = 1500
" segundo no "
x24 = 650
x25 = 900
x36 = 500
" terceiro no "
x47 = 500
x57 = 400
x67 = 400

rota1 = x12+x24+x47
rota2 = x12+x25+x57
rota3 = x13+x36+x67

if rota1 < rota2:
    rotamenor = rota1
if rota1 < rota3:
    rotamenor = rota1
else:
    rotamenor = rota3
print(rotamenor)
