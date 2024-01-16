import pygame
from tile import Tile
from blankSpace import BlankSpace
import random


class Tiles():
    def __init__(self, screen, screen_size, dimension=(3, 3)):
        width = screen_size[0] / dimension[0]
        height = screen_size[1] / dimension[1]

        self.screen = screen

        tile_lst = []

        for i in range(dimension[0]):
            for j in range(dimension[1]):
                tile_lst.append(
                    Tile((i * width),
                         (j * height),
                         width,
                         height,
                         random.choices(range(256), k=3)))

        self.blank = BlankSpace(tile_lst[-1].x, tile_lst[-1].y, width, height)
        del tile_lst[-1]
        self.tiles = tile_lst


    def moveTiles(self):
        keys = pygame.key.get_pressed()
        for i in self.tiles:
            i.moveTile(keys, self.blank)

        self.blank.swapped = False

    def drawTiles(self):
        for i in self.tiles:
            i.drawTile(self.screen)

        img = pygame.image.load('img.png')
        img = pygame.transform.scale(img, (self.blank.width, self.blank.height))
        self.screen.blit(img, self.blank)
