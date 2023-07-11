from vendas.formata import preco


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r


def formata_preco(valor):
    return f'R$ {round(valor, 2)}'.replace('.', ',')
