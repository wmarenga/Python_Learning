"""
Manipulação de Textos

Criando uma lista:
frase = list('Curso em Vídeo Python')
print(type(frase))
print(frase)
print(frase[9:13])  # Inicia no 9 e termina no 12.
print(frase[:5])  # Inicia no 0 e termina no 4.
print(frase[9:21:2])  # Inicia no 9 e termona no 20, de 2 em 2 caractéres.
print(frase[15:])  # Inicia no 15 e segue até o final.
# Inicia no 9, vai até o final, pulando de 3 em 3 caractéres.
print(frase[9::3])
print(len(frase))  # mostrar o total de caractéres.
print(frase.count('o'))  # mostra quantas letras 'o' temos na frase.

# Criando e transformando uma String:
frase = 'Curso em Vídeo Python'
print(type(frase))
print((frase))
print(frase[9:13])
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # O primeiro 'o' está no index 11.
# Quando o Python não encontrar o resultado, retorna -1.
print(frase.find('Android'))
# Retorna uma resposta ao questionamento (True ou False).
print('Curso' in frase)
# Substitui uma sequencia de caractéres.
print(frase.replace('Python', 'Android'))
print(frase.upper())  # Tudo maíusculo.
print(frase.lower())  # Tudo minúsculo.
# Primeira letra maiúscula e todas as outras minúsculas.
print(frase.capitalize())
# Todas as primeiras letras depois dos espaços ficarão maiúsculas.
print(frase.title())
novotexto = "   Aprenda Python  "
# Remove espaços desnecessários no início e fim da frase.
print(novotexto.strip())
print(novotexto)
print(novotexto.rstrip()) # Remove somente os espaços da direita.
print(novotexto.lstrip()) # Remove somente os espaços da esquerda.

# Divisão e junção de strings:

frase = 'Curso em Vídeo Python'
print(frase.split())  # Divide entre os espaços.
print('😿'.join(frase))

# Imprimindo textos longos, sempre utilizar 3 aspas duplas.

print("sdgjlkdagkjakgklkljglksajalkdjflksjdgkljkwldjsljdjsdjlgsd
lgsjlgdjsljasljflkasjdlkf
kadsjkfjdlksjalksjdlkfjlksdjflksjfl
jklsdlsafjljdsalkjsladfjlkjslkd
jkdshgkhkdvnkdnvkjndkfnvlkdnfllkfddfk")

frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
frase = frase.replace('Python', 'Android') # Alterar e reatribuir a alteração.
print(frase)

frase = 'Curso em Vídeo Python'
dividido = frase.split()
# Divide e frase entre os espaços e pega a quarta letra do índex 2.
print(dividido[2][3])

"""
