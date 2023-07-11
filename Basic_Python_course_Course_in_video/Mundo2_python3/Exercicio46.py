# Desafio 46:
# Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifício, de 10 até 0, com uma pausa de 1 seg.
# entre elas.

import emoji

from time import sleep
print("Assim se inicia a contágem regressiva para o ano novo!")
for f in range(10, -1, -1):
    print(f)
    sleep(0.5)  # Conta meio minuto.
print(emoji.emojize("FELIZ ANO NOVO! :fireworks:"))
