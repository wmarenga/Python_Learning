def soma(x: float, y: float) -> float:
    return x + y


# print(__name__)  # exibe o nome do módulo
if __name__ == '__main__':
    print(soma(10, 20))  # exibe a função diretamente sem importar

# Se acrescentarmos este if, o módulo somente poderá ser executado diretamente,
# não sendo possível executar após importado por outro módulo.
