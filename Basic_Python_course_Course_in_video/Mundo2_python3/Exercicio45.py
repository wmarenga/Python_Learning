# Desafio 45:
# Crie um programa que faça o computador jogar
# "Jokenpô" com você.

#import sys
#from cx_Freeze import setup, Executable

# Somente habilitar esta função quando não for usar o terminal.
# if sys.platform == "win32":
#    base = "Win32GUI"

#setup( name = "interface", version = "1.0", description = "JoKenPo", options = {"build_exe": build_exe_options}, executables = [Executable("Exercicio45.py")])
from time import sleep
import emoji
from random import randint
#import py_compile
# py_compile.compile('E:\Python\Curso_em_Video\Mundo2_python3\Exercicio45.py')

itens = ('\N{raised fist}', '\N{raised hand}', '\N{victory hand}')
comp = randint(0, 2)
# Atribuir um intervalo entre os prints.
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print("""
Digite uma opção para jogar:
[0] Pedra \N{raised fist}
[1] Papel \N{raised hand}
[2] Tesoura \N{victory hand}
""")
jog = int(input('Digite uma opção: '))

if jog != 0 and jog != 1 and jog != 2:
    print('Opção inválida! Digite novamente usando (0, 1 ou 2).')
else:
    print('-=' * 10)
    print('O jogador jogou: {}'.format(itens[jog]))
    print('O computador jogou: {}'.format(itens[comp]))
    print('-=' * 10)
    if jog == comp:
        print('\033[7;33mEMPATOU!!!\033[m, TENTE NOVAMENTE!!!')
    else:
        if comp == 0 and jog == 2 or comp == 1 and jog == 0 or comp == 2 and jog == 1:
            print('\033[7;31mO computador GANHOU!!!\033[m, TENTE NOVAMENTE!!!')
        else:
            print('\033[7;35mO jogador GANHOU!!!\033[m, TENTE NOVAMENTE!!!')
