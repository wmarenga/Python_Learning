"""
Associação - Usa outro objeto
Agregação - Tem o outro(s) objeto(s) como parte de sí
Composição - É dono de outro(s) objeto(s)
Herança - É outro objeto
"""
from classes import *

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Tereza', 25)
print(a1.nome, a1.idade)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()
print(p1.nome)
