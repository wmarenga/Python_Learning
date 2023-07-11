'''
Estrutura de dados:

Essa aula é inspirada em:
https://docs.python.org/3/tutorial/datastructures.html
LEE, Kent D. Python Programming Fundamentals. Second Edition. Springer - Verlag London 2014.

Métodos para listas:

        Método                      Descrição
    append(variável)        Adiciona a variável no final
    extend(outra_lista)     Adiciona mais de um elemento ao final da lista
    remove(variável)        Remove o primeiro elemento com valor variável
    count(variável)         Conta o número de elementos com o valor variável
    sort()                  Reordena elementos em ordem numérica ou alfabética
    reverse()               Inverte a ordem dos elementos
    copy()                  Retorna uma cópia da lista
    index(variável)         Retorna o índice da primeira variável da lista
    pop(índice)             Remove o elemento da lista e retorna seu valor
    
lista_inteiros = [1, 2, 3, 4, 5]
print(len(lista_inteiros))

O metodo e como se fosse uma funcao, porem aplicada diretamente sobre o objeto. 

" adiciona o elemento 6 ao final da lista "
lista_inteiros.append(6)
print(lista_inteiros)

" O metodo extend() adiciona mais de um elemento ao final da lista (adiciona os elementos separadamente a lista)
lista2 = [7, 8, 9]
lista_inteiros.extend(lista2)
print(lista_inteiros)

" Usando o append nos adicionamos a lista inteira dentro da lista existente
lista_inteiros.append(lista2)

Este metodo retorna um numero inteiro e NAO MODIFICA A LISTA
lista_letras = ['a','s','d','a','s','a']
lista_letras.count('a')

Ordenando uma lista (ordem numerica e/ou alfabetica) - este metodo modifica a lista
lista_letras = ['a','s','d','a','s','a']
lista_letras.sort()
print(lista_letras)

'''
