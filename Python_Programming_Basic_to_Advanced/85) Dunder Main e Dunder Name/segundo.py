import primeiro


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente')
else:
    print(f'segundo.py foi importado. {__name__}')

# Obs: __name__ => primeiro (o nome do arquivo importado)
