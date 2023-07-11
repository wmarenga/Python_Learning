"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saida de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

Obs: Se escrevermos uma função que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- etc...

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built in) do Python print()

print(cores)

curso = 'Programação em Python Essencial'

print(curso)

cores.append('roxo')
print(cores)

curso.append('Mais dados...') # Erro de atributo (AttributeError).
print(curso)

cores = ['verde', 'amarelo', 'azul', 'branco']
cores.clear()
print(cores)

print(help(print))

# DRY - Don't Repeat Yourself (Não seja repetitivo/ não repita seu código)

# Mas então, como definir funções?

Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por 
underline(Snake_Case);

parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, 
podendo ser opcionais ou não;

bloco_da_funcao -> Também chamado de corpo da funcao ou implementação, é onde o processamento 
da funcao acontece. Neste bloco, pode ter ou não retorno da função.

Obs: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao 
Python que estamos definindo uma função. Também abrimos o bloco de códigos com o já 
conhecido dois pontos ":" que é utilizado em Python para definir blocos.

# Definindo a primeira função

# Exemplo 1:

def diz_oi():
    print('Oi!')

Obs: 

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada.

# Utilizando funções

# Chamada de execução
# ATENÇÃO: Nunca esqueça de utilizar os parênteses, sem espaços, para executar uma 
função -> nome_da_funcao().

diz_oi()

"""

# Exemplo 2:


def cantar_parabens():
    print('Parabéns pra você!')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


cantar_parabens()

# for n in range(5):
#     cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.

canta = cantar_parabens()  # Uma variável recebendo uma função.

canta
