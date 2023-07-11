"""
Loop While

Forma Geral:

While expressão_booleana:
    ! execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Exemplo:
num = 5
num < 5
False (booleana)

# Exemplo 1:
numero = 1
while numero < 10:
    print(numero)
    numero += 1
# Em um loop while, é importante que definamos uma critério de parada, pois evitar um loop infinito.

# C ou Java
while(expressão) {
    ! execução
}

# do while (Java e C) - não existe no Python
do {
    ! execução
}while(expressão):

"""
# Exemplo 2:
resposta = ''

# Enquanto a resposta não for 's' ele continua perguntando.
while resposta != 's':
    resposta = input('Já acabou Jéssica? ').lower()[0]
# Convertemos os caracteres digitados para minusculo e pegamos a primeira letra somente