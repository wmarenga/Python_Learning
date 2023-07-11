# Abrindo arquivos

f = open("demo.txt", "a")

print(f.read())

# Escrevendo
f.write("Now you can see new content")

# Fechando
f.close()

# Criando um novo arquivo

f = open("file2.txt", "x")