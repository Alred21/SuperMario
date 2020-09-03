import pygame
from . import constant as C
from . import tools


pygame.init()
SCREEN = pygame.display.set_mode((C.screen_w, C.screen_h))

GRAPHICS = tools.load_graphics('resources/graphics')