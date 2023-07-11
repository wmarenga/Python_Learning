# Desafio 105:
# Faça um programa que tenha uma função notas() que pode
# receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# A) Quantidade de notas;
# B) A maior nota;
# C) A menor nota;
# D) A média da turma;
# E) A situação (opcional).


def notas(*n, sit=False):
    """
    -> Função para analisar as notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas_alunos = dict()
    notas_alunos['total'] = len(n)
    notas_alunos['maior'] = max(n)
    notas_alunos['menor'] = min(n)
    notas_alunos['média'] = sum(n)/len(n)
    # Somente aparece esta opção se sit=True.
    if sit:
        if notas_alunos['média'] >= 7:
            notas_alunos['situação'] = 'BOA'
        elif notas_alunos['média'] >= 5:
            notas_alunos['situação'] = 'RAZOÁVEL'
        else:
            notas_alunos['situação'] = 'RUIM'
    return notas_alunos


# PROGRAMA PRINCIPAL:
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
