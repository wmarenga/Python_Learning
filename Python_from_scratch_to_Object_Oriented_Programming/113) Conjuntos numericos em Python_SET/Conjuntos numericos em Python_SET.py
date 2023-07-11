# Conjuntos numericos em Python_SET

# SET (Aplicamos a teoria dos conjuntos, como em matematica) - Uniao, intersecao, etc

conjunto1 = {5, 10, 15, 20}
conjunto2 = {1, 3, 5, 10}

print(type(conjunto1))

# Uniao (Somente junta os elemntos unicos dos dois conjuntos)
conjunto_uniao1 = conjunto1.union(conjunto2)
print(conjunto_uniao1)
# Outra maneira de fazer a uniao entre dois conjuntos
conjunto_uniao2 = conjunto1 | conjunto2
print(conjunto_uniao2)

# Intersecao (elementos comuns em ambos os conjuntos)
conjunto_inter1 = conjunto1.intersection(conjunto2)
print(conjunto_inter1)
# Outra maneira de fazer a intersecao entre dois conjuntos
conjunto_inter2 = conjunto1 & conjunto2
print(conjunto_inter2)

'''
Operações matemáticas em sets:

Símbolo matemático	    Operador Python	                Descrição
    e ∈ S	                    in               elemento e é membro de S
    A ⊆ B	                    <=              A é um subconjunto de B
    A ⊂ B	                    <               A é um subconjunto próprio de B
    A U B	                    |                      A união com B
    A ∩ B	                    &                   A interseção com B
    A \ B	                    -                   diferença entre A e B
    Elementos que nao estao em ambos A ^ B 
'''
