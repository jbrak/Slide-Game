import pygame
from tile import Tile
from blankSpace import BlankSpace
import random
from split_image import split_image


class Tiles():
    def __init__(self, screen, screen_size, dimension, imgPath):
        width = screen_size[0] / dimension[0]
        height = screen_size[1] / dimension[1]
        self.screen = screen

        split_image(imgPath, dimension[0], dimension[1], False, False, output_dir="images")

        self.pictures = [pygame.image.load(f'images/img_{i}.png') for i in range(dimension[0] * dimension[1])]

        img_final = self.pictures[-1]
        tile_lst = []
        temp_pictures = self.pictures

        for i in range(dimension[0]):
            for j in range(dimension[1]):

                img = random.choice(temp_pictures)
                temp_pictures.remove(img)

                tile_lst.append(
                    Tile((i * width),
                         (j * height),
                         width,
                         height,
                         img))

                if img == img_final:
                    deleteMe = tile_lst[-1]

        self.blank = BlankSpace(deleteMe.x, deleteMe.y, width, height)

        tile_lst.remove(deleteMe)
        self.tiles = tile_lst

    def moveTiles(self):
        keys = pygame.key.get_pressed()
        for i in self.tiles:
            i.moveTile(keys, self.blank)

        self.blank.swapped = False

    def drawTiles(self):
        for i in self.tiles:
            i.drawTile(self.screen)
