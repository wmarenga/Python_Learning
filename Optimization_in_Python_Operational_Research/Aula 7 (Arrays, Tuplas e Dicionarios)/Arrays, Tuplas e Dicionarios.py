" Arrays, Tuplas e Dicionarios "

" ## ARRAYS ## "
" Toda lista e criada entre colchetes [] e podendo ser alterada e/ou inserir dados a qualquer momento "
nomes = ['Rafael', 'Maria', 'Ana']
idades = [10,20,15]

print(sum(idades)/len(idades))

" Acessando uma posicao do vetor "
print(nomes[2])

" ## TUPLAS ## "
" Toda Tupla e criada entre aspas () e NAO podendo ser alterada ou inserir informacoes "
sexo = ('M', 'F', 'O')

" ## DICIONARIOS ## "
" Todo dicionario e criado entre parenteses {}, possuindo uma chave antes dos : e depois dos : podemos inserir valor (int, listas, tuplas, str) "
cadastro = {'nomes': nomes, 'idades':idades, 'cidade': ['A', 'B', 'C']}

" Acessando o dicionarios "
print(nomes[0])
print(nomes[1])
print(idades[0])

" Acessamos as Tuplas da mesma maneira que as listas "
print(sexo[0])

" Acessamos o cadastro sempre pela chave "
print(cadastro['nomes'])

" Acessando o primeiro registro da chave "
print(cadastro['nomes'][0])

" Podemos realizar operacoes matematicas com um cadastro "
print(sum(cadastro['idades']))