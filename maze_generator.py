# génération d'un labyrinthe auto
import random
import pygame
from pygame.locals import *

pygame.init()

size = 20

fenetre = pygame.display.set_mode(((2 * size - 1) * 10,(2 * size - 1) * 10))

laby = {}
chemin_number = 0
chemin = True
stack = [(0,0)]
visited = [(0,0)]
visited_length = 0

L = [['8' for x in range(2 * size - 1)] for y in range(2 * size - 1)]
L[0][0] = ' '

go = True
while go:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            go = False

        while len(stack) > 0:
            # test of directions
            # pygame.time.Clock().tick(10)
            # pygame.time.wait(10)
            directions_ok = []
            if stack[-1][1] - 2 >= 0 and (stack[-1][0], stack[-1][1] - 2) not in visited:
                directions_ok.append(0)
                directions_ok.append(0)
            if stack[-1][0] + 2 < 2 * size - 1 and (stack[-1][0] + 2, stack[-1][1]) not in visited:
                directions_ok.append(1)
            if stack[-1][1] + 2 < 2 * size - 1 and (stack[-1][0], stack[-1][1] + 2) not in visited:
                directions_ok.append(2)
            if stack[-1][0] - 2 >= 0 and (stack[-1][0] - 2, stack[-1][1]) not in visited:
                directions_ok.append(3)
                directions_ok.append(3)

            if len(directions_ok) == 0 or stack[-1] == (2*(size - 1), 2*(size - 1)):
                if chemin:
                    laby[chemin_number] = stack.copy()
                    chemin_number += 1
                    chemin = False
                stack.pop()
            else:
                chemin = True
                r = random.randint(0,len(directions_ok) - 1)
                direction = directions_ok[r]
                if direction == 0:
                    L[stack[-1][1] - 1][stack[-1][0]] = ' '
                    L[stack[-1][1] - 2][stack[-1][0]] = ' '
                    stack.append((stack[-1][0], stack[-1][1] - 2))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 1:
                    L[stack[-1][1]][stack[-1][0] + 1] = ' '
                    L[stack[-1][1]][stack[-1][0] + 2] = ' '
                    stack.append((stack[-1][0] + 2, stack[-1][1]))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 2:
                    L[stack[-1][1] + 1][stack[-1][0]] = ' '
                    L[stack[-1][1] + 2][stack[-1][0]] = ' '
                    stack.append((stack[-1][0], stack[-1][1] + 2))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 3:
                    L[stack[-1][1]][stack[-1][0] - 1] = ' '
                    L[stack[-1][1]][stack[-1][0] - 2] = ' '
                    stack.append((stack[-1][0] - 2, stack[-1][1]))
                    visited.append(stack[-1])
                    visited_length += 1

            for i, r in enumerate(L):
                for j, c in enumerate(r):
                    if c == ' ':
                        pygame.draw.rect(fenetre, (200, 200, 200), (j * 10, i * 10, 10, 10))
            pygame.display.flip()

        


# class maze:
#     """Maze generator
#     The size is not optionnal"""

#     def __init__(self):
#         laby = {}
#         chemin_number = 0
#         chemin = True
#         stack = [(0,0)]
#         visited = [(0,0)]
#         visited_length = 0
#         self.size = 4

#         self.L = [['■' for x in range(2 * size - 1)] for y in range(2 * size - 1)]
#         self.L[0][0] = ' '

#         while len(stack) > 0:
#             # test of directions
#             directions_ok = []
#             if stack[-1][1] - 2 >= 0 and (stack[-1][0], stack[-1][1] - 2) not in visited:
#                 directions_ok.append(0)
#             if stack[-1][0] + 2 < 2 * size - 1 and (stack[-1][0] + 2, stack[-1][1]) not in visited:
#                 directions_ok.append(1)
#             if stack[-1][1] + 2 < 2 * size - 1 and (stack[-1][0], stack[-1][1] + 2) not in visited:
#                 directions_ok.append(2)
#             if stack[-1][0] - 2 >= 0 and (stack[-1][0] - 2, stack[-1][1]) not in visited:
#                 directions_ok.append(3)

#             if len(directions_ok) == 0 or stack[-1] == (2*(size - 1), 2*(size - 1)):
#                 if chemin:
#                     laby[chemin_number] = stack.copy()
#                     chemin_number += 1
#                     chemin = False
#                 stack.pop()
#             else:
#                 chemin = True
#                 r = random.randint(0,len(directions_ok) - 1)
#                 direction = directions_ok[r]
#                 if direction == 0:
#                     self.L[stack[-1][1] - 1][stack[-1][0]] = ' '
#                     self.L[stack[-1][1] - 2][stack[-1][0]] = ' '
#                     stack.append((stack[-1][0], stack[-1][1] - 2))
#                     visited.append(stack[-1])
#                     visited_length += 1
#                 elif direction == 1:
#                     self.L[stack[-1][1]][stack[-1][0] + 1] = ' '
#                     self.L[stack[-1][1]][stack[-1][0] + 2] = ' '
#                     stack.append((stack[-1][0] + 2, stack[-1][1]))
#                     visited.append(stack[-1])
#                     visited_length += 1
#                 elif direction == 2:
#                     self.L[stack[-1][1] + 1][stack[-1][0]] = ' '
#                     self.L[stack[-1][1] + 2][stack[-1][0]] = ' '
#                     stack.append((stack[-1][0], stack[-1][1] + 2))
#                     visited.append(stack[-1])
#                     visited_length += 1
#                 elif direction == 3:
#                     self.L[stack[-1][1]][stack[-1][0] - 1] = ' '
#                     self.L[stack[-1][1]][stack[-1][0] - 2] = ' '
#                     stack.append((stack[-1][0] - 2, stack[-1][1]))
#                     visited.append(stack[-1])
#                     visited_length += 1
