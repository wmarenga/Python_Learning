"""
Funcoes com Parametros Padrao (Default Parameters):

- Funcoes onde a passagem de parametro seja opcional:

# Exemplo de funcao onde a passagem de parametros seja opcional:
print('Geek Univesity')

print()

# Exemplo de funcao onde a passagem de parametros seja obrigatoria:

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # Type Error

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2* 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9


print(exponencial(3))   # Inserindo o parametro default (potencial=2), estaremos definindo 
                        # a potencia por padrao elevada a 2
print(exponencial(3, 5)) # Eleva a potencia informada pelo usuario

# Obs: Se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero, e sera
# calculado o quadrado deste bumero;
# Se o usuario passar 2 argumentos, o primeiro sera atribuido ao parametro numero e o segundo ao
# parametro potencia. Entao sera calculada a esta potencia.

print(exponencial()) # Apos definir 2 parametros default, podemos omitir os argumentos

# Obs: Em funcoes Python, os parametros com valores default (padrao) DEVEM sempre estar ao final
# da declaracao. 

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

print(teste(6)) # Ira gerar um erro pois nao informamos o segundo argumento para o parametro (potencia)
# Outro exemplo:

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) # TypeError (se definirmos um default, sumira o TypeError)
print(soma()) # TypeError (se definirmos um default, sumira o TypeError)

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem vindo instrutor {nome}'
    elif nome == 'Geek':
        return 'Eu sei que voce era o instrutor'
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por que utilizar parametros com valor default?
# - Nos permite ser mais flexiveis nas funcoes;
# - Evita erros com parametros incorretos;
# - Nos permite trabalhar com exemplos mais legiveis de codigo;

# Quais tipos de dados podemos utilizar como valores default para parametros?
# - Qualquer tipo de dado:
#    (Numeros, string, floats, booleanos, listas, tuplas, dicionarios, funcoes e etc.)

# Exemplos:
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Definicao de escopo, afim de evitar problemas e confusoes:

# - Variaveis globais
# - Variaveis locais

instrutor = 'Geek'

def diz_oi():
    instrutor = 'Python' # Variavel local
    return f'Oi {instrutor}'


print(diz_oi())

# Obs: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local
# tera preferencia.

def diz_oi():
    prof = 'Geek' # Variavel local
    return f'Ola {prof}'

print(diz_oi())
print(prof) # NameError

# ATENCAO com variaveis globais (se puder evitar, evite)
total = 0

def incrementa():
    total = total + 1   # UnboundLocalError (A variavel local esta sendo utilizada para 
                        # processamento sem ter sido inicializada)
    return total

print(incrementa())

# Corrigindo o codigo
total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variavel global
    total = total + 1   
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funcoes que sao declaradas dentro de funcoes, e tambem tem uma
# forma especial de escopo de variavel

def fora():
    contador = 0
    
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro()) # NameError (esta funcao somente e reconhecida dentro da funcao fora())
"""