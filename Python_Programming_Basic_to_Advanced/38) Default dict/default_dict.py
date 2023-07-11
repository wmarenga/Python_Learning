"""
Módulo Collections - Default Dict

Docs:
https://docs.python.org/3.10/library/collections.html?highlight=defaultdict#collections.defaultdict
https://docs.python.org/pt-br/3.10/library/collections.html?highlight=defaultdict#collections.defaultdict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # KeyError

# Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isto. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, esta chave será 
criada e o valor default será atribuído.

Obs: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro']) # Se fosse um dicionário comum, apresentaria "KeyError"
print(dicionario)

! defaultdict(<function <lambda> at 0x00000268C87BF280>, {'curso': 'Programação em Python: Essencial', 'outro': 0})
! Cria uma nova chave "outro" e atribui o valor "0" de lambda.

Docs do Python:
https://www.python.org/doc/
"""
