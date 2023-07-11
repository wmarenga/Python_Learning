import matplotlib.pyplot as plt 
import pandas as pd

caminho_arquivo ='D:/23) Programação/Cursos/Python/4) Python para Iniciantes (Direto ao que interessa)/Aula 33 (Graficos_Boxplot)/leitura.xlsx'
df = pd.read_excel(caminho_arquivo, sheet_name='dados')
print(df.head())

"Gerando um grafico Boxplot, este grafico mostra a mediana e os quartis (25%,50%,75%)"
df.boxplot()
plt.show()

"Exibindo somente uma coluna"
"Notamos uma bolinha no grafico, que representa o valor zero na tabela"
""
df.boxplot('temperatura')
plt.show()

"Como mostrar a temperatura == 0"
print(df[df.temperatura == df.temperatura.min()])
