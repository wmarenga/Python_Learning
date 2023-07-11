""" 
Len, Abs, Sum e Round:

len() => Retorna o tamanho (ou seja, o numero de itens) de um iteravel.

abs() => Retorna o valor absoluto de um numero inteiro ou real. De forma basica, seria o seu 
        valor real sem o sinal.

sum() => Recebe como parametros um iteravel, podendo receber um valor inicial, e retorna a soma total
        dos elementos, incluindo o valor inicial.
Obs: O valor inicial default e zero.

round() => Retorna um numero arredondado para n digiyos de precisao apos a casa decimal. Se a precisao 
        nao for informada, retorna o inteiro mais proximo da entrada.

# Len:

# Exemplo (Relembrando):
print(len('Geek University'))
print(len([1, 2, 3 ,4 , 5]))
print(len((1, 2, 3 ,4 , 5)))
print(len({1, 2, 3 ,4 , 5}))
print(len({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a funcao len() o Python faz o seguinte:
print('Geek University'.__len__())

# Dunder len (__len__())

# Abs:
# Nao podemos utilizar o abs() com strings, somente inteiros ou reais.
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum:

# Exemplos sum:
print(sum([1, 2, 3, 4 ,5])) # Lista
print(sum([1, 2, 3, 4 ,5], 5)) # Lista e inteiros (positivo)
print(sum([1, 2, 3, 4 ,5], -5)) # Lista e inteiros (negativo)
print(sum([3.14, 5.678])) # Lista float
print(sum((1, 2, 3, 4 ,5))) # Tupla
print(sum({1, 2, 3, 4 ,5})) # Set
print(sum({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}.values())) # Temos que informar que precisamos somar os valores .values()
print(sum('Geek University')) # O sum nao funciona com strings

# Round

# Exemplo Round:
print(round(10.2)) # Arredonda para baixo (10)
print(round(10.5)) # Arredonda para baixo (10), ate 10.5 o arredondamento e para baixo
print(round(10.6)) # Arregomda para 11
print(round(1.2121212121, 2)) # Arredonda para 2 casas decimais (para baixo) => 1.21
print(round(1.2199999999, 2)) # Arredonda para 2 casas decimais (para cima) => 1.22
"""
