"""
Combinations, Permutations e Product (Itertools):

- Combinação (combinations) => a ordem não importa;
- Permutação (permutations) => a ordem importa;
* Ambos não repetem valores únicos.
- Produto (product) => a ordem importa e repete valores únicos.

# Saber todas as combinações possíveis (grupo de 2 pessoas)

from itertools import combinations
pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoa, 2):
    print(grupo)

# Luiz e André == André e Luiz, sendo assim ele vai ignorar (André e Luiz)

# Se a ordem for importante, utilizamos os (permutations)

from itertools import combinations, permutations
pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in permutations(pessoa, 2):
    print(grupo)

# Agora ambos são considerados (Luiz e André/ André e Luiz).
# Contudo não temos as combinações de Luiz e Luiz, André e André, etc.

# Para termos também os valores repetidos com a ordem importando,
# temos que usar (product).

from itertools import combinations, permutations, product
pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in product(pessoa, repeat=2):
    print(grupo)

"""
