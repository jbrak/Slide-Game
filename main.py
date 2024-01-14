import pygame
import sys

pygame.init()

size = width, height = 324, 324
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
dt = 0


class Tile(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        self.x0 = x
        self.y0 = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.color = color

    def moveTile(self, keys, tiles):

        if keys[3]:
            self.x += self.width

        elif keys[1]:
            self.x -= self.width

        elif keys[2]:
            self.y += self.height

        elif keys[0]:
            self.y -= self.height

        if len(self.collidelistall(tiles)) == 1:
            self.x0 = self.x
            self.y0 = self.y

            print(keys)
            return [False for i in range(4)]
        else:
            self.x = self.x0
            self.y = self.y0
            print(keys)
            return keys

    def drawTile(self, surface):
        self.clamp_ip(surface.get_rect())
        pygame.draw.rect(surface, self.color, self)


tile1 = Tile(0, 0, 108, 108, "white")
tile2 = Tile(0, 108, 108, 108, "purple")
tile3 = Tile(0, 216, 108, 108, "green")
tile4 = Tile(108, 0, 108, 108, "orange")
tile5 = Tile(108, 108, 108, 108, "steelblue")
tile6 = Tile(108, 216, 108, 108, "red")
tile7 = Tile(216, 0, 108, 108, "yellow")
tile8 = Tile(216, 108, 108, 108, "blue")

tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill("black")

    allKeys = pygame.key.get_pressed()
    keys = [allKeys[pygame.K_w], allKeys[pygame.K_a], allKeys[pygame.K_s], allKeys[pygame.K_d]]
    print("\n", keys)
    keys = tile1.moveTile(keys, tiles)
    keys = tile2.moveTile(keys, tiles)
    keys = tile3.moveTile(keys, tiles)
    keys = tile4.moveTile(keys, tiles)
    keys = tile5.moveTile(keys, tiles)
    keys = tile6.moveTile(keys, tiles)
    keys = tile7.moveTile(keys, tiles)
    keys = tile8.moveTile(keys, tiles)
    pygame.time.delay(100)

    tile1.drawTile(screen)
    tile2.drawTile(screen)
    tile3.drawTile(screen)
    tile4.drawTile(screen)
    tile5.drawTile(screen)
    tile6.drawTile(screen)
    tile7.drawTile(screen)
    tile8.drawTile(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
