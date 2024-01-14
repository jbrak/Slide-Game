import pygame
import sys
from tiles import Tiles
from tile import Tile

pygame.init()

size = width, height = 324, 324
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
dt = 0

tiles = Tiles(screen, size, (3, 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill("black")

    tiles.moveTiles()
    pygame.time.delay(300)

    tiles.drawTiles()

    pygame.display.flip()
    dt = clock.tick(60) / 1000
