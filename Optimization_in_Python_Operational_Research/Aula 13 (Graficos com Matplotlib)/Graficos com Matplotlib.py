""" 
Instalacao:
pip install matplotlib

site oficial da biblioteca:
www.matplotlib.org

"""

import matplotlib.pyplot as plt
nomes = ['Rafael', 'Maria', 'Ana']
idades = [10,20,15]

" Grafico de linhas "
plt.plot(nomes, idades)
plt.show()

" Grafico de barras "
plt.bar(nomes, idades)
plt.show()

" Normalmente criamos a tela de plotagem e depois criamos o grafico "
plt.figure(figsize=(10,5))
plt.bar(nomes, idades)
" Podemos inserir legenda ao grafico "
plt.xlabel('nome')
plt.ylabel('idade')
plt.show()

