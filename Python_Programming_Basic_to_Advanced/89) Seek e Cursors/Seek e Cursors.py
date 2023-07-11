"""
Seek e Cursors:

seek() => É utilizada para movimentar o cursor pelo arquivo. Ela recebe um
parâmetro que indica onde queremos posicionar o cursor.

arquivo = open(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura
    de arquivos\\texto.txt')
# print(arquivo.read())

# print(arquivo.read())  # Não aparece nada (o cursor chegou ao final e parou)

# Se quisermos ler novamente o arquivo:
# Movimentando o cursor pelo arquivo com a função seek()
# arquivo.seek(0)  # Posição inicial

# print(arquivo.read())

# Temos que ler novamente o arquivo, antes
print(arquivo.read())
arquivo.seek(22)  # Lendo a partir da posição 22
print(arquivo.read())

# readline() => Função que lê o arquivo linha a linha.

# print(arquivo.readline())  # Mostra a primeira linha
# print(arquivo.readline())  # Mostra a segunda linha
# print(arquivo.readline())  # Mostra a terceira linha

ret = arquivo.readline()

print(type(ret))

print(ret) # Mostra a primeira linha

# Separando pelos espaços e gerando uma lista.
print(ret.split(' '))

# readlines() => Ler as linhas

# Gera uma lista com cada linha sendo um elemento (ítem) da lista.
linhas = arquivo.readlines()

print(len(linhas))

Obs: Quando abrimos um arquivo com a função open(), é criada uma conexão
entre o arquivo no disco do computador e o nosso programa. Essa conexão é
chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar
essa conexão. Para isso utilizamos a função close().

Passo para se trabalhar com um arquivo:

1) Abrir o arquivo;
arquivo = open('texto.txt')

2) Trabalhar o arquivo (ler, editar, etc);
print(arquivo.read())

print(arquivo.closed) # Retorna (True/ False) se o arquivo está ou não fechado.

3) Fechar o arquivo.
arquivo.close() # encerra a conexão com o arquivo.

Obs: Temos que informar ao sistema operacional, que nós não estaremos
utilizando o arquivo e sendo assim liberando para que outro usuário possa
editá-lo sem problema.

arquivo = open(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura de
    arquivos\\texto.txt')
print(arquivo.read())
print(arquivo.closed)  # Retorna False, pois o arquivo está aberto.

arquivo.close()  # encerra a conexão com o arquivo.
print(arquivo.closed)  # Retorna True, pois o arquivo está fechado.

# Obs: Se tentarmos manipular o arquivo após o seu fechamento, teremos um
ValueError.

"""
arquivo = open(
    'C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura de arquivos\\texto.txt')

# Podemos também limitar o conteúdo que será exibido

print(arquivo.read(50))  # Os primeiros 50 caractéres.
