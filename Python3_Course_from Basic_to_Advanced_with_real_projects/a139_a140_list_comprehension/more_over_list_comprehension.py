numbers = [1, 2, 3, 4, 5]
new_numbers = [number for number in numbers]
print(numbers)
print(new_numbers)

#! Criando uma nova lista dividindo por 2:
divisao = [number / 2 for number in numbers]
print(numbers)
print(divisao)

#! Criando uma nova lista multiplicacao por 2
multiplicacao = [number * 2 for number in numbers]
print(numbers)
print(multiplicacao)  # Criamdo uma nova lista multiplicada por 2

# Podemos também atribuir a funções para que possamos utilizar em todo o código


def division(x, y):
    return x / y


def multiplication(x, y):
    return x * y


def potentiation(x, y):
    return x ** y


numbers = [1, 2, 3, 4, 5]
division_list = [division(number, 2) for number in numbers]

multiplication_list = [multiplication(number, 2) for number in numbers]

potentiation_list = [potentiation(number, 2) for number in numbers]

print(numbers)
print(division_list)
print(multiplication_list)
print(potentiation_list)

# Filtrando os valores com list comprehension (condicionais)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number for number in numbers if number > 5]
impares_odd = [number for number in numbers if number % 2 != 0]
pares_even = [number for number in numbers if number % 2 == 0]
outro_if = [number if number !=
            6 else 600 for number in pares_even]

print(numbers)
print(new_numbers)
print(impares_odd)
print(pares_even)
print(outro_if)

# Usando aninhamento com list comprehension

combinacoes = []
for x in range(3):  # 3 linhas
    for y in range(2):  # 2 colunas
        combinacoes.append((x, y))
print(combinacoes)

# com list comprehension
combinacoes = [(x, y) for x in range(3) for y in range(2)]
print(combinacoes)

# Se quisermos pular valores
combinacoes = [(x, y) for x in range(3) for y in range(3) if x != 2]
print(combinacoes)

# Se o y for diferente de 2 exibe, caso contrario multiplicar por 1000
combinacoes = [(x, y) if y != 2 else (x, y * 1000) for x in range(3)
               for y in range(3) if x != 2]
print(combinacoes)

# Manipulando strings
string = 'Wellington Marenga'
nova_string = [letra for letra in string]
print(nova_string)

# Unindo novamente e string
string = 'Wellington Marenga'
nova_string = ''.join([letra for letra in string])
print(nova_string)

# Pegando grupos de letras pulando de 2 em 2
string = 'Wellington Marenga'
number_de_letras = 3
nova_string = [string[indice:indice + number_de_letras]
               for indice in range(0, len(string), 2)]

# Se quisermos separar com ponto
nova_string = '.'.join([string[indice:indice + number_de_letras]
                        for indice in range(0, len(string), 2)])
print(nova_string)

# Trabalhando com string dentro de listas
nomes = ['Luiz', 'Maria', 'Helena', 'Joana', 'Felipe']
novos_nomes = [nome for nome in nomes]
print(novos_nomes)

# Deixar minúsculo
novos_nomes_min = [nome.lower() for nome in nomes]
print(novos_nomes_min)

# Primeiras letras maiusculas
novos_nomes_maiusc = [nome.title() for nome in nomes]
print(novos_nomes_maiusc)

# Todas as letras maiusculas
novos_nomes_todas_maiusc = [nome.upper() for nome in nomes]
print(novos_nomes_todas_maiusc)

# Deixando a última letra maiuscula
ultima_maiusc = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]
print(ultima_maiusc)

# Uma única lista dentro de uma lista
numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]
print(numbers)
print(flat)
