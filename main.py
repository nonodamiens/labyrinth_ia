# coding: utf-8

from classes import *
from constantes import *

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((window_size, window_size))

pygame.display.set_caption(title)

# Boucle
go_on = True
title = True
while go_on:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            go_on = False
    
    pygame.display.flip()