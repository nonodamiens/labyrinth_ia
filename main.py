# coding: utf-8

from classes import *
from constantes import *

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((window_size, window_size))

# Boucle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False