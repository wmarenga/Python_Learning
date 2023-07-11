def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', Mínima(temperaturas), "C.")
    print('A maior temperatura do mês foi: ', Máxima(temperaturas), "C.")


def Máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max


def Mínima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min


def teste_pontual(temp, valor_esperado):
    valor_calculado = Mínima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("O valor esperado era: ", valor_esperado,
              ". valor calculado: ", valor_calculado)


def testa_mínima():
    print("Iniciando os testes!")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([32, 12, 15, 22, 25, 31, 23, 18, 2, 19, 13], 2)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes!")


print(MinMax([32, 12, 15, 22, 25, 31, 23, 18, 2, 19, 13]))
