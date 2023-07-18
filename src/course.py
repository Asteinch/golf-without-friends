import pygame

from settings import * 

class Course:

    def __init__(self, mapsize):

        self.tiles = 20
        self.tile_size = mapsize / self.tiles

        self.bgs = [pygame.image.load(RES_PATH + "bg.png"), pygame.image.load(RES_PATH + "bg2.png")]

        self.colors = ((160, 197, 74), (131, 178, 72))

    def draw_course(self, win):

        for COL in range(0, self.tiles + 1):
            for ROW in range(0, self.tiles + 1):
                if (ROW + COL) % 2 == 0:
                    win.blit(self.bgs[0], (self.tile_size * ROW, self.tile_size * COL))
                else:
                    win.blit(self.bgs[1], (self.tile_size * ROW, self.tile_size * COL))