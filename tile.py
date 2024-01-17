import pygame
from blankSpace import BlankSpace


class Tile(pygame.Rect):
    def __init__(self, x, y, width, height, img):
        self.x0 = x
        self.y0 = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.img = pygame.transform.scale(img, (self.width, self.height))

    def moveTile(self, keys, blank: BlankSpace):

        if keys[pygame.K_d]:
            self.x += self.width

        elif keys[pygame.K_a]:
            self.x -= self.width

        elif keys[pygame.K_s]:
            self.y += self.height

        elif keys[pygame.K_w]:
            self.y -= self.height

        if (self.colliderect(blank)) and (blank.swapped == False):
            blank.swap(self.x0, self.y0)
            self.x0 = self.x
            self.y0 = self.y
            pygame.time.delay(300)

        else:
            self.x = self.x0
            self.y = self.y0

    def drawTile(self, surface):
        self.clamp_ip(surface.get_rect())

        surface.blit(self.img, self)

        # pygame.draw.rect(surface, self.color, self)
