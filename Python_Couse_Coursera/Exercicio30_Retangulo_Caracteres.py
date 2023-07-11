""""
Exercício 30: 

Escreva um programa que recebe como entradas (utilize a função input)
dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente.
O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com
caracteres '#' na saída.
Por exemplo:

1 digite a largura: 10
2 digite a altura: 3
3 ##########
4 ##########
5 ##########

1 digite a largura: 2
2 digite a altura: 2
3 ##
4 ##

Dica: lembre-se que a função print pode receber um parametro 'end', que altera o último 
caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas).
"""
largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
minimo_alt = 1
while minimo_alt <= altura:
    print('#'*largura, end='\n')
    minimo_alt += 1
