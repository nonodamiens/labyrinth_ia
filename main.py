# coding: utf-8

import classes
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((200, 200))

# Boucle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False