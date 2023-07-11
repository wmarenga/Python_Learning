def faixaIdade(idade):
    if idade <= 12:
        return 'Criança'
    elif idade <= 18:
        return 'Adolescente'
    elif idade <= 80:
        return 'Adulto'
    else:
        return 'Idoso'
    
def somaQuad(n1,n2):
    return n1**2 + n2**2