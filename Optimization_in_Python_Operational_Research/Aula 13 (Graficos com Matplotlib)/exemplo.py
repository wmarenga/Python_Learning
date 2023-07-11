import matplotlib.pyplot as plt

nomes = ['rafael','joao','maria','ana','lucia']
salarios = [1000,1100,1110,1200,1300]

plt.figure(0)
plt.plot(nomes,salarios, color='blue')

plt.figure(1)
plt.bar(nomes,salarios)
plt.savefig('grafico.png')

plt.show()