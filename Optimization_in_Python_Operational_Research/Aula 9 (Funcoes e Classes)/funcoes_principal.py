import funcoes_func as teste

result1 = teste.minha_soma(5,4)
result2 = teste.minha_mult(2,3)

" Criamos uma classe vazia e vamos inserindo valores dentro dela "
""" A grande vantagem de criarmos classes e poder informar apenas o nome rafael como um argumento de uma funcao. Ela carregaria todos
os objetos dentro dela, facilitando a programacao. """
rafael = teste.estrutura()
rafael.idade = 10
rafael.cidade = 2
rafael.altura = 1

print(result1)
print(result2)

print(rafael.idade)