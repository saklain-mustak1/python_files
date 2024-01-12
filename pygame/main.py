import pygame
from time import sleep
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
bg = pygame.color.Color('#FFFFFF')
screen.fill(bg)
pygame.display.flip()
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    message_to_screen("hellow you")

sleep(5)

