'''
Estruturas de Decisao:

- O programa deve decidir entre diferentes fluxos, de acordo com as entradas;
- Por exemplo, se a nota de um aluno e maior ou igual a 7, ele e aprovado, caso contrario e reprovado. 

                      Nota
                        |
           Maior ou     |       Menor
           igual a 7    V       que 7
Aprovado <---------- Decisao ----------> Reprovado
                    (Avaliacao
                      Logica)

Como funciona:

se nota >= 7 entao:
    Aprovado

Identacao:

Java (as chaves definem o que sera executado):

if (condicao logica) {
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
}  else if (condicao logica) {
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
}  else  {
    // bloco de codigo
    // bloco de codigo
}
    
Python (a identacao - "4 espacos ou Tab" definem o que sera exevutado):

if (condicao logica):
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
elif (condicao logica):
    // bloco de codigo
    // bloco de codigo
    // bloco de codigo
else:
    // bloco de codigo
    // bloco de codigo

Estrutura do Python:

if avaliacao logica:
    Executar se verdadeiro
    Executar se verdadeiro
else:
    Executar se falso
    Executar se falso

Operadores de comparacao:

<  menor que 
>  maior que 
<= menor igual
>= maior igual
!= diferente
== igual

Operadores Logicos:

and (E)
or (ou)
not (nao)

Exemplos1:

nota = 7

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
    
Exemplo2:

nota = 7
frequencia = 90

if nota >= 7 and frequencia > 70:
    print("Aprovado")
else:
    print("Reprovado")

if nota >= 7 or frequencia > 70:
    print("Aprovado")
else:
    print("Reprovado")

nota = 7

if nota <= 4:
    print("Reprovado")
elif nota > 4 and nota <= 6:
    print("Exame")
else:
    print("Aprovado")
'''