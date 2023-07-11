""" 
Olá Wellington.

Depende qual gráfico você deseja plotar. Para uma linha, por exemplo, é sns.lineplot()

https://seaborn.pydata.org/generated/seaborn.lineplot.html



Exemplo simples

import seaborn as sns
may_flights = {1:10, 2:20, 3:15, 4:25, 5:20}
sns.lineplot(data=may_flights)


Para barras é sns.barplot()

https://seaborn.pydata.org/generated/seaborn.barplot.html



Sugiro você olhar o link abaixo e clicar nos exemplos para aprender os comandos.

https://seaborn.pydata.org/examples/index.html



Como são muitos, é difícil decorar todos, o ideal é sempre saber onde procurar e consultar.



Sobre usar IDE's além do Spyder. Vai depender se o IDE possibilita imprimir o gráfico. Se permitir, 
vai aparecer, se não, você precisará salvar o gráfico e abrir o arquivo

No matplotlib, para salvar use o comando savefig

Link referência: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

Exemplo: 

import matplotlib.pyplot as plt
 
# data for plotting
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [5, 7, 8, 1, 4, 9, 6, 3, 5, 2, 1, 8]
 
plt.plot(x, y)
 
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Matplotlib Example')
 
plt.savefig("output.jpg")


Grande abraço

"""
"Primeiro instalar a biblioteca do Seaborn (pip install seaborn)"

import matplotlib.pyplot as plt 
import pandas as pd

caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 34 (Histograma)/leitura.xlsx'
df = pd.read_excel(caminho_arquivo, sheet_name='dados')
print(df.head())

"O histograma agrupa os "
import seaborn as sns

"Histograma com uma curva de distribuicao e agrupando os valores de acordo com faixas de distribuicao"
sns.distplot(df.umidade)
sns.histplot(df.umidade)
