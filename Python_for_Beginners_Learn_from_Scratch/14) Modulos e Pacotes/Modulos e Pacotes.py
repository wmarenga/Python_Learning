''' 
Modulos:

- Conjuntos de funcionalidades organizadas em arquivos;

Usando Funcoes de um modulo:

import statistics 

x = statistics.mean(z)  # Media
y = statistics.median(z) # Mediana
    
Usando Nome Alternativo (aliaz):

import statistics as est
x = est.mean(z)
y = est.median(z)

Uso sem o nome do modulo:

from statistics import mean, median 
mean()
median()

ou

** Importa todas as funcoes do modulo
from statistics import *

Packages (Pacotes):

** Permite organizar modulos usando uma notacao de pontos;

import cienciadados.estatistica, cienciadados.machinelearning 

Bibliotecas Padrao:

- Milhares de funcoes usadas no dia a dia:
    Funcoes Matematicas;
    Numeros aleatorios;
    Criptografia;
    Leitura de arquivos;
    Protocolos de comunicacao. 

Documentacao:
https://docs.python.org/3/library/

Modulos e Pacotes Adicionais:

- Python Packaging Index: https://pypi.org

- pip e um programa para instalar modulos e pacotes;
    Instalando o pip: (prompt de comando)
        python -m ensurepip --default-pip 

- Instalando um pacote:
    python - m pip install numpy

'''