"""
import pygame
pygame.init()
pygame.mixer.music.load('abc.mp3')
pygame.mixer.music.play()
pygame.event.wait()

"""

import pygame
import os
pygame.init()
if os.path.exists('abc.mp3'):
    pygame.mixer.music.load('abc.mp3')
    pygame.mixer.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo abs.mp3 não está no diretório do script Python')
