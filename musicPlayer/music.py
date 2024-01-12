import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('Marshmello - Moving On (Official Music Video).mp3')
pygame.mixer.music.play()
sleep(10)