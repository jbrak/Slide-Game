import pygame


class BlankSpace(pygame.Rect):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.swapped = False

    def swap(self, x, y):
        self.x = x
        self.y = y
        self.swapped = True
