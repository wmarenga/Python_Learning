"""
Loop for

Loop -> estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for (int i = 0; i < 10; i++) {
    ! execução do loop
}

Python

for item in interavel:
    ! execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
nome = 'Geek University'
- Listas
lista = [1, 3, 5, 7, 9]
- Range
# Temos que transformar em uma lista (Iterando sobre uma string)
numeros = range(1, 10)

# Exemplo de "for" 1 (Iterando sobre uma String)

nome = 'Geek University'
for letra in nome:
    print(letra)

# Exemplo de "for" 2 (Iterando sobre uma lista)

lista = [1, 3, 5, 7, 9]
for numero in lista:
    print(numero)

Exemplo de "for" 3 (Iterando sobre um range)

range(valor_inicial, valor_final) - O valor final não é incluído.
numeros = range(1, 10)

for numero in range(1, 10):
    print(numero)

Obs: O valor_final nao sera incluido.
"""

"""
Enumerate:

((0,'G'), (1,'e'), (2,'e'), (3,'k'), (4,' '), (5,'U'), (6,'n'), .... )

for indice, letra in enumerate(nome):
    print(nome[indice])

# Indicamos que estamos descartando o indice com o underline "_"
Obs: Quando nao precisamos de um valor, podemos descarta-lo utilizando underline (_)

for _, letra in enumerate(nome):
    print(letra)

for indice, letra in enumerate(nome):
    print(letra)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

Mostra os índices e letras do nome.

for valor in enumerate(nome):
    print(valor)
(0, 'G')
(1, 'e')
(2, 'e')
(3, 'k')
(4, ' ')
(5, 'U')
(6, 'n')
(7, 'i')
(8, 'v')
(9, 'e')
(10, 'r')
(11, 's')
(12, 'i')
(13, 't')
(14, 'y')

Mostra os índices.
for valor in enumerate(nome):
    print(valor[0])
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14

Mostra os valores.
for valor in enumerate(nome):
    print(valor[1])
G
e
e
k
 
U
n
i
v
e
r
s
i
t
y

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

Somar números:

qtd = int(input('Quantas vezes eese loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

# mostra na mesma linha
nome = 'Geek University'
for letra in nome:
    print(letra, end='')  

Obs: No console do Python podemos digitar help(print) para ver os parametros. O Python por
defauld sempre pula uma linha (\n).

Java:
System.out.println(letra) - Ira para a proxima linha
System.out.println(letra) - NAO ira para a proxima linha

C:
printf(letra + '\n') - Ira pula uma linha
printf("%c\n", letra) - Ira pula uma linha (%c - caracter)

# Concatena os nomes
nome = 'Geek'
print(nome + ' University')

# Multiplica o nome 'GeekGeekGeek'
print(nome * 3)

## Tabela de emoji (unicode)
https://unicode.org/emoji/charts/full-emoji-list.html

U+1F600	-> U0001F600 (substituir o + por 000)	

"""
# O Emoji somente e exibido no terminal e nao na saida.
# Emoji Original: U+1F60D
# Emoji modificado: U0001F60D (substituir o sinal de '+' por '000')
for _ in range(3):
    for num in range(1, 11):
        print("\U0001F60A" * num)
