'''
Similaridades entre listas e strings:

- Ambos são indexáveis com indices a partir de [0];
- Strings, assim como listas, podem ser fatiadas;
- A funcão len(x) retorna o número de elementos de uma lista e o número de caractéres de uma string;
- A operação de soma funciona de maneira parecida;
- Ambas podem ser multiplicadas por um valor inteiro;

Mas atenção, não são do mesmo tipo!

lista_a = ['P','Y','T','H','O','N']

retorna o primeiro elemento da lista
print(lista_a[0])
print(lista_a[:2])

string_a = 'python'

As strings tambem sao indexaveis, podemos chamar da mesma maneira que as listas
print(string_a[0])

Usando Slicing
print(string_a[:2])

Funcao len para lista e strings

lista_a = ['PA','YA','TA','H','O','N']
Esta exibe o numero de elementos
print(len(lista_a))
saida: 6

string_a = 'pAyAtAhon'
Esta exibe o numero de caracteres
print(len(string_a))
saida: 9

Podemos utilizar operacoes matematicas com Strings
string_b = string_a * 3
print(string_b)

Podemos fazer o mesmo com as listas
lista_b = lista_a * 3
print(lista_b)
'''
