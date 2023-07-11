''' Peca para que o usuario digite um numero, em seguida retorne uma mensagem
dizendo se tal numero e par ou impar'''

num = int(input('Digite um numero para saber se e par ou impar: '))

if num % 2 == 0:
    print(f'Voce digi100tou o numero {num}, este numero e par!!')
else:
    print(f'Voce digitou o numero {num}, este numero e impar!!')
