"""
Os operadores em Python são:

+, -, *, /, //, **, %, ()

Precedência (1-mais prioritário => 8-menos prioritário):
Oficial:
https://docs.python.org/3/reference/expressions.html#operator-precedence

1) ()
2) **
3) *, /, //, %
4) +, -
5) ==, !=, <=, >=, >, <
6) not (bool)
7) and (bool)
8) or (bool)

+ => Soma valores (int, float) ou concatena (str);
Exemplo:
print('Soma + => 10 + 10 = ', 10 + 10)

# Irá concatenar as strings '1010'
print('Soma + => '10' + '10' = ', '10' + '10')
# Irá gerar um erro, pois não podemos unir uma str com um int.
print('Soma + => '10' + 2 = ', '10' + 2)
# Concatenando str + int com casting
print('Wellington' + ' ' + 'Marenga tem ' + str(51) + ' anos.')

- => Subtrai valores;
Exemplo:
print('Subtração - => 10 - 5 = ', 10 - 5)

* => Multiplica valores (números ou str);
Exemplo:
print('Multiplicação * => 10 x 10 = ', 10 * 10)

# Irá apresentar um erro.
print('Multiplicação * => '10' x '10' = ', '10' * '10')
# Irá repetir a str 10 vezes.
print('Multiplicação * => '10' x 10 = ', '10' * 10)

/ => Divisão normal;
Exemplo:
print('Divisão / => 10 / 2 = ', 10 / 2)  # Retorna um número float sempre

`// => Divisão inteira;
Exemplo:
print(10.5 // 3)  # Retorna um número float.
print(10 // 3)  # Retorna um número int.
print(13 // 2)  # Retorna um número int.

** => Exponenciação ou potenciação;
Exemplo:
print(2 ** 10)

&  => Retorna o módulo, resto da divisão de um número pelo outro;
Exemplo:
print(10 % 5)  # O resultado é 0, pois é o resto da divisão.
print(10 % 3)  # O resultado é 1, pois é o resto da divisão.

() => São usados para alterar as precedências em uma expressão matémática
(ordenação).
Exemplo:
print(2 * (2 + 2))
print((2 * 2) + 3)

Exemplo de Poliformismo (atua de forma diferente em determinada situação):
print(20 * 'A')  # 'AAAAAAAAAAAAAAAAAAAA'
print('20' + 'A')  # Saída '20A'
print('20' + int(20))  # Saída '2020'

"""
