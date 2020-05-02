# génération d'un labyrinthe auto
import random

class Test:
    def __init__(self):
        self.toto = 12

T = Test()
print(T.toto)


class maze:
    """Maze generator
    The size is optionnal"""

    def __init__(self, size=4):
        laby = {}
        chemin_number = 0
        chemin = True
        stack = [(0,0)]
        visited = [(0,0)]
        visited_length = 0
        self.size = size

        self.L = [['■' for x in range(2 * size - 1)] for y in range(2 * size - 1)]
        self.L[0][0] = ' '

        while len(stack) > 0:
            # test of directions
            directions_ok = []
            if stack[-1][1] - 2 >= 0 and (stack[-1][0], stack[-1][1] - 2) not in visited:
                directions_ok.append(0)
            if stack[-1][0] + 2 < 2 * size - 1 and (stack[-1][0] + 2, stack[-1][1]) not in visited:
                directions_ok.append(1)
            if stack[-1][1] + 2 < 2 * size - 1 and (stack[-1][0], stack[-1][1] + 2) not in visited:
                directions_ok.append(2)
            if stack[-1][0] - 2 >= 0 and (stack[-1][0] - 2, stack[-1][1]) not in visited:
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
                    self.L[stack[-1][1] - 1][stack[-1][0]] = ' '
                    self.L[stack[-1][1] - 2][stack[-1][0]] = ' '
                    stack.append((stack[-1][0], stack[-1][1] - 2))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 1:
                    self.L[stack[-1][1]][stack[-1][0] + 1] = ' '
                    self.L[stack[-1][1]][stack[-1][0] + 2] = ' '
                    stack.append((stack[-1][0] + 2, stack[-1][1]))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 2:
                    self.L[stack[-1][1] + 1][stack[-1][0]] = ' '
                    self.L[stack[-1][1] + 2][stack[-1][0]] = ' '
                    stack.append((stack[-1][0], stack[-1][1] + 2))
                    visited.append(stack[-1])
                    visited_length += 1
                elif direction == 3:
                    self.L[stack[-1][1]][stack[-1][0] - 1] = ' '
                    self.L[stack[-1][1]][stack[-1][0] - 2] = ' '
                    stack.append((stack[-1][0] - 2, stack[-1][1]))
                    visited.append(stack[-1])
                    visited_length += 1
