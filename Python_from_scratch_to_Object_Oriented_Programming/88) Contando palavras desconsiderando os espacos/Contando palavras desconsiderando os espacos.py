# Contando palavras desconsiderando os espacos

frase1 = str('Porto Alegre e uma cidade Brasileira.')

print(len(frase1))
print(len(frase1) - frase1.count(' '))
