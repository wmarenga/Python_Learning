"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer


with open('131) Escrevendo em arquivos CSV/filmes.csv', 'w', encoding='cp1252') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    # O cabeçalho só é escrito uma vez
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

# Se quisermos acrescentar no arquivo existente, temos que utilizar o 'a'.

from csv import writer


with open('131) Escrevendo em arquivos CSV/filmes2.csv', 'a', encoding='cp1252') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    # O cabeçalho só é escrito uma vez (temos que ignorar o cabeçalho para adicionar)
    # escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.
# fieldnames=cabecalho, recebe uma lista, mas poderia receber qualquer outro
# valor, pois é do tipo *kwargs.

from csv import DictWriter


with open('131) Escrevendo em arquivos CSV/filmes3.csv', 'a', encoding='cp1252') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

# Se quisermos acrescentar no arquivo existente, temos que utilizar o 'a'.

from csv import DictWriter


with open('131) Escrevendo em arquivos CSV/filmes3.csv', 'a', encoding='cp1252') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    # O cabeçalho só é escrito uma vez (temos que ignorar o cabeçalho para adicionar)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow(
                {"Título": filme, "Gênero": genero, "Duração": duracao})
"""
