"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelia Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
# print("Qual o seu nome?")
# nome = input()  # Input -> Entrada de dados

# Simplificando em uma linha
nome = input('Qual o seu nome?')

# Exemplo de print "antigo" 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print "moderno" a partir das versões 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo de print mais atual 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual a sua idade?")
# idade = input()

# Simplificando em uma linha
idade = int(input('Qual a sua idade?'))

# Processamento

# Saída de dados

# Exemplo de print 'antigo' 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print("A {0} tem {1} anos".format(nome, idade))

# Exemplo de print 'Mais atual' 3.7
print(f'A {nome} tem {idade} anos')

# Pega o ano atual 2018 e subtrai a idade fornecida.
print(f'A {nome} nasceu em {2020 - idade}')
