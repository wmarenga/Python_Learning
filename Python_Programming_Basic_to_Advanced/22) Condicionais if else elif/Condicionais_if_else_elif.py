"""
Estruturas condicionais (if, else, elif= (else if) - "Java e C")
"""

"""
Estrutura condicional if, else em C

if(idade < 18) {
    printf('Menor de idade')
}else if(idade == 18){
    printf('Tem 18 anos')
}else{
    printf('Maior de idade')
}
"""

"""
Estrutura condicional if, else em Java

if(idade < 18) {
    System.out.println('Menor de idade')
}else if(idade == 18){
    System.out.println('Tem 18 anos')
}else{
    System.out.println('Maior de idade')
}

"""

""" Um bloco de comandos (condicional) é iniciado por 2 pontos e a próxima linha com 4 espaços do início da linha.
Finalizamos sempre com uma linha em branco."""
idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18: # Podemos ter vários elif, mas somente 1 if e 1 else.
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
