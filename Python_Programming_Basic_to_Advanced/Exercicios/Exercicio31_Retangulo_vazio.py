"""
Exercicio 31:
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os 
caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

1 digite a largura: 10
2 digite a altura: 3
3 ##########
4 #        #
5 ##########

1 digite a largura: 2
2 digite a altura: 2
3 ##
4 ##
"""
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
minimo_alt = 1
while minimo_alt <= altura:
    if minimo_alt == 1 or minimo_alt == altura:
        print('#'*largura, end='\n')
        minimo_alt += 1
    else:
        print('#', (largura-4)*' ', '#', end='\n')
        minimo_alt += 1
