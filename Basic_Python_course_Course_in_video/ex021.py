"""
# Desafio 21:
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('sirene.wav')
pygame.mixer.music.play()
pygame.event.wait()
"""

from playsound import playsound
playsound('E/Users/Marenga/Desktop/Programação/Python/Curso_em_Video/abc.mp3')