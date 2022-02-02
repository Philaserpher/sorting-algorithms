# import pygame
BLUE = (50, 72, 168)
RED = (168, 50, 52)


class SortingBar:

    def __init__(self, height, width, pos):
        self.height = height
        self.width = width
        self.pos = pos
        self.colour = BLUE

    def get_height(self):
        return(self.height)

    def make_red(self):
        self.colour = RED

    def make_blue(self):
        self.colour = BLUE
