"""
Criando sua Própria versão de loop:

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

# Por baixo dos panos, o Python faz isto:

iter([1, 2, 3, 4, 5]) # Passam a ser interáveis (podemos aplicar o next())
iter(['Geek University']) # Passam a ser interáveis (podemos aplicar o next())

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]
meu_for(numeros)
"""
