"""
Modos de Abertura de Arquivos:

r => Abre para leitura (padrão);
w => Abre para escrita (sobrescreve caso o arquivo já exista).
x => Abre escrita somente se o arquivo não existir. Caso o arquivo
já exista, irá gerar FileExistsError;
a => Abre para escrita, adicionando no final do arquivo (append), caso exista;
+ => Abre para o modo de atualização: Leitura e Escrita.

Obs: Abrindo no modo 'a' => append, se o arquivo não existir, será criado. Caso
o arquivo exista, o novo conteúdo será adicionado ao final (SEMPRE).

Documentação:
https://docs.python.org/3/library/functions.html?highlight=open#open

Exemplo com 'x':

with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo 2.\n')

Exemplo usando try/ except:

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo com 'a':

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

# E se quisermos adicionar no topo do arquivo (início):
# Não é possível adicionar no início. Com o modo 'a', não controlamos o cursor.

with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0) # Não controlamos o cursor
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')

# Forma de adicionar no início:
with open('texto.txt', 'r+', encoding='UTF-8') as arquivo:
    texto_anterior = arquivo.read()
    arquivo.seek(0)
    arquivo.write('Novo texto inserido no início' + '\n' + texto_anterior)
"""
