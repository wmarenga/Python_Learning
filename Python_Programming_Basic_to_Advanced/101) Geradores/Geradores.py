"""
Geradores:

- Geradores (Generators) são Iterators (Iteradores):

Obs: O contrário não é verdade. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators porem ser criados com Expressões Geradoras:

Diferenças entre Funções e Generator Functions (Funções Geradoras).

---------------------------------------------------------------------------------
| Funções                             | Generator Functions                     |
---------------------------------------------------------------------------------
| >utiliza return                     | >utiliza yield                          |
---------------------------------------------------------------------------------
| >retorna uma vez                    | >podem utilizar yield múltiplas vezes   |
---------------------------------------------------------------------------------
| >quando executada, retorna um valor | >quando executada, retorna um generator |
---------------------------------------------------------------------------------

# Exemplo Generator Function (Função Geradora)
# Ao contrário do return (sai da função), quando é aplicado o yield (ainda
# ficamos na função esperando o próximo next()).


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# Obs: Uma Generator Function não é um Generator. Ela gera um generator.

# Testando o Generator

gen = conta_ate(5)

# print(type(gen))

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
print(next(gen))  # StopIteration

gen = conta_ate(10)

for num in gen:
    print(num)

gen = conta_ate(10)

print(next(gen))  # 1
print()

# Espaço para mostrar que o 1 já foi iterado, sendo assim o (for) começará no 2.
print('for => começa abaixo')

for num in gen:
    print(num)

# Poderíamos gerar todos de uma só vez

gen = list(conta_ate(10))
print(gen)
"""
