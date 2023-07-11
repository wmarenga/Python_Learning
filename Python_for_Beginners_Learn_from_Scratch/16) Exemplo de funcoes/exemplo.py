'''
Funcoes:

- Blocos de codigos reutilizaveis;
- Podem ser chamados de qualquer parte do programa;
- Podem seer chamados de outros programas. 

Exemplo Simples de Funcao:

## Definir a funcao:

def imprime(parametro opcional):
    print("esta e uma funcao")

## Chamar a funcao:

imprime()

Exemplo de Parametro para uma Funcao:

def imprime(n):
    print(n)

## Chamando a funcao:

imprime("Impressao deste texto")

Exemplo de Retorno:

def potencia(n):
    return n * n

## Chamando a funcao:

x = potencia(3)
print(x)

Exemplo com Valor Default:

def intervalo(inic=1, fim=10):
    for inic in range(1, fim + 1):
        print(inic)
        
** Podemos chamar a funcao informando 1 e 10
intervalo(1, 10)

** Ou nao informar, a funcao vai assumir valores padrao
intervalo()

'''