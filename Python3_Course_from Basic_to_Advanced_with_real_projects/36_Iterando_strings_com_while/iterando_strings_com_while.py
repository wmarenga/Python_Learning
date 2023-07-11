"""
Indices
0123456789...........................33

Se o elemento tiver índices, significa que ele é iterável.

# Iteração => Iterar

frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)
print(frase[5])

"""
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0


# while contador < tamanho_frase:
#     print(frase[contador], contador)
#     contador += 1


# Exemplo criando uma nova variável com todas as strings maiúsculas.

nova_string = ''

# while contador < tamanho_frase:
#    nova_string += frase[contador].upper()
#    contador += 1

# print(nova_string)

# Exemplo alterando as letras escolhidas pelo usuário para maiúsculo

decisao_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == decisao_usuario:
        nova_string += decisao_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
