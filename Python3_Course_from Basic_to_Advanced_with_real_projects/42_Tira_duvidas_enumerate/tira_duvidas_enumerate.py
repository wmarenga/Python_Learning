"""
Tira dúvidas de enumerate:

"""
# lista interna 0       1       2
# Índice 0 = ['Edu', 'João', 'Luiz']
# lista interna  0        1        2
# Índice 1 = ['Maria', 'Aline', 'Joana']
# lista interna  0       1     2
# Índice 2 = ['Helena', 'Ed', 'Lu']

lista = [['Edu', 'João', 'Luiz'], [
    'Maria', 'Aline', 'Joana'], ['Helena', 'Ed', 'Lu']]

print(lista[0][2])  # Luiz
print(lista[1][0])  # Maria
print(lista[2][1])  # Ed

enumerada = enumerate(lista)
print(enumerate)  # <class 'enumerate'>

# Fazendo um type casting para converter para uma lista com
# tuplas dentro.
print(list(enumerada))

# Definindo o valor para começar o v1 (que não é o índice)
# no enumerate.
for v1, v2 in enumerate(lista, 53):
    print(v1, v2)

# Desempacotamento

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
