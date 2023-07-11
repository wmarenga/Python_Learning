""" 
Variaveis:
- Espaco em memoria, para guardar um valor durante a execucao de um programa;
- Por exemplo, voce tem um programa para prever as vendas. Voce vai precisar de uma variavel
para, por exemplo, saber quantos meses para frente o programa deve prever. 

Variaveis (Tipos):
- Texto (String). Ex.: Nome;
- Inteiro: Ex.: Idade;
- Float: Ex.: Altura;
- Logica/ Booleana: Falso (Transacao fraudulenta). 

A declaracao de variaveis no Python e implicita: fracamente tipica. Significa que o tipo da variavel e criado 
de acordo com o dado atribuido. 

- Cria variavel do tipo inteiro:
x = 1
O Python automaticamente entende que a variavel e inteira. 

- Cria variavel do tipo float:
y = 3.13

- Cria variavel do tipo String:
z = "Python"
z = 'Python'

- Cria variavel do tipo logica:
w = True
y = False

Utilizacao do Python como uma calculadora:

x = 10
y = 20
z = 100
w = (x + y) * z / 100

Exibindo Valores no Console:

print("Este texto sera impresso no console")
print(x)
print(f"Texto e duas variaveis x = {x}, z = {z}")
print("Texto e duas variaveis", x, z)

Verificacao do Tipo da variavel:

type(x)

x = 10
type(x)
<class 'int'>

y = "Python"
type(y)
<class 'str'>

Entrada de Valores:

x = input("Informe um valor")
Sempre sera criada uma string nesta situacao.

- Aguarda o usuario entrar o dado;
- Criar a variavel x como string e armazena o valor;
- Independente do tipo de dado informado, a variavel sera sempre string. 

Conversao de Valores:

x = int(z)

w = str(m)

t = float(l)

Fazendo Comentarios no Python:

- Texto ignorado (Nao interpretado);
- Usado para lembretes e documentacao do codigo;

* Comentario ate o fim da linha:
    # Este texto e um comentarios
    x = 10 # a partir daqui e um comentario

* Comentario de varias linhas:
    ''' Aqui comeca um comentario
    Aqui ele continua
    e aqui ele termina '''


"""