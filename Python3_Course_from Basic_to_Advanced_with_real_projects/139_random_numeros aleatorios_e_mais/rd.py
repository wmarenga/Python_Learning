import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2)  # retorna dois nomes, porém sem repeti-los.
# sorteio = random.choices(lista, k=2) # Retorna uma lista com dois nomes, podendo ser repetidos.
# sorteio = random.choice(lista)

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters  # retorna letras maiúsculas e minúsculas
# letras = string.ascii_lowercase # retorna letras somente minúsculas
# letras = string.ascii_uppercase # retorma letras somente maiúsculas
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))

print(senha)
