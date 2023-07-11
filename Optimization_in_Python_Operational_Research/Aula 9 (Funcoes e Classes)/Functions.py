def faixaIdade(idade):
    if idade <= 12:
        return 'crianca'
    elif idade <= 18:
        return 'adolescente'
    elif idade <= 80:
        return 'adulto'
    else:
        return 'idoso'
    
def somaQuad(n1, n2):
    return n1**2 + n2**2