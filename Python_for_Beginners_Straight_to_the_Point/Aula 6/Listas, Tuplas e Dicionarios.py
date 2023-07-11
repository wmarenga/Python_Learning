"""
Dicas Jupyter Lab:

* Sempre que clicar na celula, estaremos alterando os valores dentro da celular e quando 
clicamos no lado esquerdo ao numero entre colchetes, estaremosalterando a linha como 
um todo (deletando, inserindo, etc)

** No Jupyter podemos executar os comandos sem ter a necessidade de usar o "Print", 
somente digitando o nome da variavel.

1) Listas (Pode ser alterada a qualquer momento):

Toda lista e criada entre colchetes [].

nomes = ['Rafael', 'Maria', 'Ana']
idades = [10,20,15]

print(nomes[0])

# Saida <Rafael>
print(nomes[1])

# Saida <Maria>

print(idades[0])

# Saida <10>

2) Tuplas (Nao pode ser alterada):

Toda Tupla e criada entre parenteses ().

sexo = ('M','F','O')

print(sexo[0])

# Saida <M>

3) Dicionario:

Todo dicionario e criado entre chaves. Dentro das chaves nos temos os 'indices' 
(entre aspas): variaveis.

cadastro = {'nomes': nomes,'idades':idades,'cidade':['A','B','C']}

print(cadastro['nomes'])

# Saida <['Rafael', 'Maria', 'Ana']>

print(cadastro['nomes'][0])

# Saida <Rafael>

print(cadastro['idades'])

# Saida <[10, 20, 15]>

print(sum(cadastro['idades']))

# Saida <45>

** Podemos ter listase tuplas em um mesmo dicionarios
"""
nomes = ['Rafael', 'Maria', 'Ana']
idades = [10,20,15]
cadastro = {'nomes': nomes,'idades':idades,'cidade':['A','B','C']}
print(sum(cadastro['idades']))