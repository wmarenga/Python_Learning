"""
O Bloco with:

Passo para se trabalhar com arquivos

1) Abrimos o arquivo;
2) Manipulamos o arquivo;
3) Fechamos o arquivo.

O bloco with é utilizado para criar um contexto de trabalho, onde os
recursos utilizados são fechados após o bloco with.

# O Bloco with (É a forma Pythônica de se trabalhar com arquivos)

# com o endereço de arquivo, chame ele de "arquivo" e trabalha o arquivo dentro da identação.
# A vantagem de usar o with é que ele abre e fecha o arquivo.

with open('C:\\Users\\wmare\\OneDrive\\Área de Trabalho\\Curso_Atual\\88) Leitura de arquivos\\texto.txt') as arquivo:
    print(arquivo.readlines())
    # False, pois o arquivo somente é fechado após sair do with.
    print(arquivo.closed)

# Apresenta um ValueError, pois o arquivo já foi fechado.
# print(arquivo.read())
print(arquivo.closed)  # True, já saiu do bloco with, estando assim, fechado.

"""
