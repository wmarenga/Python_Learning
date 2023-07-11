# Exercício 22 - Vogais:
# Escreva a função vogal que recebe um único caractere como
# parâmetro e devolve True se ele for uma vogal e False se
# for uma consoante.
# Exemplos de execução no shell de Python. Os valores True
# e False devolvidos devem ser do tipo bool (booleanos), e
# não strings.
# Dica: Lembre-se que para passar uma vogal como parâmetro
# ela precisa ser um texto, ou seja, precisa estar entre aspas.


def vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if x in vogais:
        return True
    elif x.isalpha():
        return False
    else:
        return False
