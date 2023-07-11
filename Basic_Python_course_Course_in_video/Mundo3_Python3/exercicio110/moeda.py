def aumentar(preço=0, taxa=0, moeda='R$'):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a percentagem do aumento
    :param moeda: qual é o tipo de moeda utilizado
    :return: o valor reajustado, com ou sem formato.
    """
    res = preço + (preço * (taxa / 100))
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def diminuir(preço=0, taxa=0, moeda='R$'):
    res = preço - (preço * (taxa / 100))
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def dobro(preço=0, moeda='R$'):
    res = preço * 2
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def metade(preço=0, moeda='R$'):
    res = preço / 2
    return f'{moeda}{res:>.2f}'.replace('.', ',')


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taum=10, tred=5):
    print('-'*34)
    print('RESUMO DO VALOR'.center(34))
    print('-'*34)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço)}')
    print(f'A metade do preç: \t{metade(preço)}')
    print(f'{taum}% de aumento: \t{aumentar(preço, taum)}')
    print(f'{tred}% de redução: \t{diminuir(preço, tred)}')
    print('-'*34)
