# Faça um progrma que abra e reproduza o áudio de um arquivo

import pygame
import time

pygame.init()
pygame.mixer.init()

music = pygame.mixer.Sound('sans.wav')
music.play()
time.sleep (20)