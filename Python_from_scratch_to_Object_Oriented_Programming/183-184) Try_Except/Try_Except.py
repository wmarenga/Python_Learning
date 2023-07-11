# Try, Except

try:
    print(variavel)
except NameError:
    pass

# Exibindo Erro Interno (que erro aconteceu)

try:
    print(a)
except NameError as erro:
    print('Ocorreu um erro: ', erro)

# Except generico:

except Exception as erro:
    print('Ocorreu um erro inesperado', erro)
