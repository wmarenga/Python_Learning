"""
Escrevendo um Iterador Customizado:

for n in range(11):  # Mesma coisa que (0, 11)
    print(n)

class Contador:
    # __init__ é uma Função especial chamada construtor.
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):  # Criado para retornar a função como interável
        return self

    def __next__(self):  # Para que possamos usar um interável, devemos
                         aplicar o next()
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration

con = Contador(1, 6)
print(con.menor)
print(con.maior)

# Transformando em um interável:
it = iter(con)
# print(next(it))  # TypeError: 'Contador' object is not iterable

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
print(next(it))  # 5
print(next(it))  # StopIteration

for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)
"""
