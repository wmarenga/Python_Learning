# Recursividade

def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


fator = fatorial(int(input('Digite o numero a descobrir o fatorial: ')))

print(f'O resultado fatorial e: {fator}')
