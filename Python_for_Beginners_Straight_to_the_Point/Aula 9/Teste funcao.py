"""
Você pode usar o comando sys, veja o exemplo abaixo

Suponha que você esteja rodando um arquivo main.py, mas deseja importar o arquivo 
func.py que está dentro de uma pasta teste, e usar a função somar

arquivo main.py

import sys
sys.path.append('./teste')
import func
print(func.somar(1,2))

arquivos teste/func.py

def somar(x,y):
    return x+y


Lembre de usar o comando abaixo antes de importar o seu arquivo .py

import sys
sys.path.append('./teste')


Fazendo isso, o python adiciona aquela pasta ao seu workspace e reconhece qualquer arquivo 
ali diretamente.

Pontos de atenção, dentro do append( ):

- Use \\ ou /, nunca use \

- Você pode usar caminhos relativos à pasta atual (usando o "." como eu fiz), mas você 
precisa ter certeza que o "workspace" está configurado para aquela pasta

- Para voltar uma pasta use ".."

- Se tiver problemas usando caminhos relativos (com ".") você pode usar caminhos absolutos 
("C:/minhapasta")

"""

import minhasfuncoes as mf

print(mf.faixaIdade(10))
print(mf.faixaIdade(81))
print(mf.faixaIdade(35))

print(mf.somaQuad(2,4))