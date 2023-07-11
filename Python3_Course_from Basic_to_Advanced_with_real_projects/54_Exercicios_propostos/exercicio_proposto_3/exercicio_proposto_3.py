"""
Crie uma função que receba 2 números. O primeiro é um valor e o
segundo um percentual (ex. 10%). Retorne (return) o valor do
primeiro número somado do aumento do percentual do mesmo.
"""


def percentual(n1, perc):
    return n1 + (n1 * (perc / 100))


print(percentual(50, 10))
