# import pygame
BLUE = (50, 72, 168)
RED = (168, 50, 52)
PURPLE = (138, 43, 226)
BLACK = (0, 0, 0)


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

    def make_purple(self):
        self.colour = PURPLE

    def make_black(self):
        self.colour = BLACK

    def get_colour(self):
        return(self.colour)
