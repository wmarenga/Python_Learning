"""
Dunder Main e Dunder Name:

Dunder = Double under

Dunder Name => __name__
Dunder Main => __main__ (main significa principal)

Em Python, são utilizados dunder para criar funções, atributos, propriedades
e etc, utilizando Double Under para não gerar conflitos com os nomes desses
elementos na programação.
# Na linguagem C, temos um programa da seguinte forma:

int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){
}

# Em Python, se executarmos um módulo Python diretamente na linha de comando,
internamente, o Python atribuirá à variável __name__ o valor __main__ indicando
que este módulo é o módulo de execução principal.

from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
else:
    print('O módulo funcoes_com_parametros.py foi importado')

"""
import primeiro
import segundo

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'primeiro', 'segundo']
