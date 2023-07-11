"""
For in em Python:
Iterando strings com for
Função range(start=0, stop, step=1)

# Exemplo com while:
texto = 'Python'

c = 0
while c < len(texto):
    print(texto[c])
    c += 1

# Exemplo com for:

texto = 'Python'

for letra in texto:
    print(letra)

# Exemplo com range range(start=0, stop, step=1):
# Crescente

for n in range(0, 10, 2):
    print(n)

# Decrescente
for n in range(20, 10, -2):
    print(n)

# Usando condições
for n in range(100):
    if n % 8 == 0:
        print(n)

"""
# Utilizando o for para mudar letra para maiúscula

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# continue => pula para o próximo laço
# break => termina o laço

# Não incluiríamos a letra 't' pois o laço irá pula o if.
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

# Irá parar após incluir a letra 'H' maiúscula.
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
