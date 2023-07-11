valor = True

# O pass ou ... deixa o código em holding (esperando um código
# futuro).
# Não gera erro, apenas não retorna nada.
if valor:
    pass
else:
    print('Tchau')

if valor:
    ...
else:
    print('Tchau')
