import pygame

from settings import *

class Obstacle:

    def __init__(self, size, pos):

        self.size = (size[0] * 40, size[1] * 40)
        self.pos = (pos[0] * 40, pos[1] * 40)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.mask = pygame.Mask((self.size[0], self.size[1]))

        self.row, self.col = self.size[1] // 40, self.size[0] // 40
        self.all_cells = self.get_all()

        self.sprite = pygame.image.load(RES_PATH + "tile.png")

    def get_all(self):

        list = []

        for c in range(self.col):
            for r in range(self.row):

                list.append(((self.pos[0]//40 + c)*40, (self.pos[1] //40 + r)*40))

        return list

    def draw(self, win):

        for cell in self.all_cells:
            win.blit(self.sprite, cell)


