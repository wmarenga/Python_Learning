"""
Escrevendo em Arquivos:

Obs: Ao abrir um arquivo para leitura ('r'), não podemos realizar a escrita
nele (apenas ler).
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo,
somente escrever nele.

Obs: Ao abrir um arquivo para escrita, o arquivo é criado no sistema
operacional.

# Exemplo de escrita (modo 'w' - write = escrita):
# Forma Pythônica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

Para escrevermos dados em um arquivo, após abrir o arquivo, utilizamos a
função write(). Esta função recebe uma string como parâmetro, caso
contrário teremos um TypeError.

with open('outro.txt', 'w') as arquivo:
    arquivo.write('Texto')
    # arquivo.write(42) # TypeError: write() argument must be str, not int
    arquivo.write('42')

# Alterando todo o conteúdo antigo, pelo conteúdo novo.
# Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir
será criado, caso ele já exista, o anterior será apagado e um novo será criado.
Dessa forma, TODO, o conteúdo no arquivo anterior será perdido.
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Mais esta é a última linha.')

# Forma tradicional (não Pythônica) de escrita de arquivos:
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()

# Gerndo um arquivo com a palavra 'Geek' 1000 vezes, pulando uma linha.
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n' * 1000)

"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
