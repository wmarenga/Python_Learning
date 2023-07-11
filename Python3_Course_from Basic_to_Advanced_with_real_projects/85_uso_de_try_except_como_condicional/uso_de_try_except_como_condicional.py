
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Erro: Isso não é número.')
    else:
        print(numero * 2)
