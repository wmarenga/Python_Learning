"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()
def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas

Dunder > Double Underscore

# dunder repr -> Representação do objeto, sobrescrevendo a representação padrão
que é mostrar o endereço de memória.

def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'

Todos os métodos são provenientes da classe object.
dir(object)
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):  # O __str__ tem preferência entre os métodos.
        return self.titulo

    def __repr__(self):  # Sobrescreve a representação padrão, que é mostrar
        # um endereço de memória.
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado da memória')

    def __add__(self, outro):  # Adição
        return f'{self} - {outro}'

    def __mul__(self, outro):  # Multiplicação
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 5)
