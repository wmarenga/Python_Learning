def aumentar(preço=0, taxa=0, moeda='R$ '):
    res = preço + (preço * (taxa / 100))
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def diminuir(preço=0, taxa=0, moeda='R$ '):
    res = preço - (preço * (taxa / 100))
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def dobro(preço=0, moeda='R$ '):
    res = preço * 2
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def metade(preço=0, moeda='R$ '):
    res = preço / 2
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
